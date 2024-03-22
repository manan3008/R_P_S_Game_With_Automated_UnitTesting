# Major game code start 
from random import randint

# create a list of play options
options = ["ROCK", "PAPER", "SCISSORS"]

# Major MainGame class decalration
class MainGame:

    # __init__ function declaration
    def __init__(self):

        self.round = 1                 # variable declaration for total round played
        self.machine_score = 0         # variable declaration for computer score
        self.human_score = 0           # variable declaration for user/human score
        self.machine_choice = None     # variable declaration for storing computer choice
        self.human_input = None        # variable declaration for storing human choice
        self.human_choice = None       # variable declaration for working with human choice
        self.human_name = ""           # variable declaration for storing user name 

    # match_input funtion declaration for confirmation of user input and display selected option
    def match_input(self):

        # converting the case of user input
        lower_human_input = self.human_input.lower()

        # condition checking for each selected option and printing relevant selected choice of user
        if lower_human_input in 'r':
            self.human_choice = 'ROCK'
            print("User selected: Rock")

        elif lower_human_input in 'p':
            self.human_choice = 'PAPER'
            print("User selected: Paper")

        elif lower_human_input in 's':
            self.human_choice = 'SCISSORS'
            print("User selected: Scissors")

        elif lower_human_input in ('q',):
            return "quit"

        else:
            return False # return flase if wrong input!!

        return True

    # function declaration for computer input
    def random_computer_input(self):

        # random input for computer and display it 
        choice = randint(0, 2)  # selecting one random choice from options list using RANDINT function

        self.machine_choice = options[choice]
        print(f"Computer turn: {self.machine_choice}")

    # function declaration for checking the winner and update the score board
    def result_score(self):

        # condition checking if same input by user and computer and return draw
        if self.human_choice == self.machine_choice:
            print("                 GAME DRAW!!!                 ")
            return "draw"
        
        # working out of the winner, if user select rock
        elif self.human_choice == "ROCK":

            if self.machine_choice == "PAPER":
                self.machine_score += 1
                print("  Paper Covers Rock, "
                      "so --> Computer wins this round !!!           ")
                return "machine"

            else:
                self.human_score += 1
                print(" Rock Smashes " + self.machine_choice +
                      " So, --> You win this round !!!             ")
                return "human"
        
        # working out of the winner, if user select paper
        elif self.human_choice == "PAPER":

            if self.machine_choice == "SCISSORS":
                self.machine_score += 1
                print("  Scissors Cuts Paper, "
                      "so --> Computer wins this round !!!           ")
                return "machine"

            else:
                self.human_score += 1
                print(" Paper Covers " + self.machine_choice +
                      " So, --> You win this round !!!             ")
                return "human"
        
        # working out of the winner, if user select scissor
        elif self.human_choice == "SCISSORS":

            if self.machine_choice == "ROCK":
                self.machine_score += 1
                print(" Rock Smashes Scissors, "
                      "So, ----> Computer wins this round !!!           ")
                return "machine"

            else:
                self.human_score += 1
                print(" Scissors Cuts " + self.machine_choice +
                      " So, --> You win this round !!!             ")
                return "human"

    # function declaration for selecting winner 
    def game_end(self):

        #if any one got 5 point either human or computer then game end!!        
        if self.human_score == 5 or self.machine_score == 5:
            return True
        return False

    # function declaration for set-up screen of game
    def welcome(self):

        # GAME START WELCOME USER 

        print('                                               ')
        print("**********|| W E L C O M E  USER||************")
        print("           ROCK ~~ PAPER ~~ SCISSORS")
        print("                 G A M E")
        print("**********************************************")
        self.human_name = input(" ENTER YOUR NAME : ")
        print('                                               ')
        print('           < S C O R E ~ ~ B O A R D >         ')

    # function declaration for displaying winning output
    def winning_output(self):

        # display the winning 
        print("--------------- (* _ *) ------------------------")
        print('                                                ')
        print(" CONGRATULATIONS || " + self.human_name + " YOU WON|| ")
        print('                                                 ')
        print("_______________ (* _ *) _________________________")
        print(" ----------------------------------------------")

    # function declaration for displaying looser screen
    @staticmethod
    def loosing_output():

        # display the loosing screen to user 
        print("----------------- (^ _ ^) -----------------")
        print('                                           ')
        print("              ALAS! --YOU LOSE--           ")
        print('                                           ')
        print("_________________ (0 _ 0) _________________")
        print(" ------------------------------------------")

    # function declaration for game playing prompts
    def start_playing(self):
        
        # start playing game with score board 
        self.welcome()

        # loop will execute till user press Q/q for quit
        while True:
            print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("    ", self.human_name, ":", self.human_score,
                  "     V/S     Computer :",
                  self.machine_score, "         ")

            print("|                  Round :", self.round,
                  "                  |")
            print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("|      FOR ROCK    ---- PRESS (r / R)          |")
            print("|      FOR PAPER   ---- PRESS (p / P)          |")
            print("|      FOR SCISSOR ---- PRESS (s / S)          |")
            print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("|            To  EXIT (q / Q)                  |")
            print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            self.human_input = input("ENTER YOUR OPTION : ")

            # match the input of player if quite or valid/invalid option
            verify_input = self.match_input()

            if verify_input == "quit":
                break

            # if match input function returns true to verify input then
            if verify_input:
                self.random_computer_input()
                self.result_score()
                self.round += 1

            else:
                # returns false input not matched with any case
                print("********** (- _ -) **********")
                print("**********PLEASE ENTER ACCURATE INPUT**********")
                print("********** (- _ -) **********")

            if self.game_end():

                if self.human_score == 5:
                    self.winning_output()

                else:
                    self.loosing_output()

                # if restart or quite the game
                # after the end of the game 
                print("|     RESTART (R / r)           QUIT (q / Q)    |")
                print(" ----------------------------------------------")

                # propmpts after the winner decided to quit or restart
                while True:

                    restart_choice = input(" Choose your choice  ")
                    lower_restart_choice = restart_choice.lower()
                    
                    if lower_restart_choice in 'q':
                        break

                    elif lower_restart_choice in 'r':
                        self.human_score = 0
                        self.machine_score = 0
                        self.round = 1
                        break

                    else:
                        print("Please Enter Accurate option")

                if lower_restart_choice in 'q':
                    break

# main method calling class with object
if __name__ == '__main__':
    rock_paper_scissor = MainGame()
    rock_paper_scissor.start_playing()
