#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ggplot_test.py
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

import numpy as np
import pandas as pd
from ggplot import *

def main():
		
	# testing ggplot
	#~ print ggplot(mtcars, aes('mpg', 'qsec')) + \
	  #~ geom_point(colour='steelblue') + \
	  #~ scale_x_continuous(breaks=[10,20,30],  \
	                     #~ labels=["horrible", "ok", "awesome"])

	print type(mtcars)
	
	randn = np.random.randn
	s = pd.Series(randn(100))
	
	d = {'one' : pd.Series(randn(100)), 'two' : pd.Series(randn(100)), 'three' : pd.Series(randn(100)), 'four' : pd.Series(randn(100))}
	df = pd.DataFrame(d)
	melt_df = pd.melt(df)
	
	# scatter plot 
	p_scatter =  ggplot(df, aes('one', 'two')) + \
		geom_point(colour='steelblue')
	
	# Histogram plot
	#~ p_hist = ggplot(aes('variable', 'value', fill = 'variable'), \
		#~ data=melt_df) + geom_histogram() + facet_wrap('variable')
		
		
	p = ggplot(melt_df, aes('value')) +  geom_density() + \
		facet_grid("variable")

#~ meat_lng = pd.melt(meat, id_vars=['date'])
#~ 
#~ p = ggplot(aes(x='date', y='value'), data=meat_lng)
#~ p + geom_point() + \
    #~ stat_smooth(colour="red") + \
    #~ facet_wrap("variable")
#~ 
#~ p + geom_hist() + facet_wrap("color")
#~ 
#~ p = ggplot(diamonds, aes(x='price'))
#~ p + geom_density() + \
    #~ facet_grid("cut", "clarity")
#~ 
#~ p = ggplot(diamonds, aes(x='carat', y='price'))
#~ p + geom_point(alpha=0.25) + \
    #~ facet_grid("cut", "clarity")


		
	print p
	
	return 0

if __name__ == '__main__':
	main()

