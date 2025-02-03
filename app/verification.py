import jwt
from config.settings import SECRET_KEY

class CredentialVerifier:
    @staticmethod
    def verify_credential(signed_credential):
        try:
            decoded_credential = jwt.decode(signed_credential, SECRET_KEY, algorithms=["HS256"])
            return {"status": "Valid", "data": decoded_credential}
        except jwt.ExpiredSignatureError:
            return {"status": "Invalid", "reason": "Expired Credential"}
        except jwt.InvalidTokenError:
            return {"status": "Invalid", "reason": "Invalid Token"}
