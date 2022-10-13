from django.shortcuts import render

from datetime import date

posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'image1.jpg',
        'author': 'Hussien',
        'date': date(2021, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared "
                   "for what happened whilst I was enjoying the view! ",
        'content': "Messor peregrinationes, tanquam brevis absolutio."
                   "Messis acceleratrix ducunt ad germanus rumor."
                   "Secundus saga absolute quaestios agripeta est."
                   "\n"
                   "Messor peregrinationes, tanquam brevis absolutio."
                   "Messis acceleratrix ducunt ad germanus rumor."
                   "Secundus saga absolute quaestios agripeta est."
                   "\n"
                   "Messor peregrinationes, tanquam brevis absolutio."
                   "Messis acceleratrix ducunt ad germanus rumor."
                   "Secundus saga absolute quaestios agripeta est."
                   "\n",

    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
    },
    {
        "slug": "into-the-woods",
        "image": "image3.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
    },
]


def get_date(post):
    return post.get('date')

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(posts, key=get_date)
    # sorted_posts = sorted(posts, key=lambda post: post.get('date'))
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts_page(request):
    sorted_posts = sorted(posts, key=get_date)
    return render(request, 'blog/all-posts.html', {
        'posts': sorted_posts
    })


def post_detail(request, slug):
    # simple searching algorithm
    chosen_post = None
    for post in posts:
        if post['slug'] == slug:
            chosen_post = post
            break

    return render(request, 'blog/post-details.html', {
        'post': chosen_post
    })
