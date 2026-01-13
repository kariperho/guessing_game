import random

class NumberGuessingGame:

    def __init__(self):
        pass  
       
    def generate_random_number(self):
        random.randint(1, 10)
      
    def ask_number(self):
        number_guessed = input("What number do you want to guess?")
              
    def add_guess_count(self):
        pass  
           
    def main_game_loop(self):
        pass

game = NumberGuessingGame()

print("Let's play a game!")
print("I'm thinking of a number between 1 and 10.")
print("Try to guess the number!")
game.main_game_loop()
