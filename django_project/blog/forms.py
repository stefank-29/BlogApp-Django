from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Leave a comment...'}))

    class Meta: 
        model = Comment
        fields = ['comment']