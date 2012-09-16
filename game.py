from Classes.UtilClass import *
from Classes.HelpClass import Help
from Classes.KlingonClass import Klingon
from Classes.PositionClass import Position
from Classes.MapClass import Map
from string import lower
from random import randint

class Game(object):
	
	def __init__(self):
		''' some game initialisations'''
		initGame()
		
	def initGame(self):
		'''Prepare the game and the map'''
		self.RemainingStarDays = 40 + randint(0, 11)
		self.CurrentStarDate = 1513.0
		self.TotalKlingons = 15 + randint(0, 7)
		self.TotalStarBases = 2 + randint(0, 4)
		self.CurrentCondition = 'GREEN'
		
		generateMap()
		
	def generateMap(self):
		'''Place objects on the federaion map'''
		
		self.map = Map()
		self.map.placeKlingons(self.TotalKlingons)
		self.map.placeStarBases(self.TotalStarBases)
		pos = self.map.placeEnterprise()
		
		self.TheEnterprise = Enterprise(
		
	def start(self):
		'''The entry method of the game'''
		
		Util.clear()
		Util.asciiArt()
		
		print  'DO YOU NEED INSTRUCTIONS (YES/NO)'
		answer = Util.prompt()
		
		if answer != None and (lower(answer) == 'y' or lower(answer) == 'yes'):
			Help.displayHelp()
		else:
			Util.Clear()
		
		Util.displayOrders(self.TotalKlingons, self.CurrentStarDate + self.RemainingStarDays, self.RemainingStarDays, self.TotalStarBases)
		answer = Util.prompt()
		self.isRestart(answer)
				
		self.displayAllRangeScan("")
		
			
	
	def isRestart(self, answer):
		if(lower(answer) == 'xxx'):
			Util.clear()
			self.initGame()
			self.start()
			
	def displayAllRangeScan(self, message):
		''' Display the current quadrant in which is the Enterprise '''
		
		CST_SHORT_RANGE = 16
		CST_GAP_SR_INFO = 3
		CST_GAP_INFO_LR = 2
		CST_SHORT_RANGE_MAP = 24
		
		max_len_Info = 18 + quadrant.Name
		
		firstLineGap = CST_SHORT_RANGE_MAP + CST_GAP_SR_INFO + max_len_Info + CST_GAP_INFO_LR
		
		if len(message) > 0:
			print "STAR TREK - %message" %message
		else:
			print "STAR TREK"

		print 'SHORT RANGE SCAN' + ' ' * firstLineGap + 'LONG RANGE SCAN'
		
		for line in range(1, 11):
			print self.getShortRangeScan(line),
			print ' ' * CST_GAP_SR_INFO,
			print self.getEnterpriseInformation(line),
			print ' ' * CST_GAP_INFO_LR, 
			print self.getLongRangeScan(line)
	
	def getShortRangeScan(self, line):
		''' Get a string representation for the short range scan '''
		
		if line == 1:
			return '-1--2--3--4--5--6--7--8-'
		elif line == 10:
			return '-' * 24
		else:
			return self.EnterpriseQuadrant.GetLine(line - 2)
			
	def getEnterpriseInformation(self, prop):
		'''Get a string representation for a propery. Used to display the short range scan '''
		
		max_len_Info = 18 + self.EnterpriseQuadrant.Name # len(Photon Torpedoes: ) = 18
		
		if prop == 1: # quadrant's name
			return ' ' * (max_len_Info - len('Region: %s' %self.EnterpriseQuadrant.Name)) + 'Region: %s' %self.EnterpriseQuadrant.Name
		elif prop == 2: #quadrant coordinates
			return ' ' * (max_len_Info - len('Quadrant: %s' %self.enterprise.Position.GetQuadrant() + 'Quadrant: [%d, %d]' %self.enterprise.Position%enterprise.Position.GetQuadrant()
		elif prop == 3: #sector coordinates
			return ' ' * (max_len_Info - len('Sector: %s' %self.enterprise.Position.GetSector() + 'Sector: %s' %self.enterprise.Position.GetSector()
		elif prop == 4: #Current Stardate
			return ' ' * (max_len_Info - len('Stardate: %.2f' %self.CurrentStarDate)) + 'Stardate: %.2f' %self.CurrentStarDate
		elif prop == 5: #Time remaining
			return ' ' * (max_len_Info - len('Time remaining: %d' %self.RemainingStarDays)) + 'Time remaining: %d' %self.RemainingStarDays
		elif prop == 6: #Conditions
			return ' ' * (max_len_Info - len('Condition: %s' %self.CurrentCondition)) + 'Condition: %s' %self.CurrentCondition
		elif prop == 7: #Energy
			return ' ' * (max_len_Info - len('Energy: %d' %self.enterprise.Energy)) + 'Energy: %d' %self.enterprise.Energy
		elif prop == 8: #Shield
			return ' ' * (max_len_Info - len('Shield: %d' %self.enterprise.Shield)) + 'Shield: %d' %self.enterprise.Shield
		elif prop == 9: #torpedoes
			return ' ' * (max_len_Info - len('Photon Torpedoes: %d' %self.enterprise.Torpedos)) + 'Photon Torpedoes: %d' %self.enterprise.Torpedos
		elif prop == 10: #enterprise is docked
			return ' ' * (max_len_Info - len('Docked: %d' %self.enterprise.Docked)) + 'Docked: %d' %self.enterprise.Docked
			
	def getLongRangeScan(self, line):
		'''Get a string representation for the long range scan'''
		
		x = self.Enterprise.Position.QuadrantX
		y = self.Enterprise.Position.QuadrantY
		
		if line == 1:
			return '-' * 19
		elif line == 2:
			return '|' + map.GetInformations(x - 1, y - 1) + '|' + map.GetInformations(x - 1, y) + '|' + map.GetInformations(x - 1, y + 1) + '|'
		elif line == 3:
			return '-' * 19
		elif line == 4:
			return '|' + map.GetInformations(x, y - 1) + '|' + map.GetInformations(x, y) + '|' + map.GetInformations(x, y + 1) + '|'
		elif line == 5:
			return '-' * 19
		elif line == 6:
			return '|' + map.GetInformations(x + 1, y - 1) + '|' + map.GetInformations(x + 1, y) + '|' + map.GetInformations(x + 1, y + 1) + '|'
		elif line == 7:
			return '-' * 19
		elif line == 8:
			return "THE THREE NUMBERS '###'"
		elif line == 9:
			return "FOR EACH QUADRANT REFER TO"
		elif line == 10:
			return "#KLINGONS, #STARBASES, #STARS"

	
g = Game()
g.start()