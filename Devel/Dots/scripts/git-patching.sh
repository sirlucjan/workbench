#!/bin/bash
srcdir=some-path
cd $srcdir
for p in ../0*-*.patch; do
echo "---> patching source with $p <---"
git apply --whitespace=fix "$p"
done
