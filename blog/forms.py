from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'body': 'Content',
            'image': 'Image',
            'image_url': 'Image Url',
            'author': 'Author',
        }
        
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-shadow'
            self.fields[field].label = False
