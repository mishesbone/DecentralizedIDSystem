from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DecentralizedIdentifier, VerifiableCredential
from .serializers import DIDSerializer, CredentialSerializer
from .utils import generate_did, sign_credential

class DIDView(APIView):
    def get(self, request):
        did = generate_did()
        did_instance = DecentralizedIdentifier.objects.create(did=did)
        serializer = DIDSerializer(did_instance)
        return Response(serializer.data)

class CredentialView(APIView):
    def post(self, request):
        data = request.data
        signed_credential = sign_credential(data)
        credential_instance = VerifiableCredential.objects.create(
            subject_did_id=data["subject_did"],
            credential=signed_credential,
            valid_until=data["valid_until"]
        )
        serializer = CredentialSerializer(credential_instance)
        return Response(serializer.data)
