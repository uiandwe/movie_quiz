from django.db import models
from core.models import TimeStampeModel, FileModel
import os
import time
import datetime
from django.db import models
from uuid import uuid4


def path_and_rename(instance, filename):
    """ 파일 저장 경로 로직 """
    now = time.time()
    upload_to = datetime.datetime.fromtimestamp(now).strftime('%Y%m%d')
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class MovieFile(models.Model):
    file = models.FileField(blank=True, default='', upload_to=path_and_rename)

    class Meta:
        ordering = ['-id']


class Movie(TimeStampeModel):
    """ 한글 저장 케릭터셋 변경 ALTER TABLE movie_movie convert to charset utf8; """
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='movie', on_delete=models.CASCADE, null=False)
    file_id = models.ForeignKey(MovieFile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Classification(TimeStampeModel):
    class_text = models.CharField(max_length=100, null=False)


class MovieClassificationBridge(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    classification_id = models.ForeignKey(Classification, on_delete=models.CASCADE)
