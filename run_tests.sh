#!/bin/bash

# Set the Django settings module environment variable
export DJANGO_SETTINGS_MODULE=shorturl.settings

# Run pytest
pytest "$@"
