from django import forms
from .models import *
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class DiscussionModelForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['subject','category', 'text']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]



