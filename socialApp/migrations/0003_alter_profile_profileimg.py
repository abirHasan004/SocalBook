# Generated by Django 4.2.7 on 2024-01-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0002_profile_loc_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='default-avatar-icon-of-social-media-user-vector.jpg', upload_to='profile_image'),
        ),
    ]
