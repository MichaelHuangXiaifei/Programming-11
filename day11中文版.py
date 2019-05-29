# card game


class Card:
    """Represents a standard playing card."""

    suit_names = ['梅花', '方片', '红桃', '黑桃']
    rank_names = ['无', 'A', '2', '3', '4', '5',
                  '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        # suits are the same... cheak ranks
        return self.rank < other.rank

    def __str__(self):
        return "%s%s" % (Card.suit_names[self.suit], Card.rank_names[self.rank])

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


class Deck:
    """Represents a set of cards"""

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


Queen_of_diamonds = Card(1, 12)

Jack_of_Hearts = Card(2, 11)

# Deck
card1 = Card(2, 11)
card2 = Card(2, 12)
print(card1.__lt__(card2))

deck = Deck()
print(deck)
