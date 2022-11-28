from django.contrib import admin
from .models import Author, Post, Tag
# from .forms import PostForm

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    # form = PostForm   # can use specific form instead of default
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
