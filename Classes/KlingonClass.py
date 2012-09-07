from UtilClass import Util
from random import randint

class Klingon(object):
	'''Represents a klingonian ship'''
	
	#constants
	ENG_LOW_LIMIT = 25.0
	ENG_HIGH_LIMIT = 100
	SYMBOL = 'K'
	
	def __init__(self, Energy, shield, pos):
		self.Energy = energy
		self.Shield = shield
		self.Position = pos
		
		#set limit based on initial energy
		ENG_HIGH_LIMIT = 0.5 * energy
		ENG_LOW_LIMIT = 0.2 * energy
	
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
