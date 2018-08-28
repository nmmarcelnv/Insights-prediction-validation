This readme describes usage of my solution for the InsightDataScience prediction-validation challenge.

Programming Language :
----------------------
Python 3


Libraries: 
----------
1. Pandas
2. Numpy


Approach:
--------
I used the Python library Pandas to implement my solution.
First parse the two inputs (actual and predicted stocks) into pandas DataFrames.
I also created a unique key for each entrie by combining the time the entry was
recorded and the stock ID. This way, it becomes easy to merge actual and predicted


Then I have a function which scans through the actual dataFrame
and performs a rolling average of errors with the predicted values (on stock price).

Running the code:
-----------------
Instructions on how to run the code can be found in the run.sh file.
For a simple test, simply perform the following on the command line:

bash run.sh


Comments:
---------

1. I was unable to test my test my solution on the website http://ec2-18-210-131-67.compute-1.amazonaws.com/test-my-repo-link
   apprently Pandas is not install there.

	Cloning repo (https://github.com/nmmarcelnv/Insights-prediction-validation) succeeded

	========

	RUNNING: test_1

	(stderr): Traceback (most recent call last):
	(stderr): File "./src/prediction_validation.py", line 1, in <module>
	(stderr): import pandas as pd
	(stderr): ImportError: No module named pandas
	-------------
	TEST RESULTS:

	Started process: 05:03:12
	Ended process: 05:03:12

	* Failed! (Applicant did not create output file.)
	Executed key tests: 0 out of 1 passed.

3. I successfully tested my Python code on a few test data I made, in addition to the small test example on the Github page. 
   However, the code failed to past the test when I ran the run_test.sh provided.

   A vimdiff of my comparison.txt file and the comparison.txt file provided by Insights shows only floating point 
   discrepancies between the two files in some entries. For example, my code gives a result of 0.04 for window 54-57 
   but the answer given in the test_1/comparison.txt is 0.03 for window 54-57. 

   For this reason, I decided to manually extract window 54-57 from both actual.txt and predicted.txt and used a bash script to find the error. 
   The answer agrees with my python code (0.04). 

   I was wondering if it's possible that there is a mistake in the results provided in test_1/comparison.txt. 

   Attached is the bash script I used to test windon 54-57. The script can be executed in a directory (say check) located in the same level as insight_testsuite. 
   (simply do bash check.sh)

Thank you,

Valery Nguemaha 
