#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_60306_L06_BKelly.py
# NAME:State Abbreviation Guessing Game
# AUTHOR(s): Brenden Kelly
# DATE: 04/16/2022
# PURPOSE: Test the user's knowledge of state abbreviations via a guessing game.

lineBreak = "#"*60
#print out more description for use:
print(lineBreak)



#Script main body
import random

#State list data derived from .csv list available at https://worldpopulationreview.com/states/state-abbreviations
states={'AL':'Alabama','AK':'Alaska','AZ':'Arizona','AR':'Arkansas','CA':'California','CO':'Colorado','DE':'Delaware','HI':'Hawaii','ID':'Idaho','IL':'Illinois','IN':'Indiana','KS':'Kansas','KY':'Kentucky','LA':'Louisiana','MD':'Maryland','MA':'Massachusetts','MI':'Michigan','MN':'Minnesota','MS':'Mississippi','MO':'Missouri','MT':'Montana','NE':'Nebraska','NH':'New Hampshire','NJ':'New Jersey','NY':'New York','ND':'North Dakota','OH':'Ohio','OK':'Oklahoma','OR':'Oregon','PA':'Pennsylvania','RI':'Rhode Island','SD':'South Dakota','TN':'Tennessee','TX':'Texas','UT':'Utah','VT':'Vermont','VA':'Virginia','WA':'Washington','WV':'West Virginia','WI':'Wisconsin','WY':'Wyoming'}

#Variables
wins = 0
losses = 0
wrongABR = list()
guessed = list()
ABRlist=list(states.keys())

#Functions:
#Introduction to game
def intro():
	print("Welcome to the State Abbreviation Guessing Game!! (United States only)")
	print("\nYou will be given an abbreviation and asked to type in the full state name.")
	pchoice=input('\nWould you like to play this awesome game? y/n ')
	if pchoice.lower()=='y':
		play()
	else:
		print("\nIt's okay, have a great day!")

#Core gameplay
def play():
	global wins
	global losses
	answer=random.choice(ABRlist)
	guessed.append(answer)
	user=input("\nWhat is the full state name of "+answer+": ? ")
	if user.lower() == states[answer].lower():
		print('\nNice job, you are correct!')
		wins += 1
	else:
		print('\nThat is incorrect, the correct answer is:',states[answer])
		losses += 1
		wrongABR.append(answer)
	print('\nWin count:',wins)
	print('Loss count:',losses)
	if wrongABR==[]:
		print('You have not missed any yet, keep it up!')
	else:
		print('The abbreviations you have missed:',wrongABR)
	pa()

#Play again question
def pa():
	pachoice=input('\nWould you like to play again? y/n ')
	if pachoice == 'y':
		play()
	else:
		print("\nIt's okay, have a great day!")

#Main
def main():
	try:
		intro()
	except:
		print('Something went wrong, please follow the instructions and try again:')
		intro()

#Run program
if __name__ == '__main__':
    main()


print(lineBreak)



#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))



