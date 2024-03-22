# Testing different functions and the behaviour of game

import unittest # importing unit testing  package
from r_s_p_game import MainGame 


class Test(unittest.TestCase):
    # MAJOR UNIT TESTING CLASS

    def setUp(self):
        self.r_p_s_game = MainGame()

    def test_random_computer_input(self):

        # test the random chose option of the machine
        # Machine make random choice from Rock, Paper and Scissor.

        self.r_p_s_game.random_computer_input()
        self.assertEqual(True, self.r_p_s_game.machine_choice
                         in ["ROCK", "PAPER", "SCISSORS"])

    def test_each_round_winner(self):
        # test the functionality of each round winner and the update of score board for all scenarios
        
        # If human's choice is Rock(1)
        self.r_p_s_game.human_choice = "ROCK"
        self.r_p_s_game.machine_choice = "ROCK"

        # check draw case because both
        # computer and human player have picked same options
        self.assertEqual("draw", self.r_p_s_game.result_score())

        # check computer win
        self.r_p_s_game.machine_choice = "PAPER"
        self.assertEqual("machine",
                         self.r_p_s_game.result_score())

        # check human win
        self.r_p_s_game.machine_choice = "SCISSORS"
        self.assertEqual("human", self.r_p_s_game.result_score())

        # If Human's choice is Paper
        self.r_p_s_game.human_choice = "PAPER"

        # check human win
        self.r_p_s_game.machine_choice = "ROCK"
        self.assertEqual("human", self.r_p_s_game.result_score())

        # check draw
        self.r_p_s_game.machine_choice = "PAPER"
        self.assertEqual("draw", self.r_p_s_game.result_score())

        # check machine win
        self.r_p_s_game.machine_choice = "SCISSORS"
        self.assertEqual("machine",
                         self.r_p_s_game.result_score())

        # IF Human's choice is Scissors
        self.r_p_s_game.human_choice = "SCISSORS"

        # check machine win
        self.r_p_s_game.machine_choice = "ROCK"
        self.assertEqual("machine",
                         self.r_p_s_game.result_score())

        # check human win
        self.r_p_s_game.machine_choice = "PAPER"
        self.assertEqual("human", self.r_p_s_game.result_score())

        # check draw
        self.r_p_s_game.machine_choice = "SCISSORS"
        self.assertEqual("draw", self.r_p_s_game.result_score())

    def test_match_input(self):
        # test the functionality of player input

        # Assume human has input 'r' for Rock
        self.r_p_s_game.human_input = 'r'
        self.assertEqual(True, self.r_p_s_game.match_input())

        # Assume human has input 'paper' for Paper
        self.r_p_s_game.human_input = 'paper'
        self.assertEqual(False, self.r_p_s_game.match_input())

        # Assume human has input 'S' for Scissors
        self.r_p_s_game.human_input = 'S'
        self.assertEqual(True, self.r_p_s_game.match_input())

        # Assume human has input wrong word
        self.r_p_s_game.human_input = 'test'
        self.assertEqual(False, self.r_p_s_game.match_input())

    def test_scores_before_after_win(self):
        #test the scores

        # initial scores are zero
        self.assertEqual(0, self.r_p_s_game.human_score)
        self.assertEqual(0, self.r_p_s_game.machine_score)

        # if human wins then check score update
        self.r_p_s_game.human_choice = "SCISSORS"
        self.r_p_s_game.machine_choice = "PAPER"
        self.assertEqual("human", self.r_p_s_game.result_score())
        self.assertEqual(0, self.r_p_s_game.machine_score)
        self.assertEqual(1, self.r_p_s_game.human_score)

        # draw case
        self.r_p_s_game.human_choice = "ROCK"
        self.r_p_s_game.machine_choice = "ROCK"
        self.assertEqual("draw", self.r_p_s_game.result_score())
        self.assertEqual(0, self.r_p_s_game.machine_score)
        self.assertEqual(1, self.r_p_s_game.human_score)

        # extend score of computer to 2 and human 1 and check the test case
        self.r_p_s_game.human_choice = "SCISSORS"
        self.r_p_s_game.machine_choice = "ROCK"
        self.assertEqual("machine",
                         self.r_p_s_game.result_score())
        self.r_p_s_game.machine_choice = "ROCK"
        self.assertEqual("machine", self.r_p_s_game.result_score())

    def test_winner_verified(self):

        # test the winner of the game who got 5 points human or machine
        self.assertEqual(0, self.r_p_s_game.machine_score)
        self.assertEqual(0, self.r_p_s_game.human_score)
        self.assertEqual(False, self.r_p_s_game.game_end())

        self.r_p_s_game.human_choice = "SCISSORS"
        self.r_p_s_game.machine_choice = "PAPER"
        self.assertEqual("human", self.r_p_s_game.result_score())
        self.assertEqual(1, self.r_p_s_game.human_score)
        self.assertEqual(False, self.r_p_s_game.game_end())

        self.assertEqual("human", self.r_p_s_game.result_score())
        self.assertEqual("human", self.r_p_s_game.result_score())
        self.assertEqual("human", self.r_p_s_game.result_score())
        self.assertEqual(False, self.r_p_s_game.game_end())

        self.assertEqual("human", self.r_p_s_game.result_score())
        self.assertEqual(0, self.r_p_s_game.machine_score)
        self.assertEqual(5, self.r_p_s_game.human_score)
        self.assertEqual(True, self.r_p_s_game.game_end())

    def test_game_end(self):
        
        # Check the function by providing 5 points to human player 
        self.r_p_s_game.human_score = 5
        self.assertEqual(True, self.r_p_s_game.game_end())

        # check the quit and restart selected by user input
        self.r_p_s_game.human_input = 'q'
        self.assertEqual(True, self.r_p_s_game.game_end())

        self.r_p_s_game.human_input = 'Q'
        self.assertEqual(True, self.r_p_s_game.game_end())

        self.r_p_s_game.human_input = 'r'
        self.assertEqual(True, self.r_p_s_game.game_end())

        self.r_p_s_game.human_input = 'R'
        self.assertEqual(True, self.r_p_s_game.game_end())

if __name__ == '__main__':
    unittest.main()
