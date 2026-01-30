from manim import *
import numpy as np
class ContinuityIntro(Scene):
    def construct(self):
        Chapter=MathTex(r"\mathbf{UNIT\;6}")
        Title=Tex("Continuity").next_to(Chapter,DOWN)
        self.play(FadeIn(Chapter))
        self.play(Write(Title))
        self.play(Wait(1))
        self.play(FadeOut(Chapter),FadeOut(Title))

class ContinuityPart1(Scene):
    def construct(self):
        Ellipse