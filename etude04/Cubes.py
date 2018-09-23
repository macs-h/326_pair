import numpy

cube = numpy.zeros([2,2,2])
print(cube)

#new_cube[face][i][j] = clockwise ? old_cube[j][2 - i] : old_cube[2 - j][i]; }