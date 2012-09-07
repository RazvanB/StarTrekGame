from Classes.UtilClass import *

#test status method
Util.displayStatusCommand(1,2,3,4,5,6,7,8,9,10)
print ""

#test navigation command
Util.displayNavigationCommand(NavParam.WARP_FACTOR)
print ""
Util.displayNavigationCommand(NavParam.COURSE)

#test record command
l = [['000','001','010','011','100','(101)','110','111'],
['000','001','010','011','100','101','110','111'],
['000','001','010','011','100','101','110','111'],
['000','001','010','011','100','101','110','111'],
['000','001','010','011','100','101','110','111'],
['000','001','010','011','100','101','110','111'],
['000','001','010','011','100','101','110','111'],
['000','001','010','011','100','101','110','111']
]

Util.displayRecordCommand(l)
print ""


