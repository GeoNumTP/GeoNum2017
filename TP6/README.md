## TP6 : Bezier surfaces

### UPDATE : using matplotlib
```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.axis('equal')
ax.axis('off')

...

for p in range(numpatch) :
    ...
    ax.plot_wireframe(X, Y, Z)
    ...

plt.show()
```
---

Today, we start working with surfaces, which means transition from 2D to 3D. We will use OpenGL for rendering, but don’t worry if you have little or no experience with OpenGL; a wrapper class `Viewer` is provided. Adding a surface patch is as easy as calling
```python
viewer.add_patch(X,Y,Z)
```

First, we need to setup the required python packages `PyOpenGL` and `PyGLFW`. Do
```bash
cd GeoNum2017/
git pull
```
or, if you don't have the local repo
```bash
git clone https://github.com/GeoNumTP/GeoNum2017.git
```
You should now have the `TP6/` and `viewer/` folders, plus two new bash scripts: `setupPackages.sh` and `exportPath.sh`.
Execute the following commands:
```bash
# download and extract packages
./setupPackages.sh
# export python path
# the extra dot in the beginning makes this change global
. ./exportPath.sh
```

Afterwards, you can test the viewer with
```
python viewer/viewer.py
```

For the TP6, you can pass datanames and density directly as command line args:
```bash
python tp6.py  [simple,wave,sphere,heart,teapot,teacup,teaspoon]  [density=10]
```

### Representation
On the implementation level, the biggest difference between curves and surfaces is the representation we'll use.
Before, we used a single matrix to represent the whole curve -- each coordinate was stored in a separate column.
For surfaces, we could do something similar using three-dimensional arrays; instead, to facilitate understanding of the code, we'll represent the three coordinates in separate matrices `Mx`, `My` and `Mz` (or `Sx`, `Sy`, `Sz` for surface points).

### Functions to modify
* `DeCasteljau` : implement the De Casteljau algorithm for surfaces.
* `BezierSurf` : compute Bezier surface points.

### ToDo
1. Implement the evaluation of Bézier surfaces for (u,v) in [0,1]².
Use `simple` and `wave` for first tests (these contain only one patch).
2. When you're sure the implementation works for the simple cases, test your algorithm on datasets with multiple patches:
`heart` (2),  `sphere` (8),  `teapot` (32), `teacup` (26), `teaspoon` (16). Don't set the `density` parameter too high, always start with smaller values (5 or 10) as the number of computed points is `density`².
