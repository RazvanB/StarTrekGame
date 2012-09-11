class StarBase(object):
	'''Represent a starbase on which the Enterprise can recharge/repair '''
	
	SYMBOL = 'B'
	
	def __init__(self, pos):
		self.Position = pos
