# Ex 23
import sys

script, encoding, error = sys.argv


def main(file, encoding, errors):
    line = file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, '<===>', cooked_string)


languages = open('ex23_sample.txt', encoding='utf-8')

main(languages, encoding, error)
