#!/usr/bin/bash

#This script is a manual check for the results (test_/output/comparison.txt) provided by Insights.
#The test is performed for window 54-57. 
#The results provided has an answer of 0.03
#The current script gives an answer of 0.04

sed 's/|/ /g' ../tests/test_1/input/actual.txt >actual.txt
sed 's/|/ /g' ../tests/test_1/input/predicted.txt >predicted.txt


start_time=54
stop_time=57
#get data for widow 54-57 only
awk '($1>='${start_time}') && ($1<='${stop_time}')' actual.txt | sort -t ' ' -k1,1n -k2,2 >atest
awk '($1>='${start_time}') && ($1<='${stop_time}')' predicted.txt |sort -t ' ' -k1,1n -k2,2  >ptest


#create a unique key to ease filtering
awk '{printf("%s%s %d %s %f\n",$1,$2, $1, $2, $3)}' atest >key_atest
awk '{printf("%s%s %d %s %f\n",$1,$2, $1, $2, $3)}' ptest >key_ptest


#find places where actual and predicted overlap and compute errors
cat /dev/null >merged
while read -r aline; do

	echo ${aline} >tmp

	key=`awk '{print $1}' tmp`

	grep -w "${key}" key_atest > tmp2

	paste tmp tmp2 >>merged


done <key_ptest


#compute error
awk '{s+= sqrt(($4-$8)^2)}END{printf("%d|%d|%.2f\n",54,57, s/NR)}' merged >comparison.txt

rm tmp tmp2 key_atest key_ptest atest ptest
