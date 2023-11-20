import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    def test_top_points(self):
        top_scores = self.stats.top(1, SortBy.POINTS)
        self.assertEqual(str(top_scores[0]), "Gretzky EDM 35 + 89 = 124")
    def test_top_goals(self):
        top_scores = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(str(top_scores[0]), "Lemieux PIT 45 + 54 = 99")
    def test_top_assists(self):
        top_scores = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(str(top_scores[0]), "Gretzky EDM 35 + 89 = 124")
    def test_search(self):
        self.assertEqual(str(self.stats.search("Gretzky")), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(self.stats.search("Connor McDonalds")), "None")
    def test_team(self):
        self.assertEqual(str(self.stats.team("EDM")[2]), "Gretzky EDM 35 + 89 = 124")