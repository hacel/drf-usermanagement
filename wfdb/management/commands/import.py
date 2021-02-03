from django.core.management.base import BaseCommand, CommandError
from wfdb.models import URL


class Command(BaseCommand):
    help = 'Generate random URLs'

    def handle(self, *args, **options):
        for i in range(1000):
            tmp = URL(url=f'http://example.com/{i}/', action=URL.ALLOW)
            tmp.save()

        self.stdout.write(self.style.SUCCESS('Done'))
