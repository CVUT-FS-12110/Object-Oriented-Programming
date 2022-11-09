"""
Factory method pattern example
"""
from abc import ABC, abstractmethod

class DataStore(ABC):

    @abstractmethod
    def create_array(self):
        pass


class Array(ABC):

    @abstractmethod
    def create_array(self):
        pass


class Vector(Array):

    pass


class Matrix(Array):

    pass


class MatrixDataStore(DataStore):

    def create_array(self):
        return Matrix()


class VectorDataStore(DataStore):

    def create_array(self):
        return Array()


storages = [MatrixDataStore(), VectorDataStore()]:
for storage in storages:
    array = storage.create_array()
    # do something nice with array
