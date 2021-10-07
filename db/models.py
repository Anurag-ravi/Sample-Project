from django.db import models

# Create your models here.
class Alumini(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    profile = models.ImageField(upload_to = "images/", default="profile.jpg")

    def __str__(self):
        return f'{self.name}'