import os

media_path = os.path.dirname(os.path.abspath(__file__)) + "/.."+'media'

if not os.path.exists(media_path):
    os.makedirs(media_path)
