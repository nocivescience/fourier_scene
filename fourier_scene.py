from manim import *
class VectorFourierScene(Scene):
    config={
        'n_vectors': 10,
        'config_vector': {
            'color': BLUE,
            'max_tip_length_to_length_ratio': 0.25,
            'tip_length': 0.25,
            'stroke_width': 1.2
        },
        'origin': ORIGIN,
        'time': 0,
    }
    def construct(self):
        pass
    def get_coef(self):
        return 3
    def get_freq(self):
        return 1
    def get_vectors(self):
        pass
    def get_vector(self, freq, coef, center_func):
        vector= Vector(RIGHT, **self.config['config_vector'])
        vector.freq= freq
        vector.coef= coef
        vector.center_func= center_func
        vector.add_updater(self.get_update_vector)
        return vector
    def get_update_vector(self, vector, dt):
        self.config['time']+= dt
        freq= vector.freq
        coef= vector.coef
        center_func= vector.center_func
        vector.become(Vector(RIGHT, **self.config['config_vector']).rotate(coef*np.cos(freq*self.config['time'])*RIGHT))
        vector.shift(center_func(self.config['time'])-vector.get_start())
        vector.rotate()