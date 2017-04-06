import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x+1, pos.y + 1, pos.z + 1, 2)
a = mc.getBlock(pos.x + 1, pos.y + 1, pos.z + 1)
b = mc.getBlockWithData(pos.x + 1, pos.y + 1, pos.z + 1)
print a , b
print b.id, b.data
mc.setBlock(pos.x+1, pos.y , pos.z + 1, b)
