"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
    return puzzle == view

def game_over(puzzle: str, view: str, cuurrent_selection: str) -> bool:
    """Return True iff the puzzle is the same as the view or current selection is QUIT.
    
    >>>game_over('banana', 'banana', 'C')
    True
    >>>game_over('apple',  'a^^le', 'Q')
    True
    >>>game_over('bitter', 'bi^t^r', 'C')
    False
    """
    return puzzle == view or cuurrent_selection == 'Q'

def bonus_letter(puzzle: str, view: str, letter_to_evaluate: str) -> bool:
    """Return True if and only if the letter appears in the puzzle but not in its view.
    
    >>>bonus_letter('apple', 'a^^^e', 'p')
    True
    >>>bonus_letter('apple', 'app^^', 'a')
    False
    """
    return ((letter_to_evaluate) in puzzle) and ((letter_to_evaluate) not in view)

def update_letter_view(puzzle: str, view: str, index: int, letter: str) -> str:
    """Return a single character representing the next view of the character at index.
    
    >>>update_letter_view('apple', 'a^^^^', 2, 'p')
    'p'
    >>>update_letter_view('bitter', '^^^^^^', 1, 't')
    '^'
    """
    
    if letter == puzzle[index]:
        return letter
    return view[index]

def calculate_score(current_score: int, number: int, letter: str) -> int:
    """Return the new score.
    
    >>>calculate_score(2, 1, CONSONANT)
    3
    >>>calculate_score(2, 1, VOWEL)
    1
    """
    
    if letter == CONSONANT:
        return (current_score) + (number) * (CONSONANT_POINTS)
    elif letter == VOWEL:
        return (current_score) - (number) * (VOWEL_PRICE)
    
def next_player(cuurent_player: str, number: int) -> str:
    """Return the next player (one of PLAYER_ONE or PLAYER_TWO).
    
    >>>next_player('Player One', 1)
    'PLAYER_ONE'
    >>>next_player('Player One', 0)
    'PLAYER_TWO'
    """
    
    if number > 0:
        return cuurent_player
    if number == 0:
        if cuurent_player == 'Player One':
            return 'Player Two'
        elif cuurent_player == 'Player Two':
            return 'Player One'
        