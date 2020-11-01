from django import forms
from .models import Info, Comment

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('person', 'info_about', 'title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('person', 'comment_about', 'text',)
