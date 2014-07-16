#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bokeh_test.py
#  
#  Copyright 2014 Yang <yang@Leo-FamilyGuy>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#~ # testing bokeh
import numpy as np
# # use this line to download sample data.
# from bokeh import sampledata; sampledata.download();
from bokeh.sampledata.stocks import AAPL, FB, GOOG, IBM, MSFT
from bokeh.plotting import *

def main():

	for i, j in zip(AAPL['date'], AAPL['adj_close']):
		print (i, j)
		
	output_file("stocks.html", title="stocks.py example")
	
	hold()
	
	figure(x_axis_type = "datetime", tools="pan,wheel_zoom,box_zoom,reset,previewsave")
	
	line(np.array(AAPL['date'], 'M64'), AAPL['adj_close'], color='#A6CEE3', legend='AAPL')
	line(np.array(FB['date'], 'M64'), FB['adj_close'], color='#1F78B4', legend='FB')
	line(np.array(GOOG['date'], 'M64'), GOOG['adj_close'], color='#B2DF8A', legend='GOOG')
	line(np.array(IBM['date'], 'M64'), IBM['adj_close'], color='#33A02C', legend='IBM')
	line(np.array(MSFT['date'], 'M64'), MSFT['adj_close'], color='#FB9A99', legend='MSFT')
	
	curplot().title = "Stock Closing Prices"
	grid().grid_line_alpha=0.3
	
	aapl = np.array(AAPL['adj_close'])
	aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)
	
	window_size = 30
	window = np.ones(window_size)/float(window_size)
	aapl_avg = np.convolve(aapl, window, 'same')
	
	figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,previewsave")
	
	scatter(aapl_dates, aapl, size=4, color='#A6CEE3', legend='close')
	line(aapl_dates, aapl_avg, color='red', legend='avg')
	
	curplot().title = "AAPL One-Month Average"
	grid().grid_line_alpha=0.3
	
	show()
	return 0

if __name__ == '__main__':
	main()

