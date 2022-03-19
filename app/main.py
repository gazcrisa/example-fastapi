from fastapi import FastAPI

from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import Settings
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)
origins = ["https://www.google.com"]

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():       
    return {"message": "Hello World"}
