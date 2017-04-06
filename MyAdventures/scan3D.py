import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
FILENAME = "tree.csv"
SIZEX = 10
SIZEY = 10
SIZEZ = 10
def scan3D(filename, originx, originy, originz):
    f = open(filename, "w")
    f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")
    for y in range(SIZEY):
        f.write("\n")
        print 1
        for x in range(SIZEX):
            line = " "
            for z in range(SIZEZ):
                blockid = mc.getBlockWithData(originx + x, originy + y, originz + z)
                if line != " ":
                    line = line + ','
                line = line + str(blockid.id) + ',' + str(blockid.data)
            f.write(line + "\n")
    f.close()
pos = mc.player.getTilePos()
scan3D(FILENAME, pos.x - (SIZEX / 2), pos.y, pos.z - (SIZEZ / 2))
