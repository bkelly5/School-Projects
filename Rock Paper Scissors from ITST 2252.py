#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE: 2252_60306_L04_Bkelly.py
# NAME: Rock Paper Scissors Game
# AUTHOR(s): Brenden Kelly
# DATE: 03/09/2022
# PURPOSE: Play a game against the computer.

lineBreak = "#"*60
#print out more description for use:
print(lineBreak)



#Script main body
#Global Variables and Import
from random import randint
CompScore = 0
PlayerScore = 0
ties = 0
FirstGame = 0


#Functions
def CompChoice():
    computer=randint(1,3)
    return computer
    # 1 = rock
    # 2 = paper
    # 3 = scissors


def scoring(a):
    global CompScore
    global PlayerScore
    global ties
    if a == 1:
        PlayerScore += 1
    elif a == 2:
        CompScore += 1
    elif a == 3:
        ties += 1


def Play():
    #if/else statement order is based on CompChoice. 1,2,3; 1,2,3; 1,2,3.
    CompChoice()
    computer=CompChoice()
    PlayerChoice=input('\nEnter your choice: rock, paper, or scissors: ')
    player=PlayerChoice.lower()
    if player == 'rock' and computer == 1:
        print('\nYou both picked rock and tied, try again.')
        scoring(3)
        Play()
    elif player == 'rock' and computer == 2:
        print('\nThe computer picked paper and beat your rock.')
        scoring(2)
    elif player == 'rock' and computer == 3:
        print('\nThe computer picked scissors and you beat it with rock.')
        scoring(1)
    elif player == 'paper' and computer == 1:
        print('\nThe computer picked rock and you beat it with paper.')
        scoring(1)
    elif player == 'paper' and computer == 2:
        print('\nYou both picked paper and tied, try again.')
        scoring(3)
        Play()
    elif player == 'paper' and computer == 3:
        print('\nThe computer picked scissors and beat your paper.')
        scoring(2)
    elif player == 'scissors' and computer == 1:
        print('\nThe computer picked rock and beat your scissors.')
        scoring(2)
    elif player == 'scissors' and computer == 2:
        print('\nThe computer picked paper and you beat it with scissors.')
        scoring(1)
    elif player == 'paper' and computer == 3:
        print('\nYou both picked scissors and tied, try again.')
        scoring(3)
        Play()
    elif player == 'dynamite':
        print("\nNice try buddy, stay within the regular rules.")
        Play()
    

def PlayAgain():
    pa = input('Do you want to play again? y/n ')
    if pa == 'y':
        main()
    elif pa == 'n':
        print('\nTotal number of rounds played:',(CompScore + PlayerScore + ties))
        print('\nThe final score is:\nYou: ',PlayerScore,'\nComputer: ',CompScore,'\nTies: ',ties,'\n')
        print('Thanks for playing, have a nice day!\n')


def ScoreDisplay():
    print('\nThe scores so far:')
    print('\nYou: ',PlayerScore,'\nComputer: ',CompScore,'\nTies: ',ties,'\n')
    if CompScore - PlayerScore > 5:
        print('You better tighten up\n')
        PlayAgain()
    elif CompScore - PlayerScore > 10:
        print("You're really not good at this\n")
        PlayAgain()
    elif CompScore - PlayerScore > 25:
        print("This is too painful, I'm ending it now for your sake.\n")
    else:
        PlayAgain()

def welcome():
    global FirstGame
    FirstGame += 1
    game=input('\nShall we play a game? y/n ')
    if game == 'y':
        game2=input('\nEnter 1 for Rock Paper Scissors or 2 for Global Thermonuclear War: ')
        if game2 == '2':
            print("\nSorry that game isn't available until next semester.")
            print("How about a nice game of Rock Paper Scissors?")
        elif game2 == '1':
            print("\nNice choice, let's play:")
    elif game == 'n':
        print("Then why did you come in the first place?\nWe're playing anyway and I choose Rock Paper Scissors.")


def main():
    if FirstGame == 0:
        welcome()
        Play()
        ScoreDisplay()
    else:
        Play()
        ScoreDisplay()


#Run program
main()


print(lineBreak)



#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))



