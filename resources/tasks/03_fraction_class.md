# 03 - Fraction class

Your task is to implement own class for representation of fraction number. The Fraction class will have the following methods:

* `__init__` - initializes all instance variables
* `__repr__` - magic method for text representation
* `normalize` - method to get a normalized Fraction from the original, it returns normalized Fraction, it changes nothing in original

* `__eq__` - implementation of magic method for `==` comparison
* `__lt__` - implementation of magic method for `<` comparison
* `__le__` - implementation of magic method for `<=` comparison

* `add`, `sub`, `mul`, `div`
  * these methods are doing basic mathematical operations, in respective order adding, subtracting, multiplying and dividing
  * every method is accepting two arguments: implicit `self` and provided `other` representing the second Fraction
  * method is just returning new Fraction instance as a result, it doesn't change any of two given fractions

* `__add__`, `__sub__`, `__mul__`, `__div__`
  * magic methods for basic mathematical operations
  * same rules as for other mathematical methods

For your solution use this [template](03_fraction_class.py). All needed instructions are included in the template. You are supposed to fill in implementation for all methods there. 

There is included function `gcd` (gratest common divisor) from math package. It might be useful in normalization of fraction. You can call it as any other function `gcd(x, y)` where `x` and `y` are input integers. It is not allowed to use any other import. Assignment with additional imports will fail automatically.

Avoid usage of floats and division in entire solution except the method `normalize()`. It is allowed and necessary to use it `normalize()`, but nowehere else!

You can expect that there wont be inputs or expected results with 0 or negative numbers in both numerator and denumerator.