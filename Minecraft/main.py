from ursina.prefabs.first_person_controller import FirstPersonController

from Map import *
from Voxel import *

size = 50
octave = 4  # Quanto menor o tamanho, menor deve ser a oitava
y_set = generator(size, octave)

app = Ursina()

for x in range(size):
    for z in range(size):
        Voxel(position=(x, y_set[x][z], z))

player = FirstPersonController()
app.run()
