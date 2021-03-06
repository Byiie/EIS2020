import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def roof(x,y,z,L,num):
    reader = csv.reader(open(str(num)+'.csv'))
    data=[]
    for r in reader:
        data.append(r)
    for i in range(10):
        for j in range(10):
            if (data[j][i]=='1'):
                mc.setBlock(x+i,y+5,z+j,75)
                
def house(x,y,z,L):
    mc.setBlocks(x,y-1,z,x+L,y+5,z+L,5,block.GOLD_ORE.id)
    mc.setBlocks(x+1,y,z+1,x+L-1,y+4,z+L-1,0)       #立方体
    mc.setBlocks(x+3,y+1,z,x+4,y+2,z,block.GLASS.id)#窗
    mc.setBlocks(x+6,y,z,x+6,y+1,z,50)              #门

x0=pos.x+1
y0=pos.y
z0=pos.z
L0=9
count=1
for i in range(3):                  
    z0=pos.z
    for j in range(3):
        x0=pos.x+1
        for k in range(3):
            house(x0,y0,z0,L0)
            roof(x0,y0,z0,L0,count)
            count += 1
            x0=x0+L0+5
        z0=z0+L0+5
    y0=y0+6+10
