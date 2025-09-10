# descope_mock.py

import jwt
import time

DESCOPE_SECRET = "K32VatiRXlrlz0rcYBXu2FiKwxe6Feoa6FyMUjfuiz6vZLAHBrhzqE4o5fj3wnkMwfe3CRZ"  # Replace with real key in prod

def generate_token(agent_id, scopes, delegated_user=None):
    payload = {
        "sub": agent_id,
        "scopes": scopes,
        "exp": int(time.time()) + 3600,
    }
    if delegated_user:
        payload["delegation"] = delegated_user
    token = jwt.encode(payload, DESCOPE_SECRET, algorithm="HS256")
    return token

def validate_token(token, required_scope):
    try:
        decoded = jwt.decode(token, DESCOPE_SECRET, algorithms=["HS256"])
        if required_scope not in decoded.get("scopes", []):
            raise Exception("Scope not allowed")
        return decoded
    except Exception as e:
        raise Exception(f"Token validation failed: {str(e)}")