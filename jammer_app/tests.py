from django.test import TestCase, Client

class TestJammingView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_start_jamming(self):
         response = self.client.post('/jammer_app/start_jamming/')
         self.assertEqual(response.status_code, 200)

    def test_start_jamming_invalid_method(self):
        response = self.client.get('/jammer_app/start_jamming/')
        self.assertEqual(resonse.status_code, 405)

    def test_stop_jamming(self):
        response = self.client.post('/jammer_app/stop_jamming')
        self.assertEqual(response.status_code, 200)
    
    def test_stop_jamming_invalid_method(self):
        response = self.client.get('/jammer_app/stop_jamming')
        self.assertEqual(response.status-code, 405)
