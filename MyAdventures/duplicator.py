import mcpi.minecraft as minecraft
import mcpi.block as block
import glob
import time
import random

mc = minecraft.Minecraft.create()
SIZEX = 10
SIZEY = 10
SIZEZ = 10
roomx = 1
roomy = 1
roomz = 1

def buildRoom(x, y, z):
    global roomx, roomy, roomz

    roomx = x
    roomy = y
    roomz = z

    mc.setBlocks(roomx, roomy, roomz, roomx + SIZEX + 1, roomy + SIZEY + 1, roomz + SIZEZ + 1, block.GLASS.id)

    mc.setBlocks(roomx + 1, roomy + 1, roomz, roomx + SIZEX, roomy + SIZEY, roomz + SIZEZ, block.AIR.id)

def demolishRoom():
    global roomx, roomy, roomz
    mc.setBlocks(roomx, roomy, roomz, roomx + SIZEX + 1, roomy + SIZEY + 1, roomz + SIZEZ + 1, block.AIR.id)

def cleanRoom():
    mc.setBlocks(roomx + 1, roomy + 1, roomz + 1, roomx + SIZEX, roomy + SIZEY, roomz + SIZEZ, block.AIR.id)

def listFiles():
    print('\nFILES:')
    files = glob.glob('*.csv')
    for filename in files:
        print(filename)
    print('\n')

def scan3D(filename, originx, originy, originz):
    f = open(filename, "w")
    f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")
    for y in range(SIZEY):
        mc.postToChat('scan:' + str(y))
        f.write("\n")
        #print 1
        for x in range(SIZEX):
            line = " "
            for z in range(SIZEZ):
                blockid = mc.getBlockWithData(originx + x, originy + y, originz + z)
                if line != " ":
                    line = line + ','
                line = line + str(blockid.id) + ',' + str(blockid.data)
            f.write(line + "\n")
    f.close()

def print3D(filename, originx, originy, originz):
    f = open(filename, "r")
    lines = f.readlines()
    coords = lines[0].split(",")
    sizex = int(coords[0])
    sizey = int(coords[1])
    sizez = int(coords[2])
    lineidx = 1
    for y in range(sizey):
        mc.postToChat(str(y))
        lineidx = lineidx + 1
        for x in range(sizex):
            line = lines[lineidx]
            lineidx = lineidx + 1
            data = line.split(",")
            for z in range(sizez * 2)[::2]:
                #print z
                time.sleep(0)
                mc.setBlock(originx + x, originy + y, originz + z / 2, int(data[z]), int(data[z + 1]))

def menu():
    while True:
        print('DUPLICATOR MENU')
        print(' 1. BUILD the dupplicator room')
        print(' 2. LIST files')
        print(' 3. SCAN from duplicator room to file')
        print(' 4. LOAD from file into duplicator room')
        print(' 5. PRINT from duplicator room to player.pos')
        print(' 6. CLEAN the duplicator room')
        print(' 7. DEMOLISH the duplicator room')
        print(' 8. QUIT')

        choice = int(raw_input('please choose: '))
        if choice < 1 or choice > 8:
            print('Sorry, please choose a number between 1 and 8')
        else:
            return choice

anotherGo = True
while anotherGo:
    choice = menu()

    if choice == 1:
        pos = mc.player.getTilePos()
        buildRoom(pos.x, pos.y, pos.z)

    elif choice == 2:
        listFiles()

    elif choice == 3:
        filename = raw_input('filename?')
        scan3D(filename, roomx + 1, roomy + 1, roomz + 1)

    elif choice == 4:
        filename = raw_input('filename?')
        print3D(filename, roomx + 1, roomy + 1, roomz + 1)

    elif choice == 5:
        scan3D('scantemp', roomx + 1, roomy + 1, roomz + 1)
        pos = mc.player.getTilePos()
        print3D('scantemp', pos.x + 1, pos.y + 1, pos.z + 1)

    elif choice == 6:
        cleanRoom()

    elif choice == 7:
        demolishRoom()

    elif choice == 8:
        anotherGo = False
