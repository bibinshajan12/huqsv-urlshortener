# urlshortener/tests/test_models.py

import pytest
from urlshortener.models import ShortURL

@pytest.mark.django_db
def test_shorturl_creation():
    original_url = 'https://www.example.com'
    short_url = ShortURL.objects.create(original_url=original_url)
    assert short_url.original_url == original_url
    assert len(short_url.short_url) == 6
