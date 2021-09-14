from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import math, random

import time

mc = Minecraft.create()


def makeBlockNearPlayer():
	pos = mc.player.getPos()
	dir = mc.player.getDirection()
	mc.setBlock(pos.x+(5*dir.x),pos.y,pos.z+(5*dir.z),1)
	# mc.setBlock(pos.x+5,pos.y,pos.z,1)

def makeBlocksNearPlayer(width, height, depth):
	player_pos = mc.player.getPos()
	dir = mc.player.getDirection()
	pos1 = Vec3(player_pos.x + (5*dir.x),player_pos.y,player_pos.z + (5*dir.z))
	
	pos2 = Vec3(pos1.x + math.copysign(width - 1,dir.x),pos1.y + height - 1, pos1.z + math.copysign(depth - 1, dir.z) )

	mc.setBlocks(pos1.x,pos1.y,pos1.z,pos2.x,pos2.y,pos2.z,1)

def getStartPos():
	player_pos = mc.player.getPos()
	player_dir = mc.player.getDirection()
	start_pos = Vec3(player_pos.x + (5*player_dir.x),player_pos.y,player_pos.z + (5*player_dir.z))
	return start_pos

def makeStairway(width,depth):
	start_pos = getStartPos()
	player_dir = mc.player.getDirection()

	pos1 = Vec3()
	pos2 = Vec3()

	for x in range(depth):
		pos1.x = start_pos.x
		pos1.y = start_pos.y + x
		pos1.z = start_pos.z + math.copysign(x, player_dir.z)

		pos2.x = start_pos.x + math.copysign(width, player_dir.x) + 1
		pos2.y = start_pos.y + x
		pos2.z = start_pos.z + math.copysign(depth - 1, player_dir.z)

		mc.setBlocks(pos1.x,pos1.y,pos1.z,pos2.x,pos2.y,pos2.z,1)

def makeFourPillars(width, height, depth, material):
	start_pos = getStartPos()
	player_dir = mc.player.getDirection()
	pos1 = Vec3()
	pos2 = Vec3()

	for i in range(4):
		print(start_pos.x)
		x = start_pos.x + ((int(i/2) % 2) * math.copysign(width, player_dir.x)) 
		z = start_pos.z + ((i % 2 ) * math.copysign(depth, player_dir.z))
		pos1.x = x
		pos1.y = start_pos.y 
		pos1.z = z

		pos2.x = x
		pos2.y = start_pos.y + height - 1
		pos2.z = z
		mc.setBlocks(pos1.x,pos1.y,pos1.z,pos2.x,pos2.y,pos2.z,material)

def makeCubePoints(width, height, depth, material):
	start_pos = getStartPos()
	player_dir = mc.player.getDirection()
	pos1 = Vec3()
	pos2 = Vec3()

	cube_points = [8]

	for i in range(8):
		point = Vec3(start_pos.x + ((i % 2) * width), start_pos.y + ((int(i/2) % 2) * height), start_pos.z + ((int(i/4) % 2) * depth))
		cube_points.append(point) 
		mc.setBlock(point.x,point.y,point.z,1)
		time.sleep(1)

def makeHollowCube(width, height, depth, material):
	start_pos = getStartPos()
	player_dir = mc.player.getDirection()
	# cube_points[i] = Vec3()
	# cube_points[i+1] = Vec3()

	cube_points = []

	for i in range(8):
		point = Vec3(start_pos.x + ((i % 2) * width), start_pos.y + ((int(i/2) % 2) * height), start_pos.z + ((int(i/4) % 2) * depth))
		cube_points.append(point) 
		
	for i in range(len(cube_points)-1):
		# print(cube_points[i].x)
		mc.setBlocks(cube_points[i].x,cube_points[i].y,cube_points[i].z,cube_points[i+1].x,cube_points[i+1].y,cube_points[i+1].z,material)

def makeCubeOutline(width, height, depth, material):
	start_pos = getStartPos()
	player_dir = mc.player.getDirection()
	# cube_points[i] = Vec3()
	# cube_points[i+1] = Vec3()

	cube_points = []

	for i in range(8):
		point = Vec3(start_pos.x + ((i % 2) * width), start_pos.y + ((int(i/2) % 2) * height), start_pos.z + ((int(i/4) % 2) * depth))
		cube_points.append(point) 
		
	for i in range(4):
		# print(cube_points[i].x)
		sec_point = i+4
		mc.setBlocks(cube_points[i].x,cube_points[i].y,cube_points[i].z,cube_points[sec_point].x,cube_points[sec_point].y,cube_points[sec_point].z,material)
		time.sleep(1)
	
	for i in {0,2,4,6}:
		sec_point = i + 1
		mc.setBlocks(cube_points[i].x,cube_points[i].y,cube_points[i].z,cube_points[sec_point].x,cube_points[sec_point].y,cube_points[sec_point].z,material)
		time.sleep(1)
	
	for i in {0,1,4,5}:
		sec_point = i + 2
		mc.setBlocks(cube_points[i].x,cube_points[i].y,cube_points[i].z,cube_points[sec_point].x,cube_points[sec_point].y,cube_points[sec_point].z,material)
		time.sleep(1)
		

def makeTwoPillars(pos1,pos2, height, material):
		mc.setBlocks(pos1.x,pos1.y,pos1.z,pos1.x,pos1.y+height,pos1.z,material)
		mc.setBlocks(pos2.x,pos2.y,pos2.z,pos2.x,pos2.y+height,pos2.z,material)





if __name__ == "__main__":
	mc.postToChat("OI")
	# for i in range(10):
	# 	makeBlockNearPlayer()
	# 	time.sleep(1)
	random_material = random.randint(1,10)
	# makeBlocksNearPlayer(4,1,5)

	# makeStairway(50, 44)
	# makeFourPillars(5,20,5,1)
	makeCubePoints(5,5,5,random_material)
	makeCubeOutline(5,5,5,random_material)

# makeBlockNearPlayer()