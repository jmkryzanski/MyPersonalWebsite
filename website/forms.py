from django import forms
from django.forms import fields
from .models import Post, Profile, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Body'
            }),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        #fields = '__all__'
        fields = ('bio',)
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Bio'
            }),
        }