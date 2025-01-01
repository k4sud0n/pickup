import os
import uuid
from typing import List

from django.conf import settings
from ninja import Router, UploadedFile, File, Form
from ninja.security import django_auth
from pydantic import BaseModel

from board.models import Board


router = Router()


class BoardSchema(BaseModel):
    id: int
    name: str
    author: str
    description: str
    created_at: str

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


@router.get("", response=List[BoardSchema])
def get_item(request):
    articles = Board.objects.all().order_by("-created_at")
    return articles
