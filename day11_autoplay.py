# auto play card games
import random


class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5',
                  '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __lt__(self, other):
        # check the suits
        if self.rank < other.rank:
            return True
        if self.rank > other.rank:
            return False
        # ranks are the same... check suit
        return self.suit < other.suit

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


class Deck:
    """Represents a set of cards"""

    def pop_card_from_top(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)


class Player:
    """Represents a player"""

    def get_card(self, deck, number):
        for i in range(number):
            self.cards.append(deck.pop_card_from_top())

    def pop_card_from_top(self):
        return self.cards.pop(0)

    def top_card(self):
        return self.cards[0]

    def __init__(self):
        self.cards = []


class Desk:
    """Represents the cards on desk"""

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def __init__(self):
        self.cards = []


the_deck = Deck()
the_deck.shuffle()

desk = Desk()

player1 = Player()
player2 = Player()

player1.get_card(the_deck, 26)
player2.get_card(the_deck, 26)

while True:
    desk.cards.append(player1.pop_card_from_top())
    desk.cards.append(player1.pop_card_from_top())
    if player1.cards == [] or player2.cards == []:
        break
