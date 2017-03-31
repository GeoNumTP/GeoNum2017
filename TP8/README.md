# TP8 : Uniform B-splines as Subdivision Surfaces

## Setup
```bash
cd GeoNum2017/
git pull
. exportPath.sh
```
Echo the `$PYTHONPATH` to verify it's been correctly set.
```bash
echo $PYTHONPATH
```
For the viewer to function properly, **python scripts need to be executed from the root dir**.
```bash
python TP8/tp8.py
```

## Implementation
There is a slight change on the implementation level compared to previous two TPs: 
instead of using three coordinate matrices `X, Y, Z`, we store data in three-dimensional array `M`:
 ```python
 X = M[0,:,:]
 Y = M[1,:,:]
 Z = M[2,:,:]
 ```
 The openness/closedness of a surface in a particular direction is controled via
 the parameters `u_closed, v_closed` (these are read from the input file).

Start by implementing the algorithm for a surface closed in both directions as this is easier to do; test on `torus`. Don't forget to use the modulo arithmetic where needed. Then, think about what needs to be changed if the surface is open in one or both directions.

## Functions to modify
* `Subdivide` : implement one subdivision step for B-spline surfaces
* `main part` : experiment with terrain parameters in `GenerateRandomTerrain(20,3.0)`

## ToDo
1. Implement one step of the above subdivision algorithm for **closed** uniform B-spline surfaces (`torus`).
2. Modify you implementation for surfaces which are **open**: either in one direction (`cylinder`) or in both directions (`grid`, `terrain`).
3. Experiment with parameters in `GenerateRandomTerrain()`.
4. [*bonus*] [Catmull–Clark subdivision scheme](https://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface) produces bicubic B-spline surfaces.  Although originally devised for quad-meshes with arbitrary topology, it work as well for uniform topologies (the ones we use in this TP). Implement this algorithm and compare the results with biquadratic surfaces. For more details of the algo, see the [wikipedia page](https://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface) and also [this article](http://www.rorydriscoll.com/2008/08/01/catmull-clark-subdivision-the-basics/).
