from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from ninja import Router
from django.contrib.auth import get_user_model
from pydantic import BaseModel

router = Router()
User = get_user_model()


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(BaseModel):
    username: str
    password: str


@router.post("/login")
def login_user(request, data: LoginSchema):
    user = authenticate(username=data.username, password=data.password)
    if user is not None:
        login(request, user)
        return {"success": f"Welcome {user.username}"}
    return {"error": "Invalid username or password"}


@router.post("/register")
def register(request, data: RegisterSchema):
    try:
        user = User.objects.create(
            username=data.username,
            password=make_password(data.password),
        )
        return {"success": f"User {user.username} created successfully"}
    except IntegrityError:
        return {"error": "Username already exists"}
