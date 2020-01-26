# This program will calculate the number of tiles
# required when tiling a wall in (m2)

length = int (input("Enter Room length:"))
width = int (input("Enter Room width:"))

area = length * width

tilesneeded = area * 1.05

print(tilesneeded,"m2")