# Generated by Django 4.0.4 on 2022-05-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=45)),
                ('familiya', models.CharField(max_length=45)),
                ('ty', models.IntegerField()),
            ],
        ),
    ]
