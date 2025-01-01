from django.conf import settings
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/", null=False)
    price = models.PositiveIntegerField(null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
