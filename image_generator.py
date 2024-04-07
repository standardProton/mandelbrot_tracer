from main import *
from PIL import Image, ImageDraw
import warnings

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
def gray_rgb(val):
    return "#%02x%02x%02x" % ((val, val, val))

def get_pixel_color(x, y, A): #black if converges, otherwise gradient for approximately how fast it diverges
    coords = calculate_coords(A, pixelToCoord((x, y)))
    size = len(coords)
    if (size >= n_points): return (0, 0, 0)
    elif (size >= 3): 
        val = int(255*(size/(n_points-3)))
        return (val, val, val)
    else: return (0, 0, 255)

def calc_pixels(A=None):
    
    x_vals = np.arange(-x_range/2, x_range/2, x_range/w) + x_offset
    y_vals = np.arange(-y_range/2, y_range/2, y_range/h)
    warnings.filterwarnings('ignore') #expected overflow warnings, if point diverges in sequence
    X, Y = np.meshgrid(x_vals, y_vals)
    grid = np.array([X.flatten(), Y.flatten()]).transpose()
    calcs = calculate_coord_vec(grid)
    #if A is None: 
    #    calcs = calculate_coord_vec(grid)
     #   print("A")
    #else: calcs = calculate_coord_vec_A(grid, A)
    warnings.filterwarnings('default')

    calcs[calcs >= n_points] = 0 #black pixel for converge
    calcs = np.uint8(255*calcs/np.max(calcs)).reshape(len(y_vals), len(x_vals))
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
    
    pixels = calc_pixels()
    mandelbrot = Image.fromarray(pixels)
    mandelbrot.save("./mandelbrot_output.jpg")

    
    #window.mainloop()
