class Singleton:
    __initialize = None

    def __init__(self, name):
        self.name = name
        if Singleton.__initialize is None:
            Singleton.__initialize = self
        else:
            raise Exception('already have an instance')


first = Singleton('first')


print(first.name)
