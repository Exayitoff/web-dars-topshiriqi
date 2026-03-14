import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django

django.setup()

from django.contrib.auth import get_user_model


username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', '')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if not username or not password:
    print('Skipping admin bootstrap: env vars not set.')
    raise SystemExit(0)

User = get_user_model()
user, created = User.objects.get_or_create(
    username=username,
    defaults={
        'email': email,
        'is_staff': True,
        'is_superuser': True,
    },
)

if email and user.email != email:
    user.email = email

user.is_staff = True
user.is_superuser = True
user.set_password(password)
user.save()

if created:
    print(f'Superuser created: {username}')
else:
    print(f'Superuser updated: {username}')
