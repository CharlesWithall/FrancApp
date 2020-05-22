# load in the letters in a function in this file.
# distribute randomly across the board
# make sure rules are followed (two words can't share more than 1 letter, minimum number of words)
# distribute longest words first and encourage overlap

#This is the test pool
#Endroit
#Tant Pis
#Remporter
#Ailleurs
#Ecraser
#Diffuser
#Epouser
#FicheLeCamp
#Mouillée
#Foudroyant
#EnPassant
#CoupDeBol

#We want it to put down fiche le camp and then spot that foudroyant also begins with f and use the same f then
#enpassant could use the t at the end of foudroyant as well etc.
#Default to 15x15?
#Getlongest word, choose a random spot where it will fit.
#Get next word, see if it can intersect with any of the existing words otherwise random
# Grid format as follows
# [0,0] [1,0] [2,0]
# [0,1] [1,1] [2,1]
# [0,2] [1,2] [2,2]

# need to add logic to add more than one word

# I need to add a list of words that have been added in a navigatable format.
# I think this will be in the format of a linked list of letters and coordinates. LinkedListLetterEntry

from Wordsearch.FA_Wordsearch_Letter_Frequency import LetterFrequencies
import Wordsearch.FA_Wordsearch_Grid_Navigation as GridNavigator
from Wordsearch.FA_Wordsearch_Grid_Navigation import WordDirection

import random

class FA_WordsearchGenerator:
    def __init__(self):
        # a lot of this stuff should be read in by the constructor and in the generate function
        self.grid_size = 15
        self.letter_grid = [[0 for x in range(self.grid_size)] for y in range(self.grid_size)]
        self.word_list = ["Endroit", "Tant Pis", "Remporter", "Ailleurs", "Ecraser", "Diffuser", "Epouser",
                          "FicheLeCamp", "Mouillée", "Foudroyant", "EnPassant", "CoupDeBol"]
        self.letter_frequencies = LetterFrequencies()

    def debug_display(self):
        for line in self.letter_grid:
            print(str(line).replace(",", "").replace("'", ""))

    def generate(self):
        existing_words = []
        for new_word in self.word_list:
            new_word = new_word.upper().replace(" ", "")
            new_word_length = len(new_word)
            word_location_found = False

            for existing_word in existing_words:
                for letter_entry in existing_word:
                    if letter_entry.letter in new_word:
                        start, direction = self.try_fit_word_to_grid(letter_entry, new_word)
                        if start is not None and direction is not None:
                            existing_words.append(self.add_word_to_grid(new_word, direction, start))
                            word_location_found = True
                            break

                if word_location_found:
                    break

            while not word_location_found:
                random_direction = random.choice(list(WordDirection))
                coordinates = GridNavigator.get_random_start_coordinate_for_word_length(random_direction, new_word_length, self.grid_size)
                if self.verify_no_overlap(coordinates[0], coordinates[1], new_word_length, random_direction):
                    existing_words.append(self.add_word_to_grid(new_word, random_direction, coordinates))
                    word_location_found = True

        self.fill_grid_with_random_letters()
        return self.letter_grid

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
            letters.append(GridNavigator.LetterEntry(letter, x, y))
            self.letter_grid[x][y] = letter
            x, y = GridNavigator.get_next_coordinate_in_direction(direction, x, y)

        return letters

    def fill_grid_with_random_letters(self):
        for x in range(0, self.grid_size):
            for y in range(0, self.grid_size):
                if self.letter_grid[x][y] == 0:
                    self.letter_grid[x][y] = self.letter_frequencies.get_letter(float(random.randint(0, 10000))/100)

# test = FA_WordsearchGenerator()
# test.generate()
# test.debug_display()
# print(0)


