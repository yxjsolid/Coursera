import simplegui
import random


CARD_SIZE = (100, 50)
Cards = []

card_a = None
card_b = None
move_cnt = 0

class Card:
    def __init__(self, id):
        self.id = id
        self.x = -1
        self.y = -1
        self.exposed = False
        self.paired = False

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def hit_test(self, pos):
        x, y = pos

        if self.x < x < self.x + CARD_SIZE[0]:
            if self.y < y < self.y + CARD_SIZE[1]:
                return True
        return False

    def draw(self, canvas, x, y):
        self.set_position(x, y)
        # Top left corner = (a, b), Bottom right = (c, d)
        a = x
        b = y
        c = x + CARD_SIZE[0]
        d = y + CARD_SIZE[1]

        if self.is_paired():
            canvas.draw_polygon([(a, b), (a, d), (c, d), (c, b)], 1, "Red", "White")
            canvas.draw_text('%d'%self.id, (a + CARD_SIZE[0]/2 - 10, b + CARD_SIZE[1]/2 + 10), 30, 'Blue')
        elif self.is_exposed():
            canvas.draw_polygon([(a, b), (a, d), (c, d), (c, b)], 1, "Red", "Yellow")
            canvas.draw_text('%d'%self.id, (a + CARD_SIZE[0]/2 - 10, b + CARD_SIZE[1]/2 + 10), 30, 'Blue')

        else:
            canvas.draw_polygon([(a, b), (a, d), (c, d), (c, b)], 1, "Red", "Yellow")

    def reset(self):
        self.exposed = False
        self.paired = False

    def set_paired(self):
        self.paired = True

    def is_paired(self):
        return self.paired

    def set_exposed(self):
        self.exposed = True

    def is_exposed(self):
        return self.exposed


# helper function to initialize globals
def new_game():
    global Cards, card_a, card_b, move_cnt
    card_a = None
    card_b = None
    move_cnt = 0
    if len(Cards) == 0:
        for i in range(8):
            Cards.append(Card(i))

        for i in range(8):
            Cards.append(Card(i))
    else:
        for card in Cards:
            card.reset()


    random.shuffle(Cards)

def get_click_card(pos):
    for card in Cards:
        if card.hit_test(pos):
            return card
    return None

# define event handlers
def mouseclick(pos):
    global card_a, card_b, move_cnt, label
    # add game state logic here
    card = get_click_card(pos)
    if card and not card.is_exposed():
        card.set_exposed()
        if not card_a:
            card_a = card
        elif not card_b:
            move_cnt += 1
            card_b = card
            if card_a.id == card_b.id:
                card_a.set_paired()
                card_b.set_paired()
                card_a = None
                card_b = None
        else:
            if card_a.id != card_b.id:
                card_a.reset()
                card_b.reset()

                card_a = card
                card_b = None
    else:
        pass

    pass


# cards are logically 50x100 pixels in size
def draw(canvas):
    x = 0
    y = 0

    for card in Cards:
        card.draw(canvas, x, y)
        x += CARD_SIZE[0]

        if x >= 800:
            x = 0
            y = CARD_SIZE[1]

    label.set_text('Turns = %d' % move_cnt)
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric