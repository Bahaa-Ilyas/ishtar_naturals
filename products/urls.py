from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:category_id>/', views.product_by_category, name='product_by_category'),
    path('category/<str:category_slug>/', views.product_by_category_slug, name='category'),
    path('featured/', views.featured_products, name='featured_products'),
]

