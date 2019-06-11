import random


class Time:
    """Represent a time object. Attributes: hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%d:%d:%d" % (self.hour, self.minute, self.second)


class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5',
                  '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        # suits are the same... check ranks
        return self.rank < other.rank

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank


class Deck:
    """Represents a set of cards"""

    def pop_card_from_top(self):
        return self.cards.pop(0)

    def random_pop_card(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

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


class Hand(Deck):
    """Represents a hand of playing cards"""

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def __init__(self, label=''):
        self.cards = []
        self.label = label


time0 = Time(25, 30, 2)
deck = Deck()
deck.shuffle()


# 11.1
def mul_time(time, number):
    total_second = time.hour * 3600 + time.minute * 60 + time.second
    total_second *= number
    hour = total_second / 3600
    minute = total_second % 3600 / 60
    second = total_second % 60
    return Time(hour, minute, second)


print(mul_time(time0, 2))


# 11.2
def average_pace(finishing_time, distance):
    total_second = finishing_time.hour * 3600 + finishing_time.minute * 60 + finishing_time.second
    total_second /= distance
    hour = total_second / 3600
    minute = total_second % 3600 / 60
    second = total_second % 60
    return Time(hour, minute, second)


print(average_pace(time0, 2))


# 11.3
def deal_hands(number_of_hands, number_of_cards_per_hand):
    hands = []
    for hand in range(number_of_hands):
        hand = Hand('hand%d' % hand)
        for i in range(number_of_cards_per_hand):
            hand.add_card(deck.pop_card_from_top())
        hands.append(hand)
    return hands


print(deal_hands(2, 2))
