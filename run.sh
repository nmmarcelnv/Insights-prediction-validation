#!/bin/bash
#
# This absh script executes the prediction_validation.py code
#
codepy=./src/prediction_validation.py  	#specifies the path to python script
input1=./input/window.txt		#path to the file window.txt
input2=./input/actual.txt		#path to file actual.txt
input3=./input/predicted.txt		#path to file predicted.txt
input4=./output/comparison.txt		#path to file comparison.txt

python ${codepy} ${input1} ${input2} ${input3} ${input4}
