<h4>trendline</h4>

<h5><b>trendline.py</b></h5>

Linear regression/gradient descent<br>
Learning rate alpha auto-generated<br> 
<b>Input</b>: 2D numpy array<br>
<b>Output</b>: m,b,r2		&nbsp;&nbsp;    (slope, intercept, r-squared)	tuple<br>

<h6>Installation:</h6>

	python setup.py install
	
	
<h6>Usage:</h6>
	
	import numpy as np
	import trendline as tl
	
	x_vals = [9,3,7,4,2,1]
	y_vals = [4,8,1,6,2,9]
	data = np.array([x_vals , y_vals])
	m,b,r2 = tl.get_trendline(data) 	
		# (m,b,r2 = slope,intercept,r-squared)
		# optional kwarg 'prec' is max. delta-cost (lower boundary); 
		# e.g., m,b,r2 = tl.get_trendline(data,prec=.01); default is prec = .0001
	
	#Plotting data with trendline:
	
	import matplotlib as mpl
	mpl.use('TkAgg')
	import matplotlib.pyplot as plt
	
	plt.scatter(x_vals,y_vals)
	
	x = np.array(range(min(x_vals), max(x_vals)+1))
	plt.plot(x,m*x+b)
	
	plt.show()

