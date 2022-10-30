"""
Iterator pattern example.
"""
# example with list
container = [1, 2, 3]

iterator = container.__iter__()

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# Custom iterator for custom container
class Iterator:

    def __init__(self, container):
        self.container = container
        self.idx = 0

    def __next__(self):
        if self.idx == len(self.container.content):
            raise StopIteration
        else:
            self.idx += 1
            return self.container.content[self.idx - 1]


class Container:

    def __init__(self):
        self.content = ["a", "b", "c"]

    def __iter__(self):
        return Iterator(self)


container = Container()
for item in container:
    print(item)
