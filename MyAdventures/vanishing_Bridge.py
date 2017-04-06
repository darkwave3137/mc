import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import copy
mc = minecraft.Minecraft.create()
bridge = []
abridge = []
def buildBridge():
    cbridge = []
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.GLASS.id)
        coordinate = [pos.x, pos.y - 1, pos.z]
        bridge.append(coordinate)
    if b != block.GLASS.id and b != block.AIR.id:
        if len(bridge) > 0:
            cbridge = copy.deepcopy(bridge)
            abridge.append(cbridge)
            print abridge
            global bridge
            bridge = []
    if len(abridge) > 1:
        for i in range(len(abridge)):
            print len(abridge)
            print i
            print abridge[i]
            if len(abridge[i]) == 0:
                continue
            coordinate = abridge[i].pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
            time.sleep(0.25)
    
while 1:
    buildBridge()
