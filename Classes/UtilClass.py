class Util(object):
	'''Helper class'''
	
	@staticmethod
	def dead(entity):
		'''Displays a message on screen and in function of the object makes 
		   some modification in the game
		'''
		
		if isinstance(entity, Enterprise):
			print "MISSION FAILED: YOUR STARSHIP WAS DESTROYED!!!\n\nTYPE 'XXX' TO PLAY AGAIN"
		
		elif isinstance(entity, Klingon):
			print "Klingon ship destroyed at sector [%d,%d]." %(entity.Position.InSectorX, entity.Position.InSectorY)

	@staticmethod
	def displayIntroduction():
		''' Displays an introductory message '''

	@staticmethod
	def displayHelpMap():
		'''Displays some informations about the federation's map'''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 THE GALAXY IS DIVIDED INTO AN 8 X 8 QUADRANT GRID, AND EACH
 QUADRANT IS FURTHER DIVIDED INTO AN 8 X 8 SECTOR GRID.
-
 YOU WILL BE ASSIGNED A STARTING POINT SOMEWHERE IN THE GALAXY
 TO BEGIN A TOUR OF DUTY AS COMMANDER OF A STARSHIP;
 YOUR MISSION: TO SEEK AND DESTROY THE FLEET OF KLINGON WARSHIPS
 WHICH ARE MENACING THE UNITED FEDERATION OF PLANETS.
-
 (TO CONTINUE, HIT 'RETURN')
"""

		
	@staticmethod
	def displayHelpShortRangeScan():
		''' Displays what is the short range scan '''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 SHORT RANGE SCAN
 ----------------
 SHOWS YOU A SCAN OF YOUR PRESENT QUADRANT...
-
  -1--2--3--4--5--6--7--8-             Region: Quadra Sigma III
 1                        |           var: [7,6]
 2             *     *  B |             Sector: [4,6]
 3    K                   |           Stardate: 2283
 4 *                      |     Time remaining: 42
 5                        |          Condition: RED
 6          E        *    |             Energy: 2997
 7    *                   |            Shields: 0
 8    *                   |   Photon Torpedoes: 10
  -=--=--=--=--=--=--=--=-             Docked: False
-
 SYMBOLOGY ON YOUR SENSOR SCREEN IS AS FOLLOWS:
-
 E = YOUR STARSHIP'S POSITION
 K = KLINGON BATTLE CRUISER
 B = FEDERATION STARBASE (REFUEL/REPAIR/RE-ARM HERE!)
 * = STAR
-
 (TO CONTINUE, HIT 'RETURN')
"""

	@staticmethod
	def displayHelpLongRangeScan():
		''' Displays how to use long range scan command '''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 LONG RANGE SCAN
----------------
 SHOWS CONDITIONS IN SPACE FOR ONE QUADRANT ON EACH SIDE
 OF YOUR STARSHIP (WHICH IS IN THE MIDDLE OF THE SCAN)
-
 -------------------
 | 000 | 005 | 115 |
 -------------------
 | 000 |(112)| 113 |
 -------------------
 | 000 | 008 | 117 |
 -------------------
-
 THE SCAN IS CODED IN THE FORM '###'. WHERE THE UNITS DIGIT
 IS THE NUMBER OF STARS, TENS DIGIT IS THE NUMBER OF STARBASES,
 AND HUNDREDS DIGIT IS THE NUMBER OF KLINGONS.
 EXAMPLE -- 117 = 1 KLINGON, 1 STARBASE, 7 STARS.
-
 YOUR POSITION IS INDICATED BY THE ().
-
 (TO CONTINUE, HIT 'RETURN')
"""

	@staticmethod
	def displayHelpCommands():
		''' Displays all possible commands '''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 commands
 --------
 YOU HAVE THE FOLLOWING TEXT COMMANDS AVAILABLE TO YOU AS THE 
 CAPTAIN OF A STARSHIP:
-
 nav = Navigation
 pha = Phaser Control
 tor = Photon Torpedo Control
 she = Shield Control
 com = Access Computer
 xxx = Restart
-
 (TO CONTINUE, HIT 'RETURN')
"""

	@staticmethod
	def displayHelpNavigationCommand():
		''' Displays how to use the navigation command '''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 nav = Navigation
 ----------------
 COURSE IS IN A CIRCULAR NUMERICAL VECTOR ARRANGEMENT AS SHOWN . . .
-
 4    3    2
  `.  :  .' 
    `.:.'   
 5----E----1
    .':`.   
  .'  :  `. 
 6    7    8
-
 INTEGER AND REAL VALUES MAY BE USED. (1.5 IS HALF- WAY BETWEEN 1 AND 2.)
 VALUES MAY APPROACH 9.0, WHICH ITSELF IS EQUIVALENT TO 1.0.
-
 ONE WARP FACTOR IS THE SIZE OF ONE QUADRANT. THEREFORE, TO GET
 FROM QUADRANT 6,5 TO 5,5, YOU WOULD USE COURSE 3, WARP FACTOR 1.
-
 (TO CONTINUE, HIT 'RETURN')
"""

	@staticmethod
	def displayHelpPhaser():
		''' Displays how to use the Phaser Control '''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 pha = Phaser Control
 --------------------
 ALLOWS YOU TO DESTROY THE KLINGON BATTLE CRUISERS BY
 ZAPPING THEM WITH SUITABLY LARGE UNITS OF ENERGY TO
 DEPLETE THEIR SHIELD POWER. (REMEMBER, KLINGONS HAVE
 PHASERS, TOO!)
-
 (TO CONTINUE, HIT 'RETURN')
"""
		
	@staticmethod
	def displayHelpTorpedo():
		''' Displays how to use the Photon Torpedo Control '''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 tor = Photon Torpedo Control
 ----------------------------
 TORPEDO COURSE IS THE SAME AS USED IN WARP ENGINE CONTROL.
 IF YOU HIT THE KLINGON VESSEL, HE IS DESTROYED AND
 CANNOT FIRE BACK AT YOU. IF YOU MISS, YOU ARE SUBJECT TO
 HIS PHASER FIRE.
-
 (TO CONTINUE, HIT 'RETURN')
"""

	@staticmethod
	def displayHelpShield():
		'''Displays how  to use the Shield Control '''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 she = Shield Control
 --------------------
 DEFINES NUMBER OF ENERGY UNITS TO BE ASSIGNED TO SHIELDS.
 ENERGY IS TAKEN FROM TOTAL SHIP'S ENERGY. NOTE THAT THE
 TOTAL ENERGY INCLUDES SHIELD ENERGY.
-
 (TO CONTINUE, HIT 'RETURN')
"""

	@staticmethod
	def displayHelpComputer():
		''' Displays all possible commands of the computer '''
		
		print """
 INSTRUCTIONS FOR ** STAR TREK ** 
-
 com = Access Computer
 ---------------------
 THE LIBRARY-COMPUTER CONTAINS SEVERAL OPTIONS AND SETTINGS:
-
 rec = Cumulative Galatic Record
 sta = Status Report
 bas = Starbase Calculator
 nav = Navigation Calculator
 col = Change Screen Color
 con = Change Screen Contrast
-
 (TO CONTINUE, HIT 'RETURN')		
"""

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
		
		print " 1 | " + "   ".join(quadrants[0][0:4]) + " | " + "  ".join(quadrants[0][4:8]) + " |"

		print """   -------------------------------------------------
   |         RIGEL         |         DENEB         |"""

		print " 2 | " + "   ".join(quadrants[1][0:4]) + " | " + "   ".join(quadrants[1][4:8]) + " |"

		print """   -------------------------------------------------
   |        PROCYON        |        CAPELLA        |"""

		print " 3 | " + "   ".join(quadrants[2][0:4]) + " | " + "   ".join(quadrants[2][4:8]) + " |"

		print """   -------------------------------------------------
   |         VEGA          |       BETELGEUSE      |"""

		print " 4 | " + "   ".join(quadrants[3][0:4]) + " | " + "   ".join(quadrants[3][4:8]) + " |"

		print """   -------------------------------------------------
   |        CANOPUS        |       ALDEBARAN       |"""

		print " 5 | " + "   ".join(quadrants[4][0:4]) + " | " + "   ".join(quadrants[4][4:8]) + " |"

		print """   -------------------------------------------------
   |        ALTAIR         |        REGULUS        |"""

		print " 6 | " + "   ".join(quadrants[5][0:4]) + " | " + "   ".join(quadrants[5][4:8]) + " |"

		print """   -------------------------------------------------
   |      SAGITTARIUS      |        ARCTURUS       |"""

		print " 7 | " + "   ".join(quadrants[6][0:4]) + " | " + "   ".join(quadrants[6][4:8]) + " |"

		print """   -------------------------------------------------
   |        POLLUX         |         SPICA         |"""

		print " 8 | " + "   ".join(quadrants[7][0:4]) + " | " + "   ".join(quadrants[7][4:8]) + " |"

		print """   -------------------------------------------------
(TO CONTINUE, HIT 'RETURN')		
"""
	
#other auxiliar classes	
class NavParam(object):
	COURSE = 1	
	WARP_FACTOR = 2
