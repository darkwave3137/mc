import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while 1:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == -128 and pos.z == 248:
        mc.postToChat("welcome home")
