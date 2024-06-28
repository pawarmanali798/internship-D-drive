import random
import sys
from enum import Enum

print(" ")
playerChoice=input("Enter.....\n 1 for rock \n 2 for paper \n 3 for Scissors\n\n")#palyerChoice =input from user

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3
    
# print(RPS(2)) #2
# print(RPS.ROCK) #ROCK
# print(RPS['ROCK']) #ROCK
# print(RPS.ROCK.value) #1

player=int(playerChoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1 or 2 or 3")
    
computerChoice=random.choice("123") #by system
computer=int(computerChoice) #str to int

print(" ")
print("Your choice:" + str(RPS(player)).replace('RPS.','')+ ".")
print("computer choice is:" + str(RPS(player)).replace('RPS.','')+ ".")
print(" ")


if player==1 and computer == 3:
    print("😎 You Win")
elif player==2 and computer ==1:
    print("😎 You Win")
elif player==3 and computer==2:
    print("😎You Win")
elif player==computer:
    print("😮Its a Tie")
else:
    print("🐍 Python Wins")





