from manim import *

class FinalVideo(Scene):
    def construct(self):
        IntroLogarithms.construct(self)
        self.wait(1)
        LogarithmExample.construct(self)
        self.wait(1)
        LogarithmExample2.construct(self)
        self.wait(1)
        FirstExercise.construct(self)
        self.wait(1)

class IntroLogarithms(Scene):
    def construct(self):
        # Titolo della scena
        title = Tex(
            "Introduzione ai Logaritmi",
            font_size=72,
            color=TEAL
        )
        title.to_edge(UP)

        # Mostrare il titolo
        self.play(Write(title), run_time=10, lagratio=0.5)
        self.wait(1)

        # Creare il logaritmo con colori diversi
        log_expression = MathTex(
            "\\log_{", "2", "}", "(", "8", ")", "=", "3",
            font_size=72
        )
        
        log_expression.set_color_by_tex("2", BLUE)       # Base in blu
        log_expression.set_color_by_tex("8", ORANGE)     # Argomento in arancione
        log_expression.set_color_by_tex("3", GREEN)      # Risultato in verde

        log_expression_general = MathTex(
            "\\log_{", "b", "}", "(", "x", ")", "=", "y",
            font_size=72
        )
        
        log_expression_general.set_color_by_tex("b", BLUE)       # Base in blu
        log_expression_general.set_color_by_tex("x", ORANGE)     # Argomento in arancione
        log_expression_general.set_color_by_tex("y", GREEN)      # Risultato in verde
        
        
        # Mostrare il logaritmo con animazioni
        self.play(Write(log_expression_general), run_time=10)
        self.wait(1)

        # Animazione di enfasi sul logaritmo
        self.play(
            log_expression_general.animate.scale(1.2),
            run_time=4
        )
        # now remove yellow color
        self.play(log_expression_general.animate.set_color_by_tex("b", BLUE).set_color_by_tex("x", ORANGE).set_color_by_tex("y", GREEN), 
                  run_time=2)
        self.wait(1)

        # Tornare ai colori originali
        #self.play(log_expression_general.animate.scale(1/1.2).set_color_by_tex("2", BLUE).set_color_by_tex("8", ORANGE).set_color_by_tex("3", GREEN))
        #self.wait(2)

        # Frase di transizione
        transition_text = Tex(
            "Scopriamo insieme come funzionano i logaritmi!",
            font_size=48,
            color=WHITE
        )
        transition_text.next_to(log_expression_general, DOWN, buff=1)
        
        definition_text = Tex(
            "Il logaritmo in base ", 
            "$b$", 
            " di un numero ", 
            "$x$", 
            ",\\\\",
            "è l'esponente ", 
            "$y$", 
            " a cui bisogna elevare ", 
            "$b$", 
            ",\\\\",
            "per ottenere ", 
            "$x$", 
            ".",
            font_size=48
        ).next_to(log_expression_general, DOWN, buff=1)

        # Applicare i colori alle variabili
        definition_text.set_color_by_tex("$b$", BLUE)   # Colora tutte le 'b'
        definition_text.set_color_by_tex("$x$", ORANGE) # Colora tutte le 'x'
        definition_text.set_color_by_tex("$y$", GREEN)  # Colora tutte le 'y'
        
        self.play(Write(transition_text), run_time=5)
        
        self.play(FadeOut(transition_text), run_time=2)
        self.wait(1)
        self.play(Write(definition_text), run_time=5)
        

        # Mostrare la frase di transizione
        
        self.wait(2)
        
        # move log_expression to the up and dedfinition_text next down to log_expression
        self.play(
            log_expression_general.animate.next_to(title, DOWN, buff=1),
            definition_text.animate.next_to(title, 2.5 * DOWN, buff=1),
            run_time=3
        )
        self.wait(1)
        
        esponential_expression = MathTex(
            "b", "^", "y", "=", "x",
            font_size=72
        ).scale(1.5).move_to(ORIGIN + DOWN * 2.5)
        
        esponential_expression.set_color_by_tex("b", BLUE)   # Base in blu
        esponential_expression.set_color_by_tex("x", ORANGE)
        esponential_expression.set_color_by_tex("y", GREEN)
        
        self.play(Write(esponential_expression), run_time=4)
        self.wait(2)
        self.play(FadeOut(VGroup(title, log_expression_general, esponential_expression, definition_text)))
        self.wait(1)
        
class LogarithmExample(Scene):
    def construct(self):
        # Creare il logaritmo con colori diversi
        log_expression = MathTex(
            "\\log_{", "2", "}", "(", "8", ")", "=", "3",
            font_size=72
        )
        
        log_expression.set_color_by_tex("2", BLUE)       # Base in blu
        log_expression.set_color_by_tex("8", ORANGE)     # Argomento in arancione
        log_expression.set_color_by_tex("3", GREEN)      # Risultato in verde

        # Mostrare il logaritmo con animazioni
        self.play(Write(log_expression), run_time=5)
        self.wait(1)

        # Animazione di enfasi sul logaritmo
        self.play(
            log_expression.animate.scale(1.2),
            run_time=2
        )
        # now remove yellow color
        self.play(log_expression.animate.set_color_by_tex("2", BLUE).set_color_by_tex("8", ORANGE).set_color_by_tex("3", GREEN))
        self.wait(1)

        # Tornare ai colori originali
       # self.play(log_expression.animate.scale(1/1.2).set_color_by_tex("2", BLUE).set_color_by_tex("8", ORANGE).set_color_by_tex("3", GREEN))
        #self.wait(2)

        # move log_expression up and write the esponential expression
        esponential_expression = MathTex(
            "2", "^", "3", "=", "8",
            font_size=72
        ).scale(1.5).move_to(ORIGIN + DOWN*2)
        
        esponential_expression.set_color_by_tex("2", BLUE)
        esponential_expression.set_color_by_tex("8", ORANGE)
        esponential_expression.set_color_by_tex("3", GREEN)

        self.play(
            log_expression.animate.move_to(ORIGIN + UP*2),
            Write(esponential_expression),
            run_time=3
        )
        self.wait(2)
        
        # add some arrows to show the relation between the two expressions
       # arrow from 2 to log_2
        Arrow1 = Arrow(start=esponential_expression[0].get_top(), end=log_expression[1].get_bottom(), buff=0.5, color=BLUE)
         # arrow from 3 to log_2
        Arrow2 = Arrow(start=esponential_expression[2].get_top(), end=log_expression[7].get_bottom(), buff=0.5, color=GREEN)
        # arrow from 8 to log_2
        Arrow3 = Arrow(start=esponential_expression[4].get_top(), end=log_expression[4].get_bottom(), buff=0.5, color=ORANGE)
        
         
        self.play(Write(Arrow1), run_time=2, lag_ratio=0.9)
        self.play(Write(Arrow2), run_time=2, lag_ratio=0.9)
        self.play(Write(Arrow3), run_time=2, lag_ratio=0.9)
        self.wait(2)
        
        #fadeout
        self.play(FadeOut(VGroup(log_expression, esponential_expression, Arrow1, Arrow2, Arrow3)))

class LogarithmExample2(Scene):
    def construct(self):
        # stesso procedimento di prima cambia i numeri e i colori 
        log_expression = MathTex(
            "\\log_{", "3", "}", "(", "81", ")", "=", "4",
            font_size=72
        )
        
        log_expression.set_color_by_tex("3", BLUE)       # Base in blu
        log_expression.set_color_by_tex("81", ORANGE)     # Argomento in arancione
        log_expression.set_color_by_tex("4", GREEN)      # Risultato in verde
        
        self.play(Write(log_expression), run_time=5)
        self.wait(1)
        
        self.play(
            log_expression.animate.scale(1.2),
            run_time=2
        )
        # now remove yellow color
        self.play(log_expression.animate.set_color_by_tex("3", BLUE).set_color_by_tex("81", ORANGE).set_color_by_tex("4", GREEN))
        self.wait(1)
        
        esponential_expression = MathTex(
            "3", "^", "4", "=", "81",
            font_size=72
        ).scale(1.5).move_to(ORIGIN + DOWN*2)
        
        esponential_expression.set_color_by_tex("3", BLUE)
        esponential_expression.set_color_by_tex("81", ORANGE)
        esponential_expression.set_color_by_tex("4", GREEN)
        
        self.play(
            log_expression.animate.move_to(ORIGIN + UP*2),
            Write(esponential_expression),
            run_time=3
        )
        self.wait(2)
        
        # add some arrows to show the relation between the two expressions
         # arrow from 3 to log_3
        Arrow1 = Arrow(start=esponential_expression[0].get_top(), end=log_expression[1].get_bottom(), buff=0.5, color=BLUE)
            # arrow from 4 to log_3
        Arrow2 = Arrow(start=esponential_expression[2].get_top(), end=log_expression[7].get_bottom(), buff=0.5, color=GREEN)
        # arrow from 81 to log_3
        Arrow3 = Arrow(start=esponential_expression[4].get_top(), end=log_expression[4].get_bottom(), buff=0.5, color=ORANGE)
        
        self.play(Write(Arrow1), run_time=2, lag_ratio=0.9)
        self.play(Write(Arrow2), run_time=2, lag_ratio=0.9)
        self.play(Write(Arrow3), run_time=2, lag_ratio=0.9)
        self.wait(2)
        #Fadeout
        self.play(FadeOut(VGroup(log_expression, esponential_expression, Arrow1, Arrow2, Arrow3)))
        
class FirstExercise(Scene):
    def construct(scene):
        # in this scene we will show the first exercise 
        # now after the equal sign we have x
        log_expression = MathTex(
            "\\log_{", "2", "}", "(", "16", ")", "=", "x",
            font_size=72
        )
        
        log_expression.set_color_by_tex("2", BLUE)       # Base in blu
        log_expression.set_color_by_tex("16", ORANGE)     # Argomento in arancione
        log_expression.set_color_by_tex("x", GREEN)      # Risultato in verde
        
        scene.play(Write(log_expression), run_time=5)
        scene.wait(1)
        
        scene.play(
            log_expression.animate.scale(1.2),
            run_time=2
        )
        # now remove yellow color
        scene.play(log_expression.animate.set_color_by_tex("2", BLUE).set_color_by_tex("16", ORANGE).set_color_by_tex("x", GREEN))
        scene.wait(1)
        
        esponential_expression = MathTex(
            "2", "^", "x", "=", "16",
            font_size=72
        ).scale(1.5).move_to(ORIGIN + DOWN*2)
        
        esponential_expression.set_color_by_tex("2", BLUE)
        esponential_expression.set_color_by_tex("16", ORANGE)
        esponential_expression.set_color_by_tex("x", GREEN)
        
        scene.play(
            log_expression.animate.move_to(ORIGIN + UP*2),
            Write(esponential_expression),
            run_time=3
        )
        scene.wait(2)
        
        # add some arrows to show the relation between the two expressions
         # arrow from 2 to log_2
        Arrow1 = Arrow(start=esponential_expression[0].get_top(), end=log_expression[1].get_bottom(), buff=0.5, color=BLUE)

        # arrow from x to log_2
        Arrow2 = Arrow(start=esponential_expression[2].get_top(), end=log_expression[7].get_bottom(), buff=0.5, color=GREEN)
        
        # arrow from 16 to log_2
        Arrow3 = Arrow(start=esponential_expression[4].get_top(), end=log_expression[4].get_bottom(), buff=0.5, color=ORANGE)
        
        scene.play(Write(Arrow1), run_time=2, lag_ratio=0.9)
        scene.play(Write(Arrow2), run_time=2, lag_ratio=0.9)
        scene.play(Write(Arrow3), run_time=2, lag_ratio=0.9)
        scene.wait(5)
        
        # solution of the exercise
        solution = MathTex(
            "x", "=", "4",
            font_size=72
        ).scale(1.5).move_to(ORIGIN + RIGHT*3)
        
        solution.set_color_by_tex("4", GREEN)
        
        scene.play(
            Write(solution),
            run_time=3
        )   
        scene.wait(2)
        
        #fadeout
        scene.play(FadeOut(VGroup(log_expression, esponential_expression, Arrow1, Arrow2, Arrow3, solution)))