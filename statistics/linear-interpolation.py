from scipy import interpolate

def search(x, points):
    # Use binary search to find left-most identical element if x <= x_point and right-most if x > x_point
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if points[mid][0] < x: 
            lo = mid + 1
        else: 
            hi = mid    
    # Extrapolate y by stepping left or right if x is out of range 
    return lo + (lo == 0) - (lo == n)

def linear_interpolation_from_scratch(n, x_points, y_points, x_input):
    # Find starting index of interpolation interval
    points = sorted(zip(x_points, y_points))
    i = search(x_input, points)
    
    # Calculate linear interpolation
    x0, y0, x1, y1 = points[i-1][0], points[i-1][1], points[i][0], points[i][1]
    if x1 == x0:
        if x_input == x0:
            return min(y0, y1)
        return max(y0, y1)
    return y0 + ((y1 - y0) / (x1 - x0)) * (x_input - x0)

def linear_interpolation(x_points, y_points, x_input):
    f = interpolate.interp1d(x_points, y_points, kind = 'linear')
    return f(x_input)

x_points = [-1.0, -2.0, 0.0, 2.0, 1.0]
y_points = [10.0, 0.0, 15.0, 5.0, 0.0]
n = len(x_points)
x_input = -0.3

linear_interpolation_from_scratch(n, x_points, y_points, x_input)
linear_interpolation(x_points, y_points, x_input)
