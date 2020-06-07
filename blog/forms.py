from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    content=forms.CharField(label="",widget=forms.Textarea(
        attrs={'class':'form-control',
        'placeholder':'text goes here',
        'rows':'4','cols':'50'}))
    class meta:
        model=Comment
        fields=['content']