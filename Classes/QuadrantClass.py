class Quadrant(object):
	''' Class used to store informations about a quadrant '''
	
	@property
	def IsEnterprise(self):
		''' Returns if in the current quadrant is the Enterprise present '''
		return self._isEnterprise
	
	def __init__(self, klingons, starbases, stars):
		''' Create an empty quadrant '''
		
		self._isEnterprise = False
		self.Klingons = klingons
		self.StarBases = starbases
		self.Stars = stars
		self.Name = 'Unknown'
		self.Sectors = [s[:] for s in [[' ']*8]*8]
		
	def Print(self):
		''' Prints all informations about the current quadrant '''
		
		if self.IsEnterprise:
			print "(%d%d%d)" %(self.Klingons, self.StarBases, self.Stars)
		else:
			print " %d%d%d " %(self.Klingons, self.StarBases, self.Stars)