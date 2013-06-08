#!/bin/env python
#purpose: print a sentence in a box 
#author: hz_linyu@20130506

sentence = raw_input("Sentense: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
box_margin = (box_width - text_width) // 2 - 1

print
print " " * left_margin + "+" + "-" * (box_width - 2) + "+"
print " " * left_margin + "|" + " " * (box_width - 2) + "|"
print " " * left_margin + "|" + " " * box_margin + sentence + " " * box_margin + "|"
print " " * left_margin + "|" + " " * (box_width - 2) + "|"
print " " * left_margin + "+" + "-" * (box_width - 2) + "+"
print 


