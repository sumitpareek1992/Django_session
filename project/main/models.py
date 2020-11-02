from django.db import models
import random
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver


# Create your models here.
def random_string():
    return str(random.randint(1000, 9999))


class Department(models.Model):
    name = models.CharField(max_length=20)
    hod = models.CharField(max_length=15)
    dec = models.TextField()

    def __str__(self):
        return self.name


class Students(models.Model):
    s_id = models.CharField(max_length=10, default=random_string())
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.EmailField(max_length=30, default="0")
    d_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="Department")
    collage_id = models.CharField(max_length=15, default="0")
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


def pre_save_c_id(sender, instance, *args, **kwargs):
    instance.collage_id = slugify(instance.name[0:1] + "-" + str(instance.age)+"-"+str(instance.s_id))


pre_save.connect(pre_save_c_id, sender=Students)
