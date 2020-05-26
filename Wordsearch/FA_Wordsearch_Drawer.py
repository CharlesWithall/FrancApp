from Wordsearch.FA_Wordsearch_Defines import letter_spacing

def snap_to_grid(x, y):
    return round(x / letter_spacing) * letter_spacing, round(y / letter_spacing) * letter_spacing

class WordSearchDrawer:
    def __init__(self, root, entries):
        self.root = root
        self.entries = entries
        self.source_coords = None
        self.drawn_line = None
        root.canvas_letter_grid.bind('<Motion>', self.draw_selection)
        root.canvas_letter_grid.bind('<ButtonPress>', self.start_draw)
        root.canvas_letter_grid.bind('<ButtonRelease>', self.stop_draw)

    def start_draw(self, event):
        self.source_coords = (snap_to_grid(event.x, event.y))

    def stop_draw(self, event):
        if self.drawn_line:
            self.root.canvas_letter_grid.delete(self.drawn_line)

        mouse_pos = snap_to_grid(event.x, event.y)

        for entry in self.entries:
            endpoint_start = (entry.get_start_point().x * letter_spacing) + letter_spacing, (entry.get_start_point().y * letter_spacing) + letter_spacing
            endpoint_end = (entry.get_end_point().x * letter_spacing) + letter_spacing, (entry.get_end_point().y * letter_spacing) + letter_spacing

            selection_is_correct = False
            if endpoint_start[0] == mouse_pos[0] and endpoint_start[1] == mouse_pos[1]:
                if endpoint_end[0] == self.source_coords[0] and endpoint_end[1] == self.source_coords[1]:
                    selection_is_correct = True

            elif endpoint_end[0] == mouse_pos[0] and endpoint_end[1] == mouse_pos[1]:
                if endpoint_start[0] == self.source_coords[0] and endpoint_start[1] == self.source_coords[1]:
                    selection_is_correct = True

            if selection_is_correct:
                if not entry.is_complete:
                    entry.is_complete = True
                    all_complete = all([t.is_complete for t in self.entries])
                    self.root.set_word_complete(entry.english, all_complete)
                    self.root.canvas_letter_grid.create_line(endpoint_start[0], endpoint_start[1], endpoint_end[0],
                                                             endpoint_end[1], fill="orange", width=10, stipple="gray50")
                break

        self.source_coords = None

    def draw_selection(self, event):
        if self.source_coords:
            if self.drawn_line:
                self.root.canvas_letter_grid.delete(self.drawn_line)
            self.drawn_line = self.root.canvas_letter_grid.create_line(self.source_coords[0], self.source_coords[1],
                                                                       event.x, event.y, fill="blue", width=10,
                                                                       stipple="gray50")
