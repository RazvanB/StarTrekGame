class Position(object):
	"""Stores the position on the map of an entity"""
	def __init__(self, qx, qy, sx, sy):
		self.InSectorX = sx
		self.InSectorY = sy
		self.QuadrantX = qx
		self.QuadrantY = qy
		self.AbsoluteX = 8 * qx + sx
		self.AbsoluteY = 8 * qy + sy