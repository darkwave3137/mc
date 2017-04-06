import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
def safeFeet():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.postToChat("not safe")
    else:
        mc.postToChat("safe")
while 1:
    time.sleep(0.1)
    safeFeet()
