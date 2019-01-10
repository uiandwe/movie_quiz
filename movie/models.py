from django.db import models
from core.models import TimeStampeModel, FileModel


class Movie(TimeStampeModel, FileModel):
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='movie', on_delete=models.CASCADE, null=False)

