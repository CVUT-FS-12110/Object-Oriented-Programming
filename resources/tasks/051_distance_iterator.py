"""
    vvvv      YOUR SOLUTION      vvvv
"""

class DistanceIterator:
    
    def __init__(self, numbers):
        # constructor of our Iterator
        pass
    
    def __iter__(self):
        # "initialize our iterator here"
        return self
    
    def __next__(self):
        # next method
        # do not forget to put `raise StopIteration`
        pass


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""

# empty number list
assert [n for n in DistanceIterator([])] == []

# one number in list --> also no distances
assert [n for n in DistanceIterator([4])] == []

# some examples
assert [n for n in DistanceIterator([4,2,-2])] == [2,6,4]
assert [n for n in DistanceIterator([3,3,3,8])] == [0, 0, 5, 0, 5, 5]
assert [n for n in DistanceIterator([-1,20,23,-5,8])] == [21, 24, 4, 9, 3, 25, 12, 28, 15, 13]
