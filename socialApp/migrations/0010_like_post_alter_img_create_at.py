# Generated by Django 4.2.9 on 2024-01-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0009_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='img',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]