from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    # Extending the default Django User model to include blockchain-related fields
    public_key = models.CharField(max_length=255, blank=True, null=True)
    blockchain_address = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # Override the related_name to prevent clashes with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username

    class Meta:
        permissions = [
            ("can_view_data", "Can view data"),
            ("can_edit_data", "Can edit data"),
        ]

class IdentityVerification(models.Model):
    # This model is for verifying a user's identity
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Verification for {self.user.username} - {'Verified' if self.verified else 'Pending'}"
    
    class Meta:
        ordering = ['-created_at']
