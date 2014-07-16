#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  d3plot.py
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
import networkx as nx 

def main():
   
	G=nx.Graph()
	G.add_edge(1,2)
	G.add_edge(1,3)
	G.add_edge(3,2)
	G.add_edge(3,4)
	G.add_edge(4,2)
	 
	with d3py.NetworkXFigure(G, name="graph",width=200, height=200) as p:
		p += d3py.ForceLayout()
		p.css['.node'] = {'fill': 'blue', 'stroke': 'magenta'}
		#~ p.save_to_files()
		p.show() 
	return 0

if __name__ == '__main__':
	main()

