"""
Malicious Hangman
This program simulates the classic hangman game
However, the computer does not choose a word until it is forced to make a choice
After, the game resumes normally

File Name: howry_hangman.py
Author: Ken Howry
Date: 12.5.23
Course: COMP 1353
Assignment: Project IV
Collaborators: N/A
Internet Source: N/A
"""
#imports
import random

class MaliciousHangman:
    """
        Description of Class:
            simulates a malicious hangman game
    """
    def __init__(self, word_length, number_of_tries):
        """
            Description of Function:
                initializes the class
            Parameters:
                word_length (int): the length of the word
                number_of_tries (int): the number of tries
            Return:
                None
        """
        self.word_dict = self.make_dict()
        self.filtered_word_list = self.word_dict[word_length]
        self.word_length = word_length
        self.number_of_tries = number_of_tries
        self.guesses = set()
        self.correct_guess = False
        self.word_display = "_" * self.word_length

    def make_dict(self):
        """
            Description:
                reading from a dictionary file and storing the values in a dictionary
            Parameters:
                None
            Return:
                dict 
        """
        #creating a dictionary to store the words
        word_dict = {}

        #reading from the dictionary file
        with open("Data_Struct/notes/Dictionary.txt", "r") as a_file:
            for line in a_file:
                data = line.strip().split(' ')

                word = data[0].upper()

                length = len(data[0])

                #storing the words in a dictionary with the length as the key
                if length in word_dict:
                    word_dict[length].append(word)
                else:
                    word_dict[length] = [word]

        return word_dict

    def user_guess(self):
        """
            Description of Function:
                returns a user input
            Parameters:
                None
            Return:
                str
        """
        #user input
        guess = input("Guess a letter: ").upper()
        return guess

    def check_guess(self, guess):
        """
            Description of Function:
                checks is the user guess is valid
                (has not been guess before and is a letter)
            Parameters:
                guess: str; user-inputted guess
            Return:
                None
        """
        #checks the input is a letter
        if len(guess) == 1:
            #if the letter has already been guessed
            if guess in self.guesses:
                print(f"You have already guessed the letter: {guess}")

            #if the letter has not been guessed already
            else:
                #adding the letter to the set
                self.guesses.add(guess)
                #decrement number of tries
                self.number_of_tries -= 1

        # if the input is not a letter
        else:
            print(f"Invalid guess. Please enter a single letter or a word that is {self.word_length} letters long. \n")

    def play_again(self):
        """
            Description of Function:
                prompts the user to play again
            Parameters:
                None
            Return:
                None
        """
        #prompt the user to play again
        restart_response = input("Would you like to play again? (Y/N): ")
        restart_response = restart_response.upper()

        while restart_response != "Y" or restart_response != "N":
        #if the user wants to play again
            if restart_response == "Y":
                play_hangman()

            #if the user wants to quit
            elif restart_response == "N":
                print("Okay, Thanks for playing!")
                exit()

            #invalid response
            else:
                print("Invalid response. Please enter Y or N. \n")
                self.play_again()

    def display_word(self):
        """
            Description of Function:
                displays and fills the word blanks
            Parameters:
                None
            Return:
                str
        """
        #intialization of empty string
        displayed_word = ""

        #for loop
        for letter in self.filtered_word_list[0]:
            #if letter has been guessed
            if letter in self.guesses:
                displayed_word += letter
            #else
            else:
                displayed_word += "_"

        print(displayed_word)

        return displayed_word

    #Malicious Hangman: Part II (In Progress) ;-;
    def malicious_hangman(self):
        """
            Description of Function:
                simulates a malicious hangman game
            Parameters:
                word_length (int): the length of the word
                number_of_tries (int): the number of tries
            Return:
                None
        """
        #while loop
        while self.number_of_tries > 0:
            #printing words
            print(self.filtered_word_list)

            #printing number of tries
            print("Number of tries remaining: ", self.number_of_tries)

            #displaying the word
            self.display_word()

            #prompting the user
            guess = self.user_guess()

            #checking the user guess
            self.check_guess(guess)

            #intializing an empty dictionary
            word_groups = {}

            #grouping words based on the guessed letter
            for word in self.filtered_word_list:
                key = "".join([letter if letter in self.guesses else "_" for letter in word])
                if key in word_groups:
                    word_groups[key].append(word)
                else:
                    word_groups[key] = [word]

            #choosing the group with the most values
            self.filtered_word_list = max(word_groups.values(), key = len)

            #if the words are eliminated, calling normal hangman
            if len(word_groups) == 1:
                self.word = random.choice(list(word_groups.values())[0])
                self.hangman(self.word)

        #if the number of tries is reached
        if self.number_of_tries == 0:
            print("Sorry, you ran out of tries.")
            print("The word was:", random.choice(self.filtered_word_list))
        
        #prompting the user to play again
        self.play_again()

    #Malicious Hangman: Part I
    def hangman(self, word):
        """
            Description of Function:
                stimulates a classic hangman game
            Parameters:
                None
            Return:
                None
        """
        correct_guess = False

        #looping until the word has been guessed or the number of tries is reached
        while not correct_guess and self.number_of_tries > 0:
            #printing number of tries
            print("Number of tries remaining: ", self.number_of_tries)

            #displaying the word
            self.display_word()

            #prompting the user
            guess = self.user_guess()

            #checking the guess
            self.check_guess(guess)

            #if the word has been guessed correctly
            if "_" not in self.display_word():
                print(f"You have correctly guessed the word: {word}")
                print(f"You had {self.number_of_tries} tries left")
                correct_guess = True

        #if the number of tries is reached
        if self.number_of_tries == 0:
            print("Sorry, you ran out of tries.")
            print("The word was:", word)
        
        #prompting the user to play again
        self.play_again()

def play_hangman():
    #game explaination and setup
    print(f"Welcome to the Hangman! \n")
    word_length = int(input("Enter your desired word_length: "))
    number_of_tries = int(input("How many tries do you want? "))
    print(f"You have {number_of_tries} tries to guess the {word_length}-letter word chosen. \n")

    game = MaliciousHangman(word_length, number_of_tries)
    game.malicious_hangman()

play_hangman()