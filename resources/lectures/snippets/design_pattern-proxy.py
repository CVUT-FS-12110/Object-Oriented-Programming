"""
Proxy pattern example.
"""
from abc import ABC, abstractmethod


class AbstractConnection(ABC):

    @abstractmethod
    def connect(self): pass


class Connection(AbstractConnection):

    def connect(self):
        print("Connecting ...")


class ProxyConnection(AbstractConnection):

    def __init__(self):
        self.connection = Connection()

    def connect(self):
        print("Checking connection security ...")
        self.connection.connect()


connection = ProxyConnection()
connection.connect()
