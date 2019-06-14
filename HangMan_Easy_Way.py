# Word Guessing Game : HANGMAN , Code by Aakash Jangid
# User will have 10 attempts to guess a Word which is exiting in our program dictionary
# User will have to guess the whole WORD 'Character by Character'
# If user enters correct character it will show up otherwise his/her attempt will be lost
# Let's begin with this shit


import random                # import random module for randomizing the word selection


wordList = ["lion", "umbrella", "window", "computer", "glass"]  # Let's create our word dictionary first

guess_word = []
secret_word = random.choice(wordList)   # Randomly selecting the word from the wordList
length_word = len(secret_word)          # get the length of the word
alphabet = " abcdefghijklmnopqrstuvwxyz"
letter_storage = []


class HangMan:
    ' HangMan by Aakash using Python 3.7.3 '

    def __init__(self):  # constructor of class HangMan with no statement i.e pass
        pass

    def start(self):
        print("Hey Nigga!\n")
        while True:
            name = input("Please, Enter your Name\n").strip()
            print(name, "Welcome To The Game\n")
            if name == "":
                print("Is your damn Name Blank , Nigga ?\nNa yeh Ni Chalega\n")
            else:
                break

    def newFunc(self):
        print("Well, Let's Start The Game!\n")

        while True:
            gameChoice = input("Shall We?\n").upper()

            if gameChoice == "YES" or gameChoice == "Y":
                break
            elif gameChoice == "NO" or gameChoice == "N":
                exit(0)
                print("That's a shame! Have a nice day")

            else:
                print("Please Answer only Yes or No")
                continue

    def change(self):
        for character in secret_word:
            guess_word.append("-")
        print("length", length_word, "chracters")
        print("You can only Enter 1 character at a time from a - z\n\n")
        print(guess_word)

    def guessing(self):
        guess_taken = 1  # initialise the guess_taken with 1 and iterate until 10
        while guess_taken < 11:
            guess = input("Enter a Letter\n").lower()
            if not guess in alphabet:
                print("Enter a letter from the alphabet ")
            elif guess in letter_storage:
                print("You have already guessed that letter")
            else:
                letter_storage.append(guess)  # append the list with the entered guess word
                if guess in secret_word:
                    print("Your Guess is Correct !!!\n")

                    for i in range(0, length_word):
                        if secret_word[i] == guess:  # if our seccret word has guessed letter then
                            guess_word[i] = guess  # store the guess the guessed word in the guess_word list
                    print(guess_word)

                    if not '-' in guess_word:  # if -- are not in the guess_word list then you won
                        print("You Won !!!\n")
                        print("Game Over !!!\n")
                        break
                else:
                    print("The letter is not in the word. Try Again!\n")
            guess_taken += 1
            print("Remaining attempts:", 11 - guess_taken)
            if guess_taken == 11:
                print("Sorry Mate, You lost! The secret word was : ", secret_word)
                break


ob = HangMan()  # declare and initialize the object of the class HangMan

ob.start()  # call the methods of class HangMan using "ob" object of class HangMan type !!!
ob.newFunc()
ob.change()
ob.guessing()
