from unittest.mock import patch  # Simulate db being available or not

from django.core.management import call_command  # Call the command in our sc
from django.db.utils import OperationalError  # Db being unavailable error
from django.test import TestCase


class CommandTest(TestCase):

    def test_for_db_ready(self):
        """Test waiting for db when db is available"""
        # This will mock the connection handler overriding it to return True
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')  # The name of the command
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)  # Replace the behavior of sleep
    def test_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
