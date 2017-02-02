# GeoNum2017 : Géométrie numérique, spring 2017 

## TP1 : Bézier curves, De Casteljau’s algorithm

### Python
If you have no prior experience with Python whatsoever, I suggest the tutorial
[Learn Python in 10 minutes](https://www.stavros.io/tutorials/python/) by Stavros Korokithakis.
For longer and more complete references, see the [Fast Lane to Python](http://heather.cs.ucdavis.edu/~matloff/Python/PLN/FastLanePython.pdf) by Norm Matloff and, of course, the [official Python 2.7.13 docs](https://docs.python.org/2/).

### NumPy
[NumPy](http://www.numpy.org/) is a Python package supporting N-dimensional arrays and linear algebra operations. We'll mostly use it to manipulate datapoints stored in matrices (two-dimensional arrays).
Here is a useful [numpy cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf).

### Matplotlib
[Matplotlib](http://matplotlib.org/) is a Python 2D plotting library -- we'll use it to visualise 2D curves 
via the [plot](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) command.
{% highlight python %}
# import the modules
import numpy as np
import matplotlib.pyplot as plt
# generate random data
points = np.random.rand(1000,2)
# plot
plt.plot(points[:,0],points[:,1],'bo')
{% endhighlight %}
