from tkinter import *
from Wordsearch.FA_Wordsearch_Generator import FA_WordsearchGenerator as WordsearchGenerator
from Wordsearch.FA_Wordsearch_Drawer import WordSearchDrawer

number_of_words = 14
grid_size = 15

class Wordsearch_Window:
    def __init__(self):
        self.window = None
        self.frame_main = None
        self.frame_letter_grid = None
        self.frame_word_list = None
        self.textbox_wordlist = None
        self.generator = WordsearchGenerator()
        self.drawer = None

    def launch(self, root):
        self.window = Toplevel(root.main_window)
        self.window.wm_title("Word Search")
        self.window.grab_set()

        self.drawer = WordSearchDrawer(self.window)

        self.frame_main = Frame(self.window)
        self.frame_letter_grid = Frame(self.frame_main)
        self.frame_word_list = Frame(self.frame_main)

        self.textbox_wordlist = Text(self.frame_word_list)

        wordsearch, wordlist = self.generator.generate(grid_size, [t.english for t in root.saved_translations], number_of_words)
        # send letters to grid here
        for i, line in enumerate(wordsearch):
            for j, character in enumerate(line):
                label = Label(self.frame_letter_grid, text=character)
                label.grid(row=i, column=j)

        wordlist.sort(key=lambda w: len(w))
        for word in wordlist:
            self.textbox_wordlist.insert(index='end', chars="{}\n".format(word))
        self.textbox_wordlist.configure(state="disabled", width=len(wordlist[-1]) + 1)

        self.textbox_wordlist.pack()
        self.frame_letter_grid.pack(side=LEFT)
        self.frame_word_list.pack(side=RIGHT)
        self.frame_main.pack()
