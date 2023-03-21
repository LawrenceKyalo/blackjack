import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": None}, 
            {"rank": "2", "value": None}, 
            {"rank": "3", "value": None}, 
            {"rank": "4", "value": None}, 
            {"rank": "5", "value": None}, 
            {"rank": "6", "value": None}, 
            {"rank": "7", "value": None}, 
            {"rank": "8", "value": None}, 
            {"rank": "9", "value": None}, 
            {"rank": "10", "value": None}, 
            {"rank": "J", "value": None}, 
            {"rank": "K", "value": None}, 
            {"rank": "Q", "value": None}
            ]

        for rank in ranks:
            if rank["rank"] == 'A':
                rank["value"] = 11
            elif rank["rank"] == 'J' or rank["rank"] == 'Q' or rank["rank"] == 'K':
                rank["value"] = 10
            else:
                rank["value"] = rank["rank"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number: int):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt



