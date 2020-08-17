"""
    date:       2020/8/17 2:15 下午
    written by: neonleexiang
"""
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
