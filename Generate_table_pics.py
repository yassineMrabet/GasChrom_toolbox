#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob, os
from os.path import splitext
os.chdir("/home/yassine/Desktop/Scripts/")
import pandas as pd



def print_mzlist(fx):
	# Read peaks table and sort according to *m/z* 
	f = pd.read_csv(fx)
	compname=str(os.path.splitext(fx)[0])
	df = pd.DataFrame(f)
	dfs = df.sort('m_z',ascending=False)
	
	
	# Strip peaks with *A* < 1
	dfss = dfs.query('A > 1')
	
	# Select base peak with A = 100% and add 1 to m/z because the ionization mode is positive
	base_peak=dfs.query('A == 100')+1
	
	# Create the list of peaks with base_peak as first element
	peaks_list = ""
	bps = str("%s MS1[%0.f]: " %(compname.title(), base_peak['m_z']))
	# Append the Compound name *compname* and *base_peak*
	peaks_list = peaks_list + bps 
	# Append peaks list
	for index, row in dfss.iterrows():
		peaks_list += str ("%.0f (%0.f), " % (row['m_z'], row['A']))
	peaks_list = peaks_list[:-2] + '.'
	return (peaks_list)

# Open the text file to store results
text_file = open("Results.txt", "w")

# Reading csv files and printing the results  
for filename in glob.glob("*.csv"):
	print "Processing the file", filename
	pk= print_mzlist(filename)
	text_file.write("{}\n".format(pk))
	print "Wrinting results to:", text_file.name
text_file.close()
print "Done"
