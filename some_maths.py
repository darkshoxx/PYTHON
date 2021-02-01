import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import copy

iris = datasets.load_iris()

X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
# print(X)
dataline = [*range(1, 10)]
# print([x / 3 for x in dataline])


phone_matrix = [list(range(1, 4)),
                list(range(4, 7)),
                list(range(7, 10))]


def transpose(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    result_matrix = [list(range(0, nrow))]
    for loopyloops in range(0, ncol-1):
        result_matrix.append(list(range(0, nrow)))
    for i in range(0, nrow):
        for j in range(0, ncol):
            result_matrix[j][i] = matrix[i][j]
    return result_matrix


def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    rows2 = len(matrix2)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])
    if cols1 != rows2:
        print("Incompatible Matrices")
        return None
    result_matrix = [list(range(0, rows1))]
    for loopyloops in range(0, cols2-1):
        result_matrix.append(list(range(0, rows1)))
    for i in range(0, rows1):
        for k in range(0, cols2):
            result_matrix[k][i] = 0
            for j in range(0, rows2):
                result_matrix[k][i] = result_matrix[k][i] + matrix1[i][j]*matrix2[j][k]
    return transpose(result_matrix)


epsi = pow(10, -10)


def matrix_inversion(matrix):
    rows1 = len(matrix)
    cols1 = len(matrix[0])
    if cols1 != rows1:
        print("Incompatible Matrices")
        return None
    result_matrix = [list(range(0, rows1))]
    for loopyloops in range(0, cols1-1):
        result_matrix.append(list(range(0, rows1)))
    for i in range(0, rows1):
        for j in range(0, rows1):
            if i == j:
                result_matrix[i][j] = 1
            else:
                result_matrix[i][j] = 0
    for j in range(0, cols1):
        pivot = matrix[j][j]
        if abs(pivot) < epsi:
            print("Matrix not invertible")
            return None
        matrix[j] = [x / pivot for x in matrix[j]]
        result_matrix[j] = [x / pivot for x in result_matrix[j]]
        for i in range(0, rows1):
            if i != j:
                help_row1 = [x * matrix[i][j] for x in matrix[j]]
                help_row2 = [x * matrix[i][j] for x in result_matrix[j]]
                # matrix[i] = [x - help_row1[matrix[i].index(x)] for x in matrix[i]]
                for looooongrow in range(0, rows1):
                    matrix[i][looooongrow] = matrix[i][looooongrow] - help_row1[looooongrow]
                    result_matrix[i][looooongrow] = result_matrix[i][looooongrow] - help_row2[looooongrow]
    return result_matrix


transposed_phone_matrix = transpose(phone_matrix)
# print(transposed_phone_matrix)

# print(phone_matrix)
new_phone = copy.deepcopy(phone_matrix)
new_phone.append(list(range(0, 3)))

# print(transpose(new_phone))

mat_produ = matrix_multiplication(new_phone, transpose(new_phone))
# print(phone_matrix)

new_new_phone = copy.deepcopy(phone_matrix)
new_new_phone[2][2] = 6
new_new_new_phone = copy.deepcopy(new_new_phone)
un_phone = matrix_inversion(new_new_phone)
test_product = matrix_multiplication(un_phone, new_new_new_phone)
# print(un_phone)
print(test_product)
# print(new_new_phone)