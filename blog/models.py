from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self) -> str:
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=25)


    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)


    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])


    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")