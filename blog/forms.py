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
            'body': 'Paragraph 1',
            'body_one': 'Paragraph 2',
            'body_two': 'Paragraph 3',
            'body_three': 'Paragraph 4',
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
            self.fields[field].widget.attrs['class'] = 'input-shadow \
                border-black rounded-0'
            self.fields[field].label = False
