from sys import argv

script, fname = argv

f = open(fname)

content = f.read()

print(content)

f.close()

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# lines = f"{line1}\n{line2}\n{line3}\n"
# target.write(lines)

# truncate() not necessary write method alredy empty the file before write to it.
