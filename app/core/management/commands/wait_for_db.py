import time
from django.db import connections
# this will execute when DB is not available 
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # Django command to pause execution until dB is available

    def handle(self, *args, **options):
        self.stdout.write('waiting for Database...')
        db_conn = None
        
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('database unavailable,  waiting on second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
