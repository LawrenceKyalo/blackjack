from deck import Deck
from card import Card
from hand import Hand

deck1 = Deck()
deck1.shuffle()

hand1 = Hand()
hand1.add_card(deck1.deal(2))

hand1.display()




