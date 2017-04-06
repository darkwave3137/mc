import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
SIZE = 50
for i in range(SIZE):
    for j in range(SIZE):
        R = random.randint(0, 15)
        mc.setBlock(pos.x+i, pos.y-1, pos.z+j, block.WOOL.id, R)
