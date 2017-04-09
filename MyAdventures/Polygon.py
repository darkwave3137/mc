import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
pos = mc.player.getTilePos()
points = []

points.append(minecraft.Vec3(pos.x, pos.y, pos.z))
points.append(minecraft.Vec3(pos.x + 20, pos.y, pos.z))
points.append(minecraft.Vec3(pos.x + 10, pos.y + 20, pos.z))

mcdrawing.drawFace(points, True, block.WOOL.id, 6)