from manim import *

class Fraction(MathTex):
    """
    A fraction of two strictly positive integers
    """

    def __init__(self, numerator, denominator):
        if numerator < 0 or denominator < 0 or not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Both numerator and denominator must be positive integers")
        self.numerator = numerator
        self.denominator = denominator
        MathTex.__init__(self, *f"{numerator} \\over {denominator}".split(" "))

    def __str__(self) -> str:
        return f"{self.numerator}\\over {self.denominator}"

class Node(object):
    
    """
    Binary tree node
    """
    def __init__(self, fraction: Fraction, left=None, right=None, parent=None, position = UP * 3):
        self.fraction = Fraction(1, 1) if fraction is None else fraction 
        self.left = left
        self.right = right
        self.parent = parent
        self.position = position    
    
    def set_left(self, left):
        self.left = left
        left.parent = self
    
    def set_right(self, right):
        self.right = right
        right.parent = self


class Tree(object):
    """
    Stern-brocot tree
    TODO: Refactor to inherit from Mobject
    """

    def __init__(
        self, 
        root_fraction: Fraction = None, 
        height: int = 0, 
        position: np.ndarray = UP * 3, 
        width: float = 3.5
    ):
        """
            constructs Stern-Brocot tree of height 'height' and root label 'root_fraction'
            TODO: Refactor and rewrite comments
        """
        self.left = None
        self.right = None
        # root step
        self.root = Node(root_fraction, position)
        self.fraction = self.root.fraction
        self.height = height
        self.position = position
        self.width = width
        self.texFraction = MathTex(*str(self.fraction).split(" ")).scale(.4).move_to(self.position)
        
        # Stop at leaf leaf
        if height == 0:
            return

        # left step:

        left = Tree(
            root_fraction = Fraction(
                numerator = self.fraction.numerator,
                denominator = self.fraction.numerator + self.fraction.denominator
            ),
            height = self.height - 1,
            position = self.position + LEFT * self.width + DOWN * 1.5,
            width = self.width / 2
        )

        # right step:
        right = Tree(
            root_fraction = Fraction(
                numerator = self.fraction.numerator + self.fraction.denominator,
                denominator = self.fraction.denominator
            ),
            height=self.height - 1,
            position = self.position + RIGHT * self.width + DOWN * 1.5,
            width = self.width / 2
        )

        # set left and right children
        self.root.set_left(left)
        self.left = left
        self.root.set_right(right)
        self.right = right

    def show(self, scene:Scene):
        """
        Draws the tree
        """

        # test for empty tree
        if self:
            scene.play(
                # write root fraction
                Write(self.fraction.scale(.5).move_to(self.position)),
                Create(Circle(arc_center = self.fraction.get_center(), radius = .3, color = WHITE))
            )

            # test for leaf
            if self.height > 0:
                scene.play(
                    # show creation of left and right edges
                    Write(Line(self.position, self.left.position, buff=SMALL_BUFF)),
                    Write(Line(self.position, self.right.position, buff=SMALL_BUFF))
                )
                # show left and right children
                self.left.show(scene)
                self.right.show(scene)


# tree = Graph(
#     vertices=list(range(5)),
#     vertex_type=Label,
#     labels={
#         0: "Optimization methods",
#         1: "Exact", 
#         2: "Approximate",
#         3: "Heuristic",
#         4: "Metaheuristic"
#     },
#     edges=[(0, 1), (0, 2), (2, 3), (2, 4)],
#     layout='tree',
#     root_vertex=0,
#     edge_type=Arrow
# )
# c = CogMobject().shift(RIGHT*1.3)
# c2 = CogMobj2ect(2, color=RED).shift(LEFT*1.8)
# self.add(c, c2)
# self.wait()
# c.add_updater(lambda mob, dt: mob.rotate(-TAU*dt/3))
# c2.add_updater(lambda mob, dt: mob.rotate(TAU*dt/6))

# self.wait(10)