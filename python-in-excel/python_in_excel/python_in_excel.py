import xlwings
from numpy import array
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# define python function as excel function
@xlwings.func
# define python function arguments as numpy arrays for excel conversion
@xlwings.arg('x_data', array)
@xlwings.arg('y_data', array)
def fit_curve(x_data, y_data):
    # define polynomial
    f = lambda x, A, B, C, D: A * x**4 + B * x**3 + C * x**2 + D * x
    # fit data
    coeffs, _ = curve_fit(f, x_data, y_data)
    # return coefficients and r^2
    return (*coeffs, "r^2:", r2_score(y_data, f(x_data, *coeffs)))