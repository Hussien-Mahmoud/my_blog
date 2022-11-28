import uuid

import django.db
from django.db import models
from django.utils.text import slugify
from django import forms
from django.core.exceptions import ValidationError


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
    image = models.ImageField(upload_to='post_images')
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

    def clean(self):
        slug = slugify(self.title)
        try:
            Post.objects.get(slug=slug)  # raise error when nothing found (new slug)
            try:
                Post.objects.get(uuid=self.uuid)    # raise error when uuid not in db (new entity)
            except Post.DoesNotExist:
                # only if the slug is old
                # and the entity is new
                raise forms.ValidationError({'title': "this name can't be slugified because it is used before"})
        except Post.DoesNotExist:
            pass
