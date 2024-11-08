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

class TitolidiCoda(Scene):
    def construct(self):
        pass

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
        # Create the square and circle
        square = Square(side_length=4, color=XKCD.BABYPURPLE).move_to(ORIGIN)
        circle = Circle(radius=2, color=XKCD.AZUL, fill_opacity=0.9, stroke_width=1).move_to(ORIGIN)
        self.play(Create(square), Create(circle))

        # Initialize display for π approximation and point count
        pi_text = Text("π ≈ 0", font_size=36).to_edge(UP)
        count_text = Text("Points: 0", font_size=36).next_to(pi_text, DOWN)
        self.play(Write(pi_text), Write(count_text))

        # Display the coordinates of the point on the left of the square
        point_text = Text("Point: (0, 0)", font_size=28).next_to(square, LEFT, buff=0.5)
        self.play(Write(point_text))

        # Display the effective distance on the right of the square
        distance_text = Text("Distance: 0.00", font_size=28).next_to(square, RIGHT, buff=0.5)
        self.play(Write(distance_text))

        # Variables for points and counters
        points = []
        n_inside = 0  
        total_points = 100  # Total number of points to display
        slow_phase_points = 10  # Number of points in the slow phase
        base_run_time = 0.2     # Initial run time for the slow phase

        for i in range(total_points):
            # Generate a random point in the square
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-2, 2)
            point = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
            points.append(point)
            
            # Set animation speed: slow for the first phase, then exponential
            if i < slow_phase_points:
                current_run_time = base_run_time
            else:
                current_run_time = base_run_time * (0.85 ** (i - slow_phase_points))  # Slightly less aggressive exponential decay
            
            # Animate the point creation
            self.play(Create(point), run_time=current_run_time)

            # Update point coordinates text dynamically
            new_point_text = Text(f"Point: ({x:.2f}, {y:.2f})", font_size=28).next_to(square, LEFT, buff=0.5)
            self.play(Transform(point_text, new_point_text), run_time=current_run_time)

            # Calculate distance from the origin to the point
            distance = np.sqrt(x**2 + y**2)
            new_distance_text = Text(f"Distance: {distance:.2f}", font_size=28).next_to(square, RIGHT, buff=0.5)
            self.play(Transform(distance_text, new_distance_text), run_time=current_run_time)

            # Determine color of vector based on point's location (inside or outside the circle)
            vector_color = XKCD.BRIGHTYELLOW if distance <= 2 else XKCD.BLOODRED
            vector = Arrow(start=ORIGIN, end=[x, y, 0], buff=0.1, color=vector_color, stroke_width=3)
            self.play(Create(vector), run_time=current_run_time)

            # Check if the point is inside the circle
            inside_circle = distance <= 2
            if inside_circle:
                n_inside += 1

            # Update the approximation of pi
            pi_value = 4 * n_inside / (i + 1)
            new_pi_text = Text(f"π ≈ {pi_value:.4f}", font_size=36).to_edge(UP)
            new_count_text = Text(f"Points: {i + 1}", font_size=36).next_to(new_pi_text, DOWN)
            self.play(Transform(pi_text, new_pi_text), Transform(count_text, new_count_text), run_time=current_run_time)

            # Show a check explanation for the first point
            if i == 0:
                # LaTeX version of the check explanation
                check_text = MathTex(
                    r"\text{Checking if } (x, y) \text{ is inside the circle:}",
                    r"\text{ Distance} = \sqrt{x^2 + y^2}",
                    r"\text{ Inside circle? Distance} \leq 2", 
                    font_size=24
                ).to_edge(DOWN)
                self.play(Write(check_text))
                self.wait(1)
                self.play(FadeOut(check_text))

            # Remove vector after each point to avoid clutter
            self.play(FadeOut(vector), run_time=current_run_time)

            # Pause after the slow phase for visual contrast
            if i == slow_phase_points - 1:
                pass
                #self.wait(.1)
                
        slow_phase_points = total_points
        current_total = slow_phase_points
        
        # Fast phase: Add multiple points per batch without the arrow
        self.wait(.1)  # Pause before fast phase for contrast
        
        
        ##############################################
        total_points += 200  # Define a large number of points for the fast phase
        batch_size = 10  # Number of points per batch in the fast phase
        # remove all the previous points
        self.play(FadeOut(point_text), FadeOut(distance_text), run_time=0.5)
        for i in range(slow_phase_points, total_points, batch_size):
            self.play(FadeOut(Group(*points)), run_time=0.1, lag_ratio=0.9)
            new_points = []
            
            n_inside_ = 0
            for _ in range(batch_size):
                
                x = np.random.uniform(-2, 2)
                y = np.random.uniform(-2, 2)
                point = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
                new_points.append(point)
                if np.sqrt(x**2 + y**2) <= 2:
                    n_inside_ += 1

            # Display the batch of points at once
            self.play(*[Create(p) for p in new_points], run_time=0.1, lag_ratio=0.9)
            points = new_points

            # Update π approximation and total count
            current_total += batch_size
            n_inside += n_inside_
            pi_value = 4 * n_inside / current_total
            new_pi_text = Text(f"π ≈ {pi_value:.5f}", font_size=36).to_edge(UP)
            new_count_text = Text(f"Points: {current_total}", font_size=36).next_to(new_pi_text, DOWN)
            self.play(Transform(pi_text, new_pi_text), Transform(count_text, new_count_text), run_time=0.1)
            

        # Fade out all elements at the end
        #self.wait(.1)
        #self.play(FadeOut(Group(*points)), run_time=0.1)
        #self.play(FadeOut(square), FadeOut(circle), FadeOut(pi_text), FadeOut(count_text), FadeOut(point_text), FadeOut(distance_text))
        
        #########################################
        ##########################################
        ##############################################
        current_total = total_points
        total_points += 2000  # Define a large number of points for the fast phase
        batch_size = 100  # Number of points per batch in the fast phase
        # remove all the previous points
        #self.play(FadeOut(Group(*points)), FadeOut(point_text), FadeOut(distance_text))
        for i in range(slow_phase_points, total_points, batch_size):
            self.play(FadeOut(Group(*points)), run_time=0.1, lag_ratio=0.9) 
            new_points = []
            
            n_inside_ = 0
            for _ in range(batch_size):
                
                x = np.random.uniform(-2, 2)
                y = np.random.uniform(-2, 2)
                point = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
                new_points.append(point)
                if np.sqrt(x**2 + y**2) <= 2:
                    n_inside_ += 1

            # Display the batch of points at once
            self.play(*[Create(p) for p in new_points], run_time=0.1)
            points = new_points

            # Update π approximation and total count
            current_total += batch_size
            n_inside += n_inside_
            pi_value = 4 * n_inside / current_total
            new_pi_text = Text(f"π ≈ {pi_value:.5f}", font_size=36).to_edge(UP)
            new_count_text = Text(f"Points: {current_total}", font_size=36).next_to(new_pi_text, DOWN)
            self.play(Transform(pi_text, new_pi_text), Transform(count_text, new_count_text), run_time=0.1, lag_ratio=0.1)
            

        # Fade out all elements at the end
        #self.wait(.1)
        #xself.play(FadeOut(Group(*points)), run_time=0.1)
        #self.play(FadeOut(square), FadeOut(circle),  FadeOut(point_text), FadeOut(distance_text))
        
        

        #########################################
        ##########################################
        #########################################
        ##########################################
        ##############################################
        current_total = total_points
        total_points += 10000000  # Define a large number of points for the fast phase
        batch_size = 50000  # Number of points per batch in the fast phase
        # remove all the previous points
        #self.play(FadeOut(Group(*points)))
        self.play(FadeOut(Group(*points)), run_time=0.1, lag_ratio=0.4) 
        self.play(FadeOut(circle), FadeOut(square))
        self.play(pi_text.animate.move_to(ORIGIN).scale(2), run_time=1)
        self.play(count_text.animate.move_to(ORIGIN+DOWN).scale(1), run_time=1)
        # animate pi text and count text in sync
        
        
        
        # move the pi text and the count text on the origin 
        new_pi_text = Text(f"π ≈ {pi_value:.5f}", font_size=36).to_edge(ORIGIN)
        new_count_text = Text(f"Points: {current_total}", font_size=36).next_to(new_pi_text, DOWN)  
        
        for i in range(slow_phase_points, total_points, batch_size):
            #self.play(FadeOut(Group(*points)), run_time=0.1, lag_ratio=0.1) 
            new_points = []
            
            n_inside_ = 0
            for _ in range(batch_size):
                
                x = np.random.uniform(-2, 2)
                y = np.random.uniform(-2, 2)
                #point = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
                #new_points.append(point)
                if np.sqrt(x**2 + y**2) <= 2:
                    n_inside_ += 1

            # Display the batch of points at once
            #self.play(*[Create(p) for p in new_points], run_time=0.1)
            points = new_points

            # Update π approximation and total count
            current_total += batch_size
            n_inside += n_inside_
            pi_value = 4 * n_inside / current_total
            new_pi_text = Text(f"π ≈ {pi_value:.8f}", font_size=36).to_edge(ORIGIN).scale(2)
            new_count_text = Text(f"Points: {current_total}", font_size=36).next_to(new_pi_text, DOWN)
            # self.play(FadeOut(*points), run_time=0.1)
            self.play(Transform(pi_text, new_pi_text), Transform(count_text, new_count_text), run_time=.1, lag_ratio=0.1)
            

        # Fade out all elements at the end
        self.wait(2)
        #self.play(FadeOut(Group(*points)), run_time=0.1)
        #self.play(FadeOut(square), FadeOut(circle), FadeOut(pi_text), FadeOut(count_text), FadeOut(point_text), FadeOut(distance_text))
        self.play(FadeOut(pi_text), FadeOut(count_text))
        #########################################       z<>,M
        ##########################################
        
        # now
        
       
       
       
       
       
       
       
       
       
       
       
       

        # now
        
       
       
       
       
       
       
       
       
       
       
       
       
