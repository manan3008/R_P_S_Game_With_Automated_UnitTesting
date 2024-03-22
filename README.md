# Rock-Paper-Scissors Game with Automated Unit Testing

## Game Implementation (r_s_p_game.py)

### Overview
The r_s_p_game.py file contains the main logic for the Rock-Paper-Scissors game. It handles user interactions, the computer's random choice generation, the game mechanics, score tracking, and determining the winner.

### Key Components
User Input Handling: The game prompts players to enter their names and select their moves (Rock, Paper, Scissors) or choose to quit the game.
Computer Move Selection: Utilizes the random library to generate the computer's move in an unpredictable manner.
Game Logic: Compares the player's and the computer's moves to determine the winner of each round. It follows the traditional rules of Rock-Paper-Scissors.
Score Tracking: Maintains and updates the score after each round. The game continues until either the player or the computer accumulates 5 points.
Game Flow Control: Manages the game rounds and displays the scores after each round. It also provides options to restart or quit the game once it concludes.

## Automated Testing (testing.py)

### Overview
The testing.py file employs Python's unittest framework to conduct automated testing on the game's functionalities. It verifies the correctness of the game logic, user input handling, computer move selection, and score tracking.

### Key Components
Test Cases for User Input: Validates that user inputs are correctly interpreted, including move selections and the decision to quit or restart the game.
Test Cases for Computer Moves: Ensures the computer's move selection is truly random and within the expected range of options.
Test Cases for Game Logic: Assesses whether the game logic correctly identifies the winner of each round based on the rules of Rock-Paper-Scissors.
Score Tracking Tests: Checks that the score is accurately updated following each round and that the game correctly identifies when a player has reached the winning score.
Running the Tests
To execute the tests, run the following command in your terminal:

### Copy code
python -m unittest testing.py
This will automatically discover and run all test methods in the testing.py file, providing a summary of passed and failed tests.

## Conclusion
This overview provides a brief insight into the programming structure and functionality of the Rock-Paper-Scissors game and its accompanying unit tests. The game demonstrates basic Python programming concepts, user interaction handling, and the application of automated testing to ensure software quality.
