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
---

## Functions to modify
* `Subdivide` : implement one subdivision step for B-spline surfaces
* `main part` : experiment with terrain parameters in `GenerateRandomTerrain(20,3.0)`

## ToDo
1. Implement one step of the above subdivision algorithm for **closed** uniform B-spline surfaces (`torus`).
2. Modify you implementation for surfaces which are **open**: either in one direction (`cylinder`) or in both directions (`grid`, `terrain`).
3. Experiment with parameters in `GenerateRandomTerrain()`.
