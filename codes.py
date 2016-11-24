#!/usr/bin/python

###############################################################################
# File: outlet.py
# Author: Mark Nguyen 
# Last modified 23-Nov-2016
# Build: Python 2.7.9 
# Description: Populates custom RF frequencies to activate my RF outlets.
#  Edit the values in the codes array to relect the RF frequencies of your outlets.
#  The codes array is setup as [on-code1, off-code1],[on-code2,off-code2],
#  [on-code3,off-code3]...
#  The number of outlets you have should replace the "10" in line 29
#  This script calls the codesend command by Tim Leland.
# Usage: outlet <outlet number> <on|off>
###############################################################################

import os
import argparse

parser = argparse.ArgumentParser(description='This activates an outlet.')
parser.add_argument('-o','--outlet', type=int, help='Outlet number',required=True)
parser.add_argument('-p','--power', choices=['on', 'off'], help='on|off', required=True)
args = parser.parse_args()


codes=[[4543795,4543804],[4543939,4543948],[4544259,4544268],[4545795,4545804],[4551939,4551948],[524
8307,5248316],[5248451,5248460],[5248771,5248780],[5250307,5250316],[5256451,5256460]]

if 1 <= args.outlet <= 10:
 if args.power == "on":
  print codes[args.outlet-1][0]
  os.system("sudo /home/pi/rfoutlet/codesend %s -l 180 -p 0" % codes[args.outlet-1][0])

 else:
  print codes[args.outlet-1][1]
  os.system("sudo /home/pi/rfoutlet/codesend %s -l 180 -p 0" % codes[args.outlet-1][1])
else:
 print ("Please choose a valid outlet number")
