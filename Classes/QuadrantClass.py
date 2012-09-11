import string

class Quadrant(object):
	''' Class used to store informations about a quadrant '''
	
	@property
	def IsEnterprise(self):
		''' Returns if in the current quadrant is the Enterprise present '''
		return self._isEnterprise
	
	@property
	def getNoOfStars(self):
		return len(self.Stars)
		
	@property
	def getNoOfKlingons(self):
		return len(Klingons)
		
	@property
	def getNoOfStarBases(self):
		return len(self.StarBases)
	
	def __init__(self):
		''' Create an empty quadrant '''
		
		self._isEnterprise = False
		self.Klingons = []
		self.StarBases = []
		self.Stars = []
		self.Name = 'Unknown'
		self.Sectors = [s[:] for s in [[' ']*8]*8]
		
	def Print(self):
		''' Prints all informations about the current quadrant (#KB*)'''
		
		if self.IsEnterprise:
			print "(%d%d%d)" %(self.Klingons, self.StarBases, self.Stars)
		else:
			print " %d%d%d " %(self.Klingons, self.StarBases, self.Stars)
			
	def PrintSectors(self):
		''' Draw the sectors of the current quadrant '''
		
		print '\n'.join([''.join(r) for r in self.Sectors])