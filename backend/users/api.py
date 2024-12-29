from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.http import JsonResponse
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
    return JsonResponse(
        {"message": "아이디 또는 비밀번호를 다시 확인하세요"}, status=400
    )


@router.post("/register")
def register(request, data: RegisterSchema):
    try:
        user = User.objects.create(
            username=data.username,
            password=make_password(data.password),
        )
        return {"success": f"User {user.username} created successfully"}
    except IntegrityError:
        return JsonResponse({"message": "이미 사용중인 아이디입니다"}, status=409)
