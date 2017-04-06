import mcpi.minecraft
import time
while 1:
    time.sleep(1)
    mc = mcpi.minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    mc.postToChat("x = " + str(pos.x) + " y = " + str(pos.y) + " z = " + str(pos.z))
