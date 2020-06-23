#
# Python modules used
import random # module that employs random api
import os     # module that import operating system api
import sys

#Declaring Variables
wordlist = "word_list.txt"
star = "*"
lives = 7

#Declairing Python list
guesses = [] #A list to hold users guesses
challenge_array = [] #The randomly choosen word from word list
originalAarry = [] #A Copy of the challenge for comparing
blank_challenge_array = [] #My therory here is to build a new list to compare with the challenge.

#Python dictionary, to learn multiple letters within challenge. To loop a scan.
# Uncomment line 44 or 99 to see this result. 
#I suggest 44 because it is more readable.
intelligence = {}

#BEGINING of the flow to genorate the arrays and lists 
total_lines_in_wordlist = int(len(open(wordlist).readlines())) # Count word per line from wordlist.
random_line = int(random.randint(0, (total_lines_in_wordlist))) #Genorates random number between zero and max lines in wordlist. However there is a problem. with the number of lines and element is the list. They dont line up, there are more lines than elements. line 51 if block fixes this
#print(total_lines_in_wordlist)# debuging for words in line.
fh = open(wordlist) # file handling opens the text file
challenge_word = fh.readlines()[random_line] # file handling reads line which is a previously calcualted.
fh.close() # File handling closes

number_letters_challenge = len(challenge_word)  # I want data based off the random word to genorate the length of a list. Without the annoying extra element.
number_blanks = (number_letters_challenge)      # Equally I want a list of blanks to help my "game engine". With the annoying extra element
true_word_line = int(random_line + 1)           #Line number of word from wordlist
#print(int(true_word_line), "true word line number")#debugging for answer

for i in range(len(challenge_word)):
  originalAarry.append(challenge_word[i]) #Loading the orrignalArray with each letter of challenge word with a for loop (the copy)

for i in range(len(challenge_word)):
	challenge_array.append(challenge_word[i]) # Loading the challange_array with each letter of the challenge word using a for loop.
	blank_challenge_array.append(star) #load the blank_challenge_array with stars
	#print(word[i])

for i in range(97, 123): # using the ascii table, the intelligence array populate elements with the lowercase alphabet
  n = {chr(i):challenge_array.count(chr(i))} # n is a var that holds ascii characters (chr 97-123) as a key, and counts values of callenge array.
  #print(n) # uncomment this to see the dictionary 
  intelligence.update(n)



if random_line == (total_lines_in_wordlist -1): 
  # The words in the word list have an addition character, ths if block removes it

    #print("This is the last word in the this")
    print("")
else:
    # This else statement rewrites the challenge_array and the blank_challenge_array because of the the trailing carrage return. Messy but is works :D 
    lastElement = len(challenge_array) - 1
    challenge_array = [l.strip() for l in challenge_array]
    challenge_array.pop(lastElement)
    originalAarry.pop(lastElement)
    #print(challenge_word)
    #Because all but the last word in the word list contains a n (carrage return) at the end
    len(challenge_word) - 1
    number_letters_challenge = number_letters_challenge -1
    number_blanks = (number_letters_challenge)
    del blank_challenge_array
    blank_challenge_array = []
    for x in range(number_blanks):
        blank_challenge_array.append('*')
##
##END OF FLOW to genorate game challenge information
##

#This funciton clears the game after each attempt
def clear():
  os.system("cls")
  os.system("clear") 

#This function ends the game is the lives equal zero
def loose(lives):
  clear()
  print("You have ",lives, " lives remaining.")
  print(challenge_word)
  print("You loose")
  sys.exit(0)

#Begining for the main function
def mainFunc(lives):
  #Game loop comparing two lists, for as long as they are not matching game will continue to roll 
  # and when they do match the loop continues on.... :D
  while originalAarry != blank_challenge_array:

    #print(challenge_array)        #This is the challenge array
    #print(originalAarry)          #This will print the original COPY of the challenge word.   
    #print(blank_challenge_array)  #This prints the list from correclty matching user input and equal lsit length of stars.
    #print(guesses)                #This is a record of user in put - i want to fix deducting allready guess letters with this.
    #print(intelligence)           #This is a dicitonary that learns there are multiple letters in cahllenge word.
    
    #Displaying remaining lives
    print("You have ",lives, " lives remaining.")
    
    #If all lives are gone we execute the lives function and break the game wile loop
    if lives == 0:
      loose(lives)
      break

    #this is the reason i failed the first time?????????????????????????
    print(*blank_challenge_array, sep=" ") # this prints the clue of stars and correct guesses without quotes or commas 
    
    ui = input("Please enter your next guess: ") # User input here <-
    
    userIn = ui.lower() # Sorry, this is a quick n dirty hack to meet mod3 requirments 

    #This function the start of user validation - No lives deducted for allready guessed words.
    if userIn in guesses:
      clear()
      mainFunc(lives)

    guesses.append(userIn) #The users input is added to the guesses list

    #This is more user validation
    
    if len(userIn) < 1: #Or less than one letter guesses
        clear()
        print("Are you playing??") # Warning no letter is inputed.
        print("")
        mainFunc(lives) # mainFunc reloads becasue non input was taken.
    elif len(userIn) > 1: #Or more than one letter guesses
        clear()
        print("Only submit one letter per try.") # Warning more than one letter is inputed. 
        print("")
        mainFunc(lives) # mainFunc reloads, users guess fell out of line for the game of hangman
    elif userIn == " ": #To prevent empty guesses
      clear()
      mainFunc(lives) # mainFunc reloads for a user input since there was no guess the life is removed
    elif userIn not in challenge_array: #One life is removed is the user in is not in challenge_array list
      clear()
      lives = lives - 1 # life taken :(
      mainFunc(lives)   # game reloads due to incorrect guess
    else:
        clear() # just to clean up the terminal

    if userIn in originalAarry: # So if just one user input is preasent this if statement fires.
      for i in range(0,intelligence.get(userIn)): # This is a loop that ranges from zero the the intelligence learned.  looping/scanning for letters as many times as needed.
        NGindex = challenge_array.index(userIn) # to remember the location and progress in a local scope variable before it is removed (next)
        challenge_array.pop(challenge_array.index(userIn)) # Here we remove(pop) matching user input itself by index number 
        challenge_array.insert(indexes, star) #Using the new local var location we insert back in a star for a correct a guess, removing it for anouther go thus preventing false positives.
        blank_challenge_array.pop(indexes) # The star string you see on screen is genorated by this. We are removing the star in the location
        blank_challenge_array.insert(indexes, userIn) # and then replacing the blank list stars with correct user input. relying on the for loop.

    else:
      #print("No letter found within the challenge word.") # This was used ffor development, hovever a usefull marker
      mainFunc(lives)  # reload the mainFunc to contine game to satify the game loop. line 96.
      continue # Works with the while loop once the while loop is satisfied the game continues bellow.

  #So here is for the win
  if originalAarry == blank_challenge_array:
    clear() # Terminal tidyup
   # print(challenge_word) #The challenge word you worked so hard for 
    print("") # a little of spacing
    print("Congratulations you win") # Your award!!
    sys.exit(0) # game end much like lives = 0 only you have won!! 

#Main function call in scope of main script.
mainFunc(lives)
