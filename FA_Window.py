from FA_Accents import FA_Accents as Accents
import FA_LanguageSelect as LanguageSelect
from FA_LanguageSelect import Language
from FA_Save import load_saved_entries
from FA_Save import save_new_entry
from FA_Translation import Translation
from FA_Translator import FA_Translator as Translator
from FA_WordList import WordList

from Wordsearch.FA_Wordsearch_Window import Wordsearch_Window

from tkinter import *

from datetime import date
from enum import Enum

class TranslateDirection(Enum):
    ForeignToEnglish = 0
    EnglishToForeign = 1

def get_icon_string():
    active_language = LanguageSelect.get_active_language()
    if active_language is Language.French:
        return "french_flag.ico"
    if active_language is Language.German:
        return "german_flag.ico"
    if active_language is Language.Spanish:
        return "spanish_flag.ico"

class MainWindow:
    def __init__(self, root):
        # region HEADER
        self.main_window = root
        self.frame_main = Frame(root)
        self.translator = Translator()
        self.saved_translations = load_saved_entries(LanguageSelect.get_active_language_string())
        self.wordsearch_window = None

        self.set_header()
        # endregion
        # region VARIABLES
        self.translate_direction = TranslateDirection.ForeignToEnglish
        self.string_source_label = StringVar()
        self.string_target_label = StringVar()
        self.string_source_label.set(str.format("{0}:", LanguageSelect.get_active_language_translated_string()))
        self.string_target_label.set("English:")
        self.string_source_text = StringVar()
        self.string_language_selection = StringVar()
        self.string_language_selection.set("Change Language")
        # endregion

        # region WIDGET DECLARATIONS
        self.frame_control = Frame(self.frame_main)
        self.label_source = Label(self.frame_control, textvariable=self.string_source_label)
        self.label_target = Label(self.frame_control, textvariable=self.string_target_label)
        self.text_source = Entry(self.frame_control, textvariable=self.string_source_text)
        self.text_source.bind("<Return>", self.translate)
        self.text_target = Entry(self.frame_control, state="readonly")
        self.button_translate = Button(self.frame_control, text="Translate", command=self.translate, state=DISABLED)
        self.button_save = Button(self.frame_control, text="Save", command=self.save, state=DISABLED)
        self.scale_direction = Scale(self.frame_control, from_=0, to=1, resolution=1, orient=HORIZONTAL, showvalue=0, command=self.set_direction)
        self.button_wordsearch = Button(self.frame_control, text="Word Search", command=self.generate_wordsearch)
        language_names = LanguageSelect.get_languages_translated_list()
        self.optionmenu_changelanguage = OptionMenu(self.frame_control, self.string_language_selection, *language_names, command=self.change_language)

        # endregion
        # region WIDGET ARRANGEMENTS
        self.label_source.grid(row=0, column=0)
        self.scale_direction.grid(row=0, column=1)
        self.label_target.grid(row=0, column=2)
        self.text_source.grid(row=1, column=0)
        self.text_target.grid(row=1, column=2)
        self.button_translate.grid(row=2, column=0)
        self.button_save.grid(row=2, column=2)
        self.button_wordsearch.grid(row=3, column=2)
        self.optionmenu_changelanguage.grid(row=4, column=2)
        self.frame_control.grid(row=0, column=0, sticky="N")
        self.frame_main.pack()

        # endregion
        # region CALLBACKS
        self.string_source_text.trace_add("write", self.on_source_changed)
        self.text_source.focus_set()
        # endregion

        self.accents = Accents(self)
        self.word_list = WordList(self.frame_main, self.saved_translations)

    def on_source_changed(self, *args):
        self.button_save.configure(state=DISABLED)
        if self.string_source_text.get() == "":
            self.button_translate.configure(state=DISABLED)
        else:
            self.button_translate.configure(state=NORMAL)

    def set_direction(self, value):
        self.translate_direction = TranslateDirection(int(value))

        swap = self.string_source_label.get()
        self.string_source_label.set(self.string_target_label.get())
        self.string_target_label.set(swap)

        swap = self.string_source_text.get()
        self.string_source_text.set(self.text_target.get())
        self.text_target.config(state="normal")
        self.text_target.delete(0, END)
        self.text_target.insert(0, swap)
        self.text_target.config(state="readonly")

        self.on_source_changed(None)

    def translate(self, event=None):
        if self.translate_direction is TranslateDirection.ForeignToEnglish:
            result = self.translator.translate_to_english(self.text_source.get())
        else:
            result = self.translator.translate_from_english(self.text_source.get())

        self.text_target.config(state="normal")
        self.text_target.delete(0, END)
        self.text_target.insert(0, result.text)
        self.text_target.config(state="readonly")
        self.button_save.configure(state=NORMAL)

    def save(self):
        if self.translate_direction is TranslateDirection.ForeignToEnglish:
            fr = self.text_source.get()
            en = self.text_target.get()
        else:
            en = self.text_source.get()
            fr = self.text_target.get()

        entry = Translation(en.title(), fr.title(), date.today().strftime("%d/%m/%Y"))
        if entry not in self.saved_translations:
            self.word_list.append_item(entry.english, entry.foreign, date.today())
            self.saved_translations.append(entry)
        save_new_entry(entry, LanguageSelect.get_active_language_string())

    def generate_wordsearch(self):
        self.wordsearch_window = Wordsearch_Window(self)

    def change_language(self, translated_string):
        new_language = LanguageSelect.get_language_from_translated_string(translated_string)
        LanguageSelect.set_active_language(new_language)
        self.frame_main.destroy()
        self.set_header()
        self.__init__(self.main_window)

    def set_header(self):
        self.main_window.title("FrancApp - Come up with a better name")
        self.main_window.iconbitmap(get_icon_string())

# endregion
