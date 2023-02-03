from datetime import date
from django.shortcuts import render
from django.http import Http404

# Create your views here.
data = [
    {
        "slug": "hike-in-the-mountain",
        "image": "anipsycho.jpg",
        "author": "Daniil",
        "date": date(2023, 2, 3),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened while I was enjoing the view!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
        """
    },
    {
        "slug": "workout",
        "image": "asspower.jpg",
        "author": "Daniil",
        "date": date(2023, 1, 15),
        "title": "Body Training",
        "excerpt": "It's time to fuck your protein power and fuck your muscles!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
        """
    },
    {
        "slug": "cybernetic",
        "image": "vovseneobed.jpg",
        "author": "Daniil",
        "date": date(2023, 1, 27),
        "title": "Cybernetic and AI",
        "excerpt": "Cybernetic scientists have developed new cyborg and AI for this!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis adipisci, officia et ad nulla temporibus vel, numquam velit qui dolorum quasi corrupti eos unde natus fugit itaque amet quae alias.
        """
    },
]

def get_date(post):
    return post['date']


def index(request):
    sorted_data = sorted(data, key=get_date)
    latest_posts = sorted_data[-3:]
    return render(request, 'blog/index.html', {"posts": latest_posts})


def show_posts(request):
    return render(request, 'blog/all-posts.html', {"posts": data})


def post_detail(request, slug):
    post = next(post for post in data if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {"post": post})
