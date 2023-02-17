# Static class context in Python.

class My_Class:
    class_var = "Class Var"

    def __init__(self, instance_var) -> None:
        self._instance_var = instance_var

    @staticmethod
    def static_method():
        return My_Class.class_var

    @classmethod
    def class_method(cls):
        return cls.class_var

    # This method can access attributes and methods of the static context.
    def instance_method(self):
        print(f'\tStatic method: {self.static_method()}, Class method: {self.class_method()}')
        print(f'\tClass var: {self.class_var}, Instance var: {self._instance_var}')

#-------------------------------------------------------------------

print(f'\n\tStatic class context in Python.')
my_class1 = My_Class('Instance Var')
print(f'\tClass var: {my_class1.class_var}, Instance var: {my_class1._instance_var}')

print(f'\n\tCreating a new variable of class.')
My_Class.class_var_2 = 'Class Var 2'
print(f'\tClass var 2: {My_Class.class_var_2}, Class var 2: {my_class1.class_var_2}')

print(f'\n\tTesting a static method: {My_Class.static_method()}')
print(f'\tTesting a class method: {My_Class.class_method()}\n')

my_class1.instance_method()

#-------------------------------------------------------------------
