from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project

class ArticleCreationForm(ModelForm):
    # # 'placeholder': '???'
    # WYSIWYG ;
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style':'height:auto; text-align: left;'})) # class와 style 미리 지정

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        # fields = ['title', 'image', 'content']
        fields = ['title', 'image', 'project', 'content']
