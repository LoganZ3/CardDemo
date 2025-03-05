import random

class PlayingCard:
    """A playing card class"""
    
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        if not isinstance(other, PlayingCard):
            return False
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    """A deck of 52 playing cards"""
    
    def __init__(self):
        self.cards = self._generate_deck()

    def _generate_deck(self):
        """Generate a full deck of 52 cards."""
        return [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draw a card from the deck. Returns None if the deck is empty."""
        return self.cards.pop() if self.cards else None

class Hand:
    """A hand of playing cards"""
    
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Add a card to the hand."""
        if card:
            self.cards.append(card)

    def display_hand(self):
        """Display the cards in the hand."""
        return ', '.join(str(card) for card in self.cards) if self.cards else "Hand is empty."

    def card_count(self):
        """Return the number of cards in the hand."""
        return len(self.cards)

