
The Mandelbrot set is a famous fractal in math, charactarized by its large cardioid shape. The mandelbrot set is the set of all numbers that don't diverge to infinity in the series T(n+1) = T(n)^2 + C, where C can be any complex constant.
In other words, starting at the point 0 + 0i, if for each step you square the last term and add a constant (working with complex components as well), do you reach infinity?

In this simple python program, you can move the mouse around to control C, the constant. If that value of C doesn't diverge, a dot is put on the screen. If you move the mouse around for long enough to calculate enough dots, you'll see the shape of the Mandelbrot set appear!