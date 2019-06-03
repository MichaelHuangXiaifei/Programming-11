# card game
import random


# def bubble_sort(nums):
#     for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
#         for j in range(len(nums) - i - 1):  # j为列表下标
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     return nums


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

    def __init__(self, suit=0, rank=2):
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


class Player:
    """Represents a set of cards on player's hand"""

    def __init__(self):
        self.cards = []


def handout_cards(deck, player1, player2):
    while deck.cards != []:
        player1.cards.append(deck.pop_card_from_top())
        player2.cards.append(deck.pop_card_from_top())


player1 = Player()
player2 = Player()
deck = Deck()

deck.shuffle()

handout_cards(deck, player1, player2)

print(player1.cards)
