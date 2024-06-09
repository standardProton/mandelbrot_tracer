from PIL import Image
import warnings
import numpy as np

w=500
h=400
n_points=100
brightness_percent = 0.7
x_offset = -0.7
x_range = 3
y_range = (h/w)*x_range

def multiply_vec(ex0, ex1): #Process many points at once. Shape = [N,2]
    r = np.zeros((len(ex0), 2))
    r[:,0] = (ex0[:,0] * ex1[:,0]) - (ex0[:,1] * ex1[:,1])
    r[:,1] = (ex0[:,0]*ex1[:,1]) + (ex0[:,1]*ex1[:,0])
    return r

def calculate_coord_vec(C, n_points): #returns vec of n before reached inf or nan
    curr = C
    r = np.zeros(len(C))
    for i in range(n_points):
        r += np.max(np.isnan(curr), axis=1)
        curr = multiply_vec(curr, curr) + C
    return (n_points*np.ones(len(C))) - r

def calculate_coord_vec_A(a, C, n_points): #variant with non-zero starting point
    curr = np.tile(a, len(C)).reshape(len(C), 2)
    r = np.zeros(len(C))
    for i in range(n_points):
        r += np.max(np.isnan(curr), axis=1)
        curr = multiply_vec(curr, curr) + C
    return (n_points*np.ones(len(C))) - r

def calc_pixels(A=None):
    
    x_vals = np.arange(-x_range/2, x_range/2, x_range/w) + x_offset
    y_vals = np.arange(-y_range/2, y_range/2, y_range/h)
    warnings.filterwarnings('ignore') #expected overflow warnings, if point diverges in sequence
    X, Y = np.meshgrid(x_vals, y_vals)
    grid = np.array([X.flatten(), Y.flatten()]).transpose()
    calcs = calculate_coord_vec(grid, n_points) if A is None else calculate_coord_vec_A(A, grid, n_points)
    warnings.filterwarnings('default')

    calcs[calcs >= n_points] = 0 #black pixel for converge
    m = 255/(np.max(calcs)*brightness_percent) #brightness
    calcs *= m
    calcs[calcs > 255] = 255
    calcs = np.uint8(calcs).reshape(len(y_vals), len(x_vals))
    return calcs


if __name__ == "__main__":
    
    pixels = calc_pixels() #calc_pixels(A=np.array([a_real, a_cmpx]))
    print("Saving...")
    mandelbrot = Image.fromarray(pixels)
    mandelbrot.save("./mandelbrot_output.jpg")
    
    #window.mainloop()
