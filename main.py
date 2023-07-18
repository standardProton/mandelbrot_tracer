import tkinter as tk
import time, math, os
from PIL import Image

window = tk.Tk()
window.title("Mandelbrot Visualization")

w=1000
h=650
pt_radius = 4
pt_diameter = 2*pt_radius
n_points = 50

x_offset = -0.5
x_range = 3
y_range = (h/w)*x_range

A = (0, 0)
C = (0, 0)
C_item = None

points=[]
lowest_hidden = -1

def add(ex0:tuple, ex1: tuple):
    return (ex0[0] + ex1[0], ex0[1] + ex1[1])

def multiply(ex0:tuple, ex1:tuple): #complex plane
    a, b = ex0; c, d = ex1
    return ((a*c) - (d*b), (a*d) + (b*c))

def calculate_coords(A, C):
    coords = [A]
    prev = A
    for i in range(1, n_points):
        prev = add(multiply(prev, prev), C)
        coords.append(prev)
        if (math.isnan(prev[0]) or math.isnan(prev[1]) or math.isinf(prev[0]) or math.isinf(prev[1])): return coords
    return coords

def coordToPixel(coord: tuple, inbounds=True):
    x = ( ((coord[0] - x_offset)/x_range) + 0.5 )*w
    y = ( (coord[1]/y_range) + 0.5 )*h
    if (math.isnan(x) or math.isnan(y) or math.isinf(x) or math.isinf(y) or (inbounds and (x < 0 or x > w or y < 0 or y > h))): return None
    return (int(x), int(y))

def pixelToCoord(coord: tuple):
    return ((coord[0]*x_range) - (x_range/2) + x_offset, (coord[1]*y_range - (y_range/2)))

def update_position(canvas: tk.Canvas,  pos: tuple):
    global lowest_hidden, A, C
    x = min(max(0, pos[0]/w), 1)
    y = min(max(0, pos[1]/h), 1)

    C = pixelToCoord((x, y))

    coords = calculate_coords(A, C)
    
    continue_render = True
    for i in range(0, max(lowest_hidden, n_points)):
        xorig, yorig, xorig2, yorig2 = canvas.coords(points[i])

        pixel = None
        if (continue_render and i < len(coords)):
            pixel = coordToPixel(coords[i])

        if (pixel == None):
            canvas.itemconfigure(points[i], state='hidden')
            continue_render = False
        else:
            canvas.move(points[i], pixel[0] - xorig - pt_radius, pixel[1] - yorig - pt_radius)
            canvas.itemconfigure(points[i], state='normal')
    
    if (len(coords) == n_points):
        marker = canvas.create_oval(pos[0]-pt_radius, pos[1]-pt_radius, pos[0]+pt_radius, pos[1]+pt_radius, fill="#d1d1d1", outline="#d1d1d1")
        canvas.tag_lower(marker)
    lowest_hidden = len(coords)
    if (C_item != None): 
        cxorig, cyorig, cxorig2, cyorig2 = canvas.coords(C_item)
        canvas.move(C_item, pos[0] - cxorig - pt_radius, pos[1] - cyorig - pt_radius)

def create_background(canvas: tk.Canvas):
    global points, A, C, C_item
    canvas.delete('all')
    xpos = coordToPixel((0, 0))[0]

    canvas.create_line(xpos, 0, xpos, h, fill="gray")
    canvas.create_line(0, h*0.5, w, h*0.5, fill="gray")

    for i in range(0, 4): #i markings
        coord = coordToPixel((0, i - 2), inbounds=False)
        canvas.create_line(-10, coord[1], 10, coord[1], fill="gray")
    
    points = []
    coords = calculate_coords(A, C)
    for i in range(0, n_points):
        coord = coords[i] if len(coords) < i else (0, 0)
        pixel = coordToPixel(coord)
        points.append(canvas.create_oval(pixel[0]-pt_radius, pixel[1]-pt_radius, pixel[0]+pt_radius, pixel[1]+pt_radius, fill="#0f88e4", outline="#0f88e4"))

    C_coords = coordToPixel(C)
    C_item = canvas.create_oval(C_coords[0]-pt_radius, C_coords[1]-pt_radius, C_coords[0]+pt_radius, C_coords[1]+pt_radius, fill="#f21212", outline="#f21212")


bg = tk.PhotoImage(os.getcwd() + "/bg.png")

canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()
create_background(canvas)

#canvas.create_image(0, 0, image=bg, anchor='nw')

window.update()

last_pos = (-1, -1)
while True:
    if (window.focus_get()):
        pos = (window.winfo_pointerx() - window.winfo_rootx(), window.winfo_pointery() - window.winfo_rooty())
        if (pos != last_pos):
            update_position(canvas, pos)
            last_pos = pos
    window.update()
