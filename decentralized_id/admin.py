from django.contrib import admin
from .models import CustomUser, IdentityVerification

# Register the CustomUser model to the Django Admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'public_key', 'blockchain_address', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'date_joined')
    ordering = ('date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)

# Register the IdentityVerification model to the Django Admin
class IdentityVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'verified', 'created_at')
    search_fields = ('user__username', 'document')
    list_filter = ('verified', 'created_at')
    ordering = ('created_at',)

admin.site.register(IdentityVerification, IdentityVerificationAdmin)
