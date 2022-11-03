import uuid
from django.db import models


# Create your models here.

class Author(models.Model):
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    excerpt = models.TextField()
    content = models.TextField()
    image_location = models.ImageField()
    date = models.DateField(auto_now=True, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return f'{self.uuid}: {self.title}'
