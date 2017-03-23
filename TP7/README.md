# TP7 : B-spline surfaces

## Update: OpenGL

The problems with OpenGL and GLFW should be resolved with the updated `setupPackages.sh` — don't forget to put the dot  `.` before the command.
```bash
cd GeoNum2017/
git pull
. setupPackages.sh
```

This will download and compile `PyOpenGL`, `PyGLFW` and `GLFW` (as a static library).
The `libglfw.so*` files are automatically copied to repo's root dir.
For the viewer to function properly, **python scripts need to be executed from the root dir**.
```bash
# test the viewer
python viewer/viewer.py
# test TP7
python TP7/tp7.py
```

Moreover, the $PYTHONPATH needs to be set up everytime you open the terminal by executing `exportPath.sh` preceded by the dot.
```bash
. exportPath.sh
```
You can `echo` the path to see if it's been set correctly.
```bash
echo $PYTHONPATH
```

---

## Functions to modify
* `DeBoorSurf` : recursively implement De Boor's algorithm for surfaces.
* `main part` : for each patch of the B-spline surface, evaluate surface points by calling `DeBoorSurf` in a double loop.

## ToDo
1. Implement evaluation of B-spline surfaces. Test with the provided datasets (`simple.bspline` and `torus.bspline`).
1. Modify the knot vectors for the simple dataset. Experiment with various configurations. How does the surface change?
1. [**Bonus**] NURBS surfaces can be used to represent the unit sphere, the same way we used NURBS curves to represent the unit circle in `TP3`. Modify your implementation of B-spline surfaces to compute NURBS surfaces. Test with the hemisphere (`hemi.nurbs`) and the modified torus (`torus.nurbs`).  
Note: full sphere control points, weights, and knots can be found in [Representing a Circle or a Sphere with NURBS](https://www.geometrictools.com/Documentation/NURBSCircleSphere.pdf) by David Eberly.
