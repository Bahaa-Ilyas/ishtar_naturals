from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from products.models import Product
from .models import ContactMessage, TeamMember
from .forms import ContactForm

def home(request):
    featured_products = Product.objects.filter(is_featured=True, is_available=True)[:3]
    context = {
        'featured_products': featured_products,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    team_members = TeamMember.objects.all()
    context = {
        'team_members': team_members,
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            
            # Send email notification (optional)
            try:
                send_mail(
                    subject=f"New Contact Message: {form.cleaned_data['subject']}",
                    message=f"From: {form.cleaned_data['name']} ({form.cleaned_data['email']})\n\n{form.cleaned_data['message']}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['info@ishtarnaturals.com'],
                    fail_silently=True,
                )
            except:
                pass
            
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('pages:contact')
    else:
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {'form': form})

def science(request):
    return render(request, 'pages/science.html')

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'pages/terms_of_service.html')


# About subpages
def team(request):
    team_members = TeamMember.objects.all().order_by('order')
    context = {
        'team_members': team_members,
    }
    return render(request, 'pages/team.html', context)

def mission(request):
    return render(request, 'pages/mission.html')

def sustainability(request):
    return render(request, 'pages/sustainability.html')

# Science subpages
def ingredients(request):
    return render(request, 'pages/ingredients.html')

def clinical_studies(request):
    return render(request, 'pages/clinical_studies.html')

def certifications(request):
    return render(request, 'pages/certifications.html')

# Contact subpages
def support(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message with support category
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=f"Support: {form.cleaned_data['subject']}",
                message=form.cleaned_data['message']
            )
            
            messages.success(request, 'Your support request has been submitted. We will respond within 24 hours.')
            return redirect('pages:support')
    else:
        form = ContactForm()
    
    return render(request, 'pages/support.html', {'form': form})

def faq(request):
    return render(request, 'pages/faq.html')

def store_locator(request):
    return render(request, 'pages/store_locator.html')

