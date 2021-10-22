from scipy import interpolate

# Uses the line of best fit to estimate y from x_input
def linear_interpolation(x_points, y_points, x_input):
    f = interpolate.interp1d(x_points, y_points, kind = 'linear')
    return f(x_input)

x_knots = [-1.0, -2.0, 0.0, 2.0, 1.0]
y_knots = [10.0, 0.0, 15.0, 5.0, 0.0]
x_input = -0.3

linear_interpolation(x_points, y_points, x_input)
