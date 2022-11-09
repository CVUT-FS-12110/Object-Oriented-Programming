"""
Lazy initialization pattern example.
"""
class NumberFactorial:

    def __init__(self, key):
        self.key = key
        self.value = self.factorial(key)

    def __str__(self):
        return "Factorial of {} is {}".format(self.key, self.value)

    def factorial(self, n):
        return 1 if (n==1 or n==0) else n * self.factorial(n - 1)


class Factorials:
    def __init__(self) -> None:
        self.numbers = {}

    def get(self, key):
        if key not in self.numbers:
            print("Calculating factorial for value: {}".format(key))
            self.numbers[key] = NumberFactorial(key)
        return self.numbers[key]

factorials = Factorials()
print(factorials.get(5))
print(factorials.get(6))
print(factorials.get(5))
