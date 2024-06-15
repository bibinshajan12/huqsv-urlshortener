# urlshortener/tests/test_forms.py

from urlshortener.forms import URLForm

def test_urlform_valid():
    form = URLForm(data={'original_url': 'https://www.samplesite.com','username': 'testuser'})
    print(f'the form data is {form}')
    assert form.is_valid()

def test_urlform_invalid():
    form = URLForm(data={'original_url': 'not-a-url'})
    assert not form.is_valid()
