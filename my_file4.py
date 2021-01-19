# rock, paper scisoor
from random import randint

# move for the players

Moves = ["rock", "paper", "scissors"]
while True:
    computer = Moves[randint(0,2)]
    players = input("rock paper or scissors (end the game) ").lower()
    if players== "end the game":
        print('game has ended')
        break

    if players==computer:
         print("Tie!")
    elif players=="rock":
         if computer== "paper":
          print("You Lose!", computer, "beats", players)
         else:
             print("you Win!", players, "beats", computer)
    elif players=="paper":
         if computer== "scissors":
          print("You Lose!", computer, "beats", players)
         else:
             print("you Win!", players, "beats", computer)
    elif players=="scissors":
         if computer== "rock":
          print("You Lose!", computer, "beats", players)
         else:
             print("you Win!", players, "beats", computer)
    else:
        print("Check Your Spelling......!")

