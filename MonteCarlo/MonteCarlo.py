 # in this file i'll make a monte carlo simulation to calculate the value of pi using the graphical library manim 
    # and the library numpy to generate random numbers
    # the idea is to generate random points in a square and calculate the number of points that are inside a circle
    # then the value of pi is calculated as 4 * (number of points inside the circle) / (total number of points)
import random
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
        self.wait
        PseudoRandomNumberGeneration.construct(self)
        self.wait(2)
        PiEstimation.construct(self)
        self.wait(2)
        MonteCarlo.construct(self)
        self.wait(2)
        PythonCodeScene.construct(self)
        self.wait(2)
        MonteCarloIntegration.construct(self)
        self.wait(2)
        MonteCarloIntegration3D.construct(self)
        self.wait(2)
        Credits.construct(self)
        

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
        self.play(Create(shapes), run_time=3)
        self.play(Create(radius_line), Write(radius_label), run_time=3)
        
        # Display each part of the formulas
        self.play(Write(area_circle), run_time=3)
        self.play(Write(area_square), run_time=3)
        
        # Show ratio formula step-by-step, keeping the position constant
        self.play(Write(ratio_formula_1), run_time=3)
        self.wait(1)
        self.play(Transform(ratio_formula_1, ratio_formula_2), run_time=3)
        self.wait(1)
        
        # Transform directly to the final formula for π and move to center, enlarging it
        self.play(Transform(ratio_formula_1, pi_formula_final), run_time=3)
        self.wait(1)
        
        # Reapply the colors explicitly after the transformation to ensure correctness
        pi_formula_final[0][0:1].set_color(RED)   # A_C in yellow
        pi_formula_final[0][3:5].set_color(YELLOW)    # A_S in green
        pi_formula_final[0][6:8].set_color(GREEN)      # \pi in red

        # Remove square and circle, and center the enlarged final formula
        self.play(FadeOut(shapes), FadeOut(radius_line), FadeOut(radius_label), FadeOut(area_circle), FadeOut(area_square), run_time=2)
        self.play(FadeOut(ratio_formula_1), run_time=2)
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
        base_run_time = 0.4     # Tempo di esecuzione iniziale per la fase lenta

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
        self.play(FadeOut(point_text), FadeOut(distance_text), FadeOut(*points), run_time=1.5)
        
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
            self.play(*[Create(p) for p in new_points], run_time=0.2)
            points = new_points

            # Aggiorna l'approssimazione di π e il conteggio totale
            current_total = i + batch_size
            n_inside += n_inside_
            pi_value = 4 * n_inside / current_total
            new_pi_text = Text(f"π ≈ {pi_value:.5f}", font_size=36).to_edge(UP)
            new_count_text = Text(f"Points: {current_total}", font_size=36).next_to(new_pi_text, DOWN)
            self.play(Transform(pi_text, new_pi_text), Transform(count_text, new_count_text), run_time=0.2)
            self.play(FadeOut(*points), run_time=0.1)
        # Dissolvi tutti gli elementi al termine
        self.wait(2)
        #self.play(FadeOut(square), FadeOut(circle), FadeOut(pi_text), FadeOut(count_text), FadeOut(Group(*points)))
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
        self.play(FadeOut(Group(*points)))
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
            
        self.play(FadeOut(square), FadeOut(circle), FadeOut(pi_text), FadeOut(count_text), FadeOut(Group(*points)))
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
        #self.play(FadeOut(Group(*points)), run_time=0.2, lag_ratio=0.9) 
        self.play(FadeOut(circle), FadeOut(square))
        self.play(pi_text.animate.move_to(ORIGIN).scale(2), run_time=1)
        self.play(count_text.animate.move_to(pi_text.get_bottom() + DOWN), run_time=1)
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
        names = ["Filippo Vicidomini", "Damiano Bacchin", "Nina Marlis Duerfeld", "Federico Segala", "Giacomo Scocca"]
        names_text = VGroup(*[Text(name, font_size=40) for name in names])
        names_text.arrange(DOWN, center=True)
        self.play(Write(names_text, shift=UP), run_time=20)

        # Display "University Ca' Foscari of Venice" at the bottom
        university_text = Text("University Ca' Foscari of Venice", font_size=36)
        university_text.to_edge(DOWN)
        self.play(Write(university_text))

        # Fade out all elements
        self.wait(5)
        self.play(FadeOut(created_by_text), FadeOut(names_text), FadeOut(university_text), run_time=5)

class PythonCodeScene(Scene): # DONE 
    # https://stackoverflow.com/questions/76197478/how-do-i-highlight-one-line-of-code-in-manim
    def construct(self):
        # Codice Python da visualizzare
        code = '''from random import random, sqrt\n
        
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
        self.play(FadeOut(python_code))

class MonteCarloIntegration(Scene): # CARINO
    def construct(self):
        # Parameters
        a, b = 0, 2.5                     # Integration interval [a, b]
        func = lambda x: np.sin(x) + 1    # Function to integrate: f(x) = sin(x) + 1
        y_max = 2.5                       # Maximum y-value for bounding box
        n_points = 20000                  # Total number of points for Monte Carlo simulation
        batch_size = 2000                 # Number of points shown per update
        max_display_dots = 100            # Maximum number of dots displayed on screen
        dot_radius = 0.025                # Radius of dots
        axis_length = (7, 4)              # Length of x and y axes

        # Calculated integral area for bounding rectangle
        integral_area = abs(b - a) * y_max

        # Initial estimate text at the top with the integral formula
        initial_text = MathTex(
            r"\int_{" + f"{a}" + "}^{" + f"{b}" + r"} \left(\sin(x) + 1\right) \, dx \approx 4.30114"
        ).scale(0.7)
        initial_text.to_edge(UP)
        self.play(Write(initial_text))

        # Axes setup without y-axis label
        axes = Axes(
            x_range=[a-0.3, b + 0.2, 0.5],
            y_range=[0, y_max + 0.3, 0.5],
            x_length=axis_length[0],
            y_length=axis_length[1],
            axis_config={"include_tip": True},
        ).add_coordinates()
        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        self.play(Create(axes), Write(x_label), run_time=2)

        # Plot the function f(x)
        func_graph = axes.plot(func, color=BLUE)
        self.play(Create(func_graph), run_time=3)

        # Monte Carlo points within bounding box
        under_curve_points = 0  # Counter for points under the curve
        dot_group = VGroup()
        estimate_text = MathTex(r"\text{Estimated Area} \approx 0.0000")
        estimate_text.next_to(axes, DOWN)
        self.play(Write(estimate_text), run_time=2)

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
            #updated_integral_text = MathTex(
            #    r"\int_{" + f"{a}" + "}^{" + f"{b}" + r"} \left(\sin(x) + 1\right) \, dx \approx " + f"{area_estimate:.4f}"
            #).to_edge(UP)

            # Remove excess dots if necessary to limit displayed dots
            if len(dot_group) + len(new_dots) > max_display_dots:
                dot_group.submobjects = dot_group.submobjects[len(new_dots):]

            dot_group.add(*new_dots)  # Add new dots to the group

            # Animate the dots and update the estimate text
            self.play(
                Create(new_dots), 
                Transform(estimate_text, new_estimate_text),
                #Transform(initial_text, updated_integral_text), 
                run_time=2, 
                lag_ratio=0.9
            )

        # Final integral estimate
        #final_text = MathTex(
         #   r"\int_{" + f"{a}" + "}^{" + f"{b}" + r"} \left(\sin(x) + 1\right) \, dx \approx " + f"{area_estimate:.4f}"
        #).to_edge(UP)
        #self.play(Transform(initial_text, final_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(initial_text), FadeOut(axes), FadeOut(func_graph), FadeOut(dot_group), FadeOut(estimate_text), FadeOut(x_label), FadeOut(dot_group), run_time=2)
        # remove all the green and red dots

class MonteCarloIntegration3D(ThreeDScene): # lento ma funziona, da aggiungere visualizzazione valore vero
    def construct(self):
        # Parameters
        a, b = -1, 1
        func = lambda x, y: np.sin(x) + np.cos(y) + 1
        z_max = max(func(x, y) for x in np.linspace(a, b, 50) for y in np.linspace(a, b, 50))  # Reduced resolution for speed
        n_points = 1000       # Lower total points
        batch_size = 100      # Larger batch size for fewer updates
        max_display_dots = 50 # Limit displayed dots
        dot_radius = 0.07     # Smaller dot radius

        # Axes setup
        axes = ThreeDAxes(
            x_range=[a - 0.3, b + 0.2, 0.5],
            y_range=[a - 0.3, b + 0.2, 0.5],
            z_range=[0, z_max + 0.3, 0.5],
            axis_config={"include_tip": True},
        ).move_to(ORIGIN - RIGHT)

        # Set initial camera view without continuous rotation
        self.camera.set_zoom(0.6)
        self.play(Create(axes), run_time=2)

        # Define and create function surface with lower resolution
        func_surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[a, b],
            v_range=[a, b],
            resolution=(5, 5),  # Lower resolution
        ).set_color_by_gradient(BLUE, YELLOW)
        self.play(Create(func_surface), run_time=3)

        # Monte Carlo simulation
        under_surface_points = 0
        dot_group = VGroup()
        integral_area = (b - a) ** 2 * z_max

        # Only update dots and text every few batches to limit number of objects
        for i in range(0, n_points, batch_size):
            new_dots = VGroup()
            batch_under_surface = 0

            for _ in range(batch_size):
                x_rand, y_rand, z_rand = np.random.uniform(a, b), np.random.uniform(a, b), np.random.uniform(0, z_max)
                dot = Dot3D(point=axes.c2p(x_rand, y_rand, z_rand), radius=dot_radius)

                if z_rand <= func(x_rand, y_rand):
                    dot.set_color(GREEN)
                    batch_under_surface += 1
                else:
                    dot.set_color(RED)

                new_dots.add(dot)

            under_surface_points += batch_under_surface
            volume_estimate = (under_surface_points / (i + batch_size)) * integral_area

            # Display limited dots and text updates only every few batches
            if i % (batch_size * 2) == 0:
                self.play(FadeOut(dot_group))  # Clear previous dots
                dot_group = new_dots
                self.play(Create(dot_group), run_time=0.5)

        self.wait(2)
        
class PseudoRandomNumberGeneration(Scene):
    def construct(self):
        # Title of the scene
        title = Text("Pseudo-Random Number Generation in Computers").scale(0.8)
        title.move_to(ORIGIN)
        self.play(Write(title), run_time=5, lag_ratio=0.9)
        self.wait(2)
        self.play(title.animate.shift(3 * UP).scale(0.6))

        # Introduction to randomness and determinism
        #self.play(FadeOut(title))
        intro_text = Text(
            "True randomness is unpredictable.\nComputers, however, are deterministic."
        ).scale(0.6)
        intro_text.move_to(ORIGIN)
        self.play(Write(intro_text), run_time=5, lag_ratio=0.9)
        self.wait(2)
        #self.play(intro_text.animate.shift(2 * UP).scale(0.8))

        # Fade out intro_text and show Determinism definition
        self.play(FadeOut(intro_text))
        determinism_text = Text(
            "Determinism: The same inputs produce\n the same outputs every time."
        ).scale(0.5)
        determinism_text.move_to(ORIGIN)
        self.play(Write(determinism_text), run_time=6, lag_ratio=0.9)
        self.wait(2)

        # Fade out determinism_text and introduce Pseudo-Random Numbers
        self.play(FadeOut(determinism_text))
        pseudo_random_text = Text(
            "To simulate randomness, computers use\npseudo-random number generators (PRNGs)."
        ).scale(0.6)
        pseudo_random_text.move_to(ORIGIN)
        self.play(Write(pseudo_random_text), run_time=6, lag_ratio=0.9)
        self.wait(2)

        # Fade out pseudo_random_text and present the LCG Algorithm
        self.play(FadeOut(pseudo_random_text))
        lcg_title = Text("Example PRNG: Linear Congruential Generator (LCG)").scale(0.6)
        lcg_title.move_to(ORIGIN)
        self.play(Write(lcg_title), run_time=6, lag_ratio=0.9)
        self.wait(1)

        # LCG Formula
        self.play(FadeOut(lcg_title))
        lcg_formula = MathTex("X_{n+1} = (a X_n + c) \\mod m").scale(0.8)
        lcg_formula.move_to(ORIGIN)
        self.play(Write(lcg_formula), run_time=5, lag_ratio=0.9)
        self.wait(2)

        # Explanation of each component in the formula
        self.play(FadeOut(lcg_formula))
        formula_explanation = Text(
            "Where:\n- 'a' is the multiplier\n- 'c' is the increment\n- 'm' is the modulus\n- 'X_n' is the previous number in the sequence"
        ).scale(0.5)
        formula_explanation.move_to(ORIGIN)
        self.play(Write(formula_explanation), run_time=5, lag_ratio=0.9)
        self.wait(2)

        # Fade out formula_explanation and show an example with specific values
        self.play(FadeOut(formula_explanation))
        specific_values = MathTex("X_{n+1} = (5 X_n + 1) \\mod 16", 
                                  #tex_to_color_map={"5": YELLOW, "1": YELLOW, "16": YELLOW}
                                  ).scale(0.8)
        specific_values.move_to(ORIGIN)
        self.play(Write(specific_values), run_time=4, lag_ratio=0.9)
        self.wait(2)

        # Fade out LCG formula and specific_values to introduce the seed and sequence
        self.play(FadeOut(specific_values))
        seed_text = Text("Starting with an initial seed: ").scale(0.6)
        seed_start = MathTex("X_0 = 7", color=YELLOW).scale(0.6)
        seed_text.move_to(ORIGIN)
        seed_start.next_to(seed_text, RIGHT)
        self.play(Write(seed_text), run_time=4, lag_ratio=0.9)
        self.play(Write(seed_start), run_time=1)
        self.wait(2)

        # Generate and display a sequence
        self.play(FadeOut(seed_text), FadeOut(seed_start))
        sequence_title = Text("Pseudo-Random Sequence Generated by LCG").scale(0.6)
        sequence_title.move_to(ORIGIN)
        self.play(Write(sequence_title), run_time=4, lag_ratio=0.9)


        # Show a sequence of values calculated using the formula
        seed = 7
        multiplier = 5
        increment = 1
        modulus = 16
        sequence_values = [seed]

        for _ in range(10):
            next_value = (multiplier * sequence_values[-1] + increment) % modulus
            sequence_values.append(next_value)

        # Generate a list of MathTex objects with random colors
        sequence_text = VGroup(
            *[MathTex(str(value), color=random.choice([RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, PINK])).scale(0.8) 
              for value in sequence_values]
        ).arrange(RIGHT, buff=0.5)
        sequence_text.next_to(sequence_title, DOWN)

        # Display each value in sequence_text with a random color
        for value in sequence_text:
            self.play(Write(value), run_time=1, lag_ratio=0.9)
        self.wait(2)


        # Explain the predictability of pseudo-random numbers
        self.play(FadeOut(sequence_text, sequence_title), run_time=1)
        predictability_text = Text(
            "The sequence appears random,\nbut it is deterministic and repeatable."
        ).scale(0.5)
        predictability_text.move_to(ORIGIN)
        self.play(Write(predictability_text), run_time=5, lag_ratio=0.9)
        self.wait(3)

        # Fade out predictability and introduce limitations
        self.play(FadeOut(predictability_text))
        limitations_text = Text(
            "Limitations of PRNGs:\n  Sequences are predictable if the seed is known.\n"
            " They eventually repeat (limited by the modulus 'm')."
        ).scale(0.5)
        limitations_text.move_to(ORIGIN)
        self.play(Write(limitations_text), run_time=5, lag_ratio=0.9)
        self.wait(3)

        # Fade out limitations and compare with true randomness
        self.play(FadeOut(limitations_text))
        true_random_text = Text(
            "True randomness lacks any predictable pattern.\n"
            "It can be generated using physical processes (e.g., radioactive decay)."
        ).scale(0.5)
        true_random_text.move_to(ORIGIN)
        self.play(Write(true_random_text), run_time=5, lag_ratio=0.9)
        self.wait(3)

        # Fade out true_random_text and conclude
        self.play(FadeOut(true_random_text))
        conclusion_text = Text(
            "Pseudo-Random Numbers are sufficient for many tasks,\nbut unsuitable for applications requiring true unpredictability (e.g., cryptography)."
        ).scale(0.6)
        conclusion_text.move_to(ORIGIN)
        self.play(Write(conclusion_text), run_time=5, lag_ratio=0.9)
        self.wait(3)

        # End scene
        self.play(FadeOut(VGroup(title, conclusion_text)), run_time=5)
        self.wait(2)

class MonteCarloIntroScene(Scene):
    def construct(self):
        # Define the continuous flow with sine and cosine for a hypnotic effect
        func = lambda pos: (np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 0.1)
        stream_lines = StreamLines(
            func,
            stroke_width=5,
            dt=.01,
            max_anchors_per_line=100,
            opacity=0.5,
            #color_by_magnitude=True
        ).rotate(PI / 2).scale(2)

        # Add and start the continuous flow animation
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=1.5)
        
        # Overlay title and subtitle text for the Monte Carlo simulation introduction
        title_text = Text("Monte Carlo Simulation", font_size=64, color=YELLOW)
        title_text.move_to(ORIGIN)
        subtitle_text = Text("Exploring Probability with Randomness", font_size=36, color=WHITE)
        subtitle_text.next_to(title_text, DOWN)
        
        # Fade in the title and subtitle
        self.play(FadeIn(title_text), FadeIn(subtitle_text), run_time=25, lag_ratio=0.9)
        self.wait(5)

        # Keep the streamlines flowing for a while to give a hypnotic effect
        self.wait(5)

        # Fade out everything to end the scene
        self.play(FadeOut(VGroup(stream_lines, title_text, subtitle_text)), run_time=10)
        
class MonteCarloWithCode(Scene):
    def construct(self):
        # Python code to display
        code = '''from random import random, sqrt

# Generate a random point
x, y = random(), random()

# Calculate the distance from the origin
distance = sqrt(x**2 + y**2)

# Check if the point is inside the circle
if distance <= 1:
    inside_circle += 1
    
return (inside_circle / n) * 4
        '''

        # Create the code object
        python_code = Code(
            code=code,
            tab_width=2,
            language="Python",
            font_size=24,
            style="monokai",
            insert_line_no=False,
        )
        python_code.to_edge(LEFT)  # Position the code on the left

        # Create geometric objects for the animation
        square = Square(side_length=4, color=XKCD.BABYPURPLE).shift(RIGHT * 4.5)
        circle = Circle(radius=2, color=XKCD.AZUL, fill_opacity=0.5).move_to(square.get_center())

        # Text to display results
        distance_text = Text("Distance: ?", font_size=24).next_to(circle, UP*1.5, buff=0.5)
        inside_text = Text("Inside Circle: ?", font_size=24).next_to(distance_text, DOWN)

        # Display the initial scene
        self.play(Write(python_code), Create(square), Create(circle), Write(distance_text), Write(inside_text))
        self.wait(1)

        # Highlight the random point generation line
        highlight_gen_point = SurroundingRectangle(python_code.code[2], color=YELLOW, buff=0.1)  # Line 3
        self.play(Create(highlight_gen_point))
        self.wait(1)
        self.play(FadeOut(highlight_gen_point))

        # Generate random numbers (step-by-step visualization)
        x = -0.8
        y = 0.7

        # Highlight random() for x-coordinate generation
        random_highlight_x = SurroundingRectangle(python_code.code[3][:28], color=GREEN, buff=0.1)  # random()
        self.play(Create(random_highlight_x))
        #x_text = Text(f"x = {x:.2f}", font_size=24).next_to(square, UP, buff=0.5)
        #self.play(Write(x_text))
        self.wait(1)
        self.play(FadeOut(random_highlight_x))

        

        # Display the generated point on the square
        new_point = Dot(point=[x, y, 0], color=WHITE).shift(RIGHT * 4.5)
        self.play(FadeIn(new_point), run_time=1)
        self.wait(1)

        highlight_if_condition = SurroundingRectangle(python_code.code[6][:28], color=YELLOW, buff=0.1)  # If condition
        self.play(Create(highlight_if_condition))
        self.wait(1)
        arrow = Arrow(circle.get_center(), end=new_point.get_center(), buff=0.1, color=WHITE, stroke_width=3)
        self.play(Create(arrow))
        self.play(FadeOut(highlight_if_condition))
        # Highlight the distance calculation line
        highlight_dist = SurroundingRectangle(python_code.code[9:10][:20], color=YELLOW, buff=0.1)  # Distance calculation line
        self.play(Create(highlight_dist))
        self.wait(1)
        self.play(FadeOut(highlight_dist))
        distance = np.sqrt(x**2 + y**2)
        
        new_distance_text = Text(f"Distance: {distance:.2f}", font_size=24).next_to(circle, UP*1.5, buff=0.5)
        self.play(Transform(distance_text, new_distance_text))
        
        self.wait(1)

        # Highlight the if condition line
        
        if distance <= 2:
            inside_text_new = Text("Inside Circle: Yes", font_size=24, color=GREEN).next_to(distance_text, DOWN)
            self.play(new_point.animate.set_color(GREEN))
        else:
            inside_text_new = Text("Inside Circle: No", font_size=24, color=RED).next_to(distance_text, DOWN)
            self.play(new_point.animate.set_color(RED))
        self.play(Transform(inside_text, inside_text_new))
        self.wait(1)

        # Clean up
        self.play(
                  FadeOut(python_code), FadeOut(square), FadeOut(circle), FadeOut(new_point), 
                  FadeOut(distance_text), FadeOut(inside_text), FadeOut(arrow))
        
        
class UniformToGaussian(Scene):
    def construct(self):
        # Create title
        title = Text("Law of Large Numbers").move_to(ORIGIN)
        self.play(Write(title), run_time=3, lag_ratio=0.9)
        self.wait(2)
        
        # move up 
        self.play(title.animate.shift(3 * UP).scale(0.8), run_time=2)
        

        # Create Cartesian plane
        axes = Axes(
            x_range=[0, 2 * np.pi, np.pi / 2],
            y_range=[0, 1.5, 0.5],
            tips=False,
            axis_config={"include_numbers": False},
        ).scale(0.8)
        x_label = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(x_label), run_time=4, lag_ratio=0.9)

        # Define flat curve (Uniform Distribution)
        flat_curve = axes.plot(
            lambda x: 0.4,
            x_range=[0, 2 * np.pi],
            color=BLUE,
        )
        #flat_label = MathTex("f(x) = 0.5").next_to(flat_curve, UP)
        self.play(Create(flat_curve), run_time=5, lag_ratio=0.9)

        # Transform flat curve into a Gaussian
        gaussian_curve = axes.plot(
            lambda x: np.exp(-((x - np.pi) ** 2) / (2 * 0.3**2)) / (np.sqrt(2 * np.pi) * 0.3),
            x_range=[0, 2 * np.pi],
            color=RED,
        )
        gaussian_label = MathTex(r"f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\pi)^2}{2\sigma^2}}").move_to(ORIGIN + RIGHT*3).scale(0.6)

        # Animate transformation
        self.play(Transform(flat_curve, gaussian_curve), Write(gaussian_label), run_time=5, lag_ratio=0.9)
        
        # Hold the final scene
        self.wait(4)
        
        # Clean up
        self.play(FadeOut(axes), FadeOut(x_label), FadeOut(flat_curve), FadeOut(gaussian_curve), FadeOut(gaussian_label))
        
        
class PRNLimitations(Scene):
    def construct(self):
        # Title
        title = Text("Limitations of PRN", font_size=48)
        title.move_to(ORIGIN)
        self.play(Write(title), run_time=2, lag_ratio=0.9)

        self.wait(2)
        
        #clean up
        self.play(FadeOut(title), run_time=2, lag_ratio=0.9)


class introToIntegration(Scene):
    def construct(self):
        # Title
        title = Text("Monte Carlo Integration", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)

        # Move title upwards
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        # Formula for integral
        integral_formula = MathTex(
            r"\int_a^b f(x) \, dx ",
            font_size=36
        )
        # TO THE CENTER
        integral_formula.move_to(ORIGIN)
        self.play(Write(integral_formula))
        
        # Hold final frame
        self.wait(2)