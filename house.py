# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MPCI must be open and in a world at this time)
mc = Minecraft.create()

length = 10
height = 10
width = 10

x = int(input("X Coordinate: "))
y = int(input("Y Coordinate: "))
z = int(input("Z Coordinate: "))

mc.setBlocks(x, y, z, x + width, y + height, z + length, 3)
             
