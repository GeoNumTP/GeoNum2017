#!/bin/sh

clear
. ./exportPath.sh
echo "==============================="
echo "PYTHONPATH set to $PYTHONPATH"

#-------------------------------------------------------------------------------
# Create local package folder
#-------------------------------------------------------------------------------
if [ ! -d "$(pwd)/lib/python2.7/site-packages/" ]; then
    echo "Creating lib/python2.7/site-packages/"
    mkdir -p "$(pwd)/lib/python2.7/site-packages/"
fi
echo "==============================="

#-------------------------------------------------------------------------------
# PyOpenGL$(pwd)
#-------------------------------------------------------------------------------
if [ ! -d "$(pwd)/lib/python2.7/site-packages/PyOpenGL-3.1.1a1-py2.7.egg/" ]; then
    wget "https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-3.1.1a1.tar.gz" -q --show-progress
    echo "-------------------------------"
    echo "Extract PyOpenGL-3.1.1a1.tar.gz"
    tar xfz PyOpenGL-3.1.1a1.tar.gz
    echo "-------------------------------"
    echo "Install PyOpenGL-3.1.1a1"
    cd PyOpenGL-3.1.1a1
    python setup.py -q install --prefix=$(pwd)/..
    cd ..    
    echo "-------------------------------"
    echo "Clean"
    rm -f PyOpenGL-3.1.1a1.tar.gz
    rm -rf PyOpenGL-3.1.1a1/
else
    echo "PyOpenGL is already installed in lib/python2.7/site-packages/"
    echo "Skipping..."
fi
echo "==============================="

#-------------------------------------------------------------------------------
# PyGLFW
#-------------------------------------------------------------------------------
if [ ! -f "$(pwd)/lib/python2.7/site-packages/glfw.py" ]; then
    wget "https://pypi.python.org/packages/01/d8/155dc626d01f2b267ced7196378da77818f0560c9471ef9cdf9f02bd8611/glfw-1.3.3.tar.gz" -q --show-progress
    echo "-------------------------------"
    echo "Extract glfw-1.3.3.tar.gz"
    tar xzf glfw-1.3.3.tar.gz
    echo "-------------------------------"
    echo "Install glfw-1.3.3"
    cd glfw-1.3.3
    python setup.py -q install --prefix=$(pwd)/..
    cd ..
    echo "-------------------------------"
    echo "Clean"
    rm -f glfw-1.3.3.tar.gz
    rm -rf glfw-1.3.3/
else
    echo "PyGLFW is already installed in lib/python2.7/site-packages/"
    echo "Skipping..."
fi
echo "==============================="

#-------------------------------------------------------------------------------
# GLFW
#-------------------------------------------------------------------------------
if [ ! -f "$(pwd)/libglfw.so" ]; then
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
    echo "-------------------------------"
    echo "Clean"
    rm -f glfw-3.2.1.zip
    rm -rf glfw-3.2.1/
else
    echo "libglfw.so is already installed in ."
    echo "Skipping..."
fi
echo "==============================="

