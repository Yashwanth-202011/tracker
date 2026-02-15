import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'period_tracker.settings')
django.setup()

User = get_user_model()

# Create Girl User (now called 'user')
if not User.objects.filter(username='user').exists():
    User.objects.create_user(username='user', password='user@123', role='user')
    print("User 'user' created with password 'user@123'")

# Create Admin User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(username='admin', password='admin@123', role='admin')
    print("User 'admin' created with password 'admin@123'")
