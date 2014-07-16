#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  classes.py
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

class TimeSeries:
	_datasize = 0

	def __init__(self):
		self._datadict = dict()

	def data_add(self, tenor, val):
		self._datadict[tenor] = val
		self.increment()

	def increment(self):
		self._datasize += 1

class Bond(TimeSeries):
	def __init__(self):
		TimeSeries.__init__(self)


class Stock(TimeSeries):
	def __init__(self):
		TimeSeries.__init__(self)
