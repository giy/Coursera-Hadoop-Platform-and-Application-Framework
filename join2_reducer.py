#!/usr/bin/env python

# ---------------------------------------------------------------
#This reducer code will input a line of text and 
#    output <word, total-count>
# ---------------------------------------------------------------
import sys

last_key      = None              #initialize these variables
running_total = 0
abc_seen = False

# -----------------------------------
# Loop thru file
#  --------------------------------
for input_line in sys.stdin:
    input_line = input_line.strip()

    this_key, value = input_line.split("\t", 1)  #the Hadoop default is tab separates key value
    if value.isdigit():
        value = int(value)
    else:
        abc_seen = True
 
    if last_key == this_key and not abc_seen:
        running_total += value
    else:
        if last_key and abc_seen==True:
            print( "{0}\t{1}".format(last_key, running_total) )
        running_total = value
        abc_seen = False
        last_key = this_key

if last_key == this_key:
    print( "{0}\t{1}".format(last_key, running_total)) 
