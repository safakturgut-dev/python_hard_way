# Ex 15
from sys import argv

script, fname = argv

txt = open(fname)

print(f"Here's your file {fname}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
