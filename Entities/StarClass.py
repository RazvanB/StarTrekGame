import Utils
from random import randint

class Star(object):
	'''Represents a star'''
	
	#constants
	SYMBOL = '*'
	DAMAGE_FACTOR = 2.0
	INFLICT_DAMAGE = 100
	
	def __init__(self, mass, becomesNova, pos):
		self.Mass = mass
		self.BecomesNova = becomesNova;
		self.Position = pos
		
	def ReceivedDamage(damage):
		self.Mass -= DAMAGE_FACTOR * damage
		
		if self.Mass <= 0:
			Utils.dead(SYMBOL)
			
			if self.BecomesNova:
				return random(0, 10) * 0.1 * INFLICT_DAMAGE 
			else:
				return 0
		
		return 0