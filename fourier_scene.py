from manim import *

class RotatingVector(Scene):
    def construct(self):
        self.time = 0

        vector = Vector(RIGHT, color=BLUE)
        vector2= vector.copy()
        vector2.add_updater(lambda v: v.move_to(vector.get_end(), v.get_start()))
        vector.add_updater(self.rotate_vector)

        self.add(vector, vector2)
        self.wait(3)

    def rotate_vector(self, vector, dt):
        self.time += dt
        vector.become(Vector(RIGHT, color=BLUE).rotate(self.time, about_point=vector.get_start()))