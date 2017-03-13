#!/bin/sh

#-------------------------------------------------------------------------------
# Create package folder
if [ ! -d "$(pwd)/lib/python2.7/site-packages/" ]; then
    mkdir -p "$(pwd)/lib/python2.7/site-packages/"
fi

#-------------------------------------------------------------------------------
# PyOpenGL
PyGLVersion="3.1.1a1"
PyGLFolder="PyOpenGL-$PyGLVersion"
PyGLArchive="$PyGLFolder.tar.gz"

echo "-------------------------------"
echo "Downloading $PyGLArchive"
curl -O "https://pypi.python.org/packages/source/P/PyOpenGL/$PyGLArchive"

echo "-------------------------------"
echo "Extracting  $PyGLArchive"
tar xfz $PyGLArchive

echo "-------------------------------"
echo "Installing  $PyGLFolder"
cd $PyGLFolder
python setup.py -q install --prefix=$(pwd)/..
cd ..
echo "-------------------------------"
echo "Done."

#-------------------------------------------------------------------------------
# PyGLFW
PyGLFWVersion="1.3.3"
PyGLFWFolder="glfw-$PyGLFWVersion"
PyGLFWArchive="$PyGLFWFolder.tar.gz"

echo "-------------------------------"
echo "Downloading $PyGLFWArchive"
curl -O "https://pypi.python.org/packages/01/d8/155dc626d01f2b267ced7196378da77818f0560c9471ef9cdf9f02bd8611/$PyGLFWArchive"

echo "-------------------------------"
echo "Extracting  $PyGLFWArchive"
tar xzf $PyGLFWArchive

echo "-------------------------------"
echo "Installing  $PyGLFWFolder"
cd $PyGLFWFolder
python setup.py -q install --prefix=$(pwd)/..
cd ..
echo "-------------------------------"
echo "Done."
