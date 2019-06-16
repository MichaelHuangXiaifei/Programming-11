# Texas Hold’em poker
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

    # def suit_hist(self):
    #     """Builds a histogram of the suits that appear in the hand.
    #
    #     Stores the result in attribute suits.
    #     """
    #     self.suits = {}
    #     for card in self.cards:
    #         self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise."""
        rank_hist = dict()
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

    def has_three_of_a_kind(self):
        """Returns True if the hand has a pair, False otherwise."""
        rank_hist = dict()
        for card in self.cards:
            rank_hist[card.rank] = rank_hist.get(card.rank, 0) + 1
        for val in rank_hist.values():
            if val == 3:
                return True
        return False

    def has_straight(self):
        rank_hist = dict()
        for card in self.cards:
            rank_hist[card.suit] = rank_hist.get(card.rank, 0) + 1
        if rank_hist.get(13, 0) >= 1:
            if rank_hist.get(1, 0) >= 1:
                rank_hist[14] = rank_hist[1]
                del rank_hist[1]
        rank_list = list()
        for rank in rank_hist:
            for time in range(rank_hist[rank]):
                rank_list.append(rank)
        rank_list.shuffle()


    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        suit_hist = dict()
        for card in self.cards:
            suit_hist[card.suit] = suit_hist.get(card.suit, 0) + 1
        for val in suit_hist.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        """Returns True if the hand has full house, False otherwise."""
        if self.has_three_of_a_kind():
            rank_hist = dict()
            for card in self.cards:
                rank_hist[card.rank] = rank_hist.get(card.rank, 0) + 1
            for number in rank_hist.values():
                if number == 2:
                    return True
        return False

    def has_four_of_a_kind(self):
        """Returns True if the hand has four of a kind, False otherwise."""
        rank_hist = dict()
        for card in self.cards:
            rank_hist[card.rank] = rank_hist.get(card.rank, 0) + 1
        for val in rank_hist.values():
            if val == 4:
                return True
        return False

    def has_straight_flush(self):
        pass

    # def __str__(self):
    #     for card in self.cards:

    def __init__(self, label=""):
        self.cards = []
        self.label = label


deck = Deck()
deck.shuffle()

# deal the cards and classify the hands
for i in range(10):
    hand = Hand()
    deck.move_cards(hand, 5)
    hand.sort()
    # print(hand)
    print(hand.has_two_pair())
