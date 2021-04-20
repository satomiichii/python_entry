class Animal:
    def __init__(self):
        self.num_eye = 2

    def breath(self):
        print('suuuu haaaa')


class Fish (Animal):
    def __init__(self):
        super().__init__()
        self.fin = True

    def breath(self):
        super().breath()
        print('Era kokyu')


sami = Fish()
sami.breath()