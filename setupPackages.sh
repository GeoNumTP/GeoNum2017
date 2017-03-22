#!/bin/sh

clear

#-------------------------------------------------------------------------------
# Create local package folder
#-------------------------------------------------------------------------------
if [ ! -d "$(pwd)/lib/python2.7/site-packages/" ]; then
    echo "Creating lib/python2.7/site-packages/"
    mkdir -p "$(pwd)/lib/python2.7/site-packages/"
fi
echo "==============================="

#-------------------------------------------------------------------------------
# PyOpenGL
#-------------------------------------------------------------------------------
wget "https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-3.1.1a1.tar.gz" -q --show-progress
echo "-------------------------------"
echo "Extract PyOpenGL-3.1.1a1.tar.gz"
tar xfz PyOpenGL-3.1.1a1.tar.gz
echo "-------------------------------"
echo "Install PyOpenGL-3.1.1a1"
cd PyOpenGL-3.1.1a1
python setup.py -q install --prefix=$(pwd)/..
cd ..
echo "==============================="

#-------------------------------------------------------------------------------
# PyGLFW
#-------------------------------------------------------------------------------
wget "https://pypi.python.org/packages/01/d8/155dc626d01f2b267ced7196378da77818f0560c9471ef9cdf9f02bd8611/glfw-1.3.3.tar.gz" -q --show-progress
echo "-------------------------------"
echo "Extract glfw-1.3.3.tar.gz"
tar xzf glfw-1.3.3.tar.gz
echo "-------------------------------"
echo "Install glfw-1.3.3"
cd glfw-1.3.3
python setup.py -q install --prefix=$(pwd)/..
cd ..
echo "==============================="

#-------------------------------------------------------------------------------
# GLFW
#-------------------------------------------------------------------------------
wget "https://github.com/glfw/glfw/releases/download/3.2.1/glfw-3.2.1.zip" -q --show-progress
echo "-------------------------------"
echo "Extract glfw-3.2.1.zip"
unzip -qqo glfw-3.2.1.zip
echo "-------------------------------"
echo "Compile libglfw.so"
mkdir glfw-3.2.1/build
cd glfw-3.2.1/build
cmake -DBUILD_SHARED_LIBS=ON ..
make -j 4 -s
cd ../../
echo "-------------------------------"
echo "copy libglfw.so* to basedir"
for file in glfw-3.2.1/build/src/libglfw.so*; do cp "$file" .;done
echo "==============================="

#-------------------------------------------------------------------------------
# clean
#-------------------------------------------------------------------------------
echo "clean"
rm -f PyOpenGL-3.1.1a1.tar.gz
rm -f glfw-1.3.3.tar.gz
rm -f glfw-3.2.1.zip
rm -rf PyOpenGL-3.1.1a1/
rm -rf glfw-1.3.3/
rm -rf glfw-3.2.1/
echo "==============================="
