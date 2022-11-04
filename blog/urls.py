from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts', views.posts_page, name='posts-page'),
    path('posts/<uuid:uuid>', views.post_detail,
         name='post-detail-page'),   # /posts/my-first-post
]
