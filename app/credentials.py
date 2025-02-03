import jwt
from config.settings import SECRET_KEY

class CredentialIssuer:
    @staticmethod
    def issue_credential(user_id, name, email):
        credential = {
            "id": f"did:example:{user_id}",
            "type": ["VerifiableCredential", "IdentityCredential"],
            "issuer": "did:example:issuer123",
            "credentialSubject": {
                "id": f"did:example:{user_id}",
                "name": name,
                "email": email
            }
        }
        signed_credential = jwt.encode(credential, SECRET_KEY, algorithm="HS256")
        return signed_credential
