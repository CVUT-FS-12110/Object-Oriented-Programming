"""
Prototype pattern example.
"""
import copy

class Prototype:

    def clone(self):
        return copy.deepcopy(self)

class Individual(Prototype):

    def __init__(self):
        self.genome = "000"

    def evolve(self, new_gene):
        self.genome += new_gene

    def __str__(self):
        return "My genome is: {}".format(self.genome)

genome1 = Individual()
genome1.evolve("101")
genome2 = genome1.clone()
genome2.evolve("111")
genome1.evolve("000")
print(genome1)
print(genome2)
