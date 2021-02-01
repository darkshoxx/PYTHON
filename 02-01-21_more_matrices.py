import some_maths
import numpy
data_length = 10
effects = [12, -5, 77]
var_x1 = numpy.random.normal(0, 1, data_length)
var_x2 = numpy.random.normal(0, 1, data_length)
error_term = numpy.random.normal(0, 5, data_length)
val_y = effects[0] + (effects[1] * var_x1) + (effects[2] * var_x2) + error_term
intercept = ([1] * data_length)
design_matrix = some_maths.transpose([intercept, var_x1, var_x2])
y_matrix = some_maths.transpose([val_y])
print(design_matrix)
print(y_matrix)

print(len(design_matrix))
print(len(design_matrix[0]))

print(len(y_matrix))
print(len(y_matrix[0]))
# some_maths.matrix_multiplication(some_maths.transpose(design_matrix), y_matrix)


def ols(x, y):
    covariance = some_maths.matrix_inversion(some_maths.matrix_multiplication(some_maths.transpose(x), x))
    print("covariance dimensions")
    print(len(covariance))
    print(len(covariance[0]))
    projection = some_maths.matrix_multiplication(some_maths.transpose(x), y)
    print("projection dimensions")
    print(len(projection))
    print(len(projection[0]))
    return some_maths.matrix_multiplication(covariance, some_maths.transpose(projection))


#print(ols(design_matrix, y_matrix))
