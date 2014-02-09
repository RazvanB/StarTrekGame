from random import randint
from Models.PositionClass import Position
from os import system

class Util(object):
	'''Helper class'''
	
	@staticmethod
	def clear():
		system('cls')
		
	@staticmethod
	def resizeConsole(w, h):
		system('mode %d,%d' %(w,h))
	
	@staticmethod
	def prompt():
		return raw_input('>')

	@staticmethod
	def getRandomPosition():
		''' Returns a random position on the map '''
		
		ax = randint(0, 63)
		ay = randint(0, 63)
			
		qx = ax / 8
		sx = ax % 8
		
		qy = ay / 8
		sy = ay % 8
		
		return Position(qx, qy, sx, sy)
	
	@staticmethod
	def asciiArt():
		''' Ascii art of The Enterprise '''
		
		chose = randint(0,1)
		
		if chose == 0:
			print """
 __  _                 _____             _    
/ _\| |_  __ _  _ __  /__   \ _ __  ___ | | __
\ \ | __|/ _` || '__|   / /\/| '__|/ _ \| |/ /
_\ \| |_| (_| || |     / /   | |  |  __/|   < 
\__/ \__|\__,_||_|     \/    |_|   \___||_|\_\\
   ___
  / _ \ __ _  _ __ ___    ___ 
 / /_\// _` || '_ ` _ \  / _ \\
/ /_\\\\| (_| || | | | | ||  __/
\____/ \__,_||_| |_| |_| \___|
"""
		else:
			print """STAR TREK GAME
     ___________________ _      __.-------.__
    /  /||||||||||||||\ | \  .-'             `-.
    \__\||||||||||||||/_|_/.'   \  ,-----,  /   `.
       ~~~~\~~~~\~~~~~~ __/ `,   \         /   ,' \\
        _,--` ___\__,--' /   /`,  \   ___ /  ,'    \\
       /__,--'    ______|       `,---`__ \ ,'  \    |
        | -------`. .   |       |==,-`  ` |    |    |
       _|_-------,______|       |==`-,__' |    |    |
       \_ `--,___ __    |       ,`---,___/ `,  /    |
         `--,    /  `--._\   \,'  /       \  `,    /
     ______/____/_________\ ,'   /         \   `, /
    /  /||||||||||||||\ | \`.   /  `-----'  \   .'
    \__\||||||||||||||/_|_/  `-.__         __.-'
       ~~~~~~~~~~~~~~~~           `-------'
"""

	# @staticmethod
	# def dead(entity):
		# '''Displays a message on screen and in function of the object makes 
		# some modification in the game
		# '''
		
		# if entity == 'E':
			# print "MISSION FAILED: YOUR STARSHIP WAS DESTROYED!!!\n\nTYPE 'XXX' TO PLAY AGAIN"
		
		# elif entity == 'K':
			# print "Klingon ship destroyed at sector [%d,%d]." %(entity.Position.InSectorX, entity.Position.InSectorY)

	@staticmethod
	def displayOrders(klingons, finalStarDate, days, starbases):
		''' Displays a message containing the scenario '''
		
		print """
 STAR TREK - THE MISSION
 -----------------------
 YOUR ORDERS ARE AS FOLLOWS:
-
 DESTROY THE %d KLINGON WARSHIPS WHICH HAVE INVADED
 THE GALAXY BEFORE THEY CAN ATTACK FEDERATION HEADQUARTERS
 ON STARDATE %.2f. THIS GIVES YOU %d DAYS. THERE ARE
 %d STARBASES IN THE GALAXY FOR RESUPPLYING YOUR SHIP.
-
 HIT 'RETURN' WHEN YOU'RE READY TO ASSUME COMMAND ---		
""" %(klingons, finalStarDate, days, starbases)

	@staticmethod
	def displayCommands():
		print """
--- Commands -----------------
nav = Navigation
pha = Phaser Control
tor = Photon Torpedo Control
she = Shield Control
com = Access Computer
xxx = Restart
Enter command:"""

	@staticmethod
	def displayNavigationCommand(param):
		''' Set navigation parameteres '''
		
		if param == NavParam.COURSE:
			print """
 4    3    2
  `.  :  .' 
    `.:.'   
 5---<E>---1
    .':`.   
  .'  :  `. 
 6    7    8
Enter course (1.0--9.0):
"""
		elif param == NavParam.WARP_FACTOR:
			print "Enter warp factor (0.1--8.0):"
	
	@staticmethod
	def displayComputerCommands():
		''' Displays computer commands '''
		
		print """
--- Main Computer --------------
rec = Cumulative Galatic Record
sta = Status Report
bas = Starbase Calculator
nav = Navigation Calculator
col = Change Screen Color to Green
con = Change Screen Contrast Low
exit = Return To The Main Command	
"""
	
	@staticmethod
	def displayStatusCommand(time, klingons, starbases, warpDamage, shortScanDamage, 
							longScanDamage, shieldDamage, mainCompDamage, torDamage, phaDamage):
		''' Displays informations about the Enterprise '''
		
		print """
STAR TREK
-
STATUS
-
               Time Remaining: %d
      Klingon Ships Remaining: %d
                    Starbases: %d
           Warp Engine Damage: %d
   Short Range Scanner Damage: %d
    Long Range Scanner Damage: %d
       Shield Controls Damage: %d
         Main Computer Damage: %d
Photon Torpedo Control Damage: %d
                Phaser Damage: %d
-
(TO CONTINUE, HIT 'RETURN')		
""" %(time, klingons, starbases, warpDamage, shortScanDamage,
	longScanDamage, shieldDamage, mainCompDamage, torDamage, phaDamage)
	
	@staticmethod
	def displayRecordCommand(quadrants):
		''' Displays all informations gathered by exploration of all quadrants '''
		
		print """
STAR TREK - CUMULATIVE GALACTIC RECORD
      1     2     3     4     5     6     7     8
   -------------------------------------------------
   |        ANTARES        |         SIRIUS        |
"""
		
		print " 1 |" + " ".join(quadrants[0][0:4]) + "|" + " ".join(quadrants[0][4:8]) + "|"

		print """   -------------------------------------------------
   |         RIGEL         |         DENEB         |"""

		print " 2 |" + " ".join(quadrants[1][0:4]) + "|" + " ".join(quadrants[1][4:8]) + "|"

		print """   -------------------------------------------------
   |        PROCYON        |        CAPELLA        |"""

		print " 3 |" + " ".join(quadrants[2][0:4]) + "|" + " ".join(quadrants[2][4:8]) + "|"

		print """   -------------------------------------------------
   |         VEGA          |       BETELGEUSE      |"""

		print " 4 |" + " ".join(quadrants[3][0:4]) + "|" + " ".join(quadrants[3][4:8]) + "|"

		print """   -------------------------------------------------
   |        CANOPUS        |       ALDEBARAN       |"""

		print " 5 |" + " ".join(quadrants[4][0:4]) + "|" + " ".join(quadrants[4][4:8]) + "|"

		print """   -------------------------------------------------
   |        ALTAIR         |        REGULUS        |"""

		print " 6 |" + " ".join(quadrants[5][0:4]) + "|" + " ".join(quadrants[5][4:8]) + "|"

		print """   -------------------------------------------------
   |      SAGITTARIUS      |        ARCTURUS       |"""

		print " 7 |" + " ".join(quadrants[6][0:4]) + "|" + " ".join(quadrants[6][4:8]) + "|"

		print """   -------------------------------------------------
   |        POLLUX         |         SPICA         |"""

		print " 8 |" + " ".join(quadrants[7][0:4]) + "|" + " ".join(quadrants[7][4:8]) + "|"

		print """   -------------------------------------------------
(TO CONTINUE, HIT 'RETURN')		
"""

	@staticmethod
	def displayShieldCommand(currentShield, energyLeft):
		'''Display informations about shield command '''
		
		print """
--- Shield Controls --------
Enter a positive value to increase shields (1 through %d).""" %(energyLeft)

		if currentShield > 0:
			print """
Enter a negative value to decrease shields (-1 through %d).""" %(-currentShield)
		
		print "Enter shield value:"
	

#other auxiliar classes	

class NavParam(object):
	COURSE = 1	
	WARP_FACTOR = 2
