class Position(object):
	"""Stores the position on the map of an entity"""
	def __init__(self, qx, qy, sx, sy):
		self.SectorX = sx
		self.SectorY = sy
		self.QuadrantX = qx
		self.QuadrantY = qy
		self.AbsoluteX = 8 * qx + sx
		self.AbsoluteY = 8 * qy + sy
		
	def GetQuadrant(self):
		'''Returns the quadrant coordinates as string'''
		return '[%d,%d]' %(self.QuadrantX, self.QuadrantY)
		
	def GetSector(self):
		'''Returns the quadrant coordinates as string'''
		return '[%d,%d]' %(self.SectorX, self.SectorY)
	
	def Print(self):
		'''For debugging'''
		print 'Q[%r,%r] - S[%r,%r]' %(self.QuadrantX, self.QuadrantY, self.SectorX, self.SectorY)