from sys import maxint
from QuadrantClass import Quadrant
from UtilClass import Util
from Models.StarClass import Star
from Models.StarBaseClass import StarBase
from Models.KlingonClass import Klingon
from Models.EnterpriseClass import Enterprise
import math
from Models.PositionClass import Position

class Map(object):
	
	NO_STARS = 250
	MAX_STARS_IN_QUADRANT = 7
	MAX_KLINGONS_IN_QUADRANT = 3
	
	QuadrantNames = [
		['ANTARES I', 'ANTARES II', 'ANTARES III', 'ANTARES IV', 'SIRIUS I', 'SIRIUS II', 'SIRIUS III', 'SIRIUS IV'],
		['RIGEL I', 'RIGEL II', 'RIGEL III', 'RIGEL IV', 'DENEB I', 'DENEB II', 'DENEB III', 'DENEB IV'],
		['PROCYON I', 'PROCYON II', 'PROCYON III', 'PROCYON IV', 'CAPELLA I', 'CAPELLA II', 'CAPELLA III', 'CAPELLA IV'],
		['VEGA I', 'VEGA II', 'VEGA III', 'VEGA IV', 'BETELGEUSE I', 'BETELGEUSE II', 'BETELGEUSE III', 'BETELGEUSE IV'],
		['CANOPUS I', 'CANOPUS II', 'CANOPUS III', 'CANOPUS IV', 'ALDEBARAN I', 'ALDEBARAN II', 'ALDEBARAN III', 'ALDEBARAN IV'],
		['ALTAIR I', 'ALTAIR II', 'ALTAIR III', 'ALTAIR IV', 'REGULUS I', 'REGULUS II', 'REGULUS III', 'REGULUS IV'],
		['SAGITTARIUS I', 'SAGITTARIUS II', 'SAGITTARIUS III', 'SAGITTARIUS IV', 'ARCTURUS I', 'ARCTURUS II', 'ARCTURUS III', 'ARCTURUS IV'],
		['POLLUX I', 'POLLUX II', 'POLLUX III', 'POLLUX IV', 'SPICA I', 'SPICA II', 'SPICA III', 'SPICA IV']
	]
	
	def __init__(self):
		''' Initialize map '''
		
		self.Quadrants = [[Quadrant() for j in range(8)] for i in range(8)]
		
		for i in range(8):
			for j in range(8):
				self.Quadrants[i][j].Name = self.QuadrantNames[i][j]
				
		self.placeStars()
				
	def placeStars(self):
		''' Populate quadrants with stars '''

		stars = self.NO_STARS
		
		while stars > 0:
			pos = Util.getRandomPosition()
			qx = pos.QuadrantX
			qy = pos.QuadrantY
			sx = pos.SectorX
			sy = pos.SectorY
			
			if self.Quadrants[qx][qy].NoOfStars <= self.MAX_STARS_IN_QUADRANT and self.Quadrants[qx][qy].Sectors[sx][sy] == ' ':
				self.Quadrants[qx][qy].Sectors[sx][sy] = Star.SYMBOL
				self.Quadrants[qx][qy].Stars.append(Star(maxint, False, pos))
				stars -= 1

	def placeKlingons(self, klingons):
		''' Place the enemy ships on the map '''
		
		while klingons > 0:
			pos = Util.getRandomPosition()
			qx = pos.QuadrantX
			qy = pos.QuadrantY
			sx = pos.SectorX
			sy = pos.SectorY
			
			if self.Quadrants[qx][qy].NoOfKlingons <= self.MAX_KLINGONS_IN_QUADRANT and self.Quadrants[qx][qy].Sectors[sx][sy] == ' ':
				self.Quadrants[qx][qy].Sectors[sx][sy] = Klingon.SYMBOL
				self.Quadrants[qx][qy].Klingons.append(Klingon(pos))
				klingons -= 1

	def placeStarBases(self, starbases):
		''' Place starbases on the map '''
		
		while starbases > 0:
			pos = Util.getRandomPosition()
			qx = pos.QuadrantX
			qy = pos.QuadrantY
			sx = pos.SectorX
			sy = pos.SectorY
			
			if self.Quadrants[qx][qy].NoOfStarBases == 0 and self.Quadrants[qx][qy].Sectors[sx][sy] == ' ':
				self.Quadrants[qx][qy].Sectors[sx][sy] = StarBase.SYMBOL
				self.Quadrants[qx][qy].StarBases.append(StarBase(pos))
				starbases -= 1

	def placeEnterprise(self):
		'''Place The Enterprise on the map and returns it's position'''
		
		while True:
			pos = Util.getRandomPosition()
			qx = pos.QuadrantX
			qy = pos.QuadrantY
			sx = pos.SectorX
			sy = pos.SectorY
			
			if self.Quadrants[qx][qy].Sectors[sx][sy] == ' ':
				self.Quadrants[qx][qy].Sectors[sx][sy] = Enterprise.SYMBOL
				self.Quadrants[qx][qy].IsEnterprise = True
				break
				
		return pos
	
	def moveEnterprise(self, course, warp, currentPos):
		''' Try to move the Enterprise to a new position. If the way is blocked the method will return the position near the obstacle '''
		
		x0 = currentPos.AbsoluteX
		y0 = currentPos.AbsoluteY
		angle = (1 - course) * 0.785
		
		x = x0 + int(8 * warp * math.sin(angle))
		y = y0 + int(8 * warp * math.cos(angle))
		
		(canMove, newPos) = self.checkPath(course, currentPos, Position(ax = x,ay = y))
		if canMove:
			self.Quadrants[currentPos.QuadrantX][currentPos.QuadrantY].IsEnterprise = False
			self.Quadrants[currentPos.QuadrantX][currentPos.QuadrantY].Sectors[currentPos.SectorX][currentPos.SectorY] = ' '
			self.Quadrants[newPos.QuadrantX][newPos.QuadrantY].IsEnterprise = True
			self.Quadrants[newPos.QuadrantX][newPos.QuadrantY].Sectors[newPos.SectorX][newPos.SectorY] = 'E'
			
		return (canMove, newPos)
		
	def checkPath(self, course, pos0, pos):
		''' Verifies if the path between the two positions is blocked. 
			Only the current quadrant is verified because afterwards it enters in hyperspace
		'''
		
		qx0 = pos0.QuadrantX
		qy0 = pos0.QuadrantY
		
		qx = pos.QuadrantX
		qy = pos.QuadrantY
		
		x = pos0.SectorX
		y = pos0.SectorY
		
		'the destionation is blocked'
		if self.Quadrants[qx][qy].Sectors[pos.SectorX][pos.SectorY] != ' ':
			return False, pos0
		
		while(True):
			(x,y) = self.moveCourseOnePosition(course, (x,y))
			
			if y == 8 or y == -1 or x == 8 or x == -1: break
			
			if qx0 == qx and qy0 == qy and pos.SectorX == x and pos.SectorY == y: break;
			
			if self.Quadrants[qx0][qy0].Sectors[x][y] != ' ':
				return False, Position(qx0, qy0, x, y)
				
		return True, pos
	
	def moveCourseOnePosition(self, course, (x0, y0)):
		'''Returns the next position in function of the course '''
		
		if course == 1:
				y0 += 1
		elif course == 2:
				y0 += 1
				x0 -= 1
		elif course == 3:
				x0 -= 1
		elif course == 4:
				y0 -= 1
				x0 -= 1
		elif course == 5:
				y0 -= 1
		elif course == 6:
				y0 -= 1
				x0 += 1
		elif course == 7:
				x0 += 1
		elif course == 8:
				y0 += 1
				x0 += 1
		
		return (x0, y0)
	
	def getInformations(self, x, y):
		''' Returns informations about the given quadrant '''
		
		if x < 0 or x > 7 :
			return ' 000 '
			
		if y < 0 or y > 7:
			return ' 000 '
			
		return self.Quadrants[x][y].GetInformations()
	
	def getBlockedStarbase(self):
		'''Returns the position of the starbase blocked by klingon ships'''
		
		for qx in range(0, 8):
			for qy in  range(0, 8):
				if self.Quadrants[qx][qy].IsEnterprise == False \
					and self.Quadrants[qx][qy].NoOfKlingons > 0 \
					and self.Quadrants[qx][qy].NoOfStarBases > 0:
					return self.Quadrants[qx][qy].StarBases[0].Position
		
		return None
					

