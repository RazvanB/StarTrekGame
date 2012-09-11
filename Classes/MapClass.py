from random import randint
from QuadrantClass import Quadrant

class Map(object):
	
	NO_STARS = 250
	MAX_STARS_IN_QUADRANT = 7
	
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
			ax = randint(0, 63)
			ay = randint(0, 63)
			
			qx = ax / 8
			sx = ax % 8
			
			qy = ay / 8
			sy = ay % 8
			
			if self.Quadrants[qx][qy].Stars <= self.MAX_STARS_IN_QUADRANT and self.Quadrants[qx][qy].Sectors[sx][sy] == ' ':
				self.Quadrants[qx][qy].Sectors[sx][sy] = '*'
				self.Stars += 1
				stars -= 1

	def placeKlingons(self, klingons):
		''' Place the enemy ships on the map '''
		
		while klingons > 0:
			ax = randint(0, 63)
			ay = randint(0, 63)
			
			qx = ax / 8
			sx = ax % 8
			
			qy = ay / 8
			sy = ay % 8
			
			if self.Quadrants[qx][qy].getNoOfStars() <= self.MAX_STARS_IN_QUADRANT and self.Quadrants[qx][qy].Sectors[sx][sy] == ' ':
				self.Quadrants[qx][qy].Sectors[sx][sy] = '*'
				self.Klingons.append(Klingon())
				stars -= 1

	def placeStarBases(self, starbases):
		''' Place starbases'''
		
		