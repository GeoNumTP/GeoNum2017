## TP4 : Subdivision curves
In this TP, you'll implement three subdivision schemes for closed curves: Chaikin, corner cutting and four-point.

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
cd TP4/
python tp4.py
```

As before, you can pass parameters directly as command line args:
```bash
python tp4.py [simple,infinity,bone,bunny]  [scheme=CH,CC,FP]  [subdivision depth]
```

For instance, to subdivide the `bone` dataset with 5 iterations of four-point:
```bash
python tp4.py bone FP 5
```

### Functions to modify
* `Chaikin` : perform one iteration of Chaikin's algorithm.
* `CornerCutting` : perform one iteration of corner cutting algorithm.
* `FourPoint` : perform one iteration of four-point algorithm.

### Subdivision
If `X0` is the base polygon and `X1` the subdivided polygon (in matrix form), two steps are needed to compute `X1` from `X0`.
* **Topological step**: curve is upsampled by inserting a new vertex between each two adjacent vertices. We implement this simply by initializing `X1` with zeros while doubling the amount of rows:  
```python
n = X0.shape[0]
X1 = np.zeros([2*n,2])
```
* **Geometric step**: new positions are computed for all vertices. Implementation: run a loop for `i` from `0` to `n-1` and compute `X1[2*i,:]` and `X1[2*i+1,:]` at each step.  
    * [Chaikin](https://tiborstanko.sk/teaching/geo-num-2017/tp4.html#chaikins-scheme)
    * [Corner cutting](https://tiborstanko.sk/teaching/geo-num-2017/tp4.html#corner-cutting)
    * [Four-point](https://tiborstanko.sk/teaching/geo-num-2017/tp4.html#four-point)

### ToDo
1. Implement the three subdivision schemes.
2. Experiment with different values of a, b in corner cutting. Specifically, try using
     - b =a+0.5
     - b~=a+0.5
   
   What do you observe?
3. *Generalized four-point* uses the mask [-w,0.5+w,0.5+w,-w]. (w=0.0625 in the original scheme.) Modify your implementation of this algorithm to account for the tension parameter w and try varying its value. You should get C1 limit curves for w in [0,sqrt(5)-1)/8] ~ [0,0.154].
