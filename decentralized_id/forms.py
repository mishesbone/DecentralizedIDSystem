from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import IdentityVerification

# User Registration Form (Extending Django's built-in UserCreationForm)
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

# Identity Verification Form
class IdentityVerificationForm(forms.ModelForm):
    # Document field for uploading identity verification document (e.g., passport, ID card, etc.)
    document = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*,application/pdf'}))
    verified = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = IdentityVerification
        fields = ['document', 'verified']

    # Custom validation for document upload
    def clean_document(self):
        file = self.cleaned_data.get('document')
        if file:
            if file.size > 5 * 1024 * 1024:  # Limit file size to 5MB
                raise forms.ValidationError("File size should not exceed 5MB.")
        return file

# Form for generating decentralized identity code (if required)
class GenerateIdentityCodeForm(forms.Form):
    public_key = forms.CharField(max_length=512, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your public key'}))
    blockchain_address = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your blockchain address'}))

    def clean_public_key(self):
        public_key = self.cleaned_data.get('public_key')
        if len(public_key) < 64:  # Assuming a basic length check for the public key
            raise forms.ValidationError("Invalid public key.")
        return public_key
    
    def clean_blockchain_address(self):
        blockchain_address = self.cleaned_data.get('blockchain_address')
        if len(blockchain_address) < 30:  # Assuming a basic length check for blockchain address
            raise forms.ValidationError("Invalid blockchain address.")
        return blockchain_address
