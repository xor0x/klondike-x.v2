from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'body'}

    def clean_body(self):
        body = self.cleaned_data['body']
        return body




class SearchForm(forms.Form):
    query = forms.CharField()
