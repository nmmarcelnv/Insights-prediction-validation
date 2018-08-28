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
First parse the two inputs (actual and predicted stocks) into pandas DataFrames.
I also created a unique key for each entrie by combining the time the entry was
recorded and the stock ID. This way, it becomes easy to merge actual and predicted


Then I have a function which scans through the actual dataFrame
and performs a rolling average of errors with the predicted values (on stock price).

