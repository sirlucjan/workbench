#!/bin/bash
srcdir=some-path
patchdir=some-path
cd $srcdir
echo "---> patching source with stable-review <---"
git apply --whitespace=fix $patchdir/*
