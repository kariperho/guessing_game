class NumberGuessingGame:

    def __init__(self, guess_count):
        self.guess_count = guess_count
       
    def generate_random_number(self):
        pass 
      
    def ask_number(self):
        pass 
              
    def add_guess_count(self):
        pass  
           
    def main_game_loop(self):
        while True:
            correct_answer = generate_random_number()
            player_answer = ask_number()
            if correct_answer == player_answer:
                print(f"Correct answer!! It was {correct_answer}")
                print(f"It took you {self.guess_count} tries.")
                break
            elseif correct_answer < player_answer:
                print(f"Wrong! {player_answer} is too high. Try again.")
                add_guess_count()
            elseif correct_answer > player_answer:
                print(f"Wrong! {player_answer} is too low. Try again.")
                add_guess_count
        

game = NumberGuessingGame()


game.main_game_loop()

