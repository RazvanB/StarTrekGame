class Position(object):
	"""Stores the position on the map of an entity"""
	def __init__(self, qx, qy, sx, sy):
		self.SectorX = sx
		self.SectorY = sy
		self.QuadrantX = qx
		self.QuadrantY = qy
		self.AbsoluteX = 8 * qx + sx
		self.AbsoluteY = 8 * qy + sy
		
	def Print(self):
		'''For debugging'''
		print 'Q[%r,%r] - S[%r,%r]' %(self.QuadrantX, self.QuadrantY, self.SectorX, self.SectorY)