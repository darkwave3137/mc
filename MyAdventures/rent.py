import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

X1 = -116
Z1 = 248
X2 = -122
Z2 = 260
HOME_X = X2 + 2
HOME_Z = Z2 + 2
HOME_Y = 50
rent = 0
inField = 0
while 1:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x < X1 + 1 and pos.x > X2 - 1 and pos.z > Z1 - 1 and pos.z < Z2 + 1:
        rent = rent + 1
        mc.postToChat("You owe rent:" + str(rent))
        inField = inField + 1
    else: inField = 0
    if inField > 3:
        mc.postToChat("To slow!")
        mc.player.setPos(HOME_X, HOME_Y, HOME_Z)
