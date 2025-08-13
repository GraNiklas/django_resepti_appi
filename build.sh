#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# python manage.py createsuperuser --no-input
python manage.py shell -c "exec(\"from django.contrib.auth import get_user_model\nUser = get_user_model()\nif not User.objects.filter(username='admin').exists():\n    User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword')\")"
