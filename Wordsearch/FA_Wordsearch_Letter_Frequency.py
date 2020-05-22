import json
import os

frequency_path = "Wordsearch/french_letter_frequencies.json"

class LetterFrequencyDefinition:
    def __init__(self, letter, frequency, cumulative_frequency):
        self.letter = letter
        self.frequency = frequency
        self.cumulative_frequency = cumulative_frequency

class LetterFrequencies:
    def __init__(self):
        self.frequency_search_list = []
        self.load_letter_frequencies()

    def load_letter_frequencies(self):
        if not os.path.exists(frequency_path):
            print("ERROR: Letter frequency path not found")
            return

        with open(frequency_path, encoding="utf-8") as json_file:
            out_array = []
            data = json.load(json_file)
            frequency_cumulation = 0
            for item in data.items():
                letter = item[0]
                frequency = item[1]
                frequency_cumulation += frequency
                entry = LetterFrequencyDefinition(letter, frequency, frequency_cumulation)
                self.frequency_search_list.append(entry)

            return out_array

    def get_letter(self, percentage):
        for entry in self.frequency_search_list:
            if entry.cumulative_frequency >= percentage:
                return entry.letter
        return 'E'
