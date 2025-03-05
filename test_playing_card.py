import unittest

from playing_card import PlayingCard, Deck, Hand

class TestPlayingCard(unittest.TestCase):

    def test_valid_card(self):
        card = PlayingCard("A", "Hearts")
        self.assertEqual(str(card), "A of Hearts")

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            PlayingCard("1", "Hearts")

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            PlayingCard("A", "Stars")

    def test_card_equality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("10", "Diamonds")
        self.assertEqual(card1, card2)

    def test_card_inequality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("J", "Diamonds")
        self.assertNotEqual(card1, card2)

class TestDeck(unittest.TestCase):
    
    def test_deck_generation(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_shuffle(self):
        deck = Deck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)  # Shuffling should change the order
        self.assertEqual(len(deck.cards), 52)  # Should still have 52 cards

    def test_draw_card(self):
        deck = Deck()
        card = deck.draw_card()
        self.assertIsInstance(card, PlayingCard)
        self.assertEqual(len(deck.cards), 51)  # Deck should now have 51 cards

    def test_draw_from_empty_deck(self):
        deck = Deck()
        for _ in range(52):
            deck.draw_card()
        self.assertIsNone(deck.draw_card())  # Drawing from an empty deck should return None

class TestHand(unittest.TestCase):
    
    def test_add_card(self):
        hand = Hand()
        card = PlayingCard("K", "Spades")
        hand.add_card(card)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(str(hand.cards[0]), "K of Spades")

    def test_display_hand(self):
        hand = Hand()
        card1 = PlayingCard("Q", "Hearts")
        card2 = PlayingCard("5", "Diamonds")
        hand.add_card(card1)
        hand.add_card(card2)
        self.assertEqual(hand.display_hand(), "Q of Hearts, 5 of Diamonds")

    def test_card_count(self):
        hand = Hand()
        self.assertEqual(hand.card_count(), 0)
        hand.add_card(PlayingCard("3", "Clubs"))
        self.assertEqual(hand.card_count(), 1)

if __name__ == "__main__":
    unittest.main()

