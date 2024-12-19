from fastapi import FastAPI
from .db import models
from .db.database import async_engine
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {"message": 'Hello World!'}

if __name__=="__main__":
    uvicorn.run("main:app",port=8000, reload=True)
