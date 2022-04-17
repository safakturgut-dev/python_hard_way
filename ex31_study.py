print("""There is one big prize in one of these three boxes.
Choose one so you might be rich!(1-2-3)""")

box = input("> ")

if box == "1":
    print('Congratulations you won a bicycle.')
    print('Big prize was not in this box.')

elif box == '2':
    print('Congrats you won the big prize.')
    print('It is a brand new Ferrari car.')

elif box == '3':
    print('Congrats you won a scooter.')
    print('No big prize, sorry.')

else:
    print('There are only 3 boxes {} this is not available.'.format(box))
