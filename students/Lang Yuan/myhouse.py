import mcpi.minecraft as minecraft
import time
import mcpi.block as block
import random


def house(x0,y0,z0,L,W,H):
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    for j in range(L):#地板
        for i in range(W):
            mc.setBlock(x0+i, y0, z0+j, 43)
    for j in range(H):#墙壁1
        for i in range(W):
            mc.setBlock(x0, y0+j, z0+i, block.GOLD_ORE.id)
            mc.setBlock(x0+W-1, y0+j, z0+i, block.GOLD_ORE.id)
    for j in range(H):#墙壁2
        for i in range(L):
            mc.setBlock(x0+i, y0+j, z0, block.GOLD_ORE.id)
            mc.setBlock(x0+i, y0+j, z0+L-1, block.GOLD_ORE.id)
    for j in range(1):#火炬
        for i in range(2):
            mc.setBlock(x0+L/2+j, y0+1+i, z0, 50)
    for j in range(10):#隔断
      for i in range(10): 
            mc.setBlock(x0+L-j, y0-i, z0, 50)
    for j in range(10):#隔断
      for i in range(15): 
            mc.setBlock(x0+W-j, y0-i, z0, 50)
    for j in range(40):#隔断
      for i in range(10):        
            mc.setBlock(x0+H-1, y0+i+2, z0+j+4, 20)
    for j in range(L):#花纹
        for i in range(W):
            num=random.randint(0,8)
            if num==0:
                mc.setBlock(x0+i, y0+H, z0+j, 14)
            elif num==1:
                mc.setBlock(x0+i, y0+H, z0+j, 16)
            elif num==2:
                mc.setBlock(x0+i, y0+H, z0+j, 2)
            elif num==3:
                mc.setBlock(x0+i, y0+H, z0+j, 20)
            elif num==4:
                mc.setBlock(x0+i, y0+H, z0+j, 48)
            elif num==5:
                mc.setBlock(x0+i, y0+H, z0+j, 41)
            elif num==6:
                mc.setBlock(x0+i, y0+H, z0+j, 45)
            elif num==7:
                mc.setBlock(x0+i, y0+H, z0+j, 42)
            elif num==8:
                mc.setBlock(x0+i, y0+H, z0+j, 35)


mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.player.setTilePos([-300,10,-300])
pos = mc.player.getTilePos()
for z in range(3):#生成3*3*3共27个房子
    house(pos.x+z*20,pos.y,pos.z,10,10,10)
    house(pos.x+z*20,pos.y,pos.z+20,10,10,10)
    house(pos.x+z*20,pos.y,pos.z+40,10,10,10)
for z in range(3):
    house(pos.x+z*20,pos.y+20,pos.z,10,10,10)
    house(pos.x+z*20,pos.y+20,pos.z+20,10,10,10)
    house(pos.x+z*20,pos.y+20,pos.z+40,10,10,10)
for z in range(3):
    house(pos.x+z*20,pos.y+40,pos.z,10,10,10)
    house(pos.x+z*20,pos.y+40,pos.z+20,10,10,10)
    house(pos.x+z*20,pos.y+40,pos.z+40,10,10,10)
