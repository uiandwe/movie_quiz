# Generated by Django 2.1.2 on 2019-01-18 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20190118_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classification',
            old_name='movies',
            new_name='movie',
        ),
    ]
