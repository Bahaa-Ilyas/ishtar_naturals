from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('science/', views.science, name='science'),
    
    # About subpages
    path('team/', views.team, name='team'),
    path('mission/', views.mission, name='mission'),
    path('sustainability/', views.sustainability, name='sustainability'),
    
    # Science subpages
    path('ingredients/', views.ingredients, name='ingredients'),
    path('clinical-studies/', views.clinical_studies, name='clinical_studies'),
    path('certifications/', views.certifications, name='certifications'),
    
    # Contact subpages
    path('support/', views.support, name='support'),
    path('faq/', views.faq, name='faq'),
    path('store-locator/', views.store_locator, name='store_locator'),
    
    # Legal pages
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms_of_service, name='terms_of_service'),
]

