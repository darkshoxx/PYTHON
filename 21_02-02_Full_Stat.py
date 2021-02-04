# import some_maths
import numpy
from scipy import stats

ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])

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
# print(type(design_matrix))


def ols(x, y):
    covariance = numpy.linalg.inv(numpy.matmul(numpy.transpose(x), x))
    projection = numpy.matmul(numpy.transpose(x), y)
    return numpy.matmul(covariance, projection)


test_beta = ols(design_matrix, y_matrix)


# print([design_matrix[2]])
# print(type(numpy.mean(val_y) + 0))
# print(some_maths.matrix_multiplication(some_maths.transpose(beta), some_maths.transpose([design_matrix[2]])))
# print(numpy.matmul(some_maths.transpose(beta), some_maths.transpose([design_matrix[2]])))
# print(numpy.matmul(numpy.transpose(beta), numpy.transpose([design_matrix[2]])))
# print([y_matrix[1]] - numpy.matmul(numpy.transpose(beta), numpy.transpose([design_matrix[2]])))


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
        sum_squares_corrected += pow(numpy.matmul(numpy.transpose(beta), numpy.transpose([x[i]])) - y_hat, 2)
    coef_of_det = 1 - sum_squares_residual / sum_squares_total
    helpful_fraction = (sample_size - 1) / (sample_size - predictors - 1)
    adj_coef_det = 1 - ((1 - coef_of_det) * helpful_fraction)
    model_degrees_freedom = predictors - 1  # df1
    error_degrees_freedom = sample_size - predictors  # df2
    mean_square_model = sum_squares_corrected / model_degrees_freedom
    mean_square_error = sum_squares_residual / error_degrees_freedom
    f_statistic = mean_square_model / mean_square_error  # following a F(p-1,n-p)
    p_value_f_test = 1 - stats.f.cdf(f_statistic, model_degrees_freedom, error_degrees_freedom)
    covariance_diagonal = numpy.diagonal(numpy.linalg.inv(numpy.matmul(numpy.transpose(x), x)))
    standard_error = pow(covariance_diagonal, 0.5)
    t_vector = numpy.transpose(beta) / standard_error
    p_vector_t_test = 1 - stats.t.cdf(numpy.abs(t_vector), sample_size - predictors)
    return [coef_of_det, adj_coef_det, f_statistic, model_degrees_freedom, error_degrees_freedom, p_value_f_test, beta,
            standard_error, t_vector, p_vector_t_test]


results = statistics(design_matrix, y_matrix)


def summary(stat_output):
    coeff_line = f"The R^2 of the regression was {numpy.round(stat_output[0][0][0], 3)}, " \
                 f"adjusted {numpy.round(stat_output[1][0][0], 3)}."
    f_line = f"The overall F-Test gave an F-Statistc of {numpy.round(stat_output[2][0][0], 3)} on" \
             f" {stat_output[3]} and {stat_output[4]} degrees of freedom, with a p-value " \
             f"of {numpy.format_float_scientific(stat_output[5][0][0], 3)}."
    predictors = stat_output[3] + 1
    string_list = ["a"] * predictors
    for i in range(0, predictors):
        string_list[
            i] = f"The {ordinal(i + 1)} predictor had a coefficient of {round(stat_output[6][i][0], 3)}. Together " \
                 f"with a standard error of {round(stat_output[7][i], 3)}, this gave a t-value " \
                 f"of {round(stat_output[8][0][i], 3)} and a one-sided p-value " \
                 f"of {numpy.format_float_scientific(stat_output[9][0][i], 3)}"

    print(coeff_line)
    print(f_line)
    for i in range(0, predictors):
        print(string_list[i])


summary(results)
