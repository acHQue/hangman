# JHub Coding Scheme (JCS) Module 3: python hangman                                 # These are the inline comments.
import random                                                                       # Importing the random python library for choosing word from wordlist.
import os                                                                           # Importing the operating system library for clearing/clearing the terminal.
import sys                                                                          # Importing the system for programe termination once won or lost.

lives = 7                                                                           #Variable for number of lifes according the challenge guidlines.
sep = ""                                                                            #Variable for joining the lists together.
origWordList = []                                                                   #List for holding the challge hold the unchanged and authentic word.
workingList = []                                                                    #List of the challenge word to allow elements to handled.
starList = []                                                                       #List of * to symbolise the blank challenge of hangman.
guesses = []                                                                        #A list to log all attempts preventing double jeopardy
wordlist = "word_list.txt"                                                          #Variable for holding the name of the word list as per challenge guidlines

def clear():
    """This function is for clearing the terminal to keep it tidy."""
    os.system("cls")
    os.system("clear")

def takeLife(lives):
    """This function subtracts 1 life from the lives variable. And passes on the lives variable back in the to flow."""
    l = lives - 1
    lives = l
    if lives == 0:
        clear()
        gameOver(lives)
    takeCheck(lives)

def gameOver(lives):
    """When you run out of lives this function displays that you have lost and terminates hangman."""
    print("You loose!")
    print("You have ",lives," lives left.")
    print(sep.join(origWordList))
    sys.exit(0)

def win():
    """This function ends the program when the word is guessed and, reveals the word."""
    clear()
    print(sep.join(origWordList))
    print("Congratulations, YOU WIN!")
    sys.exit(0)

def genWord():
    """"This function generates the the challenge word by randomly choosing (with the use of the random library) a word for the challenge.
     The total lines per line of words are counted, then a random number is picked based on that range.
     That random number is used to select a word and write it to the challenge_word variable."""
    total_lines_in_wordlist = int(len(open(wordlist).readlines()))
    random_line = (int(random.randint(0, (total_lines_in_wordlist))))
    opnwl = open(wordlist)
    challenge_word = opnwl.readlines()[random_line]
    opnwl.close()

    for i in range(0, len(challenge_word)):                                         #This for loop injects each letter of the challenge_word into 3 lists.
        origWordList.append(challenge_word[i])
        workingList.append(challenge_word[i])
        starList.append('*')

    if "\n" in challenge_word:                                                      #I noticed there was a carage return that needed to be removed. This could of been fixed in the loop with a -1.
        origWordList.remove("\n")
        workingList.remove("\n")
        starList.pop(len(starList) - 1)                                             #Since the startlist will never have a \n the last symbol is popped.

def takeCheck(lives):
    """This function contains the user interface of the program, showing lives left, *, and the input prompt.
    All the user input is converted to lowercase and "while" looped to ensure a valid user input of one character only.
    The letter is check against the working list, untempering the original list.
    If a letter is in the list elements the location is remove and replace with a *
    Then location is also removed from the startlist and the user input inserted to the same location of the working list, and the flow restarts the takecheck function.
    In the event of no letter in challenge, the else flows the program to take a life function."""

    clear()

    if starList == origWordList:
        win()

    print(sep.join(starList))
    print('Lives remaining: ', lives)
    userinput = input("Please enter your next guess: ")
    ui = userinput.lower()
    #validation
    while len(ui) < 1 or len(ui) > 1:
        ui
        guesses.append(ui)
        if ui in guesses:
            takeCheck(lives)
    #letter check
    if ui in origWordList:
        while ui in workingList:
            tempVar = workingList.index(ui)
            workingList.pop(tempVar)
            workingList.insert(tempVar, '*')
            starList.pop(tempVar)
            starList.insert(tempVar, ui)
        takeCheck(lives)
    else:
        takeLife(lives)

def main():
    """The main recursive main function of the hangman game."""
    genWord()
    takeCheck(lives)

main()
