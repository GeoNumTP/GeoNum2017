# Géométrie numérique, spring 2017
Welcome to the github repository of the course *Géométrie numérique* 2017.  
See [course website](https://tiborstanko.sk/teaching/geo-num-2017/) for more details.

## Quickstart
```bash
cd your/working/dir/
git clone https://github.com/GeoNumTP/GeoNum2017.git
cd GeoNum2017
python TP1/tp1.py
```

## Syllabus
1. Bézier curves | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp1.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP1#tp1--bézier-curves-de-casteljaus-algorithm)  
1. Bézier splines | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp2.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP2#tp2--bézier-splines-ck-smoothness)  
1. B-splines | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp3.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP3#tp3--b-splines-de-boors-algorithm)  
1. Subdivision curves | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp4.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP4#tp4--subdivision-curves)  
1. Lane-Riesenfeld | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp5.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP5#tp5--lane-riesenfeld-algorithm) 
1. Bézier surfaces | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp6.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP6#tp6--bezier-surfaces)
1. B-spline surfaces | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp7.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP7#tp7--b-spline-surfaces)
1. Subdivision B-surfaces | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp8.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP8#tp8--uniform-b-splines-as-subdivision-surfaces)
1. Triangle mesh subdivision | [theory](https://tiborstanko.sk/teaching/geo-num-2017/tp9.html) | [code](https://github.com/GeoNumTP/GeoNum2017/tree/master/TP9#tp9--subdivision-surfaces-on-triangle-meshes)

## Resources
* [Learn Python in 10 minutes](https://www.stavros.io/tutorials/python/)
* [Python 2.7 tutorial](https://docs.python.org/2.7/tutorial/)
* [Python at OverAPI](http://overapi.com/python)
* [NumPy quickstart tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
* [NumPy cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
* [Matplotlib.pyplot](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot)

## Python
If you have no prior experience with Python whatsoever, I suggest the tutorial
[Learn Python in 10 minutes](https://www.stavros.io/tutorials/python/) by Stavros Korokithakis.
For longer and more complete references, see the [Fast Lane to Python](http://heather.cs.ucdavis.edu/~matloff/Python/PLN/FastLanePython.pdf) by Norm Matloff and, of course, the [official Python 2.7 tutorial](https://docs.python.org/2.7/tutorial/).

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
>>> print i
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
[Matplotlib](http://matplotlib.org/) is a Python 2D plotting library - we'll use it to visualise 2D curves 
via [pyplot](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot).  
Example:
```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt

# generate random data
>>> A = np.random.rand(1000,2)
>>> x = A[:,0]
>>> y = A[:,1]

# plot blue circles
>>> plt.plot( x, y, 'bo')

# plot solid red lines
>>> plt.plot( x, y, 'r-')

# render and show the plot
>>> plt.show()

# plot dashed green lines and blue circles
>>> plt.plot(x, y, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
```
