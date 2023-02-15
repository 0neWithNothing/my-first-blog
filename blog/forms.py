from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

        labels = {
            "user_name": "Your Name",
            "email": "Your Email Address",
            "text": "Your Comment"
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            },
            "email": {
                "required": "Your email address must not be empty!",
            },
            "text": {
                "required": "Your can't send empty message!",
                "max_length": "Please enter a shorter text!"
            },
        }