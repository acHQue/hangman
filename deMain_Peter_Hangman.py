#
import random
import os
import sys

wordlist = "word_list.txt"
star = "*"

guesses = []
originalAarry = []
challenge_array = []
blank_challenge_array = []
intelligence = {}

total_lines_in_wordlist = int(len(open(wordlist).readlines()))
random_line = int(random.randint(0, (total_lines_in_wordlist - 1)))

fh = open(wordlist)
challenge_word = fh.readlines()[random_line]
fh.close()

number_letters_challenge = len(challenge_word) 
number_blanks = (number_letters_challenge)
true_word_line = int(random_line)

for i in range(len(challenge_word)):
  originalAarry.append(challenge_word[i])

for i in range(len(challenge_word)):
  
	challenge_array.append(challenge_word[i])
	blank_challenge_array.append(star)
	#print(word[i])

for i in range(97, 123):
  n = {chr(i):challenge_array.count(chr(i))}
  intelligence.update(n)


if random_line == (total_lines_in_wordlist -1):

    #print("This is the last word in the this")
    print("")
else:
    # This else statement basiclyy rewrite the challenge_array and the blank_challenge_array because of the the trailing carrage return. Messy but is work :D 
    #print("This number of elements in the challenge_arry list is ", len(challenge_array))
    lastElement = len(challenge_array) - 1
    challenge_array = [l.strip() for l in challenge_array]
    
    challenge_array.pop(lastElement)
    originalAarry.pop(lastElement)
    #print(challenge_word)
    #print("Because all but the last word in the word list contains a n a the end the blanks nee to be changed ", len(challenge_word) - 1)
    len(challenge_word) - 1
    number_letters_challenge = number_letters_challenge -1
    number_blanks = (number_letters_challenge)
    del blank_challenge_array
    blank_challenge_array = []
    for x in range(number_blanks):
        blank_challenge_array.append('*')

def clear():
  os.system("cls")
  os.system("clear") 

def loose():
  print("You loose")
  sys.exit(0)
  

lives = 7

def mainFunc(lives):
  

  print("")
  print("You have ",lives, " lives remaining.")
  print("")

  while originalAarry != blank_challenge_array:
    
    if lives == 0:
      loose()
      break

    print(challenge_array)
    print("")
    print("These are your guesses")
    print(guesses)
    print("")
    print("Here is your clue.")
    print(blank_challenge_array)
    print("")
    userIn = input("Please enter your next guess: ")

    

    guesses.append(userIn)

    if len(userIn) < 1:
        clear()
        print("Are you playing??")
        print("")
        mainFunc(lives)
    elif len(userIn) > 1:
        clear()
        print("Only submit one letter per try.")
        print("")
        mainFunc(lives)
    elif userIn == " ":
      clear()
      mainFunc(lives)
    elif userIn not in challenge_array:
      clear()
      lives = lives - 1
      mainFunc(lives)
    
      
    else:
        clear()

    



    if userIn in originalAarry:

      #print("There is ",intelligence[userIn], "of those.")
      #This is to find out how many to remove and add.
      #for x, y in intelligence.items():
      #  print(x, y)
      #print("Find the indexes")

      for i in range(0,intelligence.get(userIn)):
        
        #print(userIn, "User guesss.") 
        #print(word)
        #print(array.index(userIn), "This is the index of list.")
        #print(intelligence.get(userIn), "  Retreiveing data about the letter chosen. ")   
        #print(userIn)
        #print(array.index(userIn), "The indexes....")
        indexes = challenge_array.index(userIn) # to remember the location and progress.    
        #print(indexes, "Variable of remembered Index")
        #print(array.pop(array.index(userIn)), "e")
        challenge_array.pop(challenge_array.index(userIn))
        #print(array.insert(indexes, star), "f")
        challenge_array.insert(indexes, star)
        blank_challenge_array.pop(indexes)
        #print(blank.insert(indexes, userIn),"g")
        blank_challenge_array.insert(indexes, userIn)

    else:
      
      print("No letter found within the challenge word.")
      print("")
      mainFunc(lives)
    

      continue

  
  if originalAarry == blank_challenge_array:
    clear()
    print(challenge_word)
    print("Congratulations you win")
  if lives == 0:
    clear()
    print("YOU LOOSE!!")

mainFunc(lives)
#print(intelligence)


