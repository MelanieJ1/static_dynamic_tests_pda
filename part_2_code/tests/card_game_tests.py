import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("Diamond", 1)
        self.card_2 = Card("Diamond", 5)
        self.cards = [self.card_1, self.card_2]
        self.card_round = CardGame([self.card_1, self.card_2])

    def test_for_ace(self):
        self.assertTrue(1, self.card_round.check_for_ace(self.card_1))

    
    def test_for_highest_card(self):
        self.assertEqual(self.card_2, self.card_round.highest_card(self.card_1, self.card_2))


    def test_can_total_cards(self):
        self.assertEqual("You have a total of 6", self.card_round.cards_total(self.cards))



    
    
