# Project Description: Aces Up Game Implementation in Python

## Introduction
The "Aces Up Game" project is a Python implementation of the famous card game "Aces High." The game is played using two classes, `Card` and `Deck`, as described in the `cards.py` module. The project utilizes nine functions and a main function to facilitate the game. The functions handle various aspects of the game, such as initialization, dealing cards, moving cards within the tableau, validating moves, and checking for a win. The main function allows users to interact with the game and make decisions based on the displayed menu options.

## Purpose
The purpose of this project is to provide a working implementation of the "Aces High" card game, allowing users to play the game and enjoy the challenge it offers. The functions are designed to handle different aspects of the game's mechanics, providing an interactive and engaging experience for the user.

## Function Details

### 1. `init_game()`
This function initializes the Aces Up game. It sets up the foundation, tableau, and stock, using the `Deck` class to create a deck of 52 cards. The function shuffles the deck, deals one card to each column in the tableau, and returns the initial game state.

### 2. `deal_to_tableau(tableau, stock)`
This function deals one card to each of the four columns in the tableau. It uses the `Deck` class's `deal()` method to achieve this.

### 3. `validate_move_to_foundation(tableau, from_col)`
Validates a move from the tableau to the foundation. It checks if a card can be moved to the foundation based on the game rules and returns true if the move is valid, else false.

### 4. `move_to_foundation(tableau, foundation, from_col)`
Moves the bottom-most card of the chosen column to the foundation, only if the move is valid. Calls `validate_move_to_foundation()` to check the validity of the move.

### 5. `validate_move_within_tableau(tableau, from_col, to_col)`
Validates a move within the tableau from one column to another. Checks if the move is valid and returns true if it is, else false.

### 6. `move_within_tableau(tableau, from_col, to_col)`
Moves the bottom card of one column to an empty column within the tableau, only if the move is valid. Calls `validate_move_within_tableau()` to check the validity of the move.

### 7. `check_for_win(tableau, stock)`
Checks if the game has been won by verifying if the stock is empty and only aces remain in the tableau.

### 8. `display(stock, tableau, foundation)`
Displays the current status of the stock, tableau, and foundation.

### 9. `get_option()`
Prompts the user to input an option and returns a list based on the type of user input. The list is used in the main function to determine the action to be taken.

### 10. `main()`
The main function of the program. It displays the rules and the menu of options to the user. The user can choose to deal cards, move cards within the tableau, restart the game, display the menu, or quit the game. The function calls the appropriate functions to execute the chosen action. If the game is won, it displays a winning message and ends the game.

## Implementation
The project is implemented in Python, utilizing the `cards.py` module to handle the card and deck functionalities. It employs a combination of functions and user interactions to create a playable version of the Aces Up card game. The main function orchestrates the game flow, allowing users to make choices and interact with the game until they win or decide to quit. Exception handling and input validation ensure a smooth user experience. This implementation provides users with a fun and interactive way to enjoy the Aces Up card game.
