#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_60306_L08Final_BKelly.py
# NAME:Movie Trivia Game
# AUTHOR(s): Brenden Kelly
# DATE: 05/14/2022
# PURPOSE: Test the user's movie trivia knowledge with multiple choice questions.

lineBreak = "#"*60
#print out more description for use:
print(lineBreak)



#Script main body
import random

#global score variables
score=0
misses=0

#Questions and answers each in their own dictionary
q1 = {'ques':'In the movie "Blade", what type of metal was deadly to vampires?','correct':'Silver','b':'Copper','c':'Magnesium','d':'Gold'}

q2 = {'ques':'In the movie "Pulp Fiction", what weapon does Butch (Bruce Willis) finally choose in the pawn shop?','a':'Chainsaw','b':'Baseball bat','correct':'Katana','d':'Shotgun'}

q3 = {'ques':'In Harry Potter, what is the spell to disarm opponents?','a':'Stupify','b':'Sectum Sempra','c':'Reducto','correct':'Expelliarmus'}

q4 = {'ques':'In Harry Potter, what is the Animagus form of Professor McGonagall?','correct':'Cat','b':'Pigeon','c':'Black dog','d':'Beetle'}

q5 = {'ques':'In the Lord of the Rings the Fellowship of the Ring, who said "It comes in pints?!"','correct':'Pippin','b':'Merry','c':'Frodo','d':'Gimli'}

q6 = {'ques':'In Top Gun, what is the callsign of Mavericks plane?','a':'Iceman','b':'Tomcat','c':'Sundown','correct':'Ghost Rider'}

q7 = {'ques':'In Star Wars Return of the Jedi, what type of starfighter crashes into the Super Star Destroyer bridge during the final battle over the moon of Endor?','correct':'A-Wing','b':'B-Wing','c':'X-Wing','d':'Tie Fighter'}

q8 = {'ques':'How many computer-generated effects were used in the movie Lord of the Rings - Return of the King?','a':'540','b':'799','c':'1205','correct':'1488'}

q9 = {'ques':'In the movie "The Blues Brothers", what does Jake order at the diner?','a':'A medium pizza with pineapple and ham','b':'3 cheeseburgers with the works and a tall glass of milk','correct':'4 fried chickens and a Coke','d':'A small Greek salad with extra feta, a steak (well done), 2 baked potatoes, and a coffee'}

q10 = {'ques':'In the movie "The Last Starfighter", what is the name of the experimental weapon used by Alex in the final battle?','a':'Meteor Cannon','correct':'Death Blossom','c':'Photon Torpedo','d':'Excalibur'}

#List of all question dictionaries
qlist=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

#Play function, contains majority of program
def Play():
    global score
    global misses
    letters=['a','b','c','d']
    cqlist=qlist
    counter=5
    print('\nPlease choose your answer to these 3 randomly chosen multiple choice questions. Your score will display at the end.\n*And no using Google!*\n')        
    while counter > 0:
        #Allows random selection from question pool
        item=random.choice(cqlist)
        cqlist.remove(item)
        counter -= 1
        #Below section is putting keys of question into a list for indexing & printing
        currentq=list(item.keys())
        print(item[currentq[0]])
        print('a - ',item[currentq[1]])
        print('b - ',item[currentq[2]])
        print('c - ',item[currentq[3]])
        print('d - ',item[currentq[4]])
        ans=input('\nWhat is your answer? ')
        try:
            if ans.lower() in letters and ans not in currentq:
                print("\nThat's the correct answer!\n")
                score += 1
                counter -= 1
            else:
                #Anything entered that's not a-d will also result in an incorrect guess
                print("\nUnfortunately that's not the correct answer.\n")
                misses += 1
                counter -= 1
        except:
            print("Something went wrong, this guess didn't count.")
            continue
    ScoreDisplay()

#Function for replaying
def PlayAgain():
    pa = input('\nDo you want to play again? y/n ')
    if pa.lower() == 'y':
        Play()
    elif pa.lower() == 'n':
        print('\nThanks for playing, have a nice day!\n')
    else:
        print('\nPlease only enter "y" or "n".')
        PlayAgain()

#Displays score of correct and incorrect answers
def ScoreDisplay():
    global score
    global misses
    print('\nThe score so far:')
    print('\nCorrect answers: ',score,'\nIncorrect answers: ',misses)
    PlayAgain()
        
def main():
    print('Welcome to the best Movie Trivia Game in the world!')
    Play()

#Run program
if __name__ == '__main__':
    main()


print(lineBreak)



#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))



