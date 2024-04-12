from main import *
from PIL import Image, ImageDraw
import warnings

w=5000
h=4000
n_points=100
brightness_percent = 0.7

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

    '''window = tk.Tk()
    window.title("Mandelbrot Generator")

    canvas2 = tk.Canvas(window, width=w, height=h)
    canvas2.pack()
    create_background(canvas2, create_points=False)

    start_coords = coordToPixel(A)
    canvas2.create_oval(start_coords[0]-3, start_coords[1]-3, start_coords[0]+3, start_coords[1]+3, fill="#0f88e4", outline="#0f88e4")

    window.update()

    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)'''
    
    pixels = calc_pixels() #calc_pixels(A=np.array([a_real, a_cmpx]))
    mandelbrot = Image.fromarray(pixels)
    mandelbrot.save("./mandelbrot_output.jpg")

    
    #window.mainloop()
