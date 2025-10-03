# コード追記（6-4（P.303））
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options ):
        if not User.objects.filter(username = 'w241646').exists():
            User.objects.create.superuser(
                username = 'w241646',
                email = '',
                password = 'pass',
            )