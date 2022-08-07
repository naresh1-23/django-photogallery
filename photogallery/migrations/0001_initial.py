# Generated by Django 4.1 on 2022-08-07 04:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=150)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoname', models.CharField(default=None, max_length=100)),
                ('photo', models.ImageField(default=None, upload_to='')),
                ('posted_at', models.DateField(default=datetime.datetime.now)),
                ('album', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='photogallery.album')),
            ],
        ),
    ]
