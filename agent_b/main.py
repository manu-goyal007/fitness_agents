# agent_b/main.py
from fastapi import FastAPI, Header, HTTPException
from agent_b.utils import send_email
from descope_mock import validate_token

app = FastAPI(title="Agent B - Messaging Agent")

@app.post("/send_message/")
def send_message(to_email: str, message: str, authorization: str = Header(...)):
    # Validate token
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = authorization.split(" ")[1]
    try:
        validate_token(token, required_scope="message.send")
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))
    
    # Send email
    send_email(to_email, "Your Fitness Tip", message)
    return {"status": "success", "to": to_email}

