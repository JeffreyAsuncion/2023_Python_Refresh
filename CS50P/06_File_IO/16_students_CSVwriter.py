import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students_16.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
