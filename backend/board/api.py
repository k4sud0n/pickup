import os
import uuid
from typing import List

from django.conf import settings
from ninja import Router, UploadedFile, File
from ninja.security import django_auth
from pydantic import BaseModel

from board.models import Board


router = Router()


class CreateBoardSchema(BaseModel):
    title: str
    content: str


class BoardSchema(BaseModel):
    id: int
    title: str
    author: str
    content: str
    created_at: str

    class Config:
        from_attributes = True


def get_random_filename(original_filename):
    ext = os.path.splitext(original_filename)[1]
    return f"{uuid.uuid4().hex}{ext}"


@router.post("/create", auth=django_auth)
def create_article(request, data: CreateBoardSchema, file: UploadedFile = File(...)):
    random_filename = get_random_filename(file.name)
    file_path = os.path.join("uploads", random_filename)
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    board = Board.objects.create(
        title=data.title,
        content=data.content,
        author=request.user,
        image=file_path,
    )
    return {"message": "작성 완료", "id": board.id}


@router.get("", response=List[BoardSchema])
def get_articles(request):
    articles = Board.objects.all().order_by("-created_at")
    return articles
