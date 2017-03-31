#!/usr/bin/env python
import sys
import numpy as np
import OpenGL
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *  
from OpenGL.GLUT import *
OpenGL.ERROR_ON_COPY = True  
OpenGL.ERROR_CHECKING = True
import glfw
from ctypes import c_void_p
import math

VIEWER_DIR = os.path.dirname(os.path.realpath(__file__)) + "/"

#-------------------------------------------------
# Code for computing per vertex normals is from
# https://sites.google.com/site/dlampetest/python/calculating-normals-of-a-triangle-mesh-using-numpy
#-------------------------------------------------
def normalize_v3(A):
    ''' Normalize a numpy array of 3 component vectors shape=(n,3) '''
    A = np.nan_to_num(A)
    lens = np.sqrt( A[:,0]**2 + A[:,1]**2 + A[:,2]**2 )
    #np.set_printoptions(threshold='nan')
    nonzero = lens > 0
    A[ nonzero, 0 ] /= lens[nonzero]
    A[ nonzero, 1 ] /= lens[nonzero]
    A[ nonzero, 2 ] /= lens[nonzero]        
    return A

#-------------------------------------------------
def per_vertex_normals(V,F):
    N = np.zeros( V.shape, dtype=V.dtype )
    T = V[F]
    FN = np.cross( T[::,1]-T[::,0],  T[::,2]-T[::,0] )
    normalize_v3(FN)
    N[ F[:,0] ] += FN
    N[ F[:,1] ] += FN
    N[ F[:,2] ] += FN
    normalize_v3(N)
    return N
#-------------------------------------------------
def cube():
    V = np.array([
    # front
        [-1.0, -1.0, +1.0], [+1.0, -1.0, +1.0],
        [+1.0, +1.0, +1.0], [-1.0, +1.0, +1.0],
        # back
        [-1.0, -1.0, -1.0], [+1.0, -1.0, -1.0],
        [+1.0, +1.0, -1.0], [-1.0, +1.0, -1.0]
    ],  dtype=np.float32 )
    F = np.array([
        # front
        [0, 1, 2],[2, 3, 0],
        # top
        [1, 5, 6],[6, 2, 1],
        # back
        [7, 6, 5],[5, 4, 7],
        # bottom     
        [4, 0, 3],[3, 7, 4],
        # left
        [4, 5, 1],[1, 0, 4],
        # right
        [3, 2, 6],[6, 7, 3]
    ], dtype=np.uint32 )
    return V, F
#-------------------------------------------------
def test_mesh(dataname): 
    f = open(VIEWER_DIR+"testdata/"+dataname+".off","r")
    assert f.readline() == "OFF\n"
    nv, nf, zero = f.readline().split()
    nv = int(nv)
    nf = int(nf)
    V = np.fromfile(f, dtype=np.float32, count=3*nv, sep=" ")
    V = V.reshape(-1, 3)
    F = np.fromfile(f, dtype=np.uint32, count=4*nf, sep=" ")
    F = F.reshape(-1, 4)[:, 1:]
    return V, F
#-------------------------------------------------
def objmesh(): 
    #f = open("elephant.obj", "r")
    f = open(VIEWER_DIR + "horse.obj", "r")
    nv, nn, nf = f.readline().split()
    nv = int(nv)
    nn = int(nn)
    nf = int(nf)
    V = np.fromfile(f, dtype=np.float32, count=3*nv, sep=" ")
    V = V.reshape(-1, 3)
    N = np.fromfile(f, dtype=np.float32, count=3*nn, sep=" ")
    N = N.reshape(-1, 3)
    F = np.fromfile(f, dtype=np.uint32, count=3*nf, sep=" ")
    F = F.reshape(-1, 3)
    return V, F
#-------------------------------------------------
def ortho( left, right, bottom, top, nearVal, farVal):
    result = np.identity(4)
    result[0,0] =  2. / (right - left)
    result[1,1] =  2. / (top - bottom)
    result[2,2] = -2. / (farVal - nearVal)
    result[0,3] = -(right + left) / (right - left)
    result[1,3] = -(top + bottom) / (top - bottom)
    result[2,3] = -(farVal + nearVal) / (farVal - nearVal)
    return result
#-------------------------------------------------
def frustum( left, right, bottom, top, nearVal, farVal):
    result = np.zeros([4,4])
    result[0,0] = (2. * nearVal) / (right - left)
    result[1,1] = (2. * nearVal) / (top - bottom)
    result[0,2] = (right + left) / (right - left)
    result[1,2] = (top + bottom) / (top - bottom)
    result[2,2] = -(farVal + nearVal) / (farVal - nearVal)
    result[3,2] = -1.
    result[2,3] = -(2. * farVal * nearVal) / (farVal - nearVal)
    return result
#-------------------------------------------------
def lookAt( az, el, zoom ) :
    target = np.array([0,0,0])
    direction = np.array([math.cos(el) * math.sin(az), math.cos(el) * math.cos(az), math.sin(el) ])
    right = np.array([ math.sin( az - 0.5*math.pi ),  math.cos( az - 0.5*math.pi ), 0])
    up = np.cross( right, direction )
    origin = target-zoom*direction
    f = (target - origin)
    f = f / np.linalg.norm(f)
    s = np.cross(f,up)
    s = s / np.linalg.norm(s)
    u = np.cross(s,f)
    result = np.identity(4)
    result[0,0] = s[0]
    result[0,1] = s[1]
    result[0,2] = s[2]
    result[1,0] = u[0]
    result[1,1] = u[1]
    result[1,2] = u[2]
    result[2,0] = -f[0]
    result[2,1] = -f[1]
    result[2,2] = -f[2]
    result[0,3] = -np.dot(s,origin)
    result[1,3] = -np.dot(u,origin)
    result[2,3] =  np.dot(f,origin)
    return result
#-------------------------------------------------

##################################################

#-------------------------------------------------
class Viewer():

    def show_help( self ) :
        print " "
        print "------------------------------------------------"
        print "  Viewer controls : "
        print "------------------------------------------------"
        print "  left click & drag  = rotate"
        print "  mouse scroll       = zoom"
        print "  pageup/pagedown    = zoom"
        print "  [ E ]              = toggle wireframe"
        print "  [ N ]              = toggle color by normals"
        print "  [ F ]              = flip normals"
        print "  [Esc]              = quit"
        print " "

    def recompute_matrices( self ) :
        fH = math.tan(self.viewAngle / 360. * math.pi) * self.dnear
        fW = fH * self.w / self.h
        if self.ortho :
            self.proj = ortho( -fW, fW, -fH, fH, self.dnear, self.dfar )
        else : 
            self.proj = frustum( -fW, fW, -fH, fH, self.dnear, self.dfar )
        self.view = lookAt( self.az, self.el, self.zoom )
        #self.view *= self.rotation
        self.model= self.scale * np.identity(4)
        self.model[3,3] = 1.0
        self.nmat = self.view
        self.invv = np.linalg.inv( self.view )
        
    
    def mouse_button_callback( self, window, button, action, mods ) :
        if button == glfw.MOUSE_BUTTON_LEFT :
            self.rotate = ~self.rotate
            if self.rotate :
                self.xpos, self.ypos = glfw.get_cursor_pos(window)
    
    
    def mouse_scroll_callback( self, window, xoff, yoff ) :
        if yoff < 0 :
            self.zoom *= 1.1
        else :
            self.zoom *= 0.9
        self.recompute_matrices()
        return
    
    
    def window_resize_callback( self, window, w, h ) :
        self.w = float(w)
        self.h = float(h)
        glViewport(0,0,w,h);
        self.recompute_matrices()
        
        
    def key_callback( self, window, key, scancode, action, mods ) :
        if key == glfw.KEY_PAGE_UP :
            self.zoom *= 0.9
            self.recompute_matrices()
            return
        if key == glfw.KEY_PAGE_DOWN :
            self.zoom *= 1.1
            self.recompute_matrices()
            return
        if key == glfw.KEY_E and action == glfw.PRESS :
            self.wire = not self.wire
            return
        if key == glfw.KEY_N and action == glfw.PRESS :
            self.rendernormals = not self.rendernormals
            return
        if key == glfw.KEY_P and action == glfw.PRESS :
            self.ortho = not self.ortho
            self.recompute_matrices()
            return
        if key == glfw.KEY_F and action == glfw.PRESS :
            self.nrmls = -self.nrmls
            glBindBuffer( GL_ARRAY_BUFFER, self.vbo[1])
            glBufferData( GL_ARRAY_BUFFER, 
                          self.nrmls.size * self.nrmls.itemsize, self.nrmls, GL_STATIC_DRAW)
            return
        
    
    def __init__(self,wname="Viewer",size=[1200,800]) :
                
        self.wname = wname
        self.w = size[0] 
        self.h = size[1]
        
        self.verts = np.empty([0,3],dtype=np.float32)
        self.faces = np.empty([0,3],dtype=np.uint32)
        self.edges = np.empty([0,2],dtype=np.uint32)
        
        self.rotate = False
        self.rotation = np.identity(4)
        self.wire = True
        self.rendernormals = False
        self.ortho = False
        self.xpos = 0
        self.ypos = 0
        
        self.zoom = 2.0
        self.az =  45. / 180. * math.pi
        self.el = 200. / 180. * math.pi
        
        self.scale = 1.
        
        self.viewAngle = 30.
        self.dnear = 0.01
        self.dfar = 100.
        
        if not glfw.init():
            return
        
        self.show_help()
        
        
    def add_patch(self,X,Y,Z,wireframe=False) :
        
        # extract sampling density
        u = X.shape[0]
        v = X.shape[1]
        
        # vertices
        V = np.empty([u*v,3],dtype=np.float32)
        V[:,0] = X.reshape(u*v)
        V[:,1] = Y.reshape(u*v)
        V[:,2] = Z.reshape(u*v)
        
        # grid indices
        i0 = range(0,(u-1)*v)
        i1 = range(v, u   *v)
        frst = [v*i   for i in range(0,u  )]
        last = [v*i-1 for i in range(1,u+1)]
        
        i00 = list( set(i0) - set(last) )
        i01 = list( set(i0) - set(frst) )
        i10 = list( set(i1) - set(last) )
        i11 = list( set(i1) - set(frst) )
        
        # faces
        F = np.empty([2*(u-1)*(v-1),3],dtype=np.uint32)
        F[:,0] = i00 + i11
        F[:,1] = i01 + i10
        F[:,2] = i11 + i00
        
        # edges
        E = np.empty([4*(u-1)*(v-1),2],dtype=np.uint32)
        E[:,0] = i00 + i01 + i11 + i10
        E[:,1] = i01 + i11 + i10 + i00
        
        # add the mesh
        self.add_mesh(V,F,E,wireframe)
        
        
    def add_mesh(self,V,F,E=None,wireframe=False) :
        
        # Calculate edges if not provided    
        if E is None :
            f0 = F[:,0]
            f1 = F[:,1]
            f2 = F[:,2]
            E = np.empty([F.shape[0]*3,2],dtype=np.uint32)
            E[:,0] = np.concatenate([f0, f1, f2])
            E[:,1] = np.concatenate([f1, f2, f0]) 
        
        # Shift if needed            
        if self.edges.shape[0] > 0 :
            F += self.edges.max()+1
            E += self.edges.max()+1
        
        # Store
        self.verts = np.concatenate( (self.verts, V ), axis=0 )
        self.edges = np.concatenate( (self.edges, E ), axis=0 )
        if not wireframe :
            self.faces = np.concatenate( (self.faces, F ), axis=0 )
        
    def render(self) :
    
        # Glfw settings
        glfw.window_hint(glfw.SAMPLES,4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
        
        # Create a windowed mode window and its OpenGL context
        window = glfw.create_window(self.w, self.h, self.wname, None, None)
        if not window:
            glfw.terminate()
            return
        
        # Make the window's context current
        glfw.make_context_current(window)
        
        # Glfw callbacks
        glfw.set_scroll_callback( window, self.mouse_scroll_callback )
        glfw.set_mouse_button_callback( window, self.mouse_button_callback )
        glfw.set_window_size_callback( window, self.window_resize_callback )
        glfw.set_key_callback( window, self.key_callback )
               
        # OpenGL settings                    
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_OFFSET_FILL)
        glClearColor(1.0,1.0,1.0,1.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glPolygonOffset(1.0,1.0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
        # Create shader program
        program = glCreateProgram(1)  
        
        # Vertex shader
        with open(VIEWER_DIR+"shaders/mesh.vert.glsl", 'r') as VS_file:
            VS = VS_file.read()
        vshader = glCreateShader(GL_VERTEX_SHADER);
        glShaderSource(vshader,VS);
        glCompileShader(vshader);
        glAttachShader(program,vshader);
        
        # Fragment shader
        with open(VIEWER_DIR+"shaders/mesh.frag.glsl", 'r') as FS_file:
            FS = FS_file.read()
        fshader = glCreateShader(GL_FRAGMENT_SHADER);
        glShaderSource(fshader,FS);
        glCompileShader(fshader);
        glAttachShader(program,fshader);
        
        # Link shader program
        glLinkProgram(program);
        
        # Detach and delete shaders
        glDetachShader(program,vshader);
        glDetachShader(program,fshader);
        glDeleteShader(vshader);
        glDeleteShader(fshader);
        
        # Get program locations
        self.location = lambda:0
        self.location.model = glGetUniformLocation( program, 'model')
        self.location.view  = glGetUniformLocation( program, 'view')
        self.location.nmat  = glGetUniformLocation( program, 'nmat')
        self.location.proj  = glGetUniformLocation( program, 'proj')
        self.location.cmode = glGetUniformLocation( program, 'cmode') # 0 uniform 1 fixed 2 normals
        
        # Scale to uniform length
        diag = self.verts.max(0)-self.verts.min(0)
        aabb = np.linalg.norm(diag)
        if aabb > 0 :
            self.scale = 1. / aabb
        
        # Snap to centroid
        self.verts -= 0.5*(self.verts.max(0)+self.verts.min(0))
        
        # Compute per-vertex normals
        self.nrmls = per_vertex_normals(self.verts,self.faces)
        
        # Recompute Model, View, Projection matrices
        self.recompute_matrices()
        
        # Generate vertex arrays
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        
        # Generate vertex buffers
        self.vbo = glGenBuffers(4)
        
        # 0 : position
        glBindBuffer( GL_ARRAY_BUFFER, self.vbo[0])
        glBufferData( GL_ARRAY_BUFFER, 
                      self.verts.size * self.verts.itemsize, self.verts, GL_STATIC_DRAW)
        
        # 1 : normals
        glBindBuffer( GL_ARRAY_BUFFER, self.vbo[1])
        glBufferData( GL_ARRAY_BUFFER, 
                      self.nrmls.size * self.nrmls.itemsize, self.nrmls, GL_STATIC_DRAW)
        
        # 2 : face indices
        glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.vbo[2])
        glBufferData( GL_ELEMENT_ARRAY_BUFFER,
                      self.faces.size * self.faces.itemsize, self.faces, GL_STATIC_DRAW)
        
        # 3 : edge indices
        glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.vbo[3])
        glBufferData( GL_ELEMENT_ARRAY_BUFFER,
                      self.edges.size * self.edges.itemsize, self.edges, GL_STATIC_DRAW)

        # Loop until the user closes the window
        while not glfw.window_should_close(window) and glfw.get_key(window,glfw.KEY_ESCAPE) != glfw.PRESS:    
            
            # Change rotation
            if self.rotate :
                xpos, ypos = glfw.get_cursor_pos( window )
                if self.xpos != xpos or self.ypos != ypos :
    
                    # azimuth
                    self.az -= 10*(self.xpos - xpos) / self.w
                    # elevation
                    self.el -= 10*(self.ypos - ypos) / self.h
                               
                    # store new mouse coords
                    self.xpos = xpos
                    self.ypos = ypos
                    
                    # recompute MVP matrices
                    self.recompute_matrices()
            
            # Clear the buffers
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
            # Use our shader program
            glUseProgram(program)
            
            # Set uniforms
            glUniformMatrix4fv( self.location.model, 1, True, self.model )
            glUniformMatrix4fv( self.location.view , 1, True, self.view )
            glUniformMatrix4fv( self.location.nmat , 1, True, self.nmat )
            glUniformMatrix4fv( self.location.proj , 1, True, self.proj )
            
            # Enable vertex arrays
            glEnableVertexAttribArray(0)
            glEnableVertexAttribArray(1)
         
            # 0 : positions
            glBindBuffer( GL_ARRAY_BUFFER, self.vbo[0] )
            glVertexAttribPointer( 0, 3, GL_FLOAT , False, 0, None )
            
            # 1 : normals
            glBindBuffer( GL_ARRAY_BUFFER, self.vbo[1] )
            glVertexAttribPointer( 1, 3, GL_FLOAT , False, 0, None )
            
            # Draw wireframe
            if self.wire :
                # Bind element buffer
                glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.vbo[3])
                glUniform1i( self.location.cmode, 1 )
                glDrawElements(GL_LINES, self.edges.size, GL_UNSIGNED_INT, None)
            
            # Draw triangles
            if self.rendernormals :
                # Color by normals
                glUniform1i( self.location.cmode, 2 )
            else :
                # Uniform color
                glUniform1i( self.location.cmode, 0 )
            glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.vbo[2])
            glDrawElements(GL_TRIANGLES, self.faces.size, GL_UNSIGNED_INT, None)
            
            # Disable vertex arrays
            glDisableVertexAttribArray(0)
            glDisableVertexAttribArray(1)
            
            # Swap front and back buffers
            glfw.swap_buffers(window)

            # Poll for and process events
            glfw.poll_events()
        
        # Delete stuff
        glDeleteBuffers(4,self.vbo)
        glDeleteVertexArrays(1,(self.vao,))
        glDeleteProgram(program)
        glfw.terminate()

#-------------------------------------------------
if __name__ == "__main__":
        
    if len(sys.argv) > 1 :
        dataname = sys.argv[1]
    else :
        dataname = "bumpy"

    V,F = test_mesh(dataname)
    
    viewer = Viewer()
    viewer.add_mesh(V,F)
    viewer.render()
