from main import *
from PIL import Image, ImageDraw
import os

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
def gray_rgb(val):
    return "#%02x%02x%02x" % ((val, val, val))

def get_pixel_color(x, y, A):
    coords = calculate_coords(A, pixelToCoord((x, y)))
    size = len(coords)
    if (size >= n_points): return (0, 0, 0)
    elif (size >= 3): 
        val = int(255*(size/(n_points-3)))
        return (val, val, val)
    else: return (0, 0, 255)


if __name__ == "__main__":

    window = tk.Tk()
    window.title("Mandelbrot Generator")

    A = (0, 0)

    a0 = A[1] == 0

    canvas2 = tk.Canvas(window, width=w, height=h)
    canvas2.pack()
    create_background(canvas2, create_points=False)

    start_coords = coordToPixel(A)
    canvas2.create_oval(start_coords[0]-3, start_coords[1]-3, start_coords[0]+3, start_coords[1]+3, fill="#0f88e4", outline="#0f88e4")

    window.update()

    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    for y_pixel in range(0, int((h/2) if a0 else h)):
        for x_pixel in range(0, w):

            x = min(max(0, x_pixel/w), 1)
            y = min(max(0, y_pixel/h), 1)
            fill = get_pixel_color(x, y, A)
            fillhex = from_rgb(fill)

            canvas2.tag_lower(canvas2.create_rectangle(x_pixel, y_pixel, x_pixel+1, y_pixel+1, fill=fillhex, outline=fillhex))
            #draw.rectangle((x_pixel, y_pixel, x_pixel+1, y_pixel+1), fill=fill, outline=fill)
            if a0:
                canvas2.tag_lower(canvas2.create_rectangle(x_pixel, h - y_pixel, x_pixel+1, h - y_pixel + 1, fill=fillhex, outline=fillhex))
                #draw.rectangle((x_pixel, h - y_pixel, x_pixel+1, h-y_pixel+1), fill=fill, outline=fill)

        window.update()
    
    window.mainloop()
