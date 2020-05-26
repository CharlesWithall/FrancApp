from Wordsearch.FA_Wordsearch_Letter_Frequency import LetterFrequencies
import Wordsearch.FA_Wordsearch_Grid_Navigation as GridNavigator
from Wordsearch.FA_Wordsearch_Grid_Navigation import WordDirection

from Wordsearch.FA_Wordsearch_Defines import IS_CHEAT_MODE

import random

class LetterEntry:
    def __init__(self, char=None, x=None, y=None):
        self.letter = char
        self.x = x
        self.y = y

class WordsearchEntry:
    def __init__(self, en, fr, letter_entries=[]):
        self.english = en
        self.french = fr
        self.letter_entries = letter_entries
        self.is_complete = False

    def add_letter(self, character, x, y):
        self.letter_entries.append(LetterEntry(character, x, y))

    def get_start_point(self):
        return self.letter_entries[0]

    def get_end_point(self):
        return self.letter_entries[-1]

class WordsearchGenerator:
    def __init__(self):
        # a lot of this stuff should be read in by the constructor and in the generate function
        self.grid_size = 0
        self.word_list = []
        self.letter_grid = []
        self.letter_frequencies = LetterFrequencies()

    def debug_display(self):
        for line in self.letter_grid:
            print(str(line).replace(",", "").replace("'", ""))

    def generate(self, grid_size, translations, number_of_words):
        self.grid_size = grid_size
        self.letter_grid = [[0 for x in range(grid_size)] for y in range(grid_size)]

        random_word_list = random.sample(translations, number_of_words)
        entries = []
        for new_word in random_word_list:
            new_word_en = new_word.english.upper()
            new_word_fr = new_word.french.upper().replace(" ", "")
            new_word_length = len(new_word_fr)
            word_location_found = False

            for existing_word in entries:
                for letter_entry in existing_word.letter_entries:
                    if letter_entry.letter in new_word_fr:
                        start, direction = self.try_fit_word_to_grid(letter_entry, new_word_fr)
                        if start is not None and direction is not None:
                            new_entry = self.add_word_to_grid(new_word_fr, direction, start)
                            entries.append(WordsearchEntry(new_word_en, new_word_fr, new_entry))
                            word_location_found = True
                            break

                if word_location_found:
                    break

            while not word_location_found:
                random_direction = random.choice(list(WordDirection))
                coordinates = GridNavigator.get_random_start_coordinate_for_word_length(random_direction, new_word_length, self.grid_size)
                if self.verify_no_overlap(coordinates[0], coordinates[1], new_word_length, random_direction):
                    new_entry = self.add_word_to_grid(new_word_fr, random_direction, coordinates)
                    entries.append(WordsearchEntry(new_word_en, new_word_fr, new_entry))
                    word_location_found = True

        self.fill_grid_with_random_letters()
        entries.sort(key=lambda w: len(w.english))
        return self.letter_grid, entries

    def verify_no_overlap(self, x, y, length, direction):
        for i in range(length):
            if not GridNavigator.coordinates_are_in_bounds(x, y, self.grid_size):
                return False

            if self.letter_grid[x][y] is not 0:
                return False

            x, y = GridNavigator.get_next_coordinate_in_direction(direction, x, y)

        return True

    def try_fit_word_to_grid(self, letter_entry, new_word):
        for i, letter in enumerate(new_word):
            if letter_entry.letter == letter:
                word_length = len(new_word)
                for unused_index, direction in enumerate(list(WordDirection)):
                    start = GridNavigator.get_starting_coordinate_for_word(direction, letter_entry.x, letter_entry.y, i)
                    if not GridNavigator.coordinates_are_in_bounds(start[0], start[1], self.grid_size):
                        continue

                    coord = start
                    entry_found = True

                    for j in range(word_length):
                        test_letter = self.letter_grid[coord[0]][coord[1]]
                        if test_letter is not 0 and test_letter is not new_word[j]:
                            entry_found = False
                            break

                        coord = GridNavigator.get_next_coordinate_in_direction(direction, coord[0], coord[1])
                        if not GridNavigator.coordinates_are_in_bounds(coord[0], coord[1], self.grid_size):
                            entry_found = False
                            break

                    if entry_found:
                        return start, direction

        return None, None

    def add_word_to_grid(self, word, direction, coordinates):
        x = coordinates[0]
        y = coordinates[1]
        letters = []
        for letter in word:
            letters.append(LetterEntry(letter, x, y))
            self.letter_grid[x][y] = letter
            x, y = GridNavigator.get_next_coordinate_in_direction(direction, x, y)

        return letters

    def fill_grid_with_random_letters(self):
        for x in range(0, self.grid_size):
            for y in range(0, self.grid_size):
                if self.letter_grid[x][y] == 0:
                    self.letter_grid[x][y] = self.letter_frequencies.get_letter(float(random.randint(0, 10000))/100)
                    if IS_CHEAT_MODE:
                        self.letter_grid[x][y] = '.'
