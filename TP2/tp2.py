#------------------------------------------------------
#
#  TP2 : Bezier splines, C^k smoothness
#  http://tiborstanko.sk/teaching/geo-num-2017/tp2.html
#  [10-Feb-2017]
#
#------------------------------------------------------
#
#  This file is a part of the course:
#    Geometrie numerique (spring 2017)
#    https://github.com/GeoNumTP/GeoNum2017
#    M1 Informatique
#    UFR IM2AG
#
#  Course lecturer:
#    Georges-Pierre.Bonneau at inria.fr
#
#  Practical part:
#    Tibor.Stanko at inria.fr
#
#------------------------------------------------------

import sys, os
import matplotlib.pyplot as plt
import numpy as np

TP = os.path.dirname(os.path.realpath(__file__)) + "/"
DATADIR = filename = TP+"data/"


#-------------------------------------------------
# READPOLYGON()
# Read datapoints from a file.
#
# Input
#    filename :  file to be read
#
# Output
#    DataPts  :  (n+1) x 2 matrix of datapoints
#
def ReadData( filename ) :
    datafile = open(filename,'r');
    l = datafile.readline()
    degree = np.fromstring(l,sep=' ',dtype=int)
    DataPts = np.fromfile(datafile,count=2*(degree+1),sep=' ',dtype=float)
    DataPts = DataPts.reshape(-1,2)
    return DataPts


#-------------------------------------------------
# DECASTELJAU( ... )
# Perform the De Casteljau algorithm.
#
# Input
#    BezierPts :  (degree+1) x 2 matrix of Bezier control points
#    k         :  upper index of the computed point (depth of the algorithm)
#    i         :  lower index of the computed point
#    t         :  curve parameter in [0.0,1.0]
#
# Output
#    point b_i^k from the De Casteljau algorithm.
#
def DeCasteljau( BezierPts, k, i, t ) :
    if k==0 :
        return BezierPts[i,:]
    else :
        return (1-t) * DeCasteljau( BezierPts, k-1, i, t )  +  t * DeCasteljau( BezierPts, k-1, i+1, t )


#-------------------------------------------------
# BEZIERCURVE( ... )
# Compute points on the Bezier curve.
#
# Input
#    BezierPts :  (degree+1) x 2 matrix of Bezier control points
#    N         :  number of curve samples
#    
# Output
#    CurvePts  :  N x 2 matrix of curvepoints
#
def BezierCurve( BezierPts, N ) :
    degree = BezierPts.shape[0]-1
    CurvePts = np.empty([N,2])
    i=0
    for t in np.linspace(0.0, 1.0, num=N) :
        CurvePts[i,:] = DeCasteljau( BezierPts, degree, 0, t )
        i+=1
    return CurvePts


#-------------------------------------------------
# COMPUTESPLINEC1( ... )
# Compute Bezier control points for a C1 quadratic spline interpolating the given data.
#
# Input
#    DataPts   : (n+1) x 2 matrix of datapoints P_0,...,P_n
#    
# Output
#    BezierPts : (2n+1) x 2 matrix of Bezier control points 
#
def ComputeSplineC1( DataPts ) :
    
    # input: DataPts = [P_0; P_1; ... ; P_n]
    n = DataPts.shape[0]-1
    
    # BezierPts matrix will contain (2n+1) rows.
    #   n+1  :  end Bezier control pts (input data)
    #   n    :  inner Bezier control pts
    BezierPts = np.zeros([2*n+1,2])
    
    ##
    ## TODO : Compute BezierPts.
    ##
         
    return BezierPts


#-------------------------------------------------
# COMPUTESPLINEC2( ... )
# Compute Bezier control points for a C2 cubic spline interpolating the given data.
#
# Input
#    DataPts   : (n+1) x 2 matrix of datapoints P_0,...,P_n
#    
# Output
#              : (3n+1) x 2 matrix of Bezier control points 
#
def ComputeSplineC2( DataPts ) :
    
    # input: DataPts = [P_0; P_1; ... ; P_n]
    n = DataPts.shape[0]-1
    
    # matrix of the system
    M = np.zeros([3*n+1,3*n+1])
    
    # right side
    R = np.zeros([3*n+1,2])
    
    ##
    ## TODO : Fill M.
    ##          C0  :  n+1 rows
    ##          C1  :  n-1 rows
    ##          C2  :  n-1 rows
    ##          bd  :    2 rows
    ##
    
    ##
    ## TODO : Put DataPts to the first (n+1) rows of R.
    ##
    
    # return the solution
    return np.linalg.solve(M, R)    
    
#-------------------------------------------------
if __name__ == "__main__":
    
    # arg 1 : data name 
    if len(sys.argv) > 1 :
        dataname = sys.argv[1]
    else :
        dataname = "simple" # simple, infinity, spiral

    # arg 2 : sampling density
    if len(sys.argv) > 2 :
        density = int(sys.argv[2])
    else :
        density = 10

    # arg 3 : C2 continuity
    if len(sys.argv) > 3 :
        c2 = True
    else :
        c2 = False

    # filename
    filename = DATADIR + dataname + ".bcv"
    
    # check if valid datafile
    if not os.path.isfile(filename) :
        print "error:  invalid dataname '" + dataname + "'"
        print "usage:  python tp2.py  [simple,infinity,semi,spiral]  [sampling_density]  [c2]"
        
    else :    
        # read points to be interpolated
        DataPts = ReadData(filename)
        n = DataPts.shape[0]-1

        # compute Bezier points
        if c2 :
            BezierPts = ComputeSplineC2( DataPts )
            cstr='C2'
            deg=3
        else :
            BezierPts = ComputeSplineC1( DataPts )
            cstr='C1'
            deg=2

        # for each segment : compute and plot
        for i in range(0,n) :
            
            ##
            ## TODO : Put the control points of i-th spline segment into iBezierPts.
            ##        When it's done, uncomment the following code to compute and plot the segment.
            ##
            
            pass
            #CurvePts = BezierCurve( iBezierPts, density )
            #plt.plot( CurvePts[:,0], CurvePts[:,1], '-', linewidth=3 )


        # plot the datapoints
        plt.plot( DataPts[:,0], DataPts[:,1], 'k.', markersize=10 )
        
        # plot the control polygon
        plt.plot( BezierPts[:,0], BezierPts[:,1], 'k.--', linewidth=1 )
        
        # set axes with equal proportions
        plt.axis('equal')
        
        # titles
        plt.gcf().canvas.set_window_title('TP2 Bezier splines')
        plt.title(cstr+' '+dataname+', '+str(density)+" pts/segment")

        ##
        ## TODO : Uncomment if you want to save the render as png image in data/
        ##
        
        #plt.savefig( DATADIR + dataname + ".png" )
        
        # render
        plt.show()        
