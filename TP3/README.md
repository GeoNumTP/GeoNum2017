## TP3 : B-splines, De Boor's algorithm

<img alt="B-spline" width="250" src="https://tiborstanko.sk/assets/geo-num-2016/spiral_B.png">
<img alt="B-spline" width="250" src="https://tiborstanko.sk/assets/geo-num-2016/spiral_B_2.png">

In this TP, you'll implement the De Boor's algorithm for computation of B-spline curves.

```bash
cd GeoNum2017/
git pull
```
or, if you don't have the local repo
```bash
git clone https://github.com/GeoNumTP/GeoNum2017.git
```
Then
```
cd TP3/
python tp3.py
```

As before, you can pass dataname and density parameters directly as command line args.
```bash
python tp3.py [simple,spiral,circle,camel]  [sampling_density]
python tp3.py [circle7,circle9]  [sampling_density] nurbs
# example
python tp3.py spiral 24
```
If specified, the last argument tells the program to compute NURBS (`circle7.nurbs` or `circle9.nurbs`).

### Contents
* `ReadBSpline` : helper function to read B-spline control points and knots from a file.
* `DeBoor` : perform the De Boor algorithm.
* main part : evaluation and plotting.

### ToDo
1. Implement the De Boor's algorithm.
1. Evaluate B-spline for the `simple` dataset. Modify the knot vector and recompute. What changed?
1. Evaluate B-spline for the `spiral` dataset. Modify the knot vector to `0 0 0 0 1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5`. What changed?
1. Evaluate B-spline for the `camel` dataset. Move the front leg by changing the x-coordinate of the last control point to `-1.5`. Which segments of the curve have changed? Why?
1. Modify your code to work in homogeneous coordinates (if `dim=3`).
1. Evaluate `circle9.nurbs` and `circle7.nurbs`. Compare the results with `circle.bspline`.
