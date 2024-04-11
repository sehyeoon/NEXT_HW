from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']

class ReplyForm(forms.Form):
    content = forms.CharField(label='대댓글', widget=forms.Textarea)