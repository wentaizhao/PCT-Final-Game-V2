import random
import csv
import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, first, last, year, major, minor):
        self.first = first
        self.last = last
        self.year = year
        self.major = major
        self.minor = minor

class Game:
    def __init__(self):
        self.people = []
        self.search = []
        self.missed = set()
        self.score = 0
        self.round_num = 0

    def load_game(self):
        with open("data.csv") as inFile:
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

        # Setup GUI
        self.root.title("Person Guessing Game")
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.question_label = tk.Label(self.frame, text="Welcome to the Game!")
        self.question_label.grid(row=0, column=0, columnspan=2)

        self.entry1_label = tk.Label(self.frame, text="Answer 1:")
        self.entry1_label.grid(row=1, column=0)
        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=1, column=1)

        self.entry2_label = tk.Label(self.frame, text="Answer 2:")
        self.entry2_label.grid(row=2, column=0)
        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=2, column=1)

        self.entry3_label = tk.Label(self.frame, text="Answer 3:")
        self.entry3_label.grid(row=3, column=0)
        self.entry3 = tk.Entry(self.frame)
        self.entry3.grid(row=3, column=1)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.check_answers)
        self.submit_button.grid(row=4, column=0, columnspan=2)

        self.stats_button = tk.Button(self.frame, text="Show Stats", command=self.show_stats)
        self.stats_button.grid(row=5, column=0, columnspan=2)

        self.load_next_round()

    def load_next_round(self):
        idx = self.game.next_round()
        if idx is None:
            self.show_stats()
            return

        self.current_person = self.game.people[idx]
        self.mode = random.randint(0, 1)

        if self.mode == 0:
            self.question_label.config(text=f"First name: {self.current_person.first}\nYear: {self.current_person.year}")
            self.entry1_label.config(text="Last name:")
            self.entry2_label.config(text="Major:")
            self.entry3_label.config(text="Minor:")
        else:
            self.question_label.config(text=f"Last name: {self.current_person.last}\nYear: {self.current_person.year}")
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
                self.game.missed.add(self.current_person.first + " " + self.current_person.last)

            if ans2 == self.current_person.major:
                self.game.score += 1
            else:
                self.game.missed.add(self.current_person.first + " " + self.current_person.last)

            if ans3 == self.current_person.minor:
                self.game.score += 1
            else:
                self.game.missed.add(self.current_person.first + " " + self.current_person.last)
        else:
            if ans1 == self.current_person.first:
                self.game.score += 1
            else:
                self.game.missed.add(self.current_person.first + " " + self.current_person.last)

            if ans2 == self.current_person.major:
                self.game.score += 1
            else:
                self.game.missed.add(self.current_person.first + " " + self.current_person.last)

            if ans3 == self.current_person.minor:
                self.game.score += 1
            else:
                self.game.missed.add(self.current_person.first + " " + self.current_person.last)

        self.load_next_round()

    def show_stats(self):
        accuracy = self.game.score / ((self.game.round_num - 1) * 3)
        missed_names = "\n".join(self.game.missed)
        messagebox.showinfo(
            "Game Stats",
            f"Score: {self.game.score}\n"
            f"Accuracy: {accuracy:.2f}\n"
            f"Missed names ({len(self.game.missed)}):\n{missed_names}"
        )

def main():
    game = Game()
    game.load_game()

    root = tk.Tk()
    gui = GUI(root, game)
    root.mainloop()

if __name__ == "__main__":
    main()
