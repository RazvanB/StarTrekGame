from Classes.UtilClass import *
from Classes.KlingonClass import Klingon
from Classes.PositionClass import Position
from Classes.MapClass import Map
from string import lower

class Game(object):
	
	def __init__(self):
		''' some game initialisations'''
		self.Map = Map(0)
		self.KlingonShips = []
		self.StarBases = []
		self.StarDays = -1
		self.InitialStarDate = -1
		
	def generateMap(self, klingons, stars, starbases):
		'''Place objects on the federaion map'''
		
		for i in range(0, klingons):
			self.KlingonShips.append(Klingon(1000, 400, Position(1,2,1,1)))
		
		self.KlingonShips[0].Print()
		
	def start(self):
		'''The entry method of the game'''
		
		Util.asciiArt()
		
		print  'DO YOU NEED INSTRUCTIONS (YES/NO)'
		answer = Util.prompt()
		
		if answer != None and (lower(answer) == 'y' or lower(answer) == 'yes'):
			Util.displayHelp()
		
		# TODO - from here verify the restart command
		Util.displayOrders(17, 2222, 45, 4)
		answer = Util.prompt()
		self.isRestart(answer)
		
		self.generateMap(17, 100, 4)
			
			
	
	def isRestart(self, answer):
		if(lower(answer) == 'xxx'):
			#TODO - Clear screen before restart
			self.start()
		
	def initGame():
		'''  '''
			
g = Game()
g.start()