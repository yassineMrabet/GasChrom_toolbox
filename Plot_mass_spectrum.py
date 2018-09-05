#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Author: Y M'RABET
 Description: This script generate mass spectra plots
 from compounds ms peaks data (stored in csv files)
 License: GPL

'''

# import os, pandas and matplot libraries
import glob, os
import os.path
import pandas as pd
import matplotlib.pyplot as plt


# Get base peak 
'''

Base peak is the most intense (tallest) peak in a mass spectrum.
Source: http://www.chem.ucla.edu/~harding/IGOC/B/base_peak.html

'''
def find_base_peak(df):
	
	base_peak = df.query('A == 100')
	m_z, A = base_peak['m_z'].item(), base_peak['A'].item()
	return (m_z,A)

# Import csv files, plot the mass spectra and export them to pdf
''' 
	csv file should be formatted as follow :
	
	m_z,A
    27.0,3.5
    38.0,1.2
	...
	
'''

def plot_mz(path_to_dir): # change 'path_to_dir' by your own location of csv files
	# Change to the directory containing csv files 
	os.chdir(path_to_dir)
	
	# Get all csv files in this folder
	files = glob.glob('*.csv')
	
	# Print the number of files found 
	print('%d files found' % len(files)+" in "+path_to_dir)
				
	# Apply to each csv file in the directory 
	for f in files:
		df = pd.read_csv(f) # read the csv files
				
		# get m/z and Intensity of the base peak
		Mx, My = find_base_peak(df)
				
		# Prepare plotting devise	
		fig=plt.figure(figsize=(11.69, 8.27), dpi=100) # figsize for landscape A4
		ax1=fig.add_subplot(111)
		
		# Set fonts typeface
		plt.rcParams['font.family'] = 'Liberation Sans'
		#plt.rcParams['mathtext.default'] = 'rm'
		#plt.rcParams['mathtext.fontset'] = 'stix' 
		
		# Get the values		
		xval=df['m_z']
		yval=df['A']
		title_fig=str(os.path.splitext(f)[0])
		
		# Plotting		
		ax1.bar(xval,yval,width=0.1,color='#00008B') 
		ax1.set_xlabel(r"$m/z$") 
		ax1.set_ylabel(r"Relative Intensity (%)") 
		ax1.set_title(title_fig.title(),size = 14) #title labeling
		
		# Highlight the base peak
		offset = (105.0 - My)/2
		ax1.annotate('%d' % round(Mx,2), xy = (Mx,My), xytext = (Mx,My+offset), fontsize=12, ha='center', va='center', color = '#1A1A1A')
		ax1.plot(Mx,0, marker="^", markersize=10, color='#DC143C')
		
		# Save the plot as pdf
		print ('Exporting '+title_fig+' spectrum')
		plt.savefig('chart of '+title_fig+'.pdf',) #some more parameters in **kwargs
	print "Done"

