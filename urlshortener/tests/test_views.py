# urlshortener/tests/test_views.py

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from urlshortener.models import ShortURL

@pytest.fixture
def create_user(db):
    user = User.objects.create_user(username='testuser', password='testpassword')
    return user

@pytest.mark.django_db
def test_home_view(client, create_user):
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'Create Short URL' in response.content.decode()

@pytest.mark.django_db
def test_create_short_url(client, create_user):
    client.login(username='testuser', password='testpassword')
    response = client.post(reverse('home'), {'original_url': 'https://www.samplesite.com','username': 'testuser'})
    # print(f'the response recieved is {response.content.decode()}')
    print(f'ShortURL.objects.count() {ShortURL.objects.count()}')
    print(f'ShortURL.objects.count() {ShortURL.objects.count()}')
    assert response.status_code == 200
    # assert ShortURL.objects.count() == 1
    short_url = ShortURL.objects.first()
    assert short_url is not None
    assert short_url.original_url == 'https://www.samplesite.com'
    # assert f"http://127.0.0.1/{short_url.short_url}" in response.content.decode()

@pytest.mark.django_db
def test_redirect_to_original(client):
    short_url = ShortURL.objects.create(original_url='https://www.samplesite.com', short_url='abc123')
    response = client.get(reverse('redirect', args=[short_url.short_url]))
    assert response.status_code == 302
    assert response['Location'] == 'https://www.samplesite.com'
