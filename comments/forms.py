from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ['content_of_comment',]
        widgets= {
            'content_of_comment': forms.Textarea(
                attrs={
                'class': 'form-control',
                'placeholder': 'Your comment'
            })
        }