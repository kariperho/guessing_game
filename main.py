import random

class NumberGuessingGame:

    def __init__(self):
        self.guess_count = 1
       
    def generate_random_number(self):
        return random.randint(1, 10)
      
    def ask_number(self):
        number_guessed = input("What number do you want to guess? ")
        return int(number_guessed)
              
    def add_guess_count(self):
        self.guess_count += 1
           
    def main_game_loop(self):
        correct_answer = self.generate_random_number()
        while True:
            player_answer = self.ask_number()
            if correct_answer == player_answer:
                print(f"Correct answer!! It was {correct_answer}")
                print(f"It took you {self.guess_count} tries.")
                break
            elif correct_answer < player_answer:
                print(f"Wrong! {player_answer} is too high. Try again.")
                self.add_guess_count()
            elif correct_answer > player_answer:
                print(f"Wrong! {player_answer} is too low. Try again.")
                self.add_guess_count()
        
print("Let's play a game!")
print("I'm thinking of a number between 1 and 10.")
print("Try to guess the number!")
game = NumberGuessingGame()

game.main_game_loop()
