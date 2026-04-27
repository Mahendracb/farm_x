import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username="farmer").exists():
    user = User.objects.create_user(username="farmer", email="farmer@karnataka.gov.in", password="password123")
    user.first_name = "Ramesh"
    user.last_name = "Gowda"
    user.save()
    print("User 'farmer' created successfully.")
else:
    print("User 'farmer' already exists.")
