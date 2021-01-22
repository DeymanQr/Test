class A:
    def __init__(self):
        self.test_func()

    def test_func(self):
        print('Minecraft')


class B(A):
    def __init__(self):
        super().test_func()
