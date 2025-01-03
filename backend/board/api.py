import os
import uuid
from typing import List

from django.conf import settings
from django.contrib.auth import get_user_model
from ninja import Router, UploadedFile, File, Form
from ninja.security import django_auth
from pydantic import BaseModel

from board.models import Board


router = Router()

User = get_user_model()


class ListSchema(BaseModel):
    id: int
    name: str
    author: str
    image: str
    price: int
    created_at: str
    likes: int

    class Config:
        from_attributes = True


class DetailSchema(BaseModel):
    id: int
    name: str
    author: str
    description: str
    image: str
    price: int
    created_at: str
    likes: int

    class Config:
        from_attributes = True


def get_random_filename(original_filename):
    ext = os.path.splitext(original_filename)[1]
    return f"{uuid.uuid4().hex}{ext}"


@router.post("/create", auth=django_auth)
def create_item(
    request,
    name: str = Form(...),
    description: str = Form(...),
    price: int = Form(...),
    file: UploadedFile = File(...),
):
    random_filename = get_random_filename(file.name)
    file_path = os.path.join("uploads", random_filename)
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    item = Board.objects.create(
        name=name,
        author=request.user,
        image=file_path,
        description=description,
        price=price,
    )
    return {"message": "작성 완료", "id": item.id}


@router.get("", response=List[ListSchema])
def get_item_list(request):
    items = Board.objects.all().order_by("-created_at")
    return [
        {
            "id": item.id,
            "name": item.name,
            "author": item.author.username,
            "image": item.image.url,
            "price": item.price,
            "created_at": item.created_at.isoformat(),
            "likes": item.likes,
        }
        for item in items
    ]


@router.get("/{user}", response={200: List[ListSchema], 404: dict})
def get_all_item_from_user(request, user: str):
    try:
        user_obj = User.objects.get(username=user)
    except User.DoesNotExist:
        return 404, {"message": "User not found"}

    items = Board.objects.filter(author=user_obj).order_by("-created_at")
    return [
        {
            "id": item.id,
            "name": item.name,
            "author": item.author.username,
            "image": item.image.url,
            "price": item.price,
            "created_at": item.created_at.isoformat(),
            "likes": item.likes,
        }
        for item in items
    ]


@router.get("/{user}/{item_id}", response={200: DetailSchema, 404: dict})
def get_specific_item_from_user(request, user: str, item_id: int):
    if not user or not user.strip():
        return 400, {"message": "Invalid user"}

    try:
        user_obj = User.objects.get(username=user)
    except User.DoesNotExist:
        return 404, {"message": "User not found"}

    try:
        item = Board.objects.get(author=user_obj, id=item_id)
    except Board.DoesNotExist:
        return 404, {"message": "Item not found"}

    return {
        "id": item.id,
        "name": item.name,
        "author": item.author.username,
        "image": item.image.url,
        "description": item.description,
        "price": item.price,
        "created_at": item.created_at.isoformat(),
        "likes": item.likes,
    }
