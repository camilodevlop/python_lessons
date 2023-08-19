from abc import ABCMeta, abstractmethod

# ABC - Abstract Base Class.
# Ensures that the son classes implement the methods of the parent classes.

# Example without using ABC.


class BaseClass1:
    def method_1(self):
        raise NotImplementedError

    def method_2(self):
        raise NotImplementedError

class SpecificClass1(BaseClass1):
    def method_1(self):
        print(f'Method 1 overridden...')

    # The method 2 is not implemented.
    # Problem: the lack of the implementation is not reported.

# Problem: the Base class can be instantiated.
base_class = BaseClass1()
# base_class.method_1()

# SpecificClass1 works properly.
specific_class_1 = SpecificClass1()
specific_class_1.method_1()
# specific_class_1.method_2()

#-------------------------------------------------------------------

# Solving the issues presented above using ABC.
class BaseClass2(metaclass = ABCMeta):
    @abstractmethod
    def method_1(self):
        pass

    @abstractmethod
    def method_2(self):
        pass

class SpecificClass2(BaseClass2):
    def method_1(self):
        print(f'Method 1 overridden...')

    # The son class must implement all methods defined in the parent
    # class.
    def method_2(self):
        print(f'Method 2 overridden...')

# We can't instance the BaseClass2.
# base_class_2 = BaseClass2()

# Instantiating the SpecificClass2.
specific_class_2 = SpecificClass2()
specific_class_2.method_1()
specific_class_2.method_2()

#-------------------------------------------------------------------
