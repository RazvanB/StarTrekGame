from UtilClass import Util
from random import randint

class Klingon(object):
	'''Represents a klingonian ship'''
	
	#constants
	ENG_LOW_LIMIT = 25.0
	ENG_HIGH_LIMIT = 100
	MIN_SHIELD_VALUE = 300
	MIN_ENERGY_VALUE = 200
	SYMBOL = 'K'
	
	def __init__(self, pos):
		self.Energy = self.MIN_ENERGY_VALUE + randint(100)
		self.Shield = self.MIN_SHIELD_VALUE + randint(200)
		self.Position = pos
		
		#set limit based on initial energy
		ENG_HIGH_LIMIT = 0.5 * Energy
		ENG_LOW_LIMIT = 0.2 * Energy
	
	def ReceivedDamage(damage):
		'''Called when the ship was hit '''
		
		self.Shield -= damage
		
		#the ship is destroyed
		if self.Shield <= 0.0:
			Util.dead(SYMBOL)
			return -1
		
		#if the ship is nearly destroyed use the last energy as shield
		if self.Shield <= ENG_LOW_LIMIT and self.Energy > 0:
			self.Shield += self.Energy
			self.Energy = 0.0
			return 0
			
		#if the ship has enough energy counter-attack
		if self.Energy >= ENG_HIGH_LIMIT:
			return  randint(0, 10) * 0.1 * self.Energy

	def Print(self):
		'''For debugging'''
		
		print 'Klingon ship: [energy = %r, shield = %r' %(self.Energy, self.Shield), 
		print 'pos = ', 
		self.Position.Print()