# check_superusers.py
import os

from django.contrib.auth import get_user_model

User = get_user_model()

superuser_password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
superuser_args = {
    "username": os.environ.get("DJANGO_SUPERUSER_USERNAME"),
    "email": os.environ.get("DJANGO_SUPERUSER_EMAIL"),
}

# Mock user details inspired by top Ukrainian restaurants
mock_users = [
    {"username": "KyivBorscht", "email": "kyivborscht@example.com", "password": "borscht123"},
    {"username": "LvivGalushka", "email": "lvivgalushka@example.com", "password": "galushka123"},
    {"username": "OdessaSeafood", "email": "odessaseafood@example.com", "password": "seafood123"},
    {"username": "DniproDelight", "email": "dniprodelight@example.com", "password": "delight123"},
    {"username": "ZaporizhzhiaZest", "email": "zaporizhzhiazest@example.com", "password": "zest123"},
]

def create_user(user_args, is_superuser=False):
    user_filter = User.objects.filter(username=user_args["username"], email=user_args["email"])
    if user_filter.exists():
        print(f"[INFO] User already exists - {user_args['username']} - {user_args['email']}")
    else:
        if is_superuser:
            user = User.objects.create_superuser(**user_args)
        else:
            user = User.objects.create_user(**user_args)
        print(f"[SUCCESS] Created {'superuser' if is_superuser else 'user'} - {user_args['username']} - {user_args['email']}")

# Create superuser
if superuser_args["username"] and superuser_args["email"] and superuser_password:
    superuser_args['password'] = superuser_password
    create_user(superuser_args, is_superuser=True)

# Create mock users
for user_args in mock_users:
    create_user(user_args)
