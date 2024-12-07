# use manim to open a svg file and animate it

from manim import *

class SVGProva(Scene):
    def construct(self):
        svg = SVGMobject("assets/svg/samples-svgrepo-com")
        svg.set(width=3)
        svg.to_edge(RIGHT)
        
        self.add(
        svg
    )