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

#test distribution on map
for i in range(17):
	ax = randint(0, 64)
	ay = randint(0, 64)
	
	qx = ax / 8
	sx = ax % 8
	
	qy = ay / 8
	sy = ay % 8
	
	p = Position(qx, qy, sx, sy)
	p.Print()

#test creation map
m = Map()
print (m.Quadrants[1][1]).Sectors[6][6]
