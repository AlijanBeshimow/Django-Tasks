# Generated by Django 5.0.2 on 2024-03-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0020_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Work', 'Work'), ('Shop', 'Shop'), ('Travel', 'Travel'), ('Sport', 'Sport'), ('Other', 'Other')], max_length=20),
        ),
    ]
