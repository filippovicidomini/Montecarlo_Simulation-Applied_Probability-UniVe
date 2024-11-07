# in this fil im going to write a 10 minutes video using the library manim 
# and the library numpy to generate random numbers, to explain to a class what is a monte carlo simulation 
# and some kind of application of it, for exapmle the calculation of pi, and other examples 
# everi section will be divided in class and the video will be divided in 10 minutes

import numpy as np
from manim import *

# VIDEO PARAETERS FOR QUALITY OUTPUT to change only for the final video 'cause it takes a lot of time to render when set to 4k 60fps. 
#config.pixel_height = 1080
#config.pixel_width = 1920
#config.frame_rate = 30
#config.tex_template = TexTemplateLibrary.simple

class FinalVideo(Scene):
    """In this class we'll create the final video with all the sections combined.
     # how to use it:
     once you created a class for a part of the video, you can add it to the final video with the following code:
     write a part for example AAA:
     class AAA(MovingCameraScene):
        def construct(self):
            # code for the section
            pass
            
    once you finit edit the AAA section you can add it to the final video with the following code: 
            
    class FinalVideo(Scene):
        def construct(self):
            AAA.construct(self)
            BBB.construct(self)
            CCC.construct(self)
            # and so on
    

    Args:
        Scene (manim.Scene): Manim Scene class.
    """
    
class Background(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=300, opacity=0.2).rotate(PI / 2).scale(2)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=.1)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)  # #
        
        
        
class Introduction(Scene):
    def construct(self):
        # Introduction to the video
        title = Text("Monte Carlo Simulation", color=WHITE).scale(1.5)
        self.play(Write(title), run_time=4, rate_func=linear)
        self.wait()
        self.play(title.animate.shift(UP * 3).scale(0.7), run_time=2.5, rate_func=smooth)
        
        # faiin modo che il testo vada a capo nel punto giusto 
        intro_text = Text("Monte Carlo simulation \n is a technique used to understand \n the impact of risk and uncertainty in prediction and forecasting models. \n"
                          "It is a statistical method that uses random sampling to solve mathematical problems. \n"
                          "In this video, we will explore the concept of Monte Carlo simulation and its applications in various fields.", color=WHITE).scale(0.7)
        
        self.play(Write(intro_text), run_time=2, rate_func=linear)
        self.wait()

        self.play(FadeOut(title), FadeOut(intro_text), run_time=1.5, rate_func=smooth)