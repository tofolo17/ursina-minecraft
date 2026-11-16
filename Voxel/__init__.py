from ursina import *


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            highlight_color=color.lime,
        )

    # Left click places a block on the hovered face; right click breaks it.
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)
