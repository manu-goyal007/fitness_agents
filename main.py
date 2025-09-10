# def main():
#     print("Hello from fitness-agents!")
#     from agent_b.utils import send_email

#     send_email("recipient@example.com", "Test Email", "Hello! This works.")


# if __name__ == "__main__":
#     main()

import time
from fastapi import FastAPI

app=FastAPI()


@app.get("/123")
def read_root(sting: str = "world"):
    print("Hello from fitness-agents!")
    return {f"message" f"Hello{sting} from fitness-agents!"}

