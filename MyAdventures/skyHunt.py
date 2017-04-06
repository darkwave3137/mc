import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
mc = minecraft.Minecraft.create()
score = 0
RANGE = 5
treasure_x = None
treasure_y = None
treasure_z = None
def placeTreasure():
    #print("placeTreasure")
    global treasure_x, treasure_y, treasure_z
    pos = mc.player.getTilePos()
    treasure_x = random.randint(pos.x, pos.x + RANGE)
    treasure_y = random.randint(pos.y + 2, pos.y + 2 + RANGE)
    treasure_z = random.randint(pos.z, pos.z + RANGE)
    mc.setBlock(treasure_x, treasure_y, treasure_z, block.DIAMOND_BLOCK.id)
def checkHit():
    #print("checkHit")
    global score
    global treasure_x
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == treasure_x and pos.y == treasure_y and pos.z == treasure_z:
            mc.postToChat("HIT!")
            score = score + 10
            mc.setBlock(treasure_x, treasure_y, treasure_z, block.AIR.id)
            treasure_x = None
TIMEOUT = 10
timer = TIMEOUT
def homingBeacon():
    #print("homingBeacon")
    global timer
    if treasure_x != None:
        timer = timer - 1
        if timer == 0:
            timer = TIMEOUT
            pos = mc.player.getTilePos()
            diffx = abs(pos.x - treasure_x)
            diffy = abs(pos.y - treasure_y)
            diffz = abs(pos.z - treasure_z)
            diff = diffx + diffy + diffz
            mc.postToChat("score:" + str(score) + " treasure:" + str(diff))
bridge = []
def buildBridge():
    #print("Bridge")
    global score
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if treasure_x == None:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
            mc.postToChat("bridge:" + str(len(bridge)))
            time.sleep(0.25)
    elif b != block.GOLD_BLOCK.id:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.GOLD_BLOCK.id)
        coordinate = [pos.x, pos.y-1, pos.z]
        bridge.append(coordinate)
        score = score - 1
while 1:
    time.sleep(0.1)

    if treasure_x == None and len(bridge) == 0:
        placeTreasure()

    
    homingBeacon()
    checkHit()
    buildBridge()
