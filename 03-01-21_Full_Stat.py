import some_maths
import numpy
import scipy
data_length = 10
effects = [12, -5, 77]
var_x1 = numpy.random.normal(0, 1, data_length)
var_x2 = numpy.random.normal(0, 1, data_length)
error_term = numpy.random.normal(0, 5, data_length)
val_y = effects[0] + (effects[1] * var_x1) + (effects[2] * var_x2) + error_term
intercept = ([1] * data_length)
design_matrix = numpy.transpose([intercept, var_x1, var_x2])
y_matrix = numpy.transpose([val_y])

# some_maths.matrix_multiplication(some_maths.transpose(design_matrix), y_matrix)
#print(type(design_matrix))


def ols(x, y):
    covariance = numpy.linalg.inv(numpy.matmul(numpy.transpose(x), x))
    projection = numpy.matmul(numpy.transpose(x), y)
    return numpy.matmul(covariance, projection)



beta = ols(design_matrix, y_matrix)
print([design_matrix[2]])
print(type(numpy.mean(val_y) + 0))
print(some_maths.matrix_multiplication(some_maths.transpose(beta), some_maths.transpose([design_matrix[2]])))
print(numpy.matmul(some_maths.transpose(beta), some_maths.transpose([design_matrix[2]])))
print(numpy.matmul(numpy.transpose(beta), numpy.transpose([design_matrix[2]])))
print([y_matrix[1]] - numpy.matmul(numpy.transpose(beta), numpy.transpose([design_matrix[2]])))


def statistics(x, y):
    beta = ols(x, y)
    predictors = len(beta)
    sample_size = len(y)
    y_hat = numpy.mean(y)
    sum_squares_residual = 0
    sum_squares_total = 0
    sum_squares_corrected = 0
    for i in range(0, data_length):
        sum_squares_residual += pow(y[i] - numpy.matmul(numpy.transpose(beta), numpy.transpose([x[i]])), 2)
        sum_squares_total += pow(y[i] - y_hat, 2)
        sum_squares_corrected += pow(numpy.matmul(numpy.transpose(beta), numpy.transpose([x[i]])) - y_hat,2)
    coef_of_det = 1 - sum_squares_residual/sum_squares_total
    helpful_fraction = (sample_size - 1)/(sample_size - predictors - 1)
    adj_coef_det = 1 - ((1 - coef_of_det) * helpful_fraction)
    model_degrees_freedom = predictors - 1                      # df1
    error_degrees_freedom = sample_size - predictors            # df2
    mean_square_model = sum_squares_corrected / (model_degrees_freedom)
    mean_square_error = sum_squares_residual / (error_degrees_freedom)
    F_statistic = mean_square_model / mean_square_error         # following a F(p-1,n-p)
    p_value_F_test = 1 - scipy.stats.f.cdf(F_statistic, model_degrees_freedom, error_degrees_freedom)
    return [coef_of_det, adj_coef_det, p_value_F_test] #[coef_of_det]

print(statistics(design_matrix, y_matrix))