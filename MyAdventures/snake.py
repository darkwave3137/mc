import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
import  msvcrt
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
food_x = None
food_y = None
food_z = None
food_R = None
DIRECTION = 4 #0 X- 1 X+ 3 Y- 4 Y+
BOXSIZE = 30
box_x = pos.x + 1
box_y = pos.y + 1
box_z = pos.z
snake = []
SPEED = 1
def createBox():
    mc.setBlocks(box_x, box_y, box_z, box_x + BOXSIZE + 2, box_y + BOXSIZE + 2, box_z + 1, block.OBSIDIAN.id)
    mc.setBlocks(box_x + 1, box_y + 1, box_z, box_x + BOXSIZE + 1, box_y + BOXSIZE + 1, box_z + 1, block.AIR.id)
    mc.setBlocks(box_x + 1, box_y + 1, box_z + 1, box_x + BOXSIZE +1, box_y + BOXSIZE + 1, box_z + 1, block.GLASS.id)

def createSnake():
    R = random.randint(0,14)
    snake.append([box_x + 2, box_y + 1, R])
    snake.append([box_x + 1, box_y + 1, R])
    for example in snake:
        mc.setBlock(example[0], example[1], box_z, block.WOOL.id, example[2])
    mc.player.setPos(int(BOXSIZE / 2) + box_x, box_y + int(BOXSIZE / 2), box_z - int(BOXSIZE / 2 + BOXSIZE))
    time.sleep(5)

def food():
    CLASH = 0
    while True:
        x = box_x + random.randint(1, BOXSIZE + 1)
        y = box_y + random.randint(1, BOXSIZE + 1)
        for example in snake:
            if x == example[0] and y == example[1]:
                CLASH = 1
        if CLASH == 0:
            break
        CLASH = 0
    global food_x, food_y, food_z, food_R
    food_x = x
    food_y = y
    food_z = box_z
    food_R = random.randint(0, 14)
    mc.setBlock(food_x, food_y, food_z, block.WOOL.id, food_R)
    
def checkEat(x, y):
    if food_x == x and food_y == y:
        snake.insert(0,[food_x, food_y, food_R])
        return 1
    else:
        return 0
        
def move():
    global DIRECTION
    isEat = 0
    a = -1
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        if ch == 'w':
            a = 4
        elif ch == 's':
            a = 3
        elif ch == 'a':
            a = 1
        elif ch == 'd':
            a = 0
        if abs(a - DIRECTION) > 1:
            DIRECTION = a
    if DIRECTION > 2:
        move_y = DIRECTION * 2 - 7
        new = [snake[0][0], snake[0][1] + move_y]
        #checkOver(new, snake[0][1] + move_y)
        #isEat = checkEat(snake[0][0], snake[0][1] + move_y)
    else:
        move_x = DIRECTION * 2 - 1
        new = [snake[0][0] + move_x, snake[0][1]]
        #checkOver(snake[0][0] + move_x, snake[0][1])
        #isEat = checkEat(snake[0][0] + move_x, snake[0][1])
    checkOver(new[0], new[1])
    isEat = checkEat(new[0], new[1])
    if isEat:
        for example in snake:
            mc.setBlock(example[0], example[1], box_z, block.WOOL.id, example[2])
        food()
    else:
        for example in snake:
            old = [example[0], example[1]]
            example[0] = new[0]
            example[1] = new[1]
            new = old
            mc.setBlock(example[0], example[1], box_z, block.WOOL.id, example[2])
        mc.setBlock(new[0], new[1], box_z, block.AIR.id)
def checkOver(x, y):

    if x > box_x + BOXSIZE + 1 or y > box_y + BOXSIZE + 1 or x < box_x + 1 or y < box_y + 1:
        gameOver()
    for example in snake:
            if (x == example[0] and y == example[1]):
                gameOver()
def gameOver():
    mc.postToChat("YOU ARE DIE")
    for i in range(BOXSIZE * 5000):
        x = box_x + random.randint(1, BOXSIZE + 1)
        y = box_y + random.randint(1, BOXSIZE + 1)
        R = random.randint(0, 14)
        mc.setBlock(x, y, box_z, block.WOOL.id, R)
    mc.postToChat("YOU ARE DIE")
    time.sleep(3)
    mc.setBlocks(box_x, box_y , box_z , box_x + BOXSIZE + 2, box_y + BOXSIZE + 2, box_z + 2, block.AIR.id)
    exit()

createBox()
createSnake()
while True:
    if food_x == None:
        food()
    move()
    time.sleep(0.1)

    
