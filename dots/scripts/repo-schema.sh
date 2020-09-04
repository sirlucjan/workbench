#!/bin/bash
REPO=/some/path
rm -f $REPO/repo-name.*
repo-add -s $REPO/repo-name.db.tar.zst $REPO/*.pkg.tar.{xz,zst}
