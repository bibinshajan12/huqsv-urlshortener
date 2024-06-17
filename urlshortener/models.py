from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

class ShortURL(models.Model):
    """
    A model representing a shortened URL.

    Attributes:
        original_url (str): The original long URL.
        short_url (str): The shortened URL.
    """
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    created_by = models.CharField(max_length=150, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Saves the generated value onto the database
        """
        if not self.short_url:
            self.short_url = get_random_string(10)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the model.
        """

        return f'{self.short_url} - {self.original_url}'
