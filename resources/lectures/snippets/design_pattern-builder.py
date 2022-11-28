"""
Builder pattern example.
"""
from abc import ABC, abstractmethod

class Builder(ABC):

    @abstractmethod
    def get_product(self):
        pass

    @abstractmethod
    def create_partA(self):
        pass

    @abstractmethod
    def create_partB(self):
        pass


class ProductBuilder1(Builder):

    def __init__(self):
        self._product = Product()

    def get_product(self):
        return self._product

    def create_partA(self):
        self._product.add("PartA1")

    def create_partB(self):
        self._product.add("PartB1")


class Product():

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Parts: {', '.join(self.parts)}")


builder = ProductBuilder1()
builder.create_partA()
builder.create_partB()
builder.create_partA()

product001 = builder.get_product()
product001.list_parts()
