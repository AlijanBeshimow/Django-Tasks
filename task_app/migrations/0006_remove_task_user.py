# Generated by Django 4.2.7 on 2024-01-25 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0005_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]