from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import math

import time

mc = Minecraft.create()


def makeBlockNearPlayer():
	pos = mc.player.getPos()
	dir = mc.player.getDirection()
	mc.setBlock(pos.x+(5*dir.x),pos.y,pos.z+(5*dir.z),1)
	# mc.setBlock(pos.x+5,pos.y,pos.z,1)

def makeBlocksNearPlayer(width, height, depth):
	pos = mc.player.getPos()
	dir = mc.player.getDirection()
	pos1 = Vec3(pos.x + (5*dir.x),pos.y,pos.z + (5*dir.z))
	
	pos2 = Vec3(pos1.x + math.copysign(width - 1,dir.x),pos1.y + height - 1, pos1.z + math.copysign(depth - 1, dir.z) )

	mc.setBlocks(pos1.x,pos1.y,pos1.z,pos2.x,pos2.y,pos2.z,1)

def makeStairway(width,depth):
	pos = mc.player.getPos()
	dir = mc.player.getDirection()
	start_pos = Vec3(pos.x + (5*dir.x),pos.y,pos.z + (5*dir.z))
	pos1 = Vec3()
	pos2 = Vec3()

	for x in range(depth):
		pos1.x = start_pos.x
		pos1.y = start_pos.y + x
		pos1.z = start_pos.z + math.copysign(x, dir.z)

		pos2.x = start_pos.x + math.copysign(width, dir.x) + 1
		pos2.y = start_pos.y + x
		pos2.z = start_pos.z + math.copysign(depth - 1, dir.z)

		mc.setBlocks(pos1.x,pos1.y,pos1.z,pos2.x,pos2.y,pos2.z,1)

	



if __name__ == "__main__":
	mc.postToChat("OI")
	# for i in range(10):
	# 	makeBlockNearPlayer()
	# 	time.sleep(1)

	# makeBlocksNearPlayer(4,1,5)

	makeStairway(50, 44)

# makeBlockNearPlayer()