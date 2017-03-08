## TP5 : Lane-Riesenfeld algorithm
In this TP, you'll implement the classical Lane-Riesenfeld algorithm, as well as its six-point variant.

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
cd TP5/
python tp5.py
```

As before, you can pass parameters directly as command line args:
```bash
python tp5.py  [data=hepta; bone,infinity,sumsign]  [scheme=LR; SP]  [curve degree]  [subdivision depth]
```
`LR` stands for Lane-Riesenfeld algorithm, `SP` is the six-point scheme.

For instance, to subdivide the `sumsign` dataset with degree 3 six-point:
```bash
python tp5.py sumsign SP 3
```

### Functions to modify
* `LaneRiesenfeld` : perform one iteration of the Lane-Riesenfeld algorithm.
* `SixPoint` : perform one iteration of six-point variant of LR.

### Lane-Riesenfeld
The Lane-Riesenfeld algorithm is a subdivision scheme which serves for efficient evaluation of uniform B-splines.
As for the subdivision schemes we've seen in the previous TP,
two steps are needed to compute the subdivided polygon `X1` from the base polygon `X0`.
```python
n = X0.shape[0]
X1 = np.zeros([2*n,2])
```
In the topological step, the Lane-Riesenfeld scheme doubles the amount of points by taking each initial point twice.
```
P0 P0 P1 P1 ... Pn Pn
```
This sequence is then refined k times via midpoint averaging 0.5*(A+B),
with k being the degree of the curve (user-defined).
For k=2:
```
  ...P0    P0   P1    P1    P2    P2    P3    P3 
      \   / \  / \   / \   / \   / \   / \   / \
   ... P00   P01   P11   P12   P22   P23   P33 ...
        \   / \   / \   / \   / \   / \   / \
     ... P001  P011  P112  P122  P223  P233 ...
```

### ToDo
1. Implement the two subdivision schemes. Test with the provided datasets.
1. Try varying the degree parameter. How do the curves change?
1. What differences between the two schemes do you observe?  
In your opinion, which scheme gives better results? Why?
