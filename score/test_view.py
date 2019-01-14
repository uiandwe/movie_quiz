from django.test import TestCase
from .models import Score
from core.util import log, collectionToDict

class TestScoreView(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        s = Score(userName="Fred Flintstone2", score=500)
        s.save()

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_index(self):
        response = self.client.get('/score/')
        self.count = response.data["count"]
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        response1 = self.client.get('/score/')
        self.count = response1.data["count"]

        response2 = self.client.get('/score/', {'pk': self.count})
        log(collectionToDict(response2))
        self.assertEqual(response2.status_code, 200)