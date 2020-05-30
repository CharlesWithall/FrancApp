import FA_Save as Save

from enum import Enum

class Language(Enum):
    French = 0
    German = 1
    Spanish = 2

active_language = Language.German

french_abbreviation = "fr"
german_abbreviation = "de"
spanish_abbreviation = "es"

french_translated = "Français"
german_translated = "Deutsch"
spanish_translated = "Español"

def get_languages_translated_list():
    return [get_language_translated_string(language) for language in list(Language)]

def init_language():
    global active_language
    active_language = Language[Save.load_active_language()]

def get_active_language():
    return active_language

def get_active_language_string():
    return active_language.name

def get_active_language_abbreviation_string():
    if active_language is Language.French:
        return french_abbreviation
    if active_language is Language.German:
        return german_abbreviation
    if active_language is Language.Spanish:
        return spanish_abbreviation

def get_active_language_translated_string():
    return get_language_translated_string(active_language)

def get_language_translated_string(language):
    if language is Language.French:
        return french_translated
    if language is Language.German:
        return german_translated
    if language is Language.Spanish:
        return spanish_translated

def get_language_from_translated_string(string):
    if string == french_translated:
        return Language.French
    if string == german_translated:
        return Language.German
    if string == spanish_translated:
        return Language.Spanish

def set_active_language(new_language):
    global active_language
    active_language = new_language
    Save.save_active_language(new_language.name)
