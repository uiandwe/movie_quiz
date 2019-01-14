# Generated by Django 2.1.2 on 2019-01-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.CharField(max_length=255)),
                ('dateFolderPath', models.CharField(max_length=255)),
                ('fileName', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, default='', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='dateFolderPath',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='fileName',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='folder',
        ),
    ]
