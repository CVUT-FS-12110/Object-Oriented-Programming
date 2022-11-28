"""
Builder pattern example (featuring director class).
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
        self.new()

    def new(self):
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


class Director:

    def __init__(self, builder):
        self._builder = builder

    def build_ABA_product(self):
        self._builder.new()
        self._builder.create_partA()
        self._builder.create_partB()
        self._builder.create_partA()
        return self._builder.get_product()

    def build_AB_product(self):
        self._builder.new()
        self._builder.create_partA()
        self._builder.create_partB()
        return self._builder.get_product()

director = Director(ProductBuilder1())

product001 = director.build_AB_product()
product001.list_parts()

product002 = director.build_ABA_product()
product002.list_parts()
