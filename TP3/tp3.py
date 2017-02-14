#------------------------------------------------------
#
#  TP3 : B-splines, De Boor's algorithm
#  http://tiborstanko.sk/teaching/geo-num-2017/tp3.html
#  [17-Feb-2017]
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
# READBSPLINE()
# Read B-spline control points and knot sequence from a file.
#
# Input
#    filename :  file to be read
#
# Output
#    ControlPts :  (n+1) x 2 matrix of control points
#    Knots      :  (m+1) x 1 vector of knots
#
def ReadBSpline( filename, nurbs=False ) :
    
    datafile = open(filename,'r');
    
    # if nurbs, read three coordinates; otherwise read two
    if nurbs : 
        dim=3
    else : 
        dim=2
        
    # datapoints
    p = np.fromstring(datafile.readline(),sep=' ',dtype=int)
    ControlPts = np.fromfile(datafile,count=dim*p,sep=' ',dtype=float)
    ControlPts = ControlPts.reshape(-1,dim)
    
    # knots
    k = np.fromstring(datafile.readline(),sep=' ',dtype=int)
    Knots = np.fromfile(datafile,count=k,sep=' ',dtype=float)
    
    return ControlPts, Knots


#-------------------------------------------------
# DEBOOR( ... )
# Perform the De Boor's algorithm.
#
# Input
#    ControlPts :  (n+1) x 2 matrix of control points
#    Knots      :  (m+1) x 1 vector of knots
#    r          :  upper index of the computed point (depth of the algorithm)
#    j          :  lower index of the computed point
#    t          :  curve parameter in [t_i,t_i+1]
#
# Output
#   Point d_j^r from the De Boor algorithm.
#
#
# NOTE :
#   This specification assumes the algorithm will be performed recursively.
#   Feel free to modify the signature if you want iterative implementation.
#
#
def DeBoor( ControlPts, Knots, r, j, t ) :
    
    pass
    
    ##
    ## TODO : Implement the De Boor algorithm.
    ##

    
#-------------------------------------------------
if __name__ == "__main__":
    
    # arg 1 : data name 
    if len(sys.argv) > 1 :
        dataname = sys.argv[1]
    else :
        dataname = "simple" # [camel,circle,simple,spiral,spiral2] or
                            # [circle7,circle9] for nurbs

    # arg 2 : sampling density
    if len(sys.argv) > 2 :
        density = int(sys.argv[2])
    else :
        density = 20

    # arg 3 : nurbs
    if len(sys.argv) > 3 :
        nurbs = True
    else :
        nurbs = False

    # filename
    if nurbs :
        filename = DATADIR + dataname + ".nurbs"
        dim = 3
        info = "NURBS "
    else :
        filename = DATADIR + dataname + ".bspline"
        dim = 2
        info = ""
    
    # check if valid datafile
    if not os.path.isfile(filename) :
        print " error :  invalid dataname '" + dataname + "'"
        print " usage :  python tp3.py  [camel,circle,simple,spiral,spiral2]  [sampling_density]"
        print "          python tp3.py  [circle7,circle9]                     [sampling_density]  nurbs"
        
    else :    
        # read B-spline control points and knot sequence
        ControlPts, Knots = ReadBSpline(filename,nurbs)
        
        # (n+1) control points
        n = ControlPts.shape[0]-1
        
        # (m+1) knots
        m = Knots.shape[0]-1
        
        # degree of the curve = (m+1) - (n+1) - 1
        # which is the same as
        degree = m-n-1
        
        # plot the control polygon
        plt.plot( ControlPts[:,0], ControlPts[:,1], 'k--')
        
        
        ##
        ## TODO : Evaluate the B-spline curve.
        ##
        ## HINT :
        ##   Computation needs to be carried out segment-wise.
        ##   B-spline curve is defined on the interval [ t_degree, t_m-degree ) = [ t_degree, t_n+1 )
        ##   and the segments are
        ##     [ t_degree  , t_degree+1 ),
        ##     [ t_degree+1, t_degree+2 ),
        ##      ... 
        ##     [ t_n-1, t_n   ),
        ##     [ t_n  , t_n+1 ).
        ##   Beware though : some of these segments can be degenerate! (if t_i == t_i+1)
        ##
        # loop over segments
        for j in range(degree,m-degree) :
            
            ##
            ## TODO : Make sure the segment is non-degenerate.
            ##
        
            # prepare matrix of segment points
            Segment = np.zeros([density,dim])
        
            ##
            ## TODO : Perform De Boor.
            ##
            
            # plot the segment
            plt.plot( Segment[:,0], Segment[:,1], '-',linewidth=3)
        
        
        
        
        ## 
        ## TODO : Modify the above evaluation for NURBS data.
        ##
        ##
        ## HINT :
        ##   For NURBS data, the ControlPts matrix has three columns;
        ##    [ x, y, w ]
        ##   the first two are cartesian coordinates (same as before),
        ##   the third column represents control point weight.
        ##   
        ##   Normally, you should be able to use De Boor for NURBS without modification,
        ##   you only need to feed it the right control points, in homogeneous coordinates.
        ##
        ##   Steps :
        ##    1. Convert cartesian control points C = [ x, y ] to
        ##             homogeneous control points H = [ w*x, w*y, w ].
        ##    2. Perform De Boor with H-points.
        ##    3. Convert the result back to cartesian coords (divide by last coordinate).
        ##
        
        
        
        
        
        # set axes with equal proportions
        plt.axis('equal')
        
        # titles
        plt.gcf().canvas.set_window_title('TP3 B-splines')
        plt.title(info+dataname+', '+str(density)+" pts/segment")

        ##
        ## TODO : Uncomment if you want to save the render as png image in data/
        ##
        #plt.savefig( DATADIR + dataname + ".png" )
        
        # render
        plt.show()        
