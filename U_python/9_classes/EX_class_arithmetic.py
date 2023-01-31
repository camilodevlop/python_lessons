# Classes in the python language: Arithmetic.
class Arithmetic:
    def __init__(self, operand_A = 0, operand_B = 1) -> None:
        self.operand_A = operand_A
        self.operand_B = operand_B
    
    def add(self):
        return self.operand_A + self.operand_B

    def subtract(self):
        return self.operand_A - self.operand_B

    def multiply(self):
        return self.operand_A * self.operand_B
    
    def divide(self):
        if self.operand_B != 0:
            return self.operand_A / self.operand_B
        return "\n\tThe division is not defined.\n"

#-------------------------------------------------------------------

# Testing the class.
print('\n\tArithmetic class.')

arithmetic_1 = Arithmetic(5,4)

print(f'\tSum test: {arithmetic_1.add()}')
print(f'\tSubtraction test: {arithmetic_1.subtract()}')
print(f'\tMultiplication test: {arithmetic_1.multiply()}')
print(f'\tDivision test: {arithmetic_1.divide()}')

#-------------------------------------------------------------------
