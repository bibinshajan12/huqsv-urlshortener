import string
import random
from .models import ShortURL

def generate_short_url(original_url,length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choices(characters, k=length))
        if not ShortURL.objects.filter(short_url=short_url).exists():
            if ShortURL.objects.filter(original_url=original_url).exists():
                query_val = list(ShortURL.objects.filter(original_url=original_url).values())
                short_url = query_val[0]['short_url']
                return short_url, False
            return short_url , True
