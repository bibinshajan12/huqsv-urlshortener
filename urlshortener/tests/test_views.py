# urlshortener/tests/test_views.py

import pytest
from django.urls import reverse
from urlshortener.models import ShortURL

@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'Short URL Service' in response.content.decode()

@pytest.mark.django_db
def test_create_short_url(client):
    response = client.post(reverse('home'), {'original_url': 'https://www.example.com'})
    assert response.status_code == 200
    assert ShortURL.objects.count() == 1
    short_url = ShortURL.objects.first()
    assert 'Your URL has been shortened!' in response.content.decode()
    assert f"http://127.0.0.1:8000/{short_url.short_url}" in response.content.decode()

@pytest.mark.django_db
def test_redirect_to_original(client):
    short_url = ShortURL.objects.create(original_url='https://www.example.com')
    response = client.get(reverse('redirect', args=[short_url.short_url]))
    assert response.status_code == 302
    assert response['Location'] == 'https://www.example.com'
