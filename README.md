Rendered from image_generator.py:

![Rendered Mandelbrot from image_generator.py](https://github.com/standardProton/mandelbrot_tracer/blob/master/mandelbrot_large.jpg)

The Mandelbrot set is a famous fractal in math, charactarized by its large cardioid shape. The mandelbrot set is the set of all values of C where the series $Z_n = (Z_{n-1})^2+ C$ does not diverge to infinity, where C is an element of the set of complex numbers.

In main.py, you can move the mouse around to control C, the constant. The blue dots are each a term in the sequence shown on the Argand plane. If that value of C doesn't diverge, a gray dot is put on the screen. If you move the mouse around for long enough to calculate enough dots, you'll see the shape of the Mandelbrot set appear!

The image_generator.py will calculate the full image, where each pixel's coordinates on the plane is C. A black pixel is set where the sequence converges, otherwise the color gets darker the faster it diverges.
