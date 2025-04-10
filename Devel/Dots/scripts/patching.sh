#!/bin/bash
srcdir=some-path
cd $srcdir
for p in ../0*-*.patch; do
echo "---> patching source with $p <---"
patch -Np1 -i "$p"
done
