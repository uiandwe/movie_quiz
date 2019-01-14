from django.test import TestCase
from .models import Score


class TestScoreModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        s = Score(userName="Fred Flintstone", score=500)
        s.save()

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_insert_score(self):
        score = Score.objects.get(id=1)
        self.assertEquals(score.score, 500)
        self.assertEquals(score.userName, "Fred Flintstone")


