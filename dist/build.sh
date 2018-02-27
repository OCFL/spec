#!/usr/bin/env bash

echo "Building gitbook site"
gitbook build . dist
echo "Committing changes to the distribution folder"
git add dist && git commit -m "Committing changes for distribution"
echo "Deploying changes to the remote gh-pages branch"
git subtree push --prefix dist origin gh-pages