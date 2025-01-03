from django.conf import settings
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=200, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/", null=False)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
