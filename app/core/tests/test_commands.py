from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTests(TestCase):
    def test_wait_for_db_ready(self):
        # test waiting for a db when db is available
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)
    
    # we can override the wait function by using the following decorator
    # Because we have a return value in the decorator, we have to pass in another argument in our function
    # even if we don't use it in the function. 
    # To speed up the test, we dont want to wait for sleep
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        # Test Waiting for DB
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)


