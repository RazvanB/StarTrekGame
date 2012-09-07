class Enterprise(object):
	'''The enterprise herself.'''
	
	#constants
	SYMBOL = 'E'
	NR_TORPEDOS = 10
	
	
	def __init__(self, energy, pos):
		self.Energy = energy
		self.Shield = 0.0
		self.Torpedos = NR_TORPEDOS
		self.Position = pos
	
	def ReceivedDamage(damage):
		'''Called when the ship was hit '''
		
		self.Shield -= damage
		
		#the ship is destroyed
		if self.Shield <= 0.0:
			Utils.dead(SYMBOL)
			
		return 0
		