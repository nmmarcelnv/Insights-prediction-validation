#!/bin/bash
#
# This absh script executes the prediction_validation.py code
#

test_id=$1    # e.g pass 2 to run test_2 
codepy=../src/prediction_validation.py  	#specifies the path to python script
input1=./tests/test_${test_id}/input/window.txt		#path to the file window.txt
input2=./tests/test_${test_id}/input/actual.txt		#path to file actual.txt
input3=./tests/test_${test_id}/input/predicted.txt		#path to file predicted.txt
input4=./tests/test_${test_id}/output/comparison.txt		#path to file comparison.txt

python ${codepy} ${input1} ${input2} ${input3} ${input4}
