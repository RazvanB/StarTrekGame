class Quadrant(object):
	''' Class used to store informations about a quadrant '''
	
	@property
	def IsEnterprise(self):
		''' Returns if in the current quadrant is the Enterprise present '''
		return self._isEnterprise
		
	@IsEnterprise.setter
	def IsEnterprise(self, value):
		self._isEnterprise = value
	
	@property
	def NoOfStars(self):
		return self.Stars.__len__()
		
	@property
	def NoOfKlingons(self):
		return self.Klingons.__len__()
		
	@property
	def NoOfStarBases(self):
		return self.StarBases.__len__()
	
	def __init__(self):
		''' Create an empty quadrant '''
		
		self._isEnterprise = False
		self.Klingons = []
		self.StarBases = []
		self.Stars = []
		self.Name = 'Unknown'
		self.Sectors = [s[:] for s in [[' ']*8]*8]
		
	def GetInformations(self):
		''' Prints all informations about the current quadrant (#KB*)'''
		
		if self.IsEnterprise:
			return "(%d%d%d)" %(self.Klingons.__len__(), self.StarBases.__len__(), self.Stars.__len__())
		else:
			return " %d%d%d " %(self.Klingons.__len__(), self.StarBases.__len__(), self.Stars.__len__())
			
	def PrintSectors(self):
		''' Draw the sectors of the current quadrant '''
		print '\n'.join(['| '.join(r) for r in self.Sectors])
		
	def GetLine(self, line):
		''' Returns a string representation for the given line.'''
		
		strLine = '|'
		
		for i in range(8):
			strLine += ' ' + self.Sectors[line][i] + ' '
		strLine += "|"
		
		return strLine
