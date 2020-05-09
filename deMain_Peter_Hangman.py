# JHub Coding Scheme (JCS) Module 3: python
#
import random
import os
import sys

star = "*"
lives = 7
blank_challenge_array = []
originalArray = []
matchArray = []
guesses = []
intelligence = {}

wordlist = "word_list.txt" 

def getWord():
    """This function opens, counts lines, randomly chooses, and closes
    the wordlist. Loads the random word into a list, a letter per element.
    the word is a raw format, trailing a \n character which is stripped.
    the newly stripped list is then used to truely calculate original array
    elements.
    """
    
    total_lines_in_wordlist = int(len(open(wordlist).readlines()))
    random_line = (int(random.randint(0, (total_lines_in_wordlist - 1)))) 
    fh = open(wordlist)
    challenge_word = fh.readlines()[random_line]
    challenge_word_length = (len(challenge_word) - 1)
    for i in range(0, len(challenge_word)):
        originalArray.append(challenge_word[i])
        matchArray.append(challenge_word[i])
    if "\n" in originalArray:
        originalArray.remove("\n")
        matchArray.remove("\n")
        
    #print(originalArray) # cheat

    for i in range(0, len(originalArray)):
        blank_challenge_array.append(star)

    fh.close()

def clear():
    """This fuction is for clearing the terminal to keep it tidy."""
    os.system("cls")
    os.system("clear")

def takeLife(lives):
    """This function subtracts 1 life from the lives count."""
    l = lives - 1
    lives = l
    
    #print(lives)
    takeInput(lives)

def gameOver(lives):
    """When you run out of lives this fc"""
    print("")
    print("You loose!")
    print("")
    print("You have ",lives," lives left.")
    print(*originalArray,sep="")
    sys.exit(0)

def win():
    """This fucntion ends the programe when the word is guessed and, reviels
    the word"""
    clear()
    print("")
    print(*originalArray,sep="")
    print("Congratulations, YOU WIN!")
    sys.exit(0)

    
def takeInput(lives):
    """This function takes user input and validates it, along with learning
    how many letter of the alfabet are in the word for iteration in the check
    funciton."""
    clear()
    
    if lives == 0:
        gameOver(lives)
        
    #print(*originalArray,sep="")
    #print(guesses)
    print("You have ",lives," lives left.")
    print(*blank_challenge_array,sep="")
    ui = input("Please enter your next guess: ")

    while len(ui) < 1 or len(ui) > 1:
       # print("Are you playing??")
        ui = input("Please enter your next guess: ")
        
    check(ui,lives)

def intel(intelligence,originalArray):
    """using the ascii table, the intelligence array populate elements with the lowercase alphabet"""
    for i in range(97, 123):  
        n = {chr(i):originalArray.count(chr(i))}  
        intelligence.update(n)
        

def check(ui,lives):
    """This function converts user input to lowercase, checks privous guesses
    are not taking another life, checks if user input is in the word and takes
    a like if it isn't."""
    #print(intelligence) #print the intelligence dictionary
    
    print("")
    userIn = ui.lower()
    if ui in guesses:
        takeInput(lives)
    guesses.append(userIn)

    if (userIn in originalArray):
        
        for i in range(0,intelligence.get(userIn)):
            NGindex = originalArray.index(userIn)
            originalArray.pop(originalArray.index(userIn))
            originalArray.insert(NGindex, star)
            blank_challenge_array.pop(NGindex)
            blank_challenge_array.insert(NGindex, userIn)

        if matchArray == blank_challenge_array:
            win()
        
        takeInput(lives)
    else:
        
        takeLife(lives)

def main():
    """This is the main function of the programe. which calls three functions."""
    getWord()
    intel(intelligence,originalArray)
    takeInput(lives)
    
   
main()
