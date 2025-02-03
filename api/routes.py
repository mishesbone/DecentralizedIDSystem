from flask import Flask, request, jsonify
from app.did import DIDManager
from app.credentials import CredentialIssuer
from app.verification import CredentialVerifier

app = Flask(__name__)

@app.route("/create_did", methods=["GET"])
def create_did():
    did = DIDManager.create_did()
    return jsonify({"did": did})

@app.route("/issue_credential", methods=["POST"])
def issue_credential():
    data = request.json
    signed_credential = CredentialIssuer.issue_credential(data["user_id"], data["name"], data["email"])
    return jsonify({"credential": signed_credential})

@app.route("/verify_credential", methods=["POST"])
def verify_credential():
    signed_credential = request.json["credential"]
    verification_result = CredentialVerifier.verify_credential(signed_credential)
    return jsonify(verification_result)
