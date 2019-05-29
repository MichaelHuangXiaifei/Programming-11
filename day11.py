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
        # suits are the same... cheak ranks
        return self.rank < other.rank

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


class Deck:
    """Represents a set of cards"""

    def pop_card(self):
        return self.cards.pop(0)

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        # for i in range(len(self.cards) - 1):  # 这个循环负责设置冒泡排序进行的次数
        #     for j in range(len(self.cards) - i - 1):  # j为列表下标
        #         if self.cards[j].suit > nums[j + 1].suit:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
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


Queen_of_diamonds = Card(1, 12)

Jack_of_Hearts = Card(2, 11)

# Deck
card1 = Card(2, 11)
card2 = Card(2, 12)

deck = Deck()

deck.shuffle()
print(deck)
deck.sort()
print(deck)
