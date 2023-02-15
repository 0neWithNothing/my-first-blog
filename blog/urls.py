from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="start-page"),
    path("posts/", views.PostsListView.as_view(), name="posts-page"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post-detail"),
    path("read-later/", views.ReadlaterView.as_view(), name="read-later"),
]
