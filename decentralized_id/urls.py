from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # For user registration
    path('profile/', views.profile, name='profile'),      # User profile page
    path('identity-verification/', views.identity_verification, name='identity_verification'),  # Identity document upload
    path('verification-status/', views.verification_status, name='verification_status'),  # View verification status
    path('generate-identity-code/', views.generate_identity_code, name='generate_identity_code'),  # Generate identity code for linking with blockchain
]
