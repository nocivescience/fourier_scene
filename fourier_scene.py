from manim import *
class VectorFourierScene(Scene):
    config={
        'config_vector': {
            'color': BLUE,
            'max_tip_length_to_length_ratio': 0.25,
            'tip_length': 0.25,
            'stroke_width': 1.2
        },
    }
    def construct(self):
        vector=self.get_rotating_vector()
        self.add(vector)
        self.wait(2)
    def get_rotating_vector(self, freq, coef, center_func):
        vector=Vector(RIGHT,**self.config['config_vector'])
        vector.freq=freq
        vector.coef=coef
        vector.center_func=center_func
        vector.add_updater(self.get_update_rotating_vector)
        return vector
    def get_update_rotating_vector(self, vector, dt):
        time=0
        time+= dt
        coef=vector.coef
        freq=vector.freq
        center_func=vector.center_func
        phase = coef
        vector.rotate(phase, about_point=vector.get_start())