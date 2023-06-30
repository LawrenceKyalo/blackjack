from deck import Deck
from card import Card
from hand import Hand
from game import Game

#function to start game
def start():
    #create Game class instance
    g = Game()
    #call play method on game class instance
    g.play()

#run start function to start game
start()