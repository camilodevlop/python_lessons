# Classes in the Python language: Cube.
class Cube:
    def __init__(self, height = 0.0, width  = 0.0, depth = 0.0) -> None:
        self.height = height
        self.width = width
        self.depth = depth
    
    def volume(self):
        if self.height >= 0 and self.width >= 0 and self.depth >= 0:
            return self.height * self.width * self.depth
        
        return '\n\tError: either height, width or depth are negative.\n'

#-------------------------------------------------------------------

# Testing the class.
print('\n\tCube class.')
height = float(input('\tType the height: '))
width = float(input('\tType the width: '))
depth = float(input('\tType the depth: '))

cube_1 = Cube(height, width, depth)
print(f'\tVolume = {cube_1.volume()} u^3')

#-------------------------------------------------------------------
