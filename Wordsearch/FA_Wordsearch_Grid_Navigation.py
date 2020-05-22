from enum import Enum
import random

class WordDirection(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL_INCLINE = 2
    DIAGONAL_DECLINE = 3
    REVERSE_HORIZONTAL = 4
    REVERSE_VERTICAL = 5
    REVERSE_DIAGONAL_INCLINE = 6
    REVERSE_DIAGONAL_DECLINE = 7

class LetterEntry:
    def __init__(self, letter=None, x=None, y=None):
        self.letter = letter
        self.x = x
        self.y = y

def get_next_coordinate_in_direction(direction, x, y):
    if direction == WordDirection.HORIZONTAL:
        return x + 1, y
    elif direction == WordDirection.VERTICAL:
        return x, y + 1
    elif direction == WordDirection.DIAGONAL_INCLINE:
        return x + 1, y - 1
    elif direction == WordDirection.DIAGONAL_DECLINE:
        return x + 1, y + 1
    elif direction == WordDirection.REVERSE_HORIZONTAL:
        return x - 1, y
    elif direction == WordDirection.REVERSE_VERTICAL:
        return x, y - 1
    elif direction == WordDirection.REVERSE_DIAGONAL_INCLINE:
        return x - 1, y + 1
    elif direction == WordDirection.REVERSE_DIAGONAL_DECLINE:
        return x - 1, y - 1

def get_starting_coordinate_for_word(direction, x, y, i):
    for j in range(i):
        if direction == WordDirection.HORIZONTAL:
            x -= 1
        elif direction == WordDirection.VERTICAL:
            y -= 1
        elif direction == WordDirection.DIAGONAL_INCLINE:
            x -= 1
            y += 1
        elif direction == WordDirection.DIAGONAL_DECLINE:
            x -= 1
            y -= 1
        elif direction == WordDirection.REVERSE_HORIZONTAL:
            x += 1
        elif direction == WordDirection.REVERSE_VERTICAL:
            y += 1
        elif direction == WordDirection.REVERSE_DIAGONAL_INCLINE:
            x += 1
            y -= 1
        elif direction == WordDirection.REVERSE_DIAGONAL_DECLINE:
            x += 1
            y += 1
    return x, y

def get_random_start_coordinate_for_word_length(direction, length, grid_size):
    if direction == WordDirection.HORIZONTAL:
        x = random.randint(0, grid_size - length)
        y = random.randint(0, grid_size - 1)
        return x, y
    elif direction == WordDirection.VERTICAL:
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - length)
        return x, y
    elif direction == WordDirection.DIAGONAL_INCLINE:
        x = random.randint(0, grid_size - length)
        y = random.randint(length - 1, grid_size - 1)
        return x, y
    elif direction == WordDirection.DIAGONAL_DECLINE:
        x = random.randint(0, grid_size - length)
        y = random.randint(0, grid_size - length)
        return x, y
    elif direction == WordDirection.REVERSE_HORIZONTAL:
        x = random.randint(length - 1, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        return x, y
    elif direction == WordDirection.REVERSE_VERTICAL:
        x = random.randint(0, grid_size - 1)
        y = random.randint(length - 1, grid_size - 1)
        return x, y
    elif direction == WordDirection.REVERSE_DIAGONAL_INCLINE:
        x = random.randint(length - 1, grid_size - 1)
        y = random.randint(0, grid_size - length)
        return x, y
    elif direction == WordDirection.REVERSE_DIAGONAL_DECLINE:
        x = random.randint(length - 1, grid_size - 1)
        y = random.randint(length - 1, grid_size - 1)
        return x, y

def coordinates_are_in_bounds(x, y, grid_size):
    return x >= 0 and x < grid_size and y >= 0 and y < grid_size
