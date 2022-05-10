from django import forms
from .models import Comment, Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('author_name', 'comment_text')

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title', 'sub_title', 'contents', 'image')