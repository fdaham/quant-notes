from scipy import interpolate

# Binary search method that returns left-most identical element if x <= x_point 
# and right-most if x > x_point. Assumes points are sorted.
def search(x, points):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if points[mid][0] < x: 
            lo = mid + 1
        else: 
            hi = mid    
    # Handle case where x is out of bounds by stepping left or right
    return lo + (lo == 0) - (lo == n)

# Uses the line of best fit to estimate y from x_input. Returns 0 if it can't.
# Extrapolates y if x_input is out of range. 
def linear_interpolation_from_scratch(n, x_points, y_points, x_input):
    points = sorted(zip(x_points, y_points))
    i = search(x_input, points)
    x0, y0, x1, y1 = points[i-1][0], points[i-1][1], points[i][0], points[i][1]
    if x1 == x0:
        if x_input == x0:
            return min(y0, y1)
        return 0
    return y0 + ((y1 - y0) / (x1 - x0)) * (x_input - x0)

# Uses the line of best fit to estimate y from x_input
def linear_interpolation(x_points, y_points, x_input):
    f = interpolate.interp1d(x_points, y_points, kind = 'linear')
    return f(x_input)

x_points = [-1.0, -2.0, 0.0, 2.0, 1.0]
y_points = [10.0, 0.0, 15.0, 5.0, 0.0]
n = len(x_points)
x_input = -0.3

linear_interpolation(n, x_points, y_points, x_input)
linear_interpolation(x_points, y_points, x_input)
