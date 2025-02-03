from rest_framework import serializers
from .models import DecentralizedIdentifier, VerifiableCredential

class DIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecentralizedIdentifier
        fields = "__all__"

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifiableCredential
        fields = "__all__"
