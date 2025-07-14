from django.contrib import admin
from .models import ContactMessage, TeamMember

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    list_editable = ['is_read']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        return False  # Prevent adding messages through admin
    
    def has_delete_permission(self, request, obj=None):
        return True  # Allow deletion for cleanup

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'order']
    list_editable = ['order']
    search_fields = ['name', 'title']
    ordering = ['order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'bio', 'image')
        }),
        ('Settings', {
            'fields': ('linkedin_url', 'order')
        }),
    )

