#!/bin/sh

echo "\nBuild and push preprocess component"
./data_preprocess/build_image.sh

echo "\nBuild and push train component"
./model_training/build_image.sh

echo "\nBuild and push test component"
./model_testing/build_image.sh