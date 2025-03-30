# Create the following variables:
# n = 2022
# x = math.pi   # save with 5 digits after a dot (import 'math' first!)
# word = "Python"
# polish = "książka"   # 'book' in English
# Write the variables to a text file "vars.txt",
# one line for one variable.
# Print the file content on the screen.

import math

n = 2022
x = round(math.pi, 5)
word = "Python"
polish = "książka"

with open("vars.txt", "w", encoding="utf-8") as file:
    file.write(f"n = {n}\n")
    file.write(f"x = {x}\n")
    file.write(f"word = {word}\n")
    file.write(f"polish = {polish}\n")

with open("vars.txt", "r", encoding="utf-8") as file:
    print(file.read())