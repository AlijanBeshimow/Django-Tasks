# Generated by Django 4.2.7 on 2024-01-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0011_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('work', 'Work'), ('personal', 'Personal'), ('shop', 'Shop'), ('cleaning', 'Cleaning'), ('sport', 'Sport'), ('other', 'Other')], default=None, max_length=20),
        ),
    ]
