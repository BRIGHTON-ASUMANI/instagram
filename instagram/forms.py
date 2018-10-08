from django import forms
from .models import Image, Profile

class SubForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
