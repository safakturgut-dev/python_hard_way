def numbers1(ending, step):
    i = 0
    numbers = []

    while i < ending:
        print(f'At the top i is {i}')
        numbers.append(i)

        i += step
        print('Numbers now:', numbers)
        print(f'At the bottom i is {i}')

    print('The numbers: ')

    for num in numbers:
        print(num)


numbers1(11, 2)


numbers = []

for i in range(16):
    print(f'At the top i is {i}')
    numbers.append(i)

    i += 1
    print('Numbers now:', numbers)
    print(f'At the bottom i is {i}')

print('The numbers: ')

for num in numbers:
    print(num)
