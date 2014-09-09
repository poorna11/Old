# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 12:43:46 2014

@author: Poorna
"""
import cmd
import csv

color_range = [0, .14, .20, .25, .35, .45, .55, 1]
rsr=[]
f = open("E:/Leontis/2AVY-RSR.csv", "rb")
for i,row in enumerate(csv.reader(f)):
        if i==0:
            continue
        rsr.append([row[0],float(row[1])])

f.close()

#cmd.set bg_color white
        
for i,row in rsr:
     j=i.split("_")
     if  color_range[0]< row <= color_range[1]:
        cmd.color("marine", "2AVY-16S and resi "+ j[4])
     elif color_range[1] < row <= color_range[2]:
        cmd.color ("cyan","2AVY-16S and resi "+ j[4])
     elif color_range[2] < row <= color_range[3]:
        cmd.color ("green","2AVY-16S and resi "+ j[4])
     elif color_range[3] < row <= color_range[4]:
        cmd.color ("yellow","2AVY-16S and resi "+ j[4])
     elif color_range[4] < row <= color_range[5]:
        cmd.color ("orange","2AVY-16S and resi "+ j[4])
     elif color_range[5] < row <= color_range[6]:
        cmd.color ("red","2AVY-16S and resi "+ j[4])
     elif color_range[6] < row <= 1:
        cmd.color ("magenta","2AVY-16S and resi "+ j[4])

### cut below here and paste into script ###
set_view (\
    -0.651273787,    0.669810474,    0.356645435,\
     0.400719136,    0.702678859,   -0.587933362,\
    -0.644411325,   -0.239990935,   -0.726043105,\
     0.000000000,    0.000000000, -737.353515625,\
    90.952728271,    1.948154449,  -12.275173187,\
   611.372558594,  863.334594727,  -20.000000000 )
### cut above here and paste into script ###

                

         #cmd.color ("yellow", "resi j[4]")
    
