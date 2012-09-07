class Quadrant(object):
	''' Class used to store informations about a quadrant '''
	
	def __init__(self, klingons, starbases, stars):
		self.Klingons = klingons
		self.StarBases = starbases
		self.Stars = stars
		
	def Print():
		''' Prints all the informations about the quadrant '''
		
		print "%d%d%d" %(self.Klingons, self.StarBases, self.Stars)