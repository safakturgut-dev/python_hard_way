# Ex 21 study
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


age = add(30, 5)
height = subtract(70, 8)
weight = multiply(90, 2)
iq = divide(180, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ:{iq}")

r1 = divide(iq, 2)
r2 = multiply(weight, r1)
r3 = subtract(height, r2)
r4 = add(age, r3)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# formula = age + (height - (weight * (iq / 2)))

print(what, r4)

my_formula = 8 * (4 + 5) - 12 / (10 - 7)

f2 = subtract(multiply(8, add(4, 5)), divide(12, subtract(10, 7)))

print(my_formula, f2)
