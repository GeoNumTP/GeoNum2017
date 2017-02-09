## TP2 : Bézier splines, Ck smoothness
In this TP, you'll implement the C1 and C2 Bézier splines.

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

### ToDo
1. Implement the computation of control points of a quadratic interpolating Bézier spline for a given sequence of points $\mathbf p_i$ (function `ComputeSplineC1`). Evaluate and visualise splines the available datasets.
2. Try changing the position of $\mathbf b_1^0$. What happens?
1. Implement the computation of control points of a cubic interpolating Bézier spline for a given sequence of points $\mathbf p_i$ (function `ComputeSplineC2`). Evaluate and visualise splines the available datasets.
2. Compare the results with C1 splines.
