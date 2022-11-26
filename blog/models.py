import uuid
from django.db import models
from django.utils.text import slugify


# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Author(models.Model):
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    title = models.CharField(max_length=150, unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return f'{self.uuid}: {self.title}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Post, self).save(force_insert, force_update, using, update_fields)
