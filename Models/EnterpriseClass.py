

class Enterprise(object):
	'''The enterprise herself.'''
	
	#constants
	SYMBOL = 'E'
	NR_TORPEDOS = 10
	ENERGY = 4000
	
	
	def __init__(self, pos):
		self.Energy = self.ENERGY
		self.Shield = 0.0
		self.Torpedos = self.NR_TORPEDOS
		self.Docked = False
		self.Position = pos
	
	def ReceivedDamage(self, damage):
		'''Called when the ship was hit '''
		
		self.Shield -= damage
		
		#the ship is destroyed
		#if self.Shield <= 0.0:
		#	Util.dead(self.SYMBOL)
			
		return 0		
		