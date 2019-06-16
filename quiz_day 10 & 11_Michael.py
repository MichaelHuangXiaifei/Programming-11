import random


class Card:
    """Represents a standard playing card.

    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return "%s of %s" % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.

        returns: boolean
        """
        if self.rank < other.rank:
            return True
        if self.rank > other.rank:
            return False
        return self.suit < other.suit


class Deck:
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """

    def __init__(self):
        """Initializes the Deck with 52 cards.
        """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns a string representation of the deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck.

        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.

        card: Card
        """
        self.cards.remove(card)

    def pop_card(self, position=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(position)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand_name, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for num in range(num):
            hand_name.add_card(self.pop_card())


class Hand(Deck):
    """Represents a poker hand."""

    def __str__(self):
        return "score:%d, win_round:%d" % (self.score, self.win_round)

    def __init__(self):
        self.cards = []
        self.score = 0
        self.win_round = 0

    # def suit_hist(self):
    #     """Builds a histogram of the suits that appear in the hand.
    #
    #     Stores the result in attribute suits.
    #     """
    #     self.suits = {}
    #     for card in self.cards:
    #         self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        suit_hist = {}
        for card in self.cards:
            suit_hist[card.suit] = suit_hist.get(card.suit, 0) + 1
        for val in suit_hist.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise."""
        rank_hist = {}
        for card in self.cards:
            rank_hist[card.rank] = rank_hist.get(card.rank, 0) + 1
        for val in rank_hist.values():
            if val == 2:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has two pair, False otherwise."""
        rank_hist = dict()
        rank_hist_hist = dict()
        for card in self.cards:
            rank_hist[card.rank] = rank_hist.get(card.rank, 0) + 1
        for rank in rank_hist.values():
            rank_hist_hist[rank] = rank_hist.get(rank, 0) + 1
        for val in rank_hist_hist.values():
            if val == 2:
                return True
        return False


deck = Deck()
deck.shuffle()

player1 = Hand()
player2 = Hand()

for rounds in range(3):

    deck.move_cards(player1, 5)
    deck.move_cards(player2, 5)

    for time in range(5):
        player1.shuffle()
        player2.shuffle()

        player1_card = player1.pop_card()
        player2_card = player2.pop_card()

        if player1_card > player2_card:
            player1.score += 1
        elif player2_card > player1_card:
            player2.score += 1

        deck.add_card(player1_card)
        del player1_card
        deck.add_card(player2_card)
        del player2_card

    if player1.score >= 3:
        player1.win_round += 1
    elif player2.score >= 3:
        player2.win_round += 1

    player1.score = 0
    player2.score = 0

if player1.win_round > player2.win_round:
    print("player 1 win")
elif player2.win_round > player1.win_round:
    print("player 2 win")
else:
    print("tie(should never appear)")
