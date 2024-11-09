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
        
class MonteCarlo(Scene): # per pi greco funziona bene
    def construct(self):
        # Creazione del quadrato e del cerchio
        square = Square(side_length=4, color=XKCD.BABYPURPLE).move_to(ORIGIN)
        circle = Circle(radius=2, color=XKCD.AZUL, fill_opacity=0.9, stroke_width=1).move_to(ORIGIN)
        self.play(Create(square), Create(circle))

        # Inizializzazione della visualizzazione per l'approssimazione di π e conteggio punti
        pi_text = Text("π ≈ 0", font_size=36).to_edge(UP)
        count_text = Text("Points: 0", font_size=36).next_to(pi_text, DOWN)
        self.play(Write(pi_text), Write(count_text))

        # Testo per le coordinate del punto a sinistra del quadrato
        point_text = Text("Point: (0, 0)", font_size=28).next_to(square, LEFT, buff=0.5)
        self.play(Write(point_text))

        # Testo per la distanza effettiva a destra del quadrato
        distance_text = Text("Distance: 0.00", font_size=28).next_to(square, RIGHT, buff=0.5)
        self.play(Write(distance_text))

        # Variabili per i punti e i contatori
        points = []
        n_inside = 0  
        total_points = 100  # Numero totale di punti da visualizzare
        slow_phase_points = 10  # Numero di punti nella fase lenta
        base_run_time = 0.2     # Tempo di esecuzione iniziale per la fase lenta

        # Fase lenta per animare i singoli punti
        for i in range(total_points):
            # Genera un punto casuale nel quadrato
            x, y = np.random.uniform(-2, 2), np.random.uniform(-2, 2)
            point = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
            points.append(point)
            
            # Imposta la velocità di animazione: lenta per i primi punti, poi esponenziale
            current_run_time = base_run_time if i < slow_phase_points else base_run_time * (0.85 ** (i - slow_phase_points))
            
            # Anima la creazione del punto
            self.play(Create(point), run_time=current_run_time)

            # Aggiorna le coordinate del punto
            new_point_text = Text(f"Point: ({x:.2f}, {y:.2f})", font_size=28).next_to(square, LEFT, buff=0.5)
            self.play(Transform(point_text, new_point_text), run_time=current_run_time)

            # Calcola la distanza dall'origine
            distance = np.sqrt(x**2 + y**2)
            new_distance_text = Text(f"Distance: {distance:.2f}", font_size=28).next_to(square, RIGHT, buff=0.5)
            self.play(Transform(distance_text, new_distance_text), run_time=current_run_time)

            # Determina il colore del vettore basato sulla posizione del punto (dentro o fuori dal cerchio)
            vector_color = XKCD.BRIGHTYELLOW if distance <= 2 else XKCD.BLOODRED
            vector = Arrow(start=ORIGIN, end=[x, y, 0], buff=0.1, color=vector_color, stroke_width=3)
            self.play(Create(vector), run_time=current_run_time)

            # Verifica se il punto è dentro il cerchio
            if distance <= 2:
                n_inside += 1

            # Aggiorna l'approssimazione di pi
            pi_value = 4 * n_inside / (i + 1)
            new_pi_text = Text(f"π ≈ {pi_value:.4f}", font_size=36).to_edge(UP)
            new_count_text = Text(f"Points: {i + 1}", font_size=36).next_to(new_pi_text, DOWN)
            self.play(Transform(pi_text, new_pi_text), Transform(count_text, new_count_text), run_time=current_run_time)

            # Rimuovi il vettore dopo ogni punto per evitare disordine
            self.play(FadeOut(vector), run_time=current_run_time)

        # Fase rapida: aggiunta di punti multipli per batch senza il vettore
        self.wait(.3)  # Pausa prima della fase rapida per il contrasto
        
        total_points += 200  # Definisci un numero elevato di punti per la fase rapida
        batch_size = 10  # Numero di punti per batch nella fase rapida
        self.play(FadeOut(point_text), FadeOut(distance_text), run_time=0.5)
        
        for i in range(slow_phase_points, total_points, batch_size):
            new_points = []
            n_inside_ = 0
            for _ in range(batch_size):
                x, y = np.random.uniform(-2, 2), np.random.uniform(-2, 2)
                point = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
                new_points.append(point)
                if np.sqrt(x**2 + y**2) <= 2:
                    n_inside_ += 1

            # Visualizza il batch di punti contemporaneamente
            self.play(*[Create(p) for p in new_points], run_time=0.1)
            points = new_points

            # Aggiorna l'approssimazione di π e il conteggio totale
            current_total = i + batch_size
            n_inside += n_inside_
            pi_value = 4 * n_inside / current_total
            new_pi_text = Text(f"π ≈ {pi_value:.5f}", font_size=36).to_edge(UP)
            new_count_text = Text(f"Points: {current_total}", font_size=36).next_to(new_pi_text, DOWN)
            self.play(Transform(pi_text, new_pi_text), Transform(count_text, new_count_text), run_time=0.1)
            
        # Dissolvi tutti gli elementi al termine
        self.wait(2)
        self.play(FadeOut(square), FadeOut(circle), FadeOut(pi_text), FadeOut(count_text), FadeOut(Group(*points)))
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
        
class Credits(Scene): # da sistemare
    def construct(self):
        # Display "Created by:" at the top
        created_by_text = Text("Created by:", font_size=36)
        created_by_text.to_edge(UP)
        self.play(Write(created_by_text))
        
        # Display the names in a list at the center
        names = ["Filippo Vicidomini", "Nome 2", "Nome 3", "Nome 4"]
        names_text = VGroup(*[Text(name, font_size=40) for name in names])
        names_text.arrange(DOWN, center=True)
        self.play(Write(names_text, shift=UP))

        # Display "University Ca' Foscari of Venice" at the bottom
        university_text = Text("University Ca' Foscari of Venice", font_size=36)
        university_text.to_edge(DOWN)
        self.play(Write(university_text))

        # Fade out all elements
        self.wait(2)
        self.play(FadeOut(created_by_text), FadeOut(names_text), FadeOut(university_text))

class PythonCodeScene(Scene): # DONE 
    # https://stackoverflow.com/questions/76197478/how-do-i-highlight-one-line-of-code-in-manim
    def construct(self):
        # Codice Python da visualizzare
        code = '''from random import random, sqrt\nimport numpy as np\n
        
def monte_carlo_pi(n):
    #in this function we calculate the value 
    #of pi using the monte carlo method
       
    inside_circle = 0
    
    for _ in range(n):
        x, y = random(), random()
        
        if sqrt(x**2 + y**2) <= 1:
            inside_circle += 1
            
    return (inside_circle / n) * 4'''

        # Creazione dell'oggetto Code per visualizzare il codice Python
        python_code = Code(
            code=code,
            tab_width=4,
            background_stroke_width=0,
            language="Python",
            font_size=28,
            insert_line_no=False,
            style="monokai",
        )

        # Posizionamento del codice nella scena
        python_code.to_edge(UP)  # Sposta il codice verso l'alto

        # Animazione per mostrare il codice
        self.play(Write(python_code), run_time=20, lag_ratio=0.9)
        self.wait(2)
        

from manim import *
import numpy as np

from manim import *
import numpy as np

from manim import *
import numpy as np

from manim import *
import numpy as np

class MonteCarloIntegration(Scene):
    def construct(self):
        # Parameters
        a, b = 0, 2.5                     # Integration interval [a, b]
        func = lambda x: np.sin(x) + 1  # Function to integrate: f(x) = sin(x) + 1
        y_max = 2.5                     # Maximum y-value for bounding box
        n_points = 10000                # Total number of points for Monte Carlo simulation
        batch_size = 1000                 # Number of points shown per update
        max_display_dots = 100           # Maximum number of dots displayed on screen
        dot_radius = 0.025              # Radius of dots
        axis_length = (6, 4)            # Length of x and y axes

        # Calculated integral area for bounding rectangle
        integral_area = abs(b - a) * y_max

        # Axes setup
        axes = Axes(
            x_range=[a, b + 0.5, 0.5],
            y_range=[0, y_max, 0.5],
            x_length=axis_length[0],
            y_length=axis_length[1],
            axis_config={"include_tip": True},
        ).add_coordinates()
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))

        # Plot the function f(x)
        func_graph = axes.plot(func, color=BLUE)
        self.play(Create(func_graph), run_time=4)

        # Monte Carlo points within bounding box
        under_curve_points = 0  # Counter for points under the curve
        dot_group = VGroup()
        estimate_text = MathTex(r"\text{Estimated Area} \approx 0.0000")
        estimate_text.next_to(axes, DOWN)
        self.play(Write(estimate_text))

        # Loop through points in batches
        for i in range(0, n_points, batch_size):
            new_dots = VGroup()
            batch_under_curve = 0

            # Generate a batch of random points and count those under the curve
            for _ in range(batch_size):
                x_rand = np.random.uniform(a, b)
                y_rand = np.random.uniform(0, y_max)
                dot = Dot(axes.c2p(x_rand, y_rand), radius=dot_radius)

                # Determine color based on whether the point is under the curve
                if y_rand <= func(x_rand):
                    dot.set_color(GREEN)
                    batch_under_curve += 1
                else:
                    dot.set_color(RED)

                new_dots.add(dot)

            # Update overall count and estimation
            under_curve_points += batch_under_curve
            area_estimate = (under_curve_points / (i + batch_size)) * integral_area
            new_estimate_text = MathTex(r"\text{Estimated Area} \approx " + f"{area_estimate:.4f}")
            new_estimate_text.next_to(axes, DOWN)

            # Remove excess dots if necessary to limit displayed dots
            if len(dot_group) + len(new_dots) > max_display_dots:
                dot_group.submobjects = dot_group.submobjects[len(new_dots):]

            dot_group.add(*new_dots)  # Add new dots to the group

            # Animate the dots and update the estimate text
            self.play(Create(new_dots), Transform(estimate_text, new_estimate_text), run_time=0.5, LagRatio=0.9)

        # Display final result
        final_estimate = (under_curve_points / n_points) * integral_area
        final_text = MathTex(r"\text{Final Estimated Area} \approx " + f"{final_estimate:.4f}")
        final_text.next_to(axes, DOWN)
        self.play(Transform(estimate_text, final_text), run_time=2)
        self.wait(2)