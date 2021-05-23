from ursina.prefabs.first_person_controller import FirstPersonController

from Noises import *
from Voxel import *

app = Ursina()

Voxel((0, 0, 0))

for z in range(16):
    for x in range(16):
        s = combined(x, z)
        y = round(s / 4)
        Voxel(position=(x, round(y / 4), z))

        print(x, y, z)

        for y_coord in range(-5, y + 1):
            Voxel(position=(x, y_coord, z))

player = FirstPersonController()

app.run()
