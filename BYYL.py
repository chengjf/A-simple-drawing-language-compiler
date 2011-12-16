from BYYLlex import startlex
from BYYLyacc import startyacc
##from BYYLyacc import startdraw
##from BYYLyacc import startdraw1

filename=raw_input('Please input your filename:\n')
startlex(filename)
startyacc(filename)
##startdraw()
print "Please inpur any key to quit!\n"
raw_input()
