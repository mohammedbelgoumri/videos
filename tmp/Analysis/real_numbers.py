from manim import *

class Axioms(Scene):
    def construct(self):
        axioms = MathTex(
            r"1-\ \forall x, y \in \mathbb{R},\ x + y = y + x",
            r"1-\ \forall x, y \in \mathbb{R},\ x \cdot y = y \cdot x",
        ).align_submobjects(LEFT)

        self.play(Write(axioms))
        self.wait(2)

class Continuity(Scene):
    def construct(self):
        # set up the scene
        
        # create the objects
          
        real_line = NumberLine([-10, 10], 20) # real line
        line_label = MathTex(r"\mathbb{R}").to_edge(edge = LEFT, buff = SMALL_BUFF).shift(UP * .5) # R label
        
        hole = Circle( # hole
            .05, YELLOW, fill_color = BLACK, 
            fill_opacity = 1, stroke_width = 1
        ).move_to(real_line.number_to_point(2.3))
        
        # braces for A (left) and B(right)
        A_brace = BraceBetweenPoints( # left brace
            real_line.number_to_point(-7.5),
            hole.get_left(),
            direction = DOWN
        )
        A_label = MathTex("A").next_to(A_brace, DOWN, buff = SMALL_BUFF) # A label
        
        B_brace = BraceBetweenPoints( # right brace
            hole.get_right(),
            real_line.number_to_point(7.5),
            direction = DOWN
        )
        B_label = MathTex("B").next_to(B_brace, DOWN, buff = SMALL_BUFF) # B label
        
        # Draw everything
        self.play(Create(real_line), Write(line_label))
        self.play(GrowFromCenter(hole))
        self.wait()
        self.play(
            *[GrowFromCenter(brace) for brace in [A_brace, B_brace]],
            run_time = .5,
            rate_func = linear
        )
        self.play(Write(A_label), Write(B_label))
        self.wait()