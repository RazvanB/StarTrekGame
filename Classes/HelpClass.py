from UtilClass import Util

class Help(object):
	'''Static methods containing instructions'''
	
	@staticmethod
	def displayHelp():
		Util.clear()
		Help.displayHelpMap()
		Help.displayHelpShortRangeScan()
		Help.displayHelpLongRangeScan()
		Help.displayHelpCommands()
		Help.displayHelpNavigationCommand()
		Help.displayHelpPhaser()
		Help.displayHelpTorpedo()
		Help.displayHelpShield()
		Help.displayHelpComputer()
	
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
		Util.prompt()
		Util.clear()
	
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
		Util.prompt()
		Util.clear()

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
		Util.prompt()
		Util.clear()

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
		Util.prompt()
		Util.clear()

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
		Util.prompt()
		Util.clear()

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
		Util.prompt()
		Util.clear()
		
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
		Util.prompt()
		Util.clear()

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
		Util.prompt()
		Util.clear()

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
		Util.prompt()
		Util.clear()
