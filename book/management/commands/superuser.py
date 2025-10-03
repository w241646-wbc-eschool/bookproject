import os # コード修正（6-4（P.308））

# コード追記（6-4（P.303））
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options ):
        if not User.objects.filter(username = 'your_name').exists():
            User.objects.create.superuser(
                # username = 'w241646',
                username = os.environ.get('SUPERUSER_NAME'), # コード修正（6-4（P.308））
                email = '',
                # password = 'pass',
                password = os.environ.get('SUPERUSER_PASS'), # コード修正（6-4（P.308））
            )