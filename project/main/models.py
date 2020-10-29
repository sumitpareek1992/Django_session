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
    email = models.EmailField(max_length=30 ,default="")
    d_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="Department")

    def __str__(self):
        return self.name