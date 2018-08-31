#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script generate mass spectra plots
# from compounds ms peaks data (stored in csv files)


# change 'path_to_dir' by your own location of csv files


# import pandas library
import glob, os
import os.path
import pandas as pd
import matplotlib.pyplot as plt


def plot_mz(path_to_dir):
	# change to the directory containing csv files 
	os.chdir(path_to_dir)
	files = glob.glob('*.csv')
	print(files)
	for f in files:
		df = pd.read_csv(f)
		# get base peak
		base_peak=df.query('A == 100')+1
		fig=plt.figure()
		ax1=fig.add_subplot(111)
		xval=df['m_z']
		yval=df['A']
		title_fig=str(os.path.splitext(f)[0])
		
		ax1.bar(xval,yval,width=0.05) #first data (x,y,color,edgecolor) 
		ax1.set_xlabel(r"$m/z$") 
		ax1.set_ylabel(r"$Intensity\,[\%]$") 
		ax1.set_title(title_fig.title()) #some title labeling
		
		# Save the plot as pdf
		plt.savefig('chart of '+title_fig+'.pdf') #some more parameters
		
		
		

plot_mz(your_path)
print "Done"
