import uuid
import hashlib
import jwt
from cryptography.fernet import Fernet
import requests
from django.conf import settings
from .models import IdentityVerification

# Utility function to generate a decentralized identifier (DID)
def generate_did():
    """Generates a decentralized identifier (DID) using UUID and hashing."""
    unique_id = str(uuid.uuid4())
    return "did:example:" + hashlib.sha256(unique_id.encode()).hexdigest()

# Utility function to sign a credential (JWT encoding)
def sign_credential(data):
    """Signs the credential data using the secret key in settings."""
    return jwt.encode(data, settings.SECRET_KEY, algorithm="HS256")

# Utility function to generate a random UUID (can be used as unique identity code)
def generate_unique_identity_code():
    """Generates a unique identity code (UUID)."""
    return str(uuid.uuid4())

# Utility function to hash data (for example, password, or document content)
def hash_data(data):
    """Hashes a given string using SHA-256."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Encryption utilities for secure data handling (e.g., for encrypting documents or personal data)
def generate_encryption_key():
    """Generates a new encryption key using the Fernet symmetric encryption system."""
    return Fernet.generate_key()

def encrypt_data(data, key):
    """Encrypts data using the provided key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode('utf-8'))
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """Decrypts data using the provided key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data

# Blockchain interaction utility (for generating and verifying identity on the blockchain)
def verify_identity_on_blockchain(public_key, blockchain_address):
    """
    Simulate verifying identity on a blockchain by interacting with a blockchain API.
    For the sake of this example, we are using a mock function.
    Replace this with actual blockchain interaction using web3.py or any relevant API.
    """
    # Placeholder for actual blockchain interaction, here we simulate with a mock response
    response = {
        "status": "success",
        "message": f"Identity with public key {public_key} is verified on blockchain at address {blockchain_address}."
    }
    
    # In a real-world scenario, you would use a library like web3.py to interact with the blockchain.
    # For example:
    # from web3 import Web3
    # w3 = Web3(Web3.HTTPProvider('https://your-blockchain-node-url'))
    # identity_verified = w3.eth.getStorageAt(blockchain_address, public_key_hash)
    
    return response

# Helper function to save identity verification details
def save_identity_verification(user, document, verified):
    """Saves the identity verification result for a user."""
    identity_verification = IdentityVerification.objects.create(
        user=user,
        document=document,
        verified=verified
    )
    return identity_verification

# Example function to fetch identity verification status from an API (replace with actual API)
def fetch_identity_verification_status(user):
    """
    Fetches the status of identity verification from an external verification service.
    For this example, it’s a mock API interaction.
    """
    api_url = "https://api.mock-verification-service.com/status"
    response = requests.post(api_url, data={"user_id": user.id})
    
    if response.status_code == 200:
        data = response.json()
        return data.get("status", "unknown")
    else:
        return "Error fetching verification status."
