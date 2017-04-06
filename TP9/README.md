# TP9 : Subdivision Surfaces on Triangle Meshes

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
python TP9/tp9.py
```

## Functions to modify
* `InsertMidpoints` : generate new topology by inserting midpoint indices to the edge matrix; compute midpoint positions.
* `Beta` : compute the weight `Beta(N)`.
* `RecomputePositions` : recompute the positions of old vertices.
* `LoopSubdivision` : perform one iteration of Loop subdivision.

## ToDo
1. Implement the computation of the Loop subdivision scheme using the original weights (Loop).
2. Use the simplified weights (Warren) and compare the results on provided surfaces.
3. Subdivide the sphere and cube five times. Which surface is closer to the real sphere? Why?
