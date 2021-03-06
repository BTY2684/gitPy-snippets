#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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
import d3py
import pandas
import numpy as np
import matplotlib.pyplot as plt

import classes as TSs

def main():
	obj1 = TSs.Bond()
	obj2 = TSs.Stock()
	
	for i in range(10):
		obj1.data_add(obj1._datasize, i + 1)
		obj2.data_add(obj2._datasize, i - 10)
	
	print (obj1._datadict)
	print (obj2._datadict)
	
	plt.bar(obj1._datadict.values(), obj2._datadict.values(), align='center')
	plt.xticks(range(len(obj1._datadict)), obj1._datadict.keys())

	plt.show()
	
	return 0

if __name__ == '__main__':
	main()

