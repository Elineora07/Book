# Generated by Django 4.0.4 on 2022-05-31 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_en',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_uz',
        ),
    ]
