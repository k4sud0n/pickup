from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.middleware.csrf import get_token
from ninja import Router
from django.contrib.auth import get_user_model
from ninja.responses import Response
from ninja.security import django_auth
from pydantic import BaseModel

router = Router()
User = get_user_model()


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(BaseModel):
    username: str
    password: str
    confirm_password: str

    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("비밀번호가 일치하지 않습니다.")


@router.get("", auth=django_auth)
def get_user(request):
    return {
        "user": {"username": request.user.username, "id": request.user.id},
    }


@router.get("/csrf-token")
def get_csrf_token(request):
    return {"csrftoken": get_token(request)}


@router.post("/login")
def login_user(request, data: LoginSchema):
    user = authenticate(username=data.username, password=data.password)
    if user is not None:
        login(request, user)
        response = Response({"message": "success", "user": {"username": user.username}})
        response.set_cookie(
            "sessionid", request.session.session_key, httponly=True, samesite="Lax"
        )
        return response
    return {"message": "아이디 또는 비밀번호를 다시 확인하세요"}, 400


@router.post("/register")
def register(request, data: RegisterSchema):
    try:
        data.validate_passwords()
        user = User.objects.create(
            username=data.username,
            password=make_password(data.password),
        )
        return {"message": "success"}
    except IntegrityError:
        return Response({"message": "이미 사용중인 아이디입니다"}, status=409)
    except ValueError as e:
        return Response({"message": str(e)}, status=400)
