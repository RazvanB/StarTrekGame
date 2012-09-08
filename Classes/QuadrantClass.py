class Quadrant(object):
	''' Class used to store informations about a quadrant '''
	
	@property
	self.IsEnterprise = False
	
	def __init__(self, klingons, starbases, stars):
		self.Klingons = klingons
		self.StarBases = starbases
		self.Stars = stars
		self.Name = 'Unknown'
		self.Sectors = [[]]
		
	def Print(self):
		''' Prints all the informations about the quadrant '''
		
		if self.IsEnterprise:
			print "(%d%d%d)" %(self.Klingons, self.StarBases, self.Stars)
		else:
			print " %d%d%d " %(self.Klingons, self.StarBases, self.Stars)