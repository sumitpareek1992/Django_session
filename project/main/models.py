from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)
    hod = models.CharField(max_length=15)
    dec = models.TextField()

    def __str__(self):
        return self.name
class Students(models.Model):
    s_id = models.IntegerField(default=1)
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    department_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=30 ,default="")

    def __str__(self):
        return self.name