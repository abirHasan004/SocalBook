# Generated by Django 4.2.9 on 2024-01-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0007_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='POSTIMAGE/'),
        ),
    ]
