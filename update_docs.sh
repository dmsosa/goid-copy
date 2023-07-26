#!/usr/bin/env bash

# build the docs
cd docs
make clean
make html
cd ..

#commit and push
git add .
git commit -m "Building and pushing docs"
git push origin main

#switch branches and pull the data we want
git checkout gh-pages
rm -rf .
touch .nojekyll
git chekout main docs/build/html
mv .docs/build/html/* ./
rm -rf docs
git add .
git commit -m "Publishing updated docs..."
git push origin gh-pages

#switch back
git checkout main
