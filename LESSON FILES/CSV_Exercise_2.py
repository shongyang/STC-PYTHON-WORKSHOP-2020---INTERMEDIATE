import csv

# Enumerating rows

with open("breakfast.csv", "r") as f2, open("breakfasts.csv", "w", newline="") as f2a:
    rd = csv.reader(f2)
    wr = csv.writer(f2a)
    for idx, row in enumerate(rd, 0):
        output = [idx] + row[0:]  # output = [idx] + row[1:] <- removes idnex no.
        wr.writerow(output)

# Reading, Method A1

with open("breakfasts.csv", "r") as f4:
    rd = csv.reader(f4)
    for row in rd:
        print(row[0], row[1], " I had " + row[3] + " of " + row[2])

# DictReader, Method A2
with open("breakfasts.csv", "r", newline="") as filez:
    rd = csv.DictReader(filez)
    for row in rd:
        print(row["0"], " I had " + row["ounces"] + " of " + row["food"])

# Text-to-Speech, Method B
import pyttsx3

engine = pyttsx3.init()

with open("breakfasts.csv", "r") as f2:
    rd = csv.reader(f2)
    next(rd)  # skip
    for row in rd:
        typewhatever = row[0], row[1], " I had " + row[3] + " of " + row[2]
        engine.say(typewhatever)

engine.runAndWait()