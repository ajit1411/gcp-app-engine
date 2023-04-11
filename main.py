from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["Authorization"],
    allow_methods=["*"],
    allow_credentials=True
)

@app.get("/user/info")
def get_user_info(req: Request, res: Response):
    try:
        return {
            "status": True,
            "data": {
                "username": "fastapi_developer",
                "email": "user@fastapi.com",
                "contact": "1234567890"
            }
        }
    except Exception as error:
        print(f"Error:{get_user_info.__name__}::{error}")
        return {
            "status": False,
            "data": {
                "error": "Unauthorized"
            }
        }