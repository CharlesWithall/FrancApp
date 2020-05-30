from FA_Translation import Translation

import json
import os

save_path = "save_data.json"

json_active_language = "Active_Language"
json_translations = "Translations"

def save_new_entry(translation, language_name):
    if not os.path.exists(save_path):
        with open(save_path, 'w') as f:
            data = {}
            json.dump(data, f)

    with open(save_path, 'r+') as f:
        data = json.load(f)
        if json_translations not in data:
            data[json_translations] = {}
        if language_name not in data[json_translations]:
            data[json_translations][language_name] = {}

        data[json_translations][language_name][translation.foreign] = [translation.english, translation.datetime]
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def load_saved_entries(language_name):
    if not os.path.exists(save_path):
        return

    with open(save_path, 'r') as json_file:
        out_array = []
        data = json.load(json_file)
        if json_translations in data:
            if language_name in data[json_translations]:
                for item in data[json_translations][language_name].items():
                    fr = item[0]
                    en = item[1][0]
                    dt = item[1][1]
                    out_array.append(Translation(en, fr, dt))

        return out_array

def save_active_language(language_name):
    if not os.path.exists(save_path):
        with open(save_path, 'w') as f:
            data = {}
            json.dump(data, f)

    with open(save_path, 'r+') as f:
        data = json.load(f)
        data[json_active_language] = language_name
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def load_active_language():
    if not os.path.exists(save_path):
        return

    with open(save_path, 'r') as json_file:
        data = json.load(json_file)
        return data[json_active_language]

