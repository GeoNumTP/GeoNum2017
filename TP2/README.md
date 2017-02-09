## TP2 : Bézier splines, Ck smoothness
This TP is about implementing quadratic (C1) and cubic (C2) Bézier splines.

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
cd TP2/
python tp2.py
```
and you should see a plot with 4 dots.

As before, you can pass dataname and density parameters directly as command line args.
```bash
python tp2.py [simple,infinity,spiral]  [sampling_density]  [c2]
# example
python tp2.py spiral 24 c2
```
If specified, the last argument tells the program to compute a C2 cubic spline;
otherwise, the C1 quadratic spline is used.

### Contents
* `ReadData` : helper function to read datapoints from a file.
* `DeCasteljau` : perform the De Casteljau algorithm.
* `BezierCurve` : evalulate a Bézier curve.
* `ComputeSplineC1` : compute Bézier control points for a C1 quadratic spline.
* `ComputeSplineC2` : compute Bézier control points for a C2 cubic spline.
* main part : evaluation and plotting.

### ToDo
1. Implement the computation of control points of a quadratic interpolating Bézier spline for a given sequence of points (function `ComputeSplineC1`). Evaluate and visualise the available datasets.
1. Try changing the position of b_1^0. What happens?
1. (*bonus*) Implement the computation of control points of a cubic interpolating Bézier spline for a given sequence of points (function `ComputeSplineC2`). Evaluate and visualise the available datasets.
1. Compare the results with C1 splines. What changed?
