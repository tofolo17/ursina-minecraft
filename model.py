from ursina.prefabs.first_person_controller import FirstPersonController

from Voxel import *

app = Ursina()

for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
app.run()
