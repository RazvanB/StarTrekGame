from Classes.UtilClass import *
from string import lower
from Classes.HelpClass import Help
from Classes.EnterpriseClass import Enterprise
from Classes.MapClass import Map
from Classes.QuadrantClass import Quadrant

class Game(object):
	
	def __init__(self):
		''' some game initialisations'''
		Util.resizeConsole(120, 45)
		self.initGame()
		
	def initGame(self):
		'''Prepare the game and the map'''
		self.RemainingStarDays = 40 + randint(0, 11)
		self.CurrentStarDate = 1513.0
		self.TotalKlingons = 15 + randint(0, 7)
		self.TotalStarBases = 2 + randint(0, 4)
		self.CurrentCondition = 'GREEN'
		
		self.generateMap()
		
	def generateMap(self):
		'''Place objects on the federaion map'''
		
		self.map = Map()
		self.map.placeKlingons(self.TotalKlingons)
		self.map.placeStarBases(self.TotalStarBases)
		pos = self.map.placeEnterprise()
		
		#set the quadrant where the Enterprise is located
		self.EnterpriseQuadrant = self.map.Quadrants[pos.QuadrantX][pos.QuadrantY]
		self.TheEnterprise = Enterprise(pos)
		
	def start(self):
		'''The entry method of the game'''
		
		Util.clear()
		Util.asciiArt()
		
		print  'DO YOU NEED INSTRUCTIONS (YES/NO)'
		answer = Util.prompt()
		
		if answer != None and (lower(answer) == 'y' or lower(answer) == 'yes'):
			Help.displayHelp()
		else:
			Util.clear()
		
		Util.displayOrders(self.TotalKlingons, self.CurrentStarDate + self.RemainingStarDays, self.RemainingStarDays, self.TotalStarBases)
		
		answer = Util.prompt()
		self.isRestart(answer)
			
		self.displayAllRangeScan("")
		self.displayCondition()
		Util.displayCommands()
		
		while(True):
			self.command()
	
	def displayCondition(self):
		''' Display the condition of the Enterprise '''
		
		print '-'
		if self.EnterpriseQuadrant.NoOfKlingons > 0 and  self.TheEnterprise.Shield == 0:
			self.CurrentCondition = 'RED'
			print 'Condition %s: %s' %(self.CurrentCondition, 'Klingon ship detected')
			print 'Warning: Shields are down'
		elif self.EnterpriseQuadrant.NoOfKlingons > 0 and self.TheEnterprise.Shield > 0:
			self.CurrentCondition = 'RED'
			print 'Condition %s: %s' %(self.CurrentCondition, 'Klingon ship detected')
		elif self.map.getBlockedStarbase() != None:
			pos = self.map.getBlockedStarbase()
			self.CurrentCondition = 'RED'
			print 'Condition %s: %s' %(self.CurrentCondition, 'Starbase K-%d%d is blocked by Klingons' %(pos.QuadrantX, pos.QuadrantY))
		elif self.TheEnterprise.Energy < 300:
			self.CurrentCondition = 'YELLOW'
			print 'Condition %s: %s' %(self.CurrentCondition, 'Low energy level, return to starbase.')
		else:
			self.CurrentCondition = 'GREEN'
			print 'Condition %s": %s' %(self.CurrentCondition, 'This quadrant is clear.')
		print '-'
	
	def isRestart(self, answer):
		if lower(answer) == 'xxx':
			Util.clear()
			self.initGame()
			self.start()
			
	def displayAllRangeScan(self, message):
		''' Display the current quadrant in which is the Enterprise '''
		
		CST_GAP_SR_INFO = 3
		CST_GAP_INFO_LR = 2
		CST_SHORT_RANGE_MAP = 26
		
		max_len_Info = 20 + len(self.EnterpriseQuadrant.Name)
		
		
		
		if len(message) > 0:
			print "STAR TREK - %s" %message
		else:
			print "STAR TREK"
			
		firstLineGap = CST_SHORT_RANGE_MAP + CST_GAP_SR_INFO + max_len_Info + CST_GAP_INFO_LR - len('SHORT RANGE SCAN')

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
			return ' -1--2--3--4--5--6--7--8- '
		elif line == 10:
			return ' ' + '-' * 24 + ' '
		else:
			return self.EnterpriseQuadrant.GetLine(line - 2)
			
	def getEnterpriseInformation(self, prop):
		'''Get a string representation for a propery. Used to display the short range scan '''
		
		max_len_Info = 18 + len(self.EnterpriseQuadrant.Name) # len(Photon Torpedoes: ) = 18
		
		if prop == 1: # quadrant's name
			return ' ' * (max_len_Info - len('Region: %s' %self.EnterpriseQuadrant.Name)) + 'Region: %s' %self.EnterpriseQuadrant.Name
		elif prop == 2: #quadrant coordinates
			return ' ' * (max_len_Info - len('Quadrant: %s' %self.TheEnterprise.Position.GetQuadrant())) + 'Quadrant: %s' %self.TheEnterprise.Position.GetQuadrant()
		elif prop == 3: #sector coordinates
			return ' ' * (max_len_Info - len('Sector: %s' %self.TheEnterprise.Position.GetSector())) + 'Sector: %s' %self.TheEnterprise.Position.GetSector()
		elif prop == 4: #Current Stardate
			return ' ' * (max_len_Info - len('Stardate: %.2f' %self.CurrentStarDate)) + 'Stardate: %.2f' %self.CurrentStarDate
		elif prop == 5: #Time remaining
			return ' ' * (max_len_Info - len('Time remaining: %d' %self.RemainingStarDays)) + 'Time remaining: %d' %self.RemainingStarDays
		elif prop == 6: #Conditions
			return ' ' * (max_len_Info - len('Condition: %s' %self.CurrentCondition)) + 'Condition: %s' %self.CurrentCondition
		elif prop == 7: #Energy
			return ' ' * (max_len_Info - len('Energy: %d' %self.TheEnterprise.Energy)) + 'Energy: %d' %self.TheEnterprise.Energy
		elif prop == 8: #Shield
			return ' ' * (max_len_Info - len('Shield: %d' %self.TheEnterprise.Shield)) + 'Shield: %d' %self.TheEnterprise.Shield
		elif prop == 9: #torpedoes
			return ' ' * (max_len_Info - len('Photon Torpedoes: %d' %self.TheEnterprise.Torpedos)) + 'Photon Torpedoes: %d' %self.TheEnterprise.Torpedos
		elif prop == 10: #enterprise is docked
			return ' ' * (max_len_Info - len('Docked: %s' %self.TheEnterprise.Docked)) + 'Docked: %s' %self.TheEnterprise.Docked
			
	def getLongRangeScan(self, line):
		'''Get a string representation for the long range scan'''
		
		x = self.TheEnterprise.Position.QuadrantX
		y = self.TheEnterprise.Position.QuadrantY
		
		if line == 1:
			return '-' * 19
		elif line == 2:
			return '|%s|%s|%s|' %(self.map.getInformations(x - 1, y - 1), self.map.getInformations(x - 1, y), self.map.getInformations(x - 1, y + 1))
		elif line == 3:
			return '-' * 19
		elif line == 4:
			return '|%s|%s|%s|' %(self.map.getInformations(x, y - 1), self.map.getInformations(x, y), self.map.getInformations(x, y + 1))
		elif line == 5:
			return '-' * 19
		elif line == 6:
			return '|%s|%s|%s|' %(self.map.getInformations(x + 1, y - 1), self.map.getInformations(x + 1, y), self.map.getInformations(x + 1, y + 1))
		elif line == 7:
			return '-' * 19
		elif line == 8:
			return "THE THREE NUMBERS '###'"
		elif line == 9:
			return "FOR EACH QUADRANT REFER TO"
		elif line == 10:
			return "#KLINGONS, #STARBASES, #STARS"

	def command(self):
		answer = Util.prompt()
		self.isRestart(answer)
			
		if lower(answer) == 'nav':
			self.navigationCommand()
		elif lower(answer) == 'pha':
			self.pahserCommand()
		elif lower(answer) == 'tor':
			self.torpedoCommand()
		elif lower(answer) == 'she':
			self.shieldControl()
		elif lower(answer) == 'com':
			self.computerCommand()
			
	def navigationCommand(self):
		'''Command to move the Enterprise '''
		
		Util.displayNavigationCommand(NavParam.COURSE)
		
		try:
			course = float(Util.prompt())	
			if course < 1.0 or course > 9.0:
				print 'Invalid course.'
				return
		except ValueError: 
			print 'Invalid course.'
			return
			
		Util.displayNavigationCommand(NavParam.WARP_FACTOR)
		
		try:
			warp = float(Util.prompt())	
			if warp < 1.0 or warp > 9.0:
				print 'Invalid warp factor.'
				return
		except ValueError: 
			print 'Invalid warp factor.'
			return
		
		
			
g = Game()
g.start()