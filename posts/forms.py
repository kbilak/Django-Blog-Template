from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)