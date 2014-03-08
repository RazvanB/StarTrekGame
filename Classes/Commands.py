from Classes.UtilClass import Util, NavParam, GeoMath
from string import lower

class Commands(object):
    
    def navigationCommand(self, game):
        '''Command to move the Enterprise '''
        
        Util.displayNavigationCommand(NavParam.COURSE)
        
        try:
            course = float(Util.prompt())    
            if course < 1.0 or course > 9.0:
                Util.printMessage('Invalid course.')
                return ''
        except ValueError: 
            Util.printMessage('Invalid course.')
            return ''
            
        Util.displayNavigationCommand(NavParam.WARP_FACTOR)
        
        try:
            warp = float(Util.prompt())    
            if warp < 0.1 or warp > 8.0:
                Util.printMessage('Invalid warp factor.')
                return ''
        except ValueError: 
            Util.printMessage('Invalid warp factor.')
            return ''
        
        (canMove, newPos) = game.map.moveEnterprise(course, warp, game.TheEnterprise.Position)
        if not canMove: 
            return 'Error! the path is blocked'
        else:
            game.TheEnterprise.Position = newPos
            game.EnterpriseQuadrant = game.map.Quadrants[newPos.QuadrantX][newPos.QuadrantY]
            return 'Warp engine engaged'
    
    def shieldCommand(self, game):
        '''Command to change the shields '''
        
        currentShield = game.TheEnterprise.Shield
        currentEnergy = game.TheEnterprise.Energy
        
        Util.displayShieldCommand(currentShield, currentEnergy)
        
        try:
            shield = int(Util.prompt())    
            if shield < (-currentShield) or shield > currentEnergy:
                Util.printMessage('Invalid amount of energy.')
                return
        except ValueError: 
            Util.printMessage('Invalid amount of energy.')
            return
        
        game.TheEnterprise.Shield += shield
        game.TheEnterprise.Energy -= shield
        
        Util.printMessage('Shield strength is now {0}. Energy level is now {1}', game.TheEnterprise.Shield, game.TheEnterprise.Energy)
        Util.prompt()
    
    def computerCommand(self, game):
        '''Displays the computer commands'''
        
        Util.clear()
        game.displayAllRangeScan('')
        game.displayCondition()
        Util.displayComputerCommands()
        
        command = Util.prompt()
        
        if lower(command) == 'rec':
            Util.clear()
            Util.displayRecordCommand(game.map.Quadrants)
            Util.prompt()
        elif lower(command) == 'sta':
            Util.clear()
            Util.displayStatusCommand(game.RemainingStarDays, game.TotalKlingons, game.TotalStarBases, game.TheEnterprise)
            Util.prompt()
        elif lower(command) == 'bas':
            self.calculateStarBaseCommand(game)
        elif lower(command) == 'nav':
            self.calculateNavigationCommand(game)
        
    def calculateStarBaseCommand(self, game):
        '''Command to calculate the distance to dock to a starbase in the current quadrant'''
        
        if game.EnterpriseQuadrant.NoOfStarBases == 0:
            Util.printMessage('There are no starbases in this quadrant.')
        else:
            for starbase in game.EnterpriseQuadrant.StarBases:  
                dist = GeoMath.distance(game.TheEnterprise.Position.GetSectorCoordinates(), starbase.Position.GetSectorCoordinates())
                direction = 0.0
                print """Starbase in sector %s.
Direction: %.2f
Distance:  %.2f""" %(starbase.Position.GetSector(), direction, dist)
        Util.prompt()
    
    def phaserCommand(self, game):
        '''Command to fire with phaser'''
        
        if game.EnterpriseQuadrant.NoOfKlingons == 0:
            Util.printMessage('There are no Klingon ships in this quadrant.')
            return
        
        Util.printMessage('Phasers locked on target.')
        Util.printMessage('Enter phaser energy (1 - {0}):', game.TheEnterprise.Energy)
        Util.prompt()
    

    def torpedoCommand(self, game):
        '''Command to fire a torpedo'''
        
        if game.EnterpriseQuadrant.NoOfKlingons == 0:
            print 'There are no Klingon ships in this quadrant.'
        else:
            Util.displayDirections()
            
            for ship in game.EnterpriseQuadrant.Klingons:
                Util.printMessage('Klingon ship in sector {0}', ship.Position.GetSector())
            
            Util.printMessage('Enter firing direction (1.0--9.0):')
            Util.prompt()
            
            #get direction from input
            try:
                direction = float(Util.prompt())    
                if direction < 1.0 or direction > 9.0:
                    Util.printMessage('Invalid direction.')
                return ''
            except ValueError: 
                    Util.printMessage('Invalid direction.')
                    return ''
            
            