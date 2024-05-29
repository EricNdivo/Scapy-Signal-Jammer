from django.test import TestCase, Client
from unittest.mock import patch

class TestJammingView(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('jammer_app.views.jam_wireless_networks')
    def test_start_jamming(self, mock_jam_wireless_networks):
        response = self.client.post('/start_jamming/', {'interface': 'wlan0'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'Jammng started'})

    @patch('jammer_app.views.jamming', True)
    def test_start_jamming_already_in_progress(self):
        response = self.client.post('/start_jamming/', {'interface': 'wlan0'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responsejson(), {'status': 'jamming already in progress'})