from django.db import models

# Create your models here.


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    group_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name