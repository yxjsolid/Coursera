#####################################################
# Student should insert code for Hand class here
import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        ret =  "Hand contains "
        for card in self.cards:
            ret += str(card) + " "
        return ret

    def get_value(self):
        ret = 0
        cnt_A = 0
        for card in self.cards:
            rank = card.get_rank()
            val = VALUES[rank]

            if val == 1:
                cnt_A += 1
                ret += 11
            else:
                ret += val

        while cnt_A > 0:
            if ret > 21:
                ret -= 10
            cnt_A -= 1

        return ret

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)

        self.shuffle()

    def __str__(self):
        ret = "#Deck contains"
        for card in self.cards:
            ret += " "
            ret += str(card)

        return ret

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)

def Deal():
