## TP3 : B-splines, De Boor's algorithm
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
