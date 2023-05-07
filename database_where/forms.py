from django import forms
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render

from database_where.models import Comment, Post


class EmailPostForm(forms.Form):
    Имя = forms.CharField(max_length=25)
    Почта = forms.EmailField()
    Адрес_получателя = forms.EmailField()
    Комментарии = forms.CharField(required=False,
                                  widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    query = forms.CharField()
