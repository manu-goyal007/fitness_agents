# agent_a/main.py
from fastapi import FastAPI
import requests
from descope_mock import generate_token

app = FastAPI(title="Agent A - Fitness Collector")

AGENT_B_URL = "http://127.0.0.1:8081/send_message"  # Agent B endpoint

# Mock fitness data
USER_DATA = {
    "goyalm685@gmail.com": {"steps": 8200, "heart_rate": 70},
    "manavgoyal786@gmail.com": {"steps": 5000, "heart_rate": 80},
}

def summarize_fitness(data):
    steps = data["steps"]
    hr = data["heart_rate"]
    return f"You walked {steps} steps today. Average heart rate: {hr} bpm. Keep going!"

@app.post("/send_fitness_tip/{user_email}")
def send_fitness_tip(user_email: str):
    if user_email not in USER_DATA:
        return {"status": "error", "message": "User not found"}
    
    # Summarize fitness data
    summary = summarize_fitness(USER_DATA[user_email])
    
    # Request token to call Agent B
    token = generate_token(agent_id="agent_a", scopes=["message.send"], delegated_user=user_email)
    
    # Call Agent B
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(AGENT_B_URL, json={"to_email": user_email, "message": summary}, headers=headers)
    return response.json()