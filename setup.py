#!/usr/bin/env python
from setuptools import setup
def main():
	setup(
		name='trendline',
		version=0.1,
		description='Input: 2D numpy array; Output: (m,b,r2) tuple',
		packages=['trendline'],
		author='meh'
	)
	
	pass
if __name__ == '__main__':
	main()