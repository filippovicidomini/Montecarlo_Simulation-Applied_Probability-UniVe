 # in this file i'll make a monte carlo simulation to calculate the value of pi using the graphical library manim 
    # and the library numpy to generate random numbers
    # the idea is to generate random points in a square and calculate the number of points that are inside a circle
    # then the value of pi is calculated as 4 * (number of points inside the circle) / (total number of points)
from manim import *
import numpy as np

#config.frame_rate = 30

# schermo 1920x1080 
#factor = 2
#config.pixel_height = 108 * factor

#config.pixel_width = 192 * factor
# same font as 3blue1brown
#config.tex_template = TexTemplateLibrary.simple
# make it in 4k resolution

from manim import *

class FinalVideo(Scene): # HERE PUT ALL THE SCENE TOGETHER calling scene.construct(self)
    def construct(self):
        PiEstimation.construct(self)
        self.wait(2)
        MonteCarlo.construct(self)

class PiEstimation(Scene): # DONE
    def construct(self):
        # Title
        title = Text("Estimating Pi with MonteCarlo Simulation").to_edge(ORIGIN)
        self.play(Write(title))
        self.play(title.animate.shift(3 * UP).scale(0.8))
        
        # Circle and square
        circle_radius = 2
        circle = Circle(radius=circle_radius, color=BLUE, fill_opacity=0.3)
        square = Square(side_length=2*circle_radius, color=WHITE)
        
        # Center shapes on screen
        shapes = VGroup(square, circle).move_to(ORIGIN + 3 * RIGHT)
        
        # Radius line and label
        radius_line = Line(start=circle.get_center(), end=circle.get_right(), color=YELLOW)
        radius_label = MathTex("r").next_to(radius_line, UP, buff=0.1)

        # Formulas for areas
        area_circle = MathTex(r"A_C = \pi r^2", font_size=72).shift(3.5 * LEFT + 2 * UP)
        area_square = MathTex(r"A_S = (2r)^2 = 4r^2", font_size=72).next_to(area_circle, DOWN, aligned_edge=LEFT)
        
        # Apply color using indexing and slicing
        area_circle[0][0:2].set_color(YELLOW)  # A_C in yellow
        area_circle[0][3:4].set_color(RED)     # \pi in red
        #area_circle[0][5:6].set_color(BLUE)    # r in blue
        #area_circle[0][6:].set_color(BLUE)     # r^2 in blue
        
        area_square[0][0:2].set_color(GREEN)   # A_S in green
        #area_square[0][4:5].set_color(BLUE)    # r in blue
        #area_square[0][7:8].set_color(BLUE)     # r^2 in blue
        #area_square[0][9:10].set_color(BLUE)   
        #area_square[0][9:1].set_color(BLUE)     

        # Step-by-step derivation with each formula
        formula_position = 1 * DOWN + 3.5 * LEFT
        ratio_formula_1 = MathTex(r"\frac{A_C}{A_S} = \frac{\pi r^2}{4r^2}", font_size=72).move_to(formula_position)
        ratio_formula_2 = MathTex(r"\frac{A_C}{A_S} = \frac{\pi}{4}", font_size=72).move_to(formula_position)
        pi_formula_final = MathTex(r"\pi = \frac{4 \cdot A_C}{A_S}", font_size=72).move_to(formula_position)
        
        # Apply colors using indexing and slicing for ratio formulas
        ratio_formula_1[0][0:2].set_color(YELLOW)   # A_C in yellow
        ratio_formula_1[0][3:5].set_color(GREEN)    # A_S in green
        ratio_formula_1[0][6:7].set_color(RED)      # \pi in red
        # ratio_formula_1[0][8:9].set_color(BLUE)     # r in blue
        #ratio_formula_1[0][9:10].set_color(BLUE)     # r^2 in blue
        
        ratio_formula_2[0][0:2].set_color(YELLOW)   # A_C in yellow
        ratio_formula_2[0][3:5].set_color(GREEN)    # A_S in green
        ratio_formula_2[0][6:7].set_color(RED)      # \pi in red
        
        pi_formula_final[0][0:1].set_color(RED)   # A_C in yellow
        pi_formula_final[0][4:6].set_color(YELLOW)    # A_S in green
        pi_formula_final[0][8:9].set_color(GREEN)      # \pi in red

        # Animations
        self.play(Create(shapes), run_time=2)
        self.play(Create(radius_line), Write(radius_label), run_time=2)
        
        # Display each part of the formulas
        self.play(Write(area_circle), run_time=2)
        self.play(Write(area_square), run_time=2)
        
        # Show ratio formula step-by-step, keeping the position constant
        self.play(Write(ratio_formula_1), run_time=2)
        self.wait(1)
        self.play(Transform(ratio_formula_1, ratio_formula_2), run_time=2)
        self.wait(1)
        
        # Transform directly to the final formula for π and move to center, enlarging it
        self.play(Transform(ratio_formula_1, pi_formula_final), run_time=2)
        self.wait(1)
        
        # Reapply the colors explicitly after the transformation to ensure correctness
        pi_formula_final[0][0:1].set_color(RED)   # A_C in yellow
        pi_formula_final[0][3:5].set_color(YELLOW)    # A_S in green
        pi_formula_final[0][6:8].set_color(GREEN)      # \pi in red

        # Remove square and circle, and center the enlarged final formula
        self.play(FadeOut(shapes), FadeOut(radius_line), FadeOut(radius_label), FadeOut(area_circle), FadeOut(area_square))
        self.play(FadeOut(ratio_formula_1), run_time=1)
        self.play(Write(pi_formula_final.move_to(ORIGIN).scale(2)))
        
        self.wait(2)
        # clean up
        
        self.play(FadeOut(pi_formula_final), FadeOut(title))
        
        self.wait(1)
        
class MonteCarlo(Scene):
    def construct(self):
        # Create the square
        square = Square(side_length=4, color=BLUE)
        square.move_to(ORIGIN)
        self.play(Create(square))

        # Create the circle
        circle = Circle(radius=2, color=RED, fill_opacity=0.5, stroke_width=1)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

        # Initialize the display for pi value and total point count
        pi_text = Text("π ≈ 0", font_size=36).to_edge(UP)
        self.play(Write(pi_text))

        count_text = Text("Points: 0", font_size=36).next_to(pi_text, DOWN)
        self.play(Write(count_text))

        # Create the points and update the pi value and point count dynamically
        points = []
        n_inside = 0
        total_points = 30 # number of points to generate

        for i in range(total_points):
            # Generate a random point in the square
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-2, 2)
            point = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
            points.append(point)
            self.play(Create(point), run_time=0.01)

            # Check if the point is inside the circle
            
            if np.sqrt(x**2 + y**2) <= 2:
                n_inside += 1

            # Calculate and update the value of pi
            pi_value = 4 * n_inside / len(points)
            new_pi_text = Text(f"π ≈ {pi_value:.4f}", font_size=36).to_edge(UP)

            # Update the total point count
            new_count_text = Text(f"Points: {i+1}", font_size=36).next_to(new_pi_text, DOWN)

            # Replace the old pi value and count with the updated ones
            self.play(Transform(pi_text, new_pi_text), Transform(count_text, new_count_text), run_time=0.1)

        self.wait(2)
        self.play(FadeOut(square), FadeOut(circle))
        self.wait(1)
        self.play(FadeOut(Group(*points)))
        self.wait(1)