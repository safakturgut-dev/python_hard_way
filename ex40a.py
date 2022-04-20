import ex40_module as mod40

mod40.apple()

print(mod40.tangerine)


class MyStuff:
    '''Explanation'''

    def __init__(self) -> None:
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I am classy apples!")


thing = MyStuff()
thing.apple()
thing.size = 20

print(thing.size)
