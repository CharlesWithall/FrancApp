import tkinter as tk
import tkinter.font as tkfont

from Wordsearch.FA_Wordsearch_Generator import WordsearchGenerator
from Wordsearch.FA_Wordsearch_Drawer import WordSearchDrawer
from Wordsearch.FA_Wordsearch_Gameover_Window import WordsearchGameOverWindow
import Wordsearch.FA_Wordsearch_Defines as wsDef

from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC, SND_PURGE

class Wordsearch_Window:
    def __init__(self, root):
        self.root = root
        self.generator = WordsearchGenerator()

        self.clue_font = tkfont.Font(family="Helvetica", size=12)
        self.clue_complete_font = tkfont.Font(family="Helvetica", size=12, overstrike=1)

        self.window = tk.Toplevel(root.main_window)
        self.window.wm_title("Word Search")
        self.window.grab_set()

        self.frame_main = tk.Frame(self.window)
        self.frame_letter_grid = tk.Frame(self.frame_main)

        self.canvas_letter_grid = tk.Canvas(self.frame_letter_grid, width=wsDef.canvas_dimension, height=wsDef.canvas_dimension)
        self.frame_word_list = tk.Frame(self.frame_main)
        self.labelarray_wordlist = []

        self.num_words_found = 0

        letter_grid, entries = self.generator.generate(wsDef.grid_size, root.saved_translations, wsDef.number_of_words)

        for i, line in enumerate(letter_grid):
            for j, character in enumerate(line):
                x = (i * wsDef.letter_spacing) + wsDef.letter_spacing
                y = (j * wsDef.letter_spacing) + wsDef.letter_spacing
                self.canvas_letter_grid.create_text(x, y, text=character, font=("Arial", wsDef.font_size))

        for i, word in enumerate(entries):
            label = tk.Label(self.frame_word_list, text=word.english, font=self.clue_font)
            self.labelarray_wordlist.append(label)
            label.grid(row=i)

        self.canvas_letter_grid.pack()
        self.frame_letter_grid.pack(side=tk.LEFT)
        self.frame_word_list.pack(padx=5, side=tk.RIGHT)
        self.drawer = WordSearchDrawer(self, entries)
        self.frame_main.pack()

    def set_word_complete(self, word_en, all_complete):
        for label in self.labelarray_wordlist:
            if label.cget("text") == word_en:
                label.configure(font=self.clue_complete_font)
                self.num_words_found += 1
                break

        if all_complete:
            PlaySound('wordsearch/wordsearch_complete.wav', SND_FILENAME | SND_ASYNC)
            WordsearchGameOverWindow(self.root)
        else:
            sound_file = str.format('wordsearch/wordsearch_success_{0}.wav', (self.num_words_found - 1 % 5) + 1)
            PlaySound(sound_file, SND_FILENAME | SND_ASYNC)

    # TODO: What if word is longer than the grid?!
    # TODO: What if there aren't enough words?!
