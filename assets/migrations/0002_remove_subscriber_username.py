# Generated by Django 4.2.2 on 2023-06-13 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("assets", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="subscriber", name="username",),
    ]
