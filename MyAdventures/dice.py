import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for i in range(5):
    for j in range(7):
        mc.setBlock(pos.x + 3, pos.y + j, pos.z + i, block.WOOL.id)
a = [1, 3, 5, 1, 3, 5]
b = [1, 1, 1, 3, 3, 3]
for i in range(6):
    mc.setBlock(pos.x + 3, pos.y + a[i], pos.z + b[i], block.STONE.id)
