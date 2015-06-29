#!/usr/bin/env python
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import wx


class Thevenin1(gr.sync_block):
    """
    docstring for block Thevenin1
    """
    def __init__(self, s1, s2):
	self.s1 = s1
	self.s2 = s2
        gr.sync_block.__init__(self,
            name="1_Thevenin",
            in_sig=[numpy.float32, numpy.float32, numpy.float32, numpy.float32, numpy.float32, numpy.float32],
            out_sig=[numpy.float32, numpy.float32])


    def set_switch(self, s1, s2):
    	self.s1 = s1
    	self.s2 = s2
    def work(self, input_items, output_items):
        in0 = input_items[0]
	in1 = input_items[1]
	in2 = input_items[2]
	in3 = input_items[3]
	in4 = input_items[4]
	in5 = input_items[5]
	#print input_items
        out0 = output_items[0]
	out1 = output_items[1]
        # <+signal processing here+>
	if (self.s1==1 and self.s2==2):
        	out0[:] = in0 + in1
		out1[:] = in2 + in3
		print('You are in condition 1.')
		#print(out0[:])
	elif (self.s1==1 and self.s2==3):
		out0[:] = in0 * in1
		out1[:] = in2 * in3
		print('You are in condition 2.')
		#print(out0[:])
	elif (self.s1==2 and self.s2==1):
		out0[:] = in0 / in1
		out1[:] = in2 / in3
		print('You are in condition 3.')
		#print(out0[:])
	else:
		print('Choose proper option.')
        
	return len(output_items[0])
