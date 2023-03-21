import random
cards = []
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
        cards.append([suit, rank])

random.shuffle(cards)

cards_file = open("cards_file.txt", "w")
for card in cards:
    cards_file.write(str(card) + "\n")
cards_file.close()

cards_file = open("cards_file.txt", "r")
cards_read = cards_file.read()
cards_list = (cards_read.split("\n"))
cards_file.close()

def shuffle():
    random.shuffle(cards_list)

def deal(number: int):
    cards_dealt = []
    for x in range(number):
        card = cards_list.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()
card = deal(1)[0]

print(card)
