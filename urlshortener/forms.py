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
from django.core.validators import URLValidator


class URLForm(forms.Form):
    """
    The Form is used to gather the info from the user and then use that to shorten the URL specified

    Args:
        forms (_type_): Initialize the capture the form inputs and validate the same

    Raises:
        forms.ValidationError: Validations errors on the URL as a whole(for instance, the structure, path and type)
        forms.ValidationError: Scheme related errors on the input URL

    Returns:
        _type_: _description_
    """
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
    
    def clean_original_url(self):
        original_url = self.cleaned_data.get('original_url')
        url_validator = URLValidator()
        try:
            url_validator(original_url)
        except ValidationError:
            raise forms.ValidationError('Enter a valid URL.')
        if not original_url.startswith(('http://', 'https://')):
            raise forms.ValidationError('URL must start with http:// or https://')

        return original_url
