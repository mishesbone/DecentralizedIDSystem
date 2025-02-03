from django.urls import path
from .views import DIDView, CredentialView

urlpatterns = [
    path('create-did/', DIDView.as_view(), name='create_did'),
    path('issue-credential/', CredentialView.as_view(), name='issue_credential'),
]
