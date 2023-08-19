# instance, class and static methods.

class MyClass:
    def instance_method(self):
        return 'Instance method executed.', self

    @classmethod
    def class_method(cls):
        return 'Class method executed.', cls

    @staticmethod
    def static_method():
        return 'Static method executed.'

#-------------------------------------------------------------------

# Executing the instance method.
object1 = MyClass()
print(object1.instance_method())
print(MyClass.instance_method(object1))

# Executing the class method.
print(MyClass.class_method())
print(object1.class_method())

# Executing the static method.
print(MyClass.static_method())
print(object1.static_method())

#-------------------------------------------------------------------
