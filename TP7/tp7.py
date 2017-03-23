#-------------------------------------------------
#
#  TP7 : B-spline surfaces
#  http://tiborstanko.sk/teaching/geo-num-2017/tp7.html
#  [24-Mar-2017]
#
#-------------------------------------------------
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
#-------------------------------------------------

import sys, os
import numpy as np
from viewer import Viewer

TP = os.path.dirname(os.path.realpath(__file__)) + "/"

#-------------------------------------------------
# READBSPLINEMESHWITHKNOTS()
# Read B-spline surface data from a .bspline of a .nurbs file.
#
# Input
#     datafile  :  file to be read
#
# Output 
#     M         :  matrix, 3 (or 4) x (m+1) x (n+1), control net (all three (four) coordinates)
#     U         :  knot sequence in the u-direction
#     V         :  knot sequence in the v-direction
#
def ReadBSplineMeshWithKnots( datafile, nurbs=False ) :
    # if nurbs, read four coordinates; otherwise read three
    if nurbs : 
        dim=4
    else : 
        dim=3
    m,n,k,l = np.fromfile(datafile,count=4,sep=' ',dtype=int)
    M = np.fromfile(datafile,count=dim*m*n,sep=' ',dtype=float)
    M = M.reshape(-1,dim).transpose().reshape(dim,m,n)
    U = np.fromfile(datafile,count=k,sep=' ',dtype=float)
    V = np.fromfile(datafile,count=l,sep=' ',dtype=float)
    return M, U, V

#-------------------------------------------------
# DEBOORSURF( ... )
# Recursive De Boor's algorithm for surfaces.
#
# Input
#    M     :  (m+1) x (n+1) coordinate matrix, control points net
#    U     :  vector of knots in the direction u
#    V     :  vector of knots in the direction v
#    r, s  :  upper indices of the computed point (depth of the algorithm)
#    i, j  :  lower indices of the computed point
#    u, v  :  parameters, [u,v] in [ U_i, U_i+1 ] x [ V_j, V_j+1 ]
#
# Output
#   Point d_(i,j)^(r,s) from De Boor's algorithm.
# 
def DeBoorSurf( M, U, V, r, s, i, j, u, v ) :
    
    ##
    ## TODO :
    ## Implement recursive De Boor's algorithm for surfaces.
    ##
    
    pass

#-------------------------------------------------
if __name__ == "__main__":
    
    # arg 1 : data name
    if len(sys.argv) > 1 :
        dataname = sys.argv[1]
    else :
        dataname = "simple" # simple, torus

    # arg 2 : sampling density
    if len(sys.argv) > 2 :
        samples = int(sys.argv[2])
    else :
        samples = 11
        
    # arg 3 : nurbs
    if len(sys.argv) > 3 :
        nurbs = True
        ext = "nurbs"
    else :
        nurbs = False
        ext = "bspline"

    # filename
    filename = TP+"data/"+dataname+"."+ext
    
    # check if valid datafile
    if not os.path.isfile(filename) :
        print " error   :  invalid dataname '" + dataname + "'"
        print " usage   :  tp7.py  [simple,torus]  [sampling_density]"
        print " example :  python tp7.py torus 20"
        
    else :
        # init Viewer
        viewer = Viewer("TP7 : B-spline surfaces ["+dataname+"]",[1200,800])
        
        # open the datafile
        datafile = open(filename,'r');
        
        # read control points and knot sequences
        M, U, V = ReadBSplineMeshWithKnots( datafile, nurbs )
        
        # coordinate matrices
        Mx = M[0,:,:]
        My = M[1,:,:]
        Mz = M[2,:,:]
        
        # add wireframe : control net
        viewer.add_patch( Mx, My, Mz, wireframe=True)
        
        # NURBS weights
        if nurbs :
            Mw = M[3,:,:]
            ##
            ## BONUS TODO :
            ## NURBS Multiply Mx, My, Mz by Mw
            ## HINT : use the function np.multiply(A,B)
            ##
        
        # add control net wireframe to the viewer
        viewer.add_patch( Mx, My, Mz, wireframe=True)
        
        m = Mx.shape[0]-1    # m+1 points in u-direction
        n = Mx.shape[1]-1    # n+1 points in v-direction
        
        k = U.shape[0]-1     # k+1 knots in u-direction
        l = V.shape[0]-1     # l+1 knots in v-direction
        
        du = k-m-1           # degree in u-direction
        dv = l-n-1           # degree in v-direction
        
        # loop over segments in u-direction
        for i in range(du,k-du) :
            
            # check if the segment is non-degenerate
            if U[i] == U[i+1] :
                continue
            
            # loop over segments in v-direction
            for j in range(dv,l-dv) :
                
                # check if the segment is non-degenerate
                if V[j] == V[j+1] :
                    continue
            
                ##
                ## HINT : 
                ##   we are now evaluating a surface patch defined over 
                ##   [ U_i, U_i+1 ] x [ V_j, V_j+1 ]
                ##
                
                # initialize patch points : three coordinate matrices
                Sx = np.zeros([samples,samples])
                Sy = np.zeros([samples,samples])
                Sz = np.zeros([samples,samples])
                
                
                ##
                ## TODO :
                ## Compute patch points using DeBoorSurf.
                ## 
                ## HINT1 :
                ##   Use a double loop.
                ##    - loop over u in [ U_i, U_i+1 ]
                ##    -- loop over v in [ V_j, V_j+1 ]
                ##
                ## HINT2
                ##   Uniform sampling of interval [ a, b ] is computed via
                ##   np.linspace(a,b,num=samples)
                ##
                
                
                
                ##
                ## BONUS TODO :
                ## NURBS Divide Sx, Sy, Sz by Sw
                ## HINT : use the function np.divide(A,B)
                ##
                
                # after the Sx, Sy, Sz have been calculated :
                # add current patch to the viewer
                viewer.add_patch(Sx,Sy,Sz)
                
            # END for j in range( degreeV, n-degreeV )
        # END for i in range( degreeU, m-degreeU )
        
        # display the viewer
        viewer.render()
