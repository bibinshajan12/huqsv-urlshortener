from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ShortURL
from .forms import URLForm
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlparse

@login_required
def home(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    form = URLForm(username=request.user.username)
    shortened_url = None
    print(f'call from pytestttt with {request.user.username}')
    if request.method == 'POST':
        form = URLForm(request.POST, username=request.user.username)
        print(f'the form status is {form.errors}')
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            username = form.cleaned_data['username']
            print(f'the original url is {original_url}')
            # short_url = ShortURL.objects.create(original_url=original_url, created_by=username)
            # shortened_url = request.build_absolute_uri('/') + short_url.short_url
            original_url = form.cleaned_data['original_url']
            parsed_url = urlparse(original_url)
            short_url_instance = ShortURL.objects.create(original_url=original_url, created_by=request.user.username)
            # Construct the shortened URL using the scheme and netloc of the original URL
            shortened_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{short_url_instance.short_url}"
            print(f'the short_url url is {short_url_instance} and{shortened_url}')

    user_urls = ShortURL.objects.filter(created_by=request.user.username)
    return render(request, 'urlshortener/home.html', {'form': form, 'shortened_url': shortened_url, 'user': request.user, 'user_urls': user_urls})

@login_required
def run_tests(request):
    if request.method == 'POST':
        try:
            result = subprocess.run(
                ['pytest', '--tb=short', '-q'],
                capture_output=True,
                text=True,
                cwd='/app'  # Ensure the working directory is correct
            )
            output = result.stdout + '\n' + result.stderr
        except Exception as e:
            output = str(e)
        return JsonResponse({'output': output})
    return render(request, 'urlshortener/test_results.html')

def redirect_to_original(request, short_url):
    short_url_obj = get_object_or_404(ShortURL, short_url=short_url)
    return redirect(short_url_obj.original_url)

# @csrf_exempt
# def autosave_url(request):
#     if request.method == 'POST':
#         form = URLForm(request.POST)
#         if form.is_valid():
#             original_url = form.cleaned_data['original_url']
#             short_url, created = ShortURL.objects.get_or_create(original_url=original_url)
#             if created:
#                 short_url.created_by = request.user.username
#                 short_url.save()
#             return JsonResponse({'short_url': request.build_absolute_uri('/') + short_url.short_url})
#     return JsonResponse({'error': 'Invalid request'}, status=400)



@login_required
def view_saved_urls(request):
    """This is used view the saved/generaetd urls for the used

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered saved URL page.
    """
    urls = ShortURL.objects.all()
    return render(request, 'urlshortener/saved_urls.html', {'urls': urls})

def documentation(request):
    """This is will give the entire autogenerated documentation structure for the URL shortener code base

    Args:
        request: The HTTP request object.

    Returns:
        The index.html page of the sphinx autodocumentation script
    """
    return redirect('/docs/_build/html/index.html')
