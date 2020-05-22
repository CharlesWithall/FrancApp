from tkinter import *
from datetime import datetime

class WordList:
    def __init__(self, root, saved_words):
        self.textbox_wordlist = Text(root)
        self.textbox_wordlist.grid(row=0, column=1)

        self.month = 0
        for item in saved_words:
            dt = datetime.strptime(item.datetime, '%d/%m/%Y')
            self.append_item(item.english, item.french, dt)

    def append_item(self, en, fr, dt):
        self.textbox_wordlist.configure(state="normal")
        if dt.month is not self.month:
            self.month = dt.month
            self.textbox_wordlist.insert(index='end', chars="------------------------------------\n")
            self.textbox_wordlist.insert(index='end', chars=dt.strftime("%B") + "\n")
            self.textbox_wordlist.insert(index='end', chars="------------------------------------\n")
        self.textbox_wordlist.insert(index='end', chars="{}: {}\n".format(fr, en))
        self.textbox_wordlist.configure(state="disabled")



