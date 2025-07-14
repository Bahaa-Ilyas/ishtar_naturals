from django.contrib import admin
from .models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_featured', 'is_available', 'created_at']
    list_filter = ['category', 'is_featured', 'is_available', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_featured', 'is_available']
    ordering = ['-created_at']
    inlines = [ProductImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'short_description', 'description')
        }),
        ('Pricing & Availability', {
            'fields': ('price', 'is_available', 'is_featured')
        }),
        ('Product Details', {
            'fields': ('ingredients', 'benefits', 'usage_instructions', 'image')
        }),
    )

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'alt_text', 'is_primary']
    list_filter = ['is_primary']
    search_fields = ['product__name', 'alt_text']

