from django import forms
from .models import Blog

class WriteForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['category','title','blog','preview','author','reading_time']
        widgets = {
            'preview': forms.Textarea(attrs={'rows':3, 'cols':50,'placeholder':'Write a brief preview to you article.'}),
            'blog': forms.Textarea(attrs={'placeholder':'Start writing...'}),
            'reading_time': forms.TextInput(attrs={'placeholder':'Aproximate reading time in minutes'}),
        }
       