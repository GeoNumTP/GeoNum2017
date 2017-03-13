#-------------------------------------------------
#
#  TP6 : Bezier surfaces
#  http://tiborstanko.sk/teaching/geo-num-2017/tp6.html
#  [17-Mar-2017]
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
from OpenGL.GL import *
from OpenGL.GLUT import *
from viewer import Viewer

TP = os.path.dirname(os.path.realpath(__file__)) + "/"
DATADIR = TP+"data/"


#-------------------------------------------------
# READBEZIERMESH()
# Read Bezier control net from a BPT file.
#
# Input
#    filename :  file to be read
#
# Output
#    X, Y, Z  :  three matrices, one for each (3d) coordinate of the control mesh
#
def ReadBezierMesh( datafile ) :
    line = datafile.readline()
    deg = np.fromstring(line,sep=' ',dtype=int)
    M = np.fromfile(datafile,count=3*(deg[0]+1)*(deg[1]+1),sep=' ',dtype=float)
    M = M.reshape(-1,3).transpose().reshape( 3, deg[0]+1, deg[1]+1 )
    return M[0,:,:], M[1,:,:], M[2,:,:]


#-------------------------------------------------
# DECASTELJAU( ... )
# Compute point on a Bezier surface using the De Casteljau algorithm.
#
# Input
#    M        :  m x n matrix
#                control mesh, one coordinate
#    u, v     :  parameters
#
# Output      :  one coordinate of the surface point S(u,v)
#
def DeCasteljau(M,u,v) :
    
    #
    # TODO Implement the De Casteljau algorithm for surfaces.
    #
    # hint:
    # The above signature is for non-recursive implementation.
    # For recursive implementation, you can use
    #   def DeCasteljau(X,k,l,i,j,u,v) :
    #
    
    pass


#-------------------------------------------------
# BEZIERSURF( ... )
# Compute Bezier surface points.
#
# Input
#    M        :  m x n matrix
#                control mesh, one coordinate
#    density  :  sampling density
#
# Output
#    S        :  density x density matrix
#                surface points, one coordinate
#
# Note :
# This function is later called three times,
# for each 3d coordinate individually.
#

def BezierSurf(M,density) :
    
    # surface degrees
    m, n = M.shape - np.array([1,1])
    
    # init surface points
    S = np.zeros([density,density])

    #
    # TODO Fill surface points.
    #
    #
    # hint:
    # to generate uniform sampling of the interval [0.0,1.0], use:
    # >> u = np.linspace(0.0,1.0,num=density)
    #
    
    return S


#-------------------------------------------------
if __name__ == "__main__":
    
    # arg 1 : data name
    if len(sys.argv) > 1 :
        dataname = sys.argv[1]
    else :
        dataname = "simple"

    # arg 2 : sampling density
    if len(sys.argv) > 2 :
        density = int(sys.argv[2])
    else :
        density = 10

    # filename
    filename = TP+"data/"+dataname+".bpt"
    
    # check if valid datafile
    if not os.path.isfile(filename) :
        print " error   :  invalid dataname '" + dataname + "'"
        print " usage   :  tp6.py  [simple,wave,sphere,heart,teapot,teacup,teaspoon]  [density=10]"
        print " example :  python tp6.py wave 20"
        
    else :
        # open the datafile
        datafile = open(filename,'r');
        
        # get first line = number of patches
        numpatch = np.fromstring( datafile.readline(), sep=' ',dtype=int)[0]
        
        # init Viewer
        viewer = Viewer("TP6 : Bezier surfaces ["+dataname+"]",[1200,800])

        # read and compute each patch
        for p in range(0,numpatch) :
            
            # print patch id
            print " patch",p+1,"/",numpatch
            
            # read Bezier control points
            BX, BY, BZ = ReadBezierMesh( datafile )
            
            # compute surface points
            X = BezierSurf( BX, density )
            Y = BezierSurf( BY, density )
            Z = BezierSurf( BZ, density )
            
            # add patch to the Viewer
            viewer.add_patch(X,Y,Z)

        # print final message
        print " done."
        
        # display the viewer
        viewer.render()
