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

    classification = ["pair", "two pair", "three of a kind", "straight",
                      "flush", "full house", "four of a kind", "straight flush", "royal flush"]

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
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has two pair, False otherwise."""
        rank_hist = dict()
        times = 0
        for card in self.cards:
            rank_hist[card.rank] = rank_hist.get(card.rank, 0) + 1
        for val in rank_hist.values():
            if val >= 2:
                times += 1
        if times >= 2:
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
        rank_list = list()
        accumulator = 0
        for card in self.cards:
            rank_list.append(card.rank)
        rank_list.sort()
        if 1 not in rank_list:
            for times in range(4):
                # if times == 3 and rank_list[times + 1] == 1:
                #     rank_list[times + 1] = 14
                if rank_list[times] + 1 == rank_list[times + 1]:
                    accumulator += 1
            if accumulator >= 4:
                return True
        else:
            for times in range(4):
                # if times == 3 and rank_list[times + 1] == 1:
                #     rank_list[times + 1] = 14
                if rank_list[times] + 1 == rank_list[times + 1]:
                    accumulator += 1
            if accumulator >= 4:
                return True
            accumulator = 0
            for rank in range(len(rank_list)):
                if rank_list[rank] == 1:
                    rank_list[rank] = 14
            for times in range(4):
                # if times == 3 and rank_list[times + 1] == 1:
                #     rank_list[times + 1] = 14
                if rank_list[times] + 1 == rank_list[times + 1]:
                    accumulator += 1
            if accumulator >= 4:
                return True
        return False
        # rank_hist = dict()
        # accumulator = 0
        # for card in self.cards:
        #     rank_hist[card.suit] = rank_hist.get(card.rank, 0) + 1
        # if rank_hist.get(13, 0) >= 1:
        #     if rank_hist.get(1, 0) >= 1:
        #         rank_hist[14] = rank_hist[1]
        #         del rank_hist[1]
        # rank_list = list()
        # for rank in rank_hist:
        #     for time in range(rank_hist[rank]):
        #         rank_list.append(rank)
        # rank_list.sort()
        # for rank in range(len(rank_list) - 1):
        #     if rank_list[rank] + 1 == rank_list[rank + 1]:
        #         accumulator += 1
        # if accumulator >= 4:
        #     return True
        # return False

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
        """Returns True if the hand has straight flush, False otherwise."""
        if self.has_straight():
            if self.has_flush():
                return True
        return False

    def has_royal_flush(self):
        """Returns True if the hand has royal flush, False otherwise."""
        if self.has_straight():
            if self.has_flush():
                for card in self.cards:
                    if card.rank == 1:
                        return True

    def classify(self):
        """Check the hand and change it label"""
        if self.has_royal_flush():
            self.label = Hand.classification[8]
        elif self.has_straight_flush():
            self.label = Hand.classification[7]
        elif self.has_four_of_a_kind():
            self.label = Hand.classification[6]
        elif self.has_full_house():
            self.label = Hand.classification[5]
        elif self.has_flush():
            self.label = Hand.classification[4]
        elif self.has_straight():
            self.label = Hand.classification[3]
        elif self.has_three_of_a_kind():
            self.label = Hand.classification[2]
        elif self.has_two_pair():
            self.label = Hand.classification[1]
        elif self.has_pair():
            self.label = Hand.classification[0]

    # def __str__(self):
    #     for card in self.cards:

    def __init__(self, label="high card"):
        self.cards = []
        self.label = label


# # deal the cards and classify the hands
# for i in range(10):
#     hand = Hand()
#     deck.move_cards(hand, 5)
#     hand.sort()
#     # print(hand)
#     print(hand.has_two_pair())


def proportion(hist):
    total = 0
    for value in hist.values():
        total += value
    if "high card" in hist:
        print("high card: %.5f%%" % (hist["high card"] / total * 100))
    if "pair" in hist:
        print("pair: %.5f%%" % (hist["pair"] / total * 100))
    if "two pair" in hist:
        print("two pair: %.5f%%" % (hist["two pair"] / total * 100))
    if "three of a kind" in hist:
        print("three of a kind: %.5f%%" % (hist["three of a kind"] / total * 100))
    if "straight" in hist:
        print("straight: %.5f%%" % (hist["straight"] / total * 100))
    if "flush" in hist:
        print("flush: %.5f%%" % (hist["flush"] / total * 100))
    if "full house" in hist:
        print("full house: %.5f%%" % (hist["full house"] / total * 100))
    if "four of a kind" in hist:
        print("four of a kind: %.5f%%" % (hist["four of a kind"] / total * 100))
    if "straight flush" in hist:
        print("straight flush: %.5f%%" % (hist["straight flush"] / total * 100))
    if "royal flush" in hist:
        print("royal flush: %.5f%%" % (hist["royal flush"] / total * 100))


classification_hist = dict()

for i in range(2598960):  # 2598960
    deck = Deck()
    deck.shuffle()
    hand0 = Hand()
    deck.move_cards(hand0, 5)
    hand0.classify()
    # if hand0.label == "pair":
    #     print(hand0)
    classification_hist[hand0.label] = classification_hist.get(hand0.label, 0) + 1
    del hand0
    del deck
# print(classification_hist)
proportion(classification_hist)
