from app import app
from starlette.middleware.sessions import SessionMiddleware 
from routers import *
from securities import authentication
from models .UserModel import SQLModel
import os
from dotenv import load_dotenv
load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
# Create database tables 
SQLModel.metadata.create_all(bind=engine)


app.include_router(authentication.router, tags=['Authentication'])
