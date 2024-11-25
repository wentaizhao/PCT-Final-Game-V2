import random
import csv
from collections import defaultdict
import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, first, last, year, major, minor):
        self.first = first
        self.last = last
        self.year = year
        self.major = major
        self.minor = minor

class Entry:
    def __init__(self, category, answered, correct):
        self.category = category
        self.answered = answered
        self.correct = correct

class Game:
    def __init__(self):
        self.people = []
        self.search = []
        self.missed = defaultdict(list)
        self.score = 0
        self.round_num = 0

    def load_game(self):
        with open("f24.csv") as inFile:
            readerObj = csv.reader(inFile)
            for line in readerObj:
                info = tuple(line)
                self.people.append(Person(info[0], info[1], info[2], info[3], info[4]))
            
        self.search = list(range(len(self.people)))
        random.shuffle(self.search)

    def next_round(self):
        if self.round_num < len(self.people):
            idx = self.search[self.round_num]
            self.round_num += 1
            return idx
        return None

class GUI:
    def __init__(self, root, game):
        self.game = game
        self.root = root
        self.current_person = None
        self.mode = 0

        self.root.title("PCT Final Game")
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.round_label = tk.Label(self.frame, text="Round: 0/0", font=("Arial", 16))
        self.round_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.question_label = tk.Label(self.frame, text="Welcome to the Game!", font=("Arial", 14), wraplength=400)
        self.question_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.entry1_label = tk.Label(self.frame, text="Answer 1:")
        self.entry1_label.grid(row=2, column=0, sticky=tk.W)
        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=2, column=1)

        self.entry2_label = tk.Label(self.frame, text="Answer 2:")
        self.entry2_label.grid(row=3, column=0, sticky=tk.W)
        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=3, column=1)

        self.entry3_label = tk.Label(self.frame, text="Answer 3:")
        self.entry3_label.grid(row=4, column=0, sticky=tk.W)
        self.entry3 = tk.Entry(self.frame)
        self.entry3.grid(row=4, column=1)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.check_answers)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.stats_button = tk.Button(self.frame, text="Show Stats", command=self.show_stats)
        self.stats_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.load_next_round()

    def load_next_round(self):
        idx = self.game.next_round()
        if idx is None:
            self.show_stats()
            return

        self.current_person = self.game.people[idx]
        self.mode = random.randint(0, 1)

        self.round_label.config(
            text=f"Round: {self.game.round_num}/{len(self.game.people)}"
        )

        if self.mode == 0:
            self.question_label.config(
                text=f"First name: {self.current_person.first}\nYear: {self.current_person.year}"
            )
            self.entry1_label.config(text="Last name:")
            self.entry2_label.config(text="Major:")
            self.entry3_label.config(text="Minor:")
        else:
            self.question_label.config(
                text=f"Last name: {self.current_person.last}\nYear: {self.current_person.year}"
            )
            self.entry1_label.config(text="First name:")
            self.entry2_label.config(text="Major:")
            self.entry3_label.config(text="Minor:")

        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)

    def check_answers(self):
        ans1 = self.entry1.get().strip()
        ans2 = self.entry2.get().strip()
        ans3 = self.entry3.get().strip()

        if self.mode == 0:
            if ans1 == self.current_person.last:
                self.game.score += 1
            else:
                self.game.missed[f"{self.current_person.first} {self.current_person.last}"].append(Entry("Last", ans1, self.current_person.last))

            if ans2 == self.current_person.major:
                self.game.score += 1
            else:
                self.game.missed[f"{self.current_person.first} {self.current_person.last}"].append(Entry("Major", ans2, self.current_person.major))

            if ans3 == self.current_person.minor:
                self.game.score += 1
            else:
                self.game.missed[f"{self.current_person.first} {self.current_person.last}"].append(Entry("Minor", ans3, self.current_person.minor))
        else:
            if ans1 == self.current_person.first:
                self.game.score += 1
            else:
                self.game.missed[f"{self.current_person.first} {self.current_person.last}"].append(Entry("First", ans1, self.current_person.first))

            if ans2 == self.current_person.major:
                self.game.score += 1
            else:
                self.game.missed[f"{self.current_person.first} {self.current_person.last}"].append(Entry("Major", ans2, self.current_person.major))

            if ans3 == self.current_person.minor:
                self.game.score += 1
            else:
                self.game.missed[f"{self.current_person.first} {self.current_person.last}"].append(Entry("Minor", ans3, self.current_person.minor))

        self.load_next_round()

    def show_stats(self):
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Stats")
        stats_window.geometry("800x300") 

        text_widget = tk.Text(stats_window, wrap=tk.WORD)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(stats_window, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget.config(yscrollcommand=scrollbar.set)

        stats_text = (
            f"Score: {self.game.score}/{((self.game.round_num - 1) * 3)}\n\n"
            f"Missed Names ({len(self.game.missed)}):\n\n"
        )
        if self.game.missed:
            for name, entries in self.game.missed.items():
                stats_text += f"    {name.title().center(30, "-")}\n"
                for entry in entries:
                    stats_text += f"    {entry.category}\n"
                    stats_text += f"        Correct: {entry.correct}\n"
                    stats_text += f"        Answered: {entry.answered}\n"
                stats_text += "\n"
        else:
            stats_text += "None"

        text_widget.insert(tk.END, stats_text)
        text_widget.config(state=tk.DISABLED)

def main():
    game = Game()
    game.load_game()

    root = tk.Tk()
    gui = GUI(root, game)
    root.mainloop()

if __name__ == "__main__":
    main()
