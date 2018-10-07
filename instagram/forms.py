from django import forms
from .models import Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
