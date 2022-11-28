from django.shortcuts import render
from .models import Author, Post, Tag


# Create your views here.


def starting_page(request):
    sorted_posts = Post.objects.all().order_by('-date')
    # sorted_posts = sorted(posts, key=lambda post: post.get('date'))
    latest_posts = sorted_posts[0:3]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts_page(request):
    sorted_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        'posts': sorted_posts
    })


def post_detail(request, slug):
    chosen_post = Post.objects.get(slug=slug)
    return render(request, 'blog/post-details.html', {
        'post': chosen_post
    })
