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
=======
# Géométrie numérique, spring 2017
Welcome to the github repository of the course *Géométrie numérique* 2017.
See [course website](https://tiborstanko.sk/teaching/geo-num-2017/) for more details.

## Python
If you have no prior experience with Python whatsoever, I suggest the tutorial
[Learn Python in 10 minutes](https://www.stavros.io/tutorials/python/) by Stavros Korokithakis.
For longer and more complete references, see the [Fast Lane to Python](http://heather.cs.ucdavis.edu/~matloff/Python/PLN/FastLanePython.pdf) by Norm Matloff and, of course, the [official Python 2.7 docs](https://docs.python.org/2/).

## NumPy
[NumPy](http://www.numpy.org/) is a Python package supporting N-dimensional arrays and linear algebra operations. We'll mostly use it to manipulate datapoints stored in matrices (two-dimensional arrays).
If you're not familiar with numpy, have a look at this [cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf).

Here are some useful numpy commands; you can test them in the `python` console.

```python
>>> import numpy as np

# define a 50x3 matrix of zeros
>>> Z = np.zeros([50,3])

# define a 2x3 matrix
>>> A = np.array([[1,2,3],[4,5,6]])
>>> print A
[[1 2 3]
 [4 5 6]]

# define a vector with 10 evenly-spaced values between 0 and 1 
>>> t = np.linspace(0,1,10)
>>> print t 
[ 0.          0.11111111  0.22222222  0.33333333  0.44444444  0.55555556
  0.66666667  0.77777778  0.88888889  1.        ]
  
# define a range
>>> i = np.arange(10)   # same as np.arange(0,10)
print i
[0 1 2 3 4 5 6 7 8 9]
>>> j = np.arange(5,45,10)
>>> print j
[ 5 15 25 35]

# get dimensions of a matrix
>>> S = A.shape
>>> print S[0]  # number of rows in A 
2
>>> print S[1]  # number of cols in A
3

# access a specific row
>>> print A[0,:]
[1 2 3]

# access a specific col
>>> print A[:,1]
[2 5]

# slicing: access cols 0 to 1
>>> print A[:,0:2]
[[1 2]
 [4 5]]

# slicing: access cols 1 to end
>>> print A[:,1:]
[[2 3]
 [5 6]]
 
# reshape A to have 3 rows and 2 cols
>>> B = A.reshape(3,2)
>>> print B
[[1, 2],
 [3, 4],
 [5, 6]]

# reshape A to have 2 cols
# number of rows is determined automatically
>>> C = B.reshape(-1,3)
>>> print C
[[1 2 3]
 [4 5 6]]
```

## Matplotlib
[Matplotlib](http://matplotlib.org/) is a Python 2D plotting library -- we'll use it to visualise 2D curves 
via the [plot](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) command.

```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt

# generate random data
>>> A = np.random.rand(1000,2)

# plot & render
>>> plt.plot( A[:,0], A[:,1], 'bo')
>>> plt.show()
```

## TP1 : Bézier curves, De Casteljau’s algorithm
In this TP, you'll implement the De Casteljau’s algorithm, and you'll use it to compute and visualise the curves in the `data` folder. Start by cloning the repo and testing the code for the TP1.
```bash
cd your/working/dir/
git clone https://github.com/GeoNumTP/GeoNum2017.git
cd GeoNum2017
python TP1/tp1.py
```

### Code structure

### ToDo
1. Implement the De Casteljau algorithm and use it to evaluate the Bézier curves in the `data` folder. Visualise the curves together with their control polygons.
2. Try varying the sampling density. How many samples are needed to give the impression of a smooth curve?
3. Pick one dataset and visualise *all* intermediate polygons `b_i^k` from the De Casteljau algorithm for a fixed parameter, for instance `t=0.5`. **Hint**: each column in the above schema represents one such polygon.
