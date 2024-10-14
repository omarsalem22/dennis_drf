from django.db import models

# Create your models here.

class Advocate(models.Model):
    username=models.CharField(max_length=50)
    bio=models.TextField(max_length=300,null=True,blank=True)

    def __str__(self) -> str:
        return self.username
