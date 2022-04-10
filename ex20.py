# Ex 20
from sys import argv

script, f = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_line(linecount, f):
    print(linecount, f.readline())


current_file = open(f)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

cur_line = 1
print_line(cur_line, current_file)

cur_line += 1
print_line(cur_line, current_file)

cur_line += 1
print_line(cur_line, current_file)
