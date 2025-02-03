from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import IdentityVerification
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

class CustomUserModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='securepassword',
            public_key='testpublickey',
            blockchain_address='testblockchainaddress'
        )

    def test_user_creation(self):
        """Test that a CustomUser can be created successfully"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('securepassword'))
        self.assertEqual(self.user.public_key, 'testpublickey')
        self.assertEqual(self.user.blockchain_address, 'testblockchainaddress')

    def test_user_str_method(self):
        """Test the string representation of the CustomUser model"""
        self.assertEqual(str(self.user), 'testuser')


class IdentityVerificationModelTest(TestCase):
    def setUp(self):
        # Create a test user for verification
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='securepassword',
            public_key='testpublickey',
            blockchain_address='testblockchainaddress'
        )

        # Create a test identity verification instance
        self.test_document = SimpleUploadedFile(
            "test_document.pdf",
            b"file_content",
            content_type="application/pdf"
        )
        self.verification = IdentityVerification.objects.create(
            user=self.user,
            document=self.test_document,
            verified=True,
            created_at=timezone.now()
        )

    def test_identity_verification_creation(self):
        """Test that IdentityVerification can be created successfully"""
        self.assertEqual(self.verification.user.username, 'testuser')
        self.assertEqual(self.verification.document.name, 'documents/2025/02/03/test_document.pdf')
        self.assertTrue(self.verification.verified)
        self.assertIsInstance(self.verification.created_at, timezone.datetime)

    def test_identity_verification_str_method(self):
        """Test the string representation of the IdentityVerification model"""
        self.assertEqual(str(self.verification), f"Verification for testuser - Verified")

    def test_verification_status_update(self):
        """Test that the verification status can be updated"""
        self.verification.verified = False
        self.verification.save()
        self.assertFalse(self.verification.verified)

    def test_identity_verification_document_upload(self):
        """Test that the document is uploaded correctly"""
        self.assertTrue(self.verification.document.name.startswith('documents/'))
        self.assertTrue(self.verification.document.name.endswith('test_document.pdf'))

