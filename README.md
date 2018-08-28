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

