from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    exp = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.name} {self.exp}"
