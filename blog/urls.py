from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="start-page"),
    path("posts/", views.show_posts, name="posts-page"),
    path("posts/<slug:slug>/", views.post_detail, name="post-detail"),
]
