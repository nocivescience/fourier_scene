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
    }
    def construct(self):
        self.add_vectors()
    def add_vectors(self):
        vectors=self.get_rotating_vectors()
        self.add(vectors)
        self.wait(4)
    def get_freqs(self, n=None):
        if n is None:
            n= self.config['n_vectors']
        all_freqs = list(np.arange(1,n+1))
        all_freqs.sort(reverse=True)
        return all_freqs
    def get_coef(self):
        return [complex(0) for _ in range(self.config['n_vectors'])]
    def get_rotating_vectors(self, freqs=None, coefs=None):
        if freqs is None:
            freqs=self.get_freqs()
        if coefs is None:
            coefs=self.get_coef()
        vectors=VGroup()
        self.center_tracker= VectorizedPoint(self.config['origin'])
        last_vector=None
        for freq, coef in zip(freqs, coefs):
            if last_vector is None:
                center_func=lambda: self.center_tracker.get_location()
            else:
                center_func=lambda: last_vector.get_end()
            vector=self.get_rotating_vector(freq, coef, center_func)
            vectors.add(vector) 
            last_vector=vector
        return vectors
    def get_rotating_vector(self, freq, coef, center_func):
        vector=Vector(RIGHT,**self.config['config_vector'])
        vector.scale(abs(coef))
        if abs(coef)>0:
            vector.set_color(self.config['config_vector']['color'])
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