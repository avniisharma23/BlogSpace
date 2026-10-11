from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'content']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter your blog title'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Enter author name'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your story here...',
                'rows': 8
            }),
        }