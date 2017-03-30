#-------------------------------------------------
#
#  TP8 : Uniform B-splines as Subdivision Surfaces
#  http://tiborstanko.sk/teaching/geo-num-2017/tp8.html
#  [31-Mar-2017]
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
# READPOINTS()
# Read control network (grid) of points from a file.
#
# Input
#     datafile  :  .net file to be read
#
# Output 
#     M         :  matrix, 3 x m x n, control grid (all three coordinates)
#     u_closed  :  True  = surface is closed in u-direction
#                  False = surface is open   in u-direction
#     v_closed  :  True  = surface is closed in v-direction
#                  False = surface is open   in v-direction
#
def ReadPoints( datafile ) :
    m,n,u_closed,v_closed = np.fromfile(datafile,count=4,sep=' ',dtype=int)
    M = np.fromfile(datafile,count=3*m*n,sep=' ',dtype=float)
    M = M.reshape(-1,3).transpose().reshape(3,m,n)
    return M, u_closed==1, v_closed==1

#-------------------------------------------------
# GENERATERANDOMTERRAIN()
# Generate random terrain and save it to data/terrain.net
#
# Input
#      N    :  grid size in X, Y
#    Amp    :  amplitude in Z
#
def GenerateRandomTerrain(N,Amp) :
    X,Y = np.meshgrid(range(N-1,-1,-1),range(N))
    V = np.array([X,Y,Amp*np.random.rand(N,N)]).transpose().reshape(-1,3)
    f = open(TP+"data/terrain.net","wa")
    f.write('%d %d %d %d \n' % (N,N,0,0))
    np.savetxt(f,V,fmt='%.4f')
    f.close()

#-------------------------------------------------
# SUBDIVIDE()
# Perform one subdivision step.
#
# Input
#        M0   :  3 x M x N, control network of points
#  u_closed   :  True if closed in u-direction, False otherwise
#  v_closed   :  True if closed in v-direction, False otherwise
#
# Output
#       M1    :  array with subdivided network
#
def Subdivide( M0, u_closed, v_closed ) :
    
    # dim is equal to 3
    dim, m, n = M0.shape
    
    #
    # TODO
    #  Implement one subdivision step for uniform B-splines.
    #  Store the result in array M1.
    #
    
    #
    # TODO
    # Change the following to 'return M1' when appropriate
    return M0
    
#-------------------------------------------------
if __name__ == "__main__":
    
    # arg 1 : data name
    if len(sys.argv) > 1 :
        dataname = sys.argv[1]
        if dataname == "terrain" :
            GenerateRandomTerrain(20,3.0)
    else :
        dataname = "torus"

    # arg 2 : subdivision depth
    if len(sys.argv) > 2 :
        depth = int(sys.argv[2])
    else :
        depth = 1

    # filename
    filename = TP+"data/"+dataname+".net"
    
    # check if valid datafile
    if not os.path.isfile(filename) :
        print " error   :  invalid dataname '" + dataname + "'"
        print " usage   :  tp8.py  [torus,cylinder,grid,terrain]  [subdivision_depth=1]"
        print " example :  python tp8.py torus 3"
        
    else :
        # init Viewer
        viewer = Viewer("TP8 : Uniform B-spline SubSurf["+dataname+"]",[1200,800])
        
        # open the datafile
        datafile = open(filename,'r');
        
        # read control points and u_closed, v_closed
        M, u_closed, v_closed = ReadPoints( datafile )
        
        # add wireframe : control net
        viewer.add_patch( M[0,:,:], M[1,:,:], M[2,:,:], wireframe=True)
                
        # iterative subdivision
        for d in range(depth) :
            M = Subdivide(M,u_closed,v_closed)
        
        # u_closed : make rows periodic
        if u_closed :
            rows = np.append( np.arange(M.shape[1]), 0)
            M = M[:,rows,:]
            
        # v_closed : make cols periodic
        if v_closed :
            cols = np.append( np.arange(M.shape[2]), 0)
            M = M[:,:,cols]
        
        # add patch : subdivision surface
        viewer.add_patch( M[0,:,:], M[1,:,:], M[2,:,:])
        
        # display the viewer
        viewer.render()
