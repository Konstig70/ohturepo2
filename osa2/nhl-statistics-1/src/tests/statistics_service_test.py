import unittest
from statistics_service import StatisticsService
from player_reader_stub import PlayerReaderStub
from player import Player

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_haetaan_pelaaja(self):
        #Haetaan ensin oikea pelaaja
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")
        #Nyt haetaan ei löytyvää
        self.assertEqual(self.stats.search("eilöydy"), None)

    def test_haetaan_joukkue(self):
        #Haetaan joukkue, mikä löytyy
        self.assertEqual(len(self.stats.team("EDM")), 3)
        #Haetaan ei löytyvä
        self.assertEqual(len(self.stats.team("EILÖYDY")), 0)

    def test_top(self): 
        #Otetaan validi määrä
        self.assertEqual(len(self.stats.top(2)), 3)
        #Otetaan epävalidi määrä
        self.assertEqual(len(self.stats.top(2000)), 5)
