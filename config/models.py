from django.db import models

class DecentralizedIdentifier(models.Model):
    did = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class VerifiableCredential(models.Model):
    subject_did = models.ForeignKey(DecentralizedIdentifier, on_delete=models.CASCADE)
    credential = models.TextField()  # JWT or JSON payload
    issued_at = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField()
