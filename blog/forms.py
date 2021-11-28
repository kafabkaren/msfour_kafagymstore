from django import forms
from .models import PostComment

class CommentForm(forms.ModelForm):
    class Meta:
        Model = PostComment
        fields = ['subject', 'comment']