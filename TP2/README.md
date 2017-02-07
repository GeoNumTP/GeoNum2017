## TP2 : Bézier splines, $C^k$ smoothness
In this TP, you'll implement the De Casteljau’s algorithm, and you'll use it to compute and visualise the curves in the `data` folder.
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
```

### ToDo
1. Implement the computation C1 quadratic interpolating Bézier spline for a given sequence of datapoints
(`ComputeSplineC1`). Evaluate and visualise the spline for all datasets and various sampling densities.
1. Implement the computation C2 cubic interpolating Bézier spline for a given sequence of datapoints
(`ComputeSplineC2`). Evaluate and visualise the spline for all datasets and various sampling densities.
