from django.db import models
from core.models import TimeStampeModel


class Score(TimeStampeModel):
    score = models.IntegerField()
    userName = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']



