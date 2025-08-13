#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# python manage.py createsuperuser --no-input
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); \
if not User.objects.filter(username='admin').exists(): \
    User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword')"
