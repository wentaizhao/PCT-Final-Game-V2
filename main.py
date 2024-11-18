# import random
# import csv

# class Person:
#     def __init__(self, first, last, year, major, minor):
#         self.first = first
#         self.last = last
#         self.year = year
#         self.major = major
#         self.minor = minor

# class Game:
#     def __init__(self):
#         self.people = []
#         self.search = []
#         self.missed = []
#         self.score = 0

#     def load_game(self):
#         with open("data.csv") as inFile:
#             readerObj = csv.reader(inFile)
#             for line in readerObj:
#                 info = tuple(line)
#                 self.people.append(Person(info[0], info[1], info[2], info[3], info[4]))
            
#         self.search = list(range(len(self.people)))
#         random.shuffle(self.search)

#     def play_game(self):
#         for i in range(len(self.people)):
#             self.play_round(self.search[i], i)

#     def play_round(self, idx, round_num):
#         person = self.people[idx]
#         first_correct = person.first
#         last_correct = person.last
#         year_correct = person.year
#         major_correct = person.major
#         minor_correct = person.minor

#         mode = random.randint(0, 1)

#         print(f"-----------Round: {round_num + 1}/{len(self.people)}-----------")
#         ans1 = ""
#         ans2 = ""
#         ans3 = ""

#         if mode == 0:
#             print(f"First name: {first_correct}")
#             print(f"Year: {year_correct}\n")

#             ans1 = input("Last name: ")
#             ans2 = input("Major: ")
#             ans3 = input("Minor: ")

#         else:
#             print(f"Last name: {last_correct}")
#             print(f"Year: {year_correct}\n")

#             ans1 = input("First name: ")
#             ans2 = input("Major: ")
#             ans3 = input("Minor: ")

#         if mode == 0:
#             if ans1 == last_correct:
#                 print("Correct")
#                 self.score += 1
#             else:
#                 print(f"Incorrect - {last_correct}")
#                 self.missed.append(first_correct)
#         else:
#             if ans1 == first_correct:
#                 print("Correct")
#                 self.score += 1
#             else:
#                 print(f"Incorrect - {first_correct}")
#                 self.missed.append(first_correct)

#         if ans2 == major_correct:
#                 print("Correct")
#                 self.score += 1
#         else:
#             print(f"Incorrect - {major_correct}")
#             self.missed.append(first_correct)

#         if ans3 == minor_correct:
#             print("Correct")
#             self.score += 1
#         else:
#             print(f"Incorrect - {minor_correct}")
#             self.missed.append(first_correct)

#         print("\n\n")

#     def print_stats(self):
#         print("-----------Game Complete-----------")
#         print(f"Score: {self.score}")
#         accuracy = self.score / (len(self.people) * 3)
#         print(f"Accuracy: {accuracy:.2f}")
#         print("Missed names:")
#         for name in self.missed:
#             print(f"\t{name}")

# def main():
#     game = Game()
#     game.load_game()
#     game.play_game()
#     game.print_stats()

# if __name__ == "__main__":
#     main()
