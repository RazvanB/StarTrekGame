from Classes.UtilClass import *
from random import randint
from Classes.PositionClass import Position
from Classes.MapClass import Map
from Classes.QuadrantClass import Quadrant

#test status method
Util.displayStatusCommand(1,2,3,4,5,6,7,8,9,10)
print ""

#test navigation command
Util.displayNavigationCommand(NavParam.WARP_FACTOR)
print ""
Util.displayNavigationCommand(NavParam.COURSE)

#test record command
l = [[' 000 ',' 001 ',' 010 ',' 011 ',' 100 ','(101)',' 110 ',' 111 '],
	[' 000 ',' 001 ',' 010 ',' 011 ',' 100 ','(101)',' 110 ',' 111 '],
	[' 000 ',' 001 ',' 010 ',' 011 ',' 100 ','(101)',' 110 ',' 111 '],
	[' 000 ',' 001 ',' 010 ',' 011 ',' 100 ','(101)',' 110 ',' 111 '],
	[' 000 ',' 001 ',' 010 ',' 011 ',' 100 ','(101)',' 110 ',' 111 '],
	[' 000 ',' 001 ',' 010 ',' 011 ',' 100 ','(101)',' 110 ',' 111 '],
	[' 000 ',' 001 ',' 010 ',' 011 ',' 100 ','(101)',' 110 ',' 111 '],
	[' 000 ',' 001 ',' 010 ',' 011 ',' 100 ','(101)',' 110 ',' 111 '],
]

Util.displayRecordCommand(l)
print ""

#test creation map
m = Map()
print 'Q[1,1] Name = %r' %(m.Quadrants[1][1].Name)

#test print sectors
m.Quadrants[1][1].PrintSectors()
