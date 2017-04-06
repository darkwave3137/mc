import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
size = int(raw_input("size/2 of area to clear? "))
mc.setBlocks(pos.x + size , pos.y, pos.z + size, pos.x - size, pos.y + size, pos.z - size, block.AIR.id)
mc.setBlocks(pos.x - size, pos.y - 1, pos.z - size, pos.x + size, pos.y - 2, pos.z + size, block.STONE.id)
