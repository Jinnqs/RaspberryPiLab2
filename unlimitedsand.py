# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MPCI must be open and in a world at this time)
mc = Minecraft.create()
import time

count = 0;
while count < 5:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y - 1, pos.z, 12)
    time.sleep(1)

 
