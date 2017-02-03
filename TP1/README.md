## TP1 : Bézier curves, De Casteljau’s algorithm
In this TP, you'll implement the De Casteljau’s algorithm, and you'll use it to compute and visualise the curves in the `data` folder. Start by cloning the repo and testing the code for the TP1.
```bash
cd your/working/dir/
git clone https://github.com/GeoNumTP/GeoNum2017.git
cd GeoNum2017
python TP1/tp1.py
```
You should see something like the following figure.
![simple Bezier control polygon](https://raw.githubusercontent.com/GeoNumTP/GeoNum2017/master/_assets/simple.png)

To test with different datasets and sampling densities, you can pass the arguments directly in the command line
```bash
python [simple,infinity,spiral]  [sampling_density]
```
for instance
```bash
python spiral 24
```

### Code structure
The code in `tp1.py` contains three helper functions plus the main part.
* `ReadPolygon` : reads Bézier curve control polygon from a file. The result is returned as a 2-column matrix.
* `DeCasteljau` : returns the point b_i^k from De Casteljau algorithm.
* `BezierCurve` : uniform evaluation of the Bézier curve.
* main part : controls the computation and plots results. 


### ToDo
1. Implement the De Casteljau algorithm (`DeCasteljau`) and use it to evaluate the provided Bézier curves (`BezierCurve`). Visualise the curves together with their control polygons.
2. Try varying the sampling density. How many samples are needed to give the impression of a smooth curve?
3. Pick one dataset and visualise *all* intermediate polygons `b_i^k` from the De Casteljau algorithm for a fixed parameter, for instance `t=0.5`. **Hint**: each column in [the schema](https://tiborstanko.sk/teaching/geo-num-2017/tp1.html#decasteljau-schema) represents one such polygon.
