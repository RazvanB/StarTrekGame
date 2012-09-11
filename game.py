from Classes.UtilClass import *
from Classes.KlingonClass import Klingon
from Classes.PositionClass import Position
from Classes.MapClass import Map
from string import lower
from random import ranint

class Game(object):
	
	def __init__(self):
		''' some game initialisations'''
		self.map = Map()
		self.RemainingStarDays = 40 + randint(11)
		self.InitialStarDate = 1513.0
		self.TotalKlingons = 15 + randint(7)
		self.TotalStarBases = 2 + randint(4)
		
	def generateMap(self):
		'''Place objects on the federaion map'''
		
		m.placeKlingons(self.TotalKlingons)
		m.placeStarBases(self.TotalStarBases)
		
	def start(self):
		'''The entry method of the game'''
		
		Util.asciiArt()
		
		print  'DO YOU NEED INSTRUCTIONS (YES/NO)'
		answer = Util.prompt()
		
		if answer != None and (lower(answer) == 'y' or lower(answer) == 'yes'):
			Util.displayHelp()
		
		# TODO - from here verify the restart command
		Util.displayOrders(self.TotalKlingons, self.InitialStarDate + self.RemainingStarDays, self.RemainingStarDays, self.TotalStarBases)
		answer = Util.prompt()
		self.isRestart(answer)
		
		self.generateMap()
			
	
	def isRestart(self, answer):
		if(lower(answer) == 'xxx'):
			#TODO - Clear screen before restart
			self.start()
			
g = Game()
g.start()