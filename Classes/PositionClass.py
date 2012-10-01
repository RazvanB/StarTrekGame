class Position(object):
	"""Stores the position on the map of an entity"""
	def __init__(self, qx = None, qy = None, sx = None, sy = None, ax = None, ay = None):
		if ax == None and ay == None:
			self.SectorX = sx
			self.SectorY = sy
			self.QuadrantX = qx
			self.QuadrantY = qy
			self.AbsoluteX = 8 * qx + sx
			self.AbsoluteY = 8 * qy + sy
		else:
			self.SectorX = ax % 8
			self.SectorY = ay % 8
			self.QuadrantX = ax / 8
			self.QuadrantY = ay / 8
			self.AbsoluteX = ax
			self.AbsoluteY = ay
		
	def GetQuadrant(self):
		'''Returns the quadrant coordinates as string'''
		return '[%d,%d]' %(self.QuadrantX + 1, self.QuadrantY + 1)
		
	def GetSector(self):
		'''Returns the quadrant coordinates as string'''
		return '[%d,%d]' %(self.SectorX + 1, self.SectorY + 1)
	
	def Print(self):
		'''For debugging'''
		print 'Q[%r,%r] - S[%r,%r]' %(self.QuadrantX, self.QuadrantY, self.SectorX, self.SectorY)