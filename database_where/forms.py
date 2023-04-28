from django import forms

from database_where.models import Comment


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
