from FA_Translation import Translation

import json
import os

save_path = "save_data.json"

def save_new_entry(translation):
    if not os.path.exists(save_path):
        with open(save_path, 'w') as f:
            data = {}
            json.dump(data, f)

    with open(save_path, 'r+') as f:
        data = json.load(f)
        data[translation.french] = [translation.english, translation.datetime]
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def load_saved_entries():
    if not os.path.exists(save_path):
        return

    with open(save_path, 'r') as json_file:
        out_array = []
        data = json.load(json_file)
        for item in data.items():
            fr = item[0]
            en = item[1][0]
            dt = item[1][1]
            out_array.append(Translation(en, fr, dt))

        return out_array
