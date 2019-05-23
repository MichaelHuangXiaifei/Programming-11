class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5',
                  '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


Queen_of_diamonds = Card(1, 12)
print(Queen_of_diamonds)
Jack_of_Hearts = Card(2, 11)
print(Jack_of_Hearts)
