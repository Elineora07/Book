# Generated by Django 4.0.4 on 2022-05-29 13:24

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.models.carousel_upload_to)),
                ('header', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=150)),
            ],
        ),
    ]