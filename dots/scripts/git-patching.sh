#!/bin/bash
srcdir=some-path
cd $srcdir
# for p in ../000{1,2,3,4,5,6,7,8,9}-*.patch; do
for p in ../000*-*.patch; do
echo "---> patching source with $p <---"
git apply --whitespace=fix "$p"
done
