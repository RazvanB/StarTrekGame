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
	def displayHelpShortRangeScan():
		''' Displays how short range works '''
		
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
		''' Displays how long range works '''
		
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
		''' Displays all possible commands'''
		
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
		''' Displays how navigation command works '''
		
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
		''' Displays how Phaser Control works '''
		
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
		''' Displays how Photon Torpedo Control works'''
		
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
		''' '''