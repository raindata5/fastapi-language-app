
from fastapi import FastAPI

from .routers import users, languages, auth, spokenlanguages

from .db import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware
# models.Base.metadata.create_all(bind=engine)

origins =[
    "*"
]


    
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(spokenlanguages.router)
app.include_router(users.router)
app.include_router(languages.router)
app.include_router(auth.router)








# redis_client.set('apidatastarbucks01', json.dumps({"location":"Miami"}))


@app.get('/')
def home():
    return {"message": "Connected ^_"}