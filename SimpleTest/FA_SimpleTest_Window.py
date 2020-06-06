# window loads a word and then four buttons
# 10 questions
# keep score but don't save
import random
import tkinter as tk
import tkinter.font as tkfont

from SimpleTest.FA_SimpleTest_Question import Question
import SimpleTest.FA_SimpleTest_Defines as Defines

from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC, SND_PURGE

class SimpleTest_Window:
    def __init__(self, root):
        self.root = root

        self.font = tkfont.Font(family="Helvetica", size=12)

        self.window = tk.Toplevel(root.main_window)
        self.window.wm_title("Quiz")
        self.window.grab_set()

        self.score = 0
        self.question_index = 0

        self.font = tkfont.Font(family="Helvetica", size=14)
        self.big_font = tkfont.Font(family="Helvetica", size=24)

        self.frame_main = None

        self.questions = self.qenerate_test_questions(root.saved_translations)
        self.given_answer_indices = []
        self.display_next_question()

    @staticmethod
    def qenerate_test_questions(word_list):
        questions = []
        clue_word_entries = random.sample(word_list, Defines.num_questions)
        for entry in clue_word_entries:
            question = Question(entry.foreign)
            potential_answers = random.sample(word_list, 4)
            answers = [entry.english]
            for wrong_answer in potential_answers:
                if wrong_answer.foreign is not entry.foreign and len(answers) < 4:
                    answers.append(wrong_answer.english)
            random.shuffle(answers)
            question.answers = answers
            question.answer_index = answers.index(entry.english)
            questions.append(question)
        return questions

    def display_next_question(self):
        self.frame_main = tk.Frame(self.window)
        frame_question = tk.Frame(self.frame_main)
        frame_answers = tk.Frame(self.frame_main)
        frame_score = tk.Frame(self.frame_main)

        label_clue = tk.Label(frame_question, font=self.font, text=self.questions[self.question_index].clue)
        label_clue.pack()

        for i, answer in enumerate(self.questions[self.question_index].answers):
            button_answer = tk.Button(frame_answers, text=answer, font=self.font,
                                      command=lambda i=i: self.answer_callback(i))
            button_answer.grid(column=i & (1 << 0), row=i & (1 << 1))

        label_score = tk.Label(frame_score, font=self.font, text=str.format("{0}/{1}", self.score, Defines.num_questions))
        label_score.pack()

        frame_question.pack()
        frame_answers.pack()
        frame_score.pack()

        self.frame_main.pack()

    def game_over(self):
        self.frame_main = tk.Frame(self.window)

        frame_left = tk.Frame(self.frame_main)
        label_score = tk.Label(frame_left, text=str.format("{0}/{1}", self.score, Defines.num_questions), font=self.big_font)
        button_new_game = tk.Button(frame_left, text="New Game", font=self.font, command=self.regenerate)
        button_exit = tk.Button(frame_left, text="Exit", font=self.font, command=self.exit)

        button_new_game.grid(row=1, column=0, padx=5, pady=5)
        button_exit.grid(row=1, column=1, padx=5, pady=5)

        frame_right = tk.Frame(self.frame_main)
        for i, question in enumerate(self.questions):
            given_answer_index = self.given_answer_indices[i]
            text = str.format("{0}: {1} - You Answered: {2}", question.clue, question.get_correct_answer(), question.answers[given_answer_index])
            label = tk.Label(frame_right, text=text, font=self.font)
            if question.answer_index is given_answer_index:
                label.config(fg="green")
            else:
                label.config(fg="red")
            label.grid(row=i)

        label_score.grid(row=0, columnspan=1)
        frame_left.pack(side=tk.LEFT)
        frame_right.pack(side=tk.RIGHT)
        self.frame_main.pack()

    def regenerate(self):
        self.exit()
        self.root.generate_simpletest()

    def exit(self):
        self.window.destroy()

    def answer_callback(self, i):
        self.frame_main.destroy()
        self.given_answer_indices.append(i)

        if i is self.questions[self.question_index].answer_index:
            self.score += 1

        self.question_index += 1
        # TODO: play sound effect
        if self.question_index < Defines.num_questions:
            self.display_next_question()
        else:
            self.game_over()


    # TODO: End game summary screen of correct and incorrect answers









