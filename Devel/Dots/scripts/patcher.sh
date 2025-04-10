#!/bin/bash
srcdir=some-path
patchdir=some-path
cd $srcdir
echo "---> patching source with stable-review <---"
patch -Np1 -i $patchdir/*
