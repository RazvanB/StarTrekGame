from Classes.UtilClass import Util, NavParam

class Commands(object):
    
    def navigationCommand(self, game):
        '''Command to move the Enterprise '''
        
        Util.displayNavigationCommand(NavParam.COURSE)
        
        try:
            course = int(Util.prompt())    
            if course < 1 or course > 9:
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
        
        Util.clear()
        game.displayCondition()
        Util.displayCommands()
    
    