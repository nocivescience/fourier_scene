from manim import *
class FourierScene(Scene):
    Config={
        'n_vectors':12,
        'vector_config': {
            'color': BLUE,
            'max_tip_length_to_length_ratio': 0.25,
            'tip_length': 0.15,
            'max_stroke_width_to_length_ratio': 0.005,
            'stroke_width': 1,
        },
        'time': 0,
    }
    def construct(self):
        self.add(self.get_vectors_rotating())
        self.wait(2)
    def get_vectors_rotating(self, freqs=None, coeffs=None):
        vectors= VGroup()
        for n in range(1, self.Config['n_vectors']+1):
            vector= self.get_vector_rotating(n, self.Config['vector_config']['color'])
            vectors.add(vector)
        return vectors
    def get_vector_rotating(self, coefficient, freq, center_func=None):
        vector= Vector(RIGHT, **self.Config['vector_config'])
        vector.add_updater(lambda v: self.get_update_vector(v, dt))
        return vector
    def get_update_vector(self, vector, dt):
        time= self.Config['time']
        vector.rotate(time, about_point=ORIGIN)