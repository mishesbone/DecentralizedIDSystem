from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from .models import CustomUser, IdentityVerification
from .forms import IdentityVerificationForm
from .utils import generate_verification_code
from django.core.files.storage import FileSystemStorage

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}!")
            return redirect('profile')  # Redirect to profile page after successful registration
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'identity/register.html', {'form': form})

# User Profile View
def profile(request):
    user = request.user
    return render(request, 'identity/profile.html', {'user': user})

# Identity Verification View (For document upload and verification)
def identity_verification(request):
    if request.method == 'POST':
        form = IdentityVerificationForm(request.POST, request.FILES)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.user = request.user
            verification.save()
            messages.success(request, "Your identity verification is under review.")
            return redirect('profile')
        else:
            messages.error(request, "There was an error with your document submission. Please try again.")
    else:
        form = IdentityVerificationForm()
    return render(request, 'identity/identity_verification.html', {'form': form})

# Verification status API (Optional)
def verification_status(request):
    user = request.user
    try:
        verification = IdentityVerification.objects.get(user=user)
        return JsonResponse({
            'status': 'Verified' if verification.verified else 'Pending',
            'document': verification.document.url if verification.document else None
        })
    except IdentityVerification.DoesNotExist:
        return JsonResponse({'status': 'No verification found'}, status=404)

# Generate Decentralized Identity Code (For linking public key or blockchain address)
def generate_identity_code(request):
    if request.method == 'POST':
        public_key = request.POST.get('public_key', '')
        blockchain_address = request.POST.get('blockchain_address', '')
        if public_key and blockchain_address:
            verification_code = generate_verification_code(public_key, blockchain_address)
            return JsonResponse({'verification_code': verification_code})
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)
    return render(request, 'identity/generate_identity_code.html')
