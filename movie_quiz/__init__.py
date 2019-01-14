import os
from django.conf import settings

media_path = os.path.dirname(os.path.abspath(__file__)) + "/../" + getattr(settings, "MEDIA_URL", None)

if not os.path.exists(media_path):
    os.makedirs(media_path)
