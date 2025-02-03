import uuid
from hashlib import sha256

class DIDManager:
    @staticmethod
    def create_did():
        unique_id = str(uuid.uuid4())
        did = "did:example:" + sha256(unique_id.encode()).hexdigest()
        return did

from config.settings import SECRET_KEY
from jwcrypto import jwt
