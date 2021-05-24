from ursina.prefabs.first_person_controller import FirstPersonController

from Map import *
from Voxel import *

y_set = generator()

app = Ursina()

for x in range(21):
    for z in range(21):
        Voxel(position=(x, y_set[x][z], z))

player = FirstPersonController()
app.run()
