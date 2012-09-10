from QuadrantClass import Quadrant

class Map(object):
	
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
		self.Quadrants = [[Quadrant(0,0,0) for j in range(8)] for i in range(8)]
		
		for i in range(8):
			for j in range(8):
				self.Quadrants[i][j].Name = self.QuadrantNames[i][j]
