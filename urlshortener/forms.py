# from django import forms
# from .models import ShortURL

# class URLForm(forms.ModelForm):
#     class Meta:
#         model = ShortURL
#         fields = ['original_url']
#         widgets = {
#             'original_url': forms.URLInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter the original URL'
#             })
#         }
from django import forms

class URLForm(forms.Form):
    original_url = forms.URLField(
        label='Enter URL to shorten',
        max_length=200,
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL here'})
    )
    username = forms.CharField(
        widget=forms.HiddenInput()
    )

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        super(URLForm, self).__init__(*args, **kwargs)
        if username:
            self.fields['username'].initial = username
