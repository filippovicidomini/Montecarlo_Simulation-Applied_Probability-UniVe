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
        total_points = 30

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