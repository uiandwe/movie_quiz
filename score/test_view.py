from django.test import TestCase


class TestScoreView(TestCase):

    def test_index(self):
        response = self.client.get('/score/')
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        response = self.client.get('/score/', {'pk': '1'})
        self.assertEqual(response.status_code, 200)