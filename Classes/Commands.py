from Classes.UtilClass import Util, NavParam, GeoMath
from string import lower

class Commands(object):
    
    def navigationCommand(self, game):
        '''Command to move the Enterprise '''
        
        Util.displayNavigationCommand(NavParam.COURSE)
        
        try:
            course = float(Util.prompt())    
            if course < 1.0 or course > 8.0:
                print 'Invalid course.'
                return ''
        except ValueError: 
            print 'Invalid course.'
            return ''
            
        Util.displayNavigationCommand(NavParam.WARP_FACTOR)
        
        try:
            warp = float(Util.prompt())    
            if warp < 0.1 or warp > 8.0:
                print 'Invalid warp factor.'
                return ''
        except ValueError: 
            print 'Invalid warp factor.'
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
                print 'Invalid amount of energy.'
                return
        except ValueError: 
            print 'Invalid amount of energy.'
            return
        
        game.TheEnterprise.Shield += shield
        game.TheEnterprise.Energy -= shield
        
        print 'Shield strength is now %d. Energy level is now %d' %(game.TheEnterprise.Shield, game.TheEnterprise.Energy)
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
        if game.EnterpriseQuadrant.NoOfStarBases == 0:
            print 'There are no starbases in this quadrant.'
        else:
            for starbase in game.EnterpriseQuadrant.StarBases:  
                dist = GeoMath.distance(game.TheEnterprise.Position.GetSectorCoordinates(), starbase.Position.GetSectorCoordinates())
                direction = 0.0
                print """Starbase in sector %s.
Direction: %.2f
Distance:  %.2f""" %(starbase.Position.GetSector(), direction, dist)
        Util.prompt()
    
    
            
    