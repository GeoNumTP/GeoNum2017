## TP6 : Bezier surfaces
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
You should have the `TP6/`, but also the `viewer/` and two bash scripts: `setupPackages.sh` and `exportPath.sh`.
Run
```bash
# download and extract packages
./setupPackages.sh
# export python path
# note the extra dot in the beginning
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
We can no longer do this for surfaces. Instead, we'll represent the surface using three matrices `X`, `Y` and `Z`,
one for each coordinate.

### Functions to modify
* `DeCasteljau` : implement the De Casteljau algorithm for surfaces.
* `BezierSurf` : compute Bezier surface points.

### ToDo
