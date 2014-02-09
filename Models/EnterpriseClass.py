

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
		self.warpDamage = 0.0
		self.shortScanDamage = 0.0
		self.longScanDamage = 0.0
		self.shieldDamage = 0.0
		self.mainCompDamage = 0.0
		self.torDamage = 0.0
		self.phaDamage = 0.0
	
	def ReceivedDamage(self, damage):
		'''Called when the ship was hit '''
		
		self.Shield -= damage
		
		#the ship is destroyed
		#if self.Shield <= 0.0:
		#	Util.dead(self.SYMBOL)
			
		return 0		
		