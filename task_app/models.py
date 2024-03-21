from django.db import models
from django.contrib.auth.models import User


def get_category_choices():
    return [
        ('Home', 'Home'),
        ('Job', 'Job'),
        ('Shop', 'Shop'),
        ('Travel', 'Travel'),
        ('Sport', 'Sport'),
        ('Cleaning', 'Cleaning'),
        ('Notes', 'Notes'),
    ]


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=get_category_choices)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
