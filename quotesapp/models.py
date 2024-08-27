from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    born_date = models.DateField(null=False)
    bio = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f"{self.name}"

class Quote(models.Model):
    text = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f"{self.text}"
