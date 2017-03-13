## TP5 : Lane-Riesenfeld algorithm
In this TP, you'll implement the classical Lane-Riesenfeld algorithm, as well as its four-point and six-point variants.

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
python tp5.py  [data=hepta; bone,infinity,sumsign]  [scheme=LR; FP,SP]  [curve degree]  [subdivision depth]
```
`LR` stands for Lane-Riesenfeld algorithm, `FP` is the four-point scheme, `SP` is the six-point scheme.

For instance, to subdivide the `sumsign` dataset with degree 3 six-point:
```bash
python tp5.py sumsign SP 3
```

### Functions to modify
* `LaneRiesenfeld` : perform one iteration of the Lane-Riesenfeld algorithm.
* `FourPoint` : perform one iteration of four-point variant of LR.
* `SixPoint` : perform one iteration of six-point variant of LR.

### Lane-Riesenfeld
The Lane-Riesenfeld algorithm is a subdivision scheme which serves for efficient evaluation of uniform B-splines.
As for the subdivision schemes we've seen in the previous TP,
two steps are needed to compute the subdivided polygon `X1` from the base polygon `X0`.

In the refining phase, the Lane-Riesenfeld scheme doubles the amount of points by taking each initial point twice.
```
P0 P0 P1 P1 ... Pn Pn
```
This sequence is then smoothed k times via midpoint averaging 0.5*(A+B),
with k being the degree of the curve (user-defined).
For k=2:
```
 ... P0    P0   P1    P1    P2    P2    P3    P3 ...
      \   / \  / \   / \   / \   / \   / \   / \
   ... P00   P01   P11   P12   P22   P23   P33   P34 ...
        \   / \   / \   / \   / \   / \   / \   /
     ... P001  P011  P112  P122  P223  P233  P334 ...
```
Here, each point is calculated as an average of two above points. Points in the last row are taken as the new control polygon. 

### Variations
We'll also look at two variations of the Lane-Riesenfeld algorithm, which use the same principle: initial sequence is first refined and then smoothed k times.

Refining:
```
P0 R0 P1 R1 ... Pn Rn
```
where the new vertices Ri are not doubled, but computed as
```
R_i = 1/16 * (- P_i-1 + 9*P_i + 9*P_i+1 - P_i+2)                                 # 4-point
R_i = 1/256 * (3*P_i-2 - 25*P_i-1 + 150*P_i + 150*P_i+1 - 25*P_i+2 + 3*P_i+3)    # 6-point
```
Smoothing: as in the original agorithm, we then smooth k times using the same masks as in the refining step, but applied on the new sequence.

### ToDo
1. Implement the three subdivision schemes. Test with the provided datasets.
1. Try varying the degree parameter. How do the curves change?
1. What differences between the three schemes do you observe?  
In your opinion, which scheme gives better results? Why?
1. Simplify the original Lane-Riesenfeld scheme for degree k=2. What do you observe?
