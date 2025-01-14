# Generated by Django 4.2.7 on 2024-01-07 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialApp', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='POST',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='POSTIMAGE')),
                ('Captions', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
