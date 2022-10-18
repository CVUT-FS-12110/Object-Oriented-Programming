from abc import ABC, abstractmethod

class NumberInterface(ABC):

    @abstractmethod
    def do_operation(self, value: int): pass

class ComplexNumberService():

    def do_the_complex_trick(self, value):
        if isinstance(value, complex):
            return complex(value.real * 2, value.imag * 3)
        else:
            raise Exception("Value is not complex")

class ServiceAdapter(NumberInterface, ComplexNumberService):

    def do_operation(self, value):
        value = complex(value)
        self.do_the_complex_trick(value)
        return value.real


a1 = ComplexNumberService()
print(a1.do_the_complex_trick(10+5j))

a2 = ServiceAdapter()
print(a2.do_operation(10))
