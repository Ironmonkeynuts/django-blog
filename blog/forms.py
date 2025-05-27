from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        """
        Form class for users to comment on a post 
        """
        model = Comment
        fields = ('body',)
