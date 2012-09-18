from sys import maxint
from random import randint
from QuadrantClass import Quadrant
from UtilClass import Util
from StarClass import Star
from StarBaseClass import StarBase
from KlingonClass import Klingon
from EnterpriseClass import Enterprise

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
				
	def getInformations(self, x, y):
		''' Returns informations about the given quadrant '''
		
		if x < 0 or x > 7 :
			return ' 000 '
			
		if y < 0 or y > 7:
			return ' 000 '
			
		return self.Quadrants[x][y].GetInformations()

