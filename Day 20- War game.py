# 11 = J, 12= Q, 13 = K, 14 = A
import random

card_values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ["clubs", "hearts", "diamonds", "spades"]

face_cards= {
    "J":11,
    "Q":12,
    "K":13,
    "A":14,
    11:"J",
    12:"Q",
    13:"K",
    14:"A",
}


class Card:
    
    def __init__(self,value, suit) -> None:
        self.value = value
        self.suit = suit
        
def generate_cards():
        cards = []
        for value in card_values:
            for suit in suits:
                if value in face_cards:
                    _card = Card(face_cards[value],suit)
                else:
                    _card = Card(value, suit)
                cards.append(_card)
        return cards
    
    
cards = generate_cards()
for card in cards:
    print(card.value, card.suit)
    
    

def split_deck(cards=cards):
    yours = random.sample(cards, 26)
    opp = [i for i in cards if i not in yours]
    random.shuffle(opp)
    return yours, opp


your_cards , opp_cards = split_deck()

def draw(cards):
    return cards.pop(0)

def play_turn(yours= your_cards, opp=opp_cards):
    your_play = draw(yours)
    opp_play =draw(opp)
    your_val = your_play.value if your_play.value not in face_cards else face_cards[your_play.value]
    opp_val = opp_play.value if opp_play.value not in face_cards else face_cards[opp_play.value]
    print(f"Your play: {your_val} {your_play.suit}")
    print(f"Opp play: {opp_val} {opp_play.suit}")
    if your_val > opp_val:
        yours.append(your_play)
        yours.append(opp_play)
    elif opp_val > your_val:
        opp.append(your_play)
        opp.append(opp_play)
    else:
        yours.append(your_play)
        opp.append(opp_play)
    return yours, opp


yours, opp = play_turn()
counter= 0
while yours and opp:
    counter += 1
    yours, opp = play_turn(yours, opp)
    print(counter)
    print(len(yours), len(opp))
    if len(yours) == 0:
        print("You Lose!")
    if len(opp) == 0:
        print("You Win!")   