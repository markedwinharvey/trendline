#!/usr/bin/env python
'''trendline.py
Linear regression/gradient descent
Learning rate alpha is determined automatically. 
Takes a single 2D numpy array as input and returns m,b,r2 
(slope,intercept,r-squared) values as tuple.
  
Usage:
	import numpy as np
	import trendline as tl
	
	data = np.array([x_list,y_list])
	m,b,r2 = tl.get_trendline(data,prec=.00001)
'''

import numpy as np
import time
start_time = time.time()

#-------start functions---------#
def th0_sum(th0,th1,x,y):		#gradient sum of partial derivatives wrt th0
	return sum([th0+th1*x[i]-y[i] for i in range(len(x))])
	
def th1_sum(th0,th1,x,y):		#gradient sum of partial derivatives wrt th1
	return sum([( th0+th1*x[i]-y[i] )*x[i] for i in range(len(x))])
	
def J_sum(th0,th1,x,y):			#J(cost) sum for squared residuals
	return sum([ (th0+th1*x[i]-y[i])**2 for i in range(len(x))])
	
def compute_trendline(alpha,th0,th1,prec,x,y):
	th0_tmp=0.
	num_points=len(x)
	J_new=0.;J_old=0.
	grad_iter = 1
	
	while 1:
		th0_tmp=th0-alpha/num_points*th0_sum(th0,th1,x,y)
		th1=th1-alpha/num_points*th1_sum(th0,th1,x,y)
		th0=th0_tmp
		J_old=J_new
		J_new=1./(2*num_points)*J_sum(th0,th1,x,y)
		if J_new > (J_old+1000000):
			return 'high'
		diff=J_new-J_old
		grad_iter+=1
		if abs(diff) < prec:				#cost minimized
			print 'gradient iterations:',grad_iter
			return th0,th1,grad_iter

#------get_trendline------#		
def get_trendline(xy_array,**kwargs):		#xy_array is np.array

	prec = kwargs['prec'] if kwargs['prec'] else .0001
	
	x = xy_array.T[:,0]						#take transpose
	y = xy_array.T[:,1]
	
		#-----get starting parameters-----#					
	th1 = 1.*(y[-1] - y[0])/(x[-1]-x[0])	# m=(y2-y1)/(x2-x1)
	th0 = y[0]-th1*x[0]						# b = y-mx
	alpha=.1
	alpha_iter=1	#track total iterations to finding alpha that promotes J convergence
	
	while 1:		#auto-generate alpha value
		result=compute_trendline(alpha,th0,th1,prec,x,y)	
		if result == 'high':
			alpha=alpha*9./10				#no convergence in J; reduce alpha
			alpha_iter+=1
		else:
			th0=int(100*result[0])/100.
			th1=int(100*result[1])/100.
			grad_iter=result[2]
			break
	elapsed_time = 1000./(time.time()-start_time),'s'
	
	#--calculate r-squared value
	m=th1; b=th0
	y_mean = 1./len(y)*sum(y)
	SStot = sum( (y - y_mean)**2 )
	SSres = sum( (y - (m*x+b))**2 )
	r2 = 1- SSres/SStot
	
	return m,b,r2

def main():
	pass
	
if __name__ == '__main__':
	main()