"""
Decorator pattern example.
"""
class TitledName():

    def __init__(self, name_str):
        self._name_str = name_str

    def get(self):
        return self._name_str


class NameDecorator():

    def __init__(self, name):
        self._name = name

    def get(self):
        return self._name.get()


class MscDecorator(NameDecorator):

    def get(self):
        return "Msc. {}".format(self._name.get())


class PhdDecorator(NameDecorator):

    def get(self):
        return "{}, Ph.D.".format(self._name.get())


name1 = TitledName("Jane Doe")
name1 = MscDecorator(name1)
name1 = PhdDecorator(name1)

name2 = TitledName("John Doe")
name2 = MscDecorator(name2)

print(name1.get())
print(name2.get())
