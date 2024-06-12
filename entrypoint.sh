#!/bin/bash

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Check if the superuser exists and create one if it doesn't
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
EOF

# Run the Django server
exec "$@"
