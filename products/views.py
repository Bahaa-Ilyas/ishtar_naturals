from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    
    def get_queryset(self):
        return Product.objects.filter(is_available=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    
    def get_queryset(self):
        return Product.objects.filter(is_available=True)

def product_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_available=True)
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'products/product_list.html', context)

def featured_products(request):
    products = Product.objects.filter(is_featured=True, is_available=True)[:6]
    return render(request, 'products/featured_products.html', {'products': products})


def product_by_category_slug(request, category_slug):
    # Map category slugs to category names or IDs
    category_mapping = {
        'lip-balm': 'Lip Balm',
        'deodorant': 'Deodorant', 
        'bundles': 'Bundle',
    }
    
    category_name = category_mapping.get(category_slug)
    if not category_name:
        # If category slug not found, show all products
        products = Product.objects.filter(is_available=True)
        current_category = None
    else:
        try:
            category = Category.objects.get(name__icontains=category_name)
            products = Product.objects.filter(category=category, is_available=True)
            current_category = category
        except Category.DoesNotExist:
            products = Product.objects.filter(is_available=True)
            current_category = None
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category,
        'category_slug': category_slug,
    }
    return render(request, 'products/product_list.html', context)

