#!/bin/bash -e

# Build VLFEAT library
cd common/vlfeat-0.9.18
make
cd ../..

# Build YAEL library
cd common/yael_v260_modif/
./configure.sh
make
cd ../..

# Build SIFT extractor
cd indexer/local_descriptors
make
cd ../..

# Download Hessian-Affine SIFT detector (See original videosearch repository for more information)
platform="$(uname -s)"
if [ "$(uname -s)" == "Darwin" ]; then
  desc_bin="compute_descriptors_mac"
elif [ "$(uname -s)" == "Linux" ]; then
  desc_bin="compute_descriptors_linux64"
else
  echo "Platform not supported"
fi
wget -N -P indexer/local_descriptors http://www.irisa.fr/texmex/people/jegou/src/$desc_bin
chmod a+x indexer/local_descriptors/$desc_bin

# Build retriever
cd retriever
make
cd ..
