#-------------------------------------------------
#
#  TP9 : Subdivision surfaces on triangle meshes
#  http://tiborstanko.sk/teaching/geo-num-2017/tp9.html
#  [07-Apr-2017]
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

import sys, os, math
import numpy as np
from viewer import Viewer
TP = os.path.dirname(os.path.realpath(__file__)) + "/"


#-------------------------------------------------
# READMESH()
# Read mesh vertices and faces from a file.
def ReadMesh( datafile ) :
    assert datafile.readline() == "OFF\n"
    nv,nf,zero = np.fromfile(datafile,count=3,sep=' ',dtype=np.uint32)
    V = np.fromfile(datafile,count=3*nv,sep=' ',dtype=np.float32).reshape(-1,3)
    F = np.fromfile(datafile,count=4*nf,sep=' ',dtype=np.uint32).reshape(-1, 4)[:,1:]
    return V, F


#-------------------------------------------------
# FINDEDGES(F,e0,e1)
# Find all instances of the edge [e0,e1] or [e1,e0] in F.
#
#  Input
#      F        :   #F x 3 matrix with mesh faces
#      e0, e1   :   indices of vertices in the edge
#
#  Output
#      faces    :   2x1 array, indices of the faces which contain the edge [e0,e1]
#      eindex   :   2x1 array, location of [e0,e1] in the corresponding face (0, 1 or 2)
#      oppos    :   2x1 array, location of vertex opposite to [e0,e1] in the corresponding face (0, 1 or 2)
#
def FindEdges(F,e0,e1) :
    
    # find rows with indices e0,e1
    faces = np.where((F==e0).any(axis=1) & (F==e1).any(axis=1))[0]
    
    # check length
    # for closed meshes, length of frows should be always 2
    assert(len(faces)==2)
    
    # init edge indices
    eindex = np.zeros( faces.shape, dtype=int)
    
    # init opposite indices
    oppos = np.zeros( faces.shape, dtype=int)
    
    # loop over the (two) faces which contain [e0,e1]
    i=0
    for f in faces :
        
        # compute sum of locations of [e0,e1] in the face F[f]
        s = np.where(F[f]==e0)[0] + np.where(F[f]==e1)[0]
        
        # edge 0+1
        if s == 1 :
            eindex[i] = 0
            oppos[i] = 2
            
        # edge 1+2
        elif s == 3 :
            eindex[i] = 1
            oppos[i] = 0
            
        # edge 2+0
        elif s == 2 :
            eindex[i] = 2
            oppos[i] = 1
        
        i+=1
    
    return faces, eindex, oppos


#-------------------------------------------------
# GETADJACENTVERTICES(F,v)
# Get indices of vertices adjacent to the vertex v.
#
#  Input
#      F        :   #F x 3 matrix with mesh faces
#      v        :   index of a vertex
#
#  Output
#      array with indices of neighbors of the vertex v
#
def GetAdjacentVertices(F,v) :
    return np.setdiff1d( np.unique( F[ np.where((F==v).any(axis=1))[0]].reshape(-1) ), np.array([v]) )


#-------------------------------------------------
# EXTRACTFACES(Edge)
# Extract subdivided faces from edge matrix.
#
#  Input
#      E        :   #E x 6 edge matrix   [ v0 m01 v1 m12 v2 m20 ]
#
#  Output
#      F        :   #F x 3 matrix with mesh faces
#
def ExtractFaces(E) :
    f = E.shape[0]
    F = np.empty([4*f,3],dtype=np.uint32)
    F[:,0] = E[:,[1,3,5,1]].transpose().reshape(-1)
    F[:,1] = E[:,[2,4,0,3]].transpose().reshape(-1)
    F[:,2] = E[:,[3,5,1,5]].transpose().reshape(-1)
    return F


#-------------------------------------------------
# INSERTMIDPOINTS(V,F,Warren)
# Insert midpoints to the mesh and compute 

#  Input
#      V        :   #V x 3 matrix with mesh vertices
#      F        :   #F x 3 matrix with mesh faces
# 
#  Output
#      M        :   #M x 3 matrix with edge midpoints
#      E        :   #E x 6 edge matrix   [ v0 m01 v1 m12 v2 m20 ]
#
def InsertMidpoints(V,F) :
   
    # number of vertices, faces
    v = V.shape[0]
    f = F.shape[0]
    
    # number of edges : Euler's formula V-E+F=2
    e = v+f-2
    
    # E : f x 6  face-edge matrix for storing midpoints
    # init with -1
    E = -1*np.ones([f,6],dtype=int)
    
    # fill even cols with F
    E[:,::2] = F
    
    # M : init midpoint positions
    M = np.zeros([e,3],dtype=np.float32)
            
    # init midpoint indexing
    m=0
    
    # loop over faces
    for i in range(f) :
        
        # loop over edges/midpoints
        for j in range(3) :
            
            # check if -1, otherwise do nothing
            if E[i,2*j+1] == -1 :
        
                #
                # TODO 
                #
                # 1) Put midpoint index m into corresponding locations in matrix E.
                #
                # 2) Compute position of the midpoint m.
                #
                # Hint : use the function FindEdges
                #
                pass
    
    return M, E


#-------------------------------------------------
# BETA(N,Warren=False)
# Compute vertex weights Beta for Loop's subdivision scheme.
#
#  Input
#      N        :   valence
#      Warren   :   False = use Loop's weights
#                           Beta(N) = 1/N * (5/8 - ( 3/8 + 1/4 * cos(2*PI/N) )^2)
#                   True = use Warren's weights
#                           Beta(3) = 3/16
#                           Beta(N) = 3/8/N  if  N>3
#  Output
#      weight Beta(N)
#
def Beta(N,Warren) :
    #
    # TODO compute the weights Beta.
    #
    #
    # Hint : for Loop's weights, use math.cos and math.pi
    #
    return 0
    

#-------------------------------------------------
# RECOMPUTEPOSITIONS(V,F,Warren)
# Update positions of old vertices in the mesh.

#  Input
#      V        :   #V x 3 matrix with mesh vertices
#      F        :   #F x 3 matrix with mesh faces
#      Warren   :   False = use Loop's weights
#                   True = use Warren's weights
# 
#  Output
#   newV        :   #newV x 3 matrix with new positions
#
def RecomputePositions(V,F,Warren) :
    
    # number of vertices
    v = V.shape[0]
    
    # init new positions
    newV = np.zeros(V.shape,dtype=np.float32)
    
    # update old vertices
    for i in range(v) :
        #
        # TODO 
        #
        # Recompute positions of old vertices.
        #
        # Hint : use the functions GetAdjacentVertices and Beta
        #
        pass
        
    return newV


#-------------------------------------------------
# LOOPSUBDIVISION(V,F,Warren)
# Perform one iteration of Loop's subdivision scheme.
#
#  Input
#      V        :   #V x 3 matrix with mesh vertices
#      F        :   #F x 3 matrix with mesh faces
#      Warren   :   False = use Loop's weights
#                   True = use Warren's weights
#
#  Output
#    vertices, faces of the subdivided mesh
#
def LoopSubdivision(V,F,Warren) :
    
    #
    # TODO
    # Uncomment the following code when needed.
    #

    ## 1) insert new vertices : midpoints
    #M,E = InsertMidpoints(V,F)

    ## 2) recompute positions of original vertices
    #nV = RecomputePositions(V,F,Warren)
    
    ## 3) extract subdivided faces from edge matrix
    #F = ExtractFaces(E)
    
    ## 4) concatenate original vertices and the midpoints
    #V = np.concatenate((nV,M),axis=0)
    
    return V, F


#-------------------------------------------------
if __name__ == "__main__":
    
    # defaults
    dataname = "cube"
    depth = 1
    
    # arg 1 : data name
    if len(sys.argv) > 1 :
        dataname = sys.argv[1]

    # arg 2 : subdivision depth
    if len(sys.argv) > 2 :
        depth = int(sys.argv[2])

    # filename
    filename = TP+"data/"+dataname+".off"
    
    # check if valid datafile
    if not os.path.isfile(filename) :
        print " error   :  invalid dataname '" + dataname + "'"
        print " usage   :  tp9.py  [dataname]  [subdivision_depth=2]"
        print " example :  python tp9.py cube 3"
        
    else :
        # open the datafile
        datafile = open(filename,'r');
        
        # read mesh
        mV,mF = ReadMesh( datafile )
        
        # init subdivided mesh
        V = mV
        F = mF
        
        # use Warren's weights?
        Warren = False
        
        print "Loop subdivision..."
        print "         #V      #F"
        # iterative subdivision
        for d in range(depth) :
            print "%3d %7d %7d" % (d,V.shape[0],F.shape[0])
            V,F = LoopSubdivision(V,F,Warren)
        print "%3d %7d %7d" % (depth,V.shape[0],F.shape[0])
        print "Done."
        
        # init Viewer
        viewer = Viewer("TP9 : Subdivision Surfaces ["+dataname+"]",[1200,800])
        
        # display control mesh
        #viewer.add_mesh(mV,mF,E=None,wireframe=True);
        
        # display subdivision surface
        viewer.add_mesh(V,F,E=None,wireframe=False);
        
        # display the viewer
        viewer.render()
