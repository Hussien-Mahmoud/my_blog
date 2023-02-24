from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Author, Post, Tag, User, Comment
from .forms import CommentForm


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

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # --------getting or making a new user--------
            data = comment_form.cleaned_data
            user, _ = User.objects.get_or_create(
                name=data.get('name'),
                email=data.get('email'),
            )
            # --------------------------------------------

            # --------checking the post parameter--------
            uuid = request.POST.get('post-id') or ''
            post = Post.objects.filter(uuid=uuid).first()
            if post is None:
                return HttpResponseBadRequest()
            # -------------------------------------------

            # ----------creating a new comment----------
            Comment.objects.create(
                user=user,
                text=data.get('comment'),
                post=post
            )
            # ------------------------------------------

        else:
            return HttpResponseBadRequest()

    chosen_post = Post.objects.get(slug=slug)
    return render(request, 'blog/post-details.html', {
        'post': chosen_post,
        'comment': CommentForm,
    })
