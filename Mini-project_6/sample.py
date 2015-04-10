# Mini-project #6 - Blackjack

import simplegui
import random

CARD_PAD = 5
DEALER_CARD_POS = (0, 0)
PLAYER_CARD_POS = (0, 200)
FONT_SIZE = 30
# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player = None
dealer = None
deck = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
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

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)



# define hand class
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

    def drawScore(self, canvas, pos):
        x, y = pos
        score = self.get_value()

        canvas.draw_text('score:', (x, y + FONT_SIZE), FONT_SIZE, 'Yellow')
        y += 12
        if score > 21:
            color = "Red"
        else:
            color = "Yellow"
        canvas.draw_text(str(score), (x, y + FONT_SIZE), FONT_SIZE, color)



    def draw(self, canvas, pos, hideHole=False):
        self.drawScore(canvas, pos)

        x, y = pos
        x += FONT_SIZE * 10
        for index, card in enumerate(self.cards):
            if hideHole and index == 0:
                card.draw_back(canvas, (x, y))

            else:
                card.draw(canvas, (x, y))
            x += CARD_SIZE[0] + CARD_PAD


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



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer
    # your code goes here
    in_play = True
    deck = Deck()
    player = Hand()
    dealer = Hand()

    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())


def hit():
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global outcome, in_play, deck, player, dealer

    if in_play:
        player.add_card(deck.deal_card())
        val = player.get_value()
        if val > 21:
            in_play = False
            result()
    else:
        stand()

def stand():
    global outcome, in_play, deck, player, dealer
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    if in_play:
        while in_play:
            dealer.add_card(deck.deal_card())
            val = dealer.get_value()
            if val > 21:
                in_play = False
            elif val >= 17:
                in_play = False

    result()


def result():
    pass

# draw handler
def draw(canvas):
    global outcome, in_play, deck, player, dealer
    dealer.draw(canvas, DEALER_CARD_POS, in_play)
    player.draw(canvas, PLAYER_CARD_POS)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


