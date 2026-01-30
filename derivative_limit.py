from manim import *
import numpy as np
from manim.opengl import *
class Testy(Scene):
    def construct(self):
        ax=Axes(x_range=(-2*np.pi,2*np.pi),y_range=(-1.5,1.5))
        curve=ax.plot(lambda x:np.sin(x),color=RED)
        area=ax.get_area(curve,x_range=(-2*np.pi,0))
        self.play(Create(ax,run_time=2,color=BLUE))
        self.play(Create(curve), run_time=2)
        self.play(FadeIn(area))

class Testy2(Scene):
    def construct(self):
        green_sqr=Square(color=GREEN,fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_sqr))
        bluecircle=Circle(color=BLUE,fill_opacity=0.5)
        self.play(ReplacementTransform(green_sqr,bluecircle))
        self.play(FadeOut(bluecircle))

class Testy3(Scene):
    def construct(self):
        ax=Axes(x_range=(-2*np.pi,2*np.pi),y_range=(-2,2))
        func=ax.plot(lambda x:np.sin(x),color=BLUE_E)
        self.play(Create(ax,run_time=4), Create(func, run_time=3))
        self.wait(np.pi/4)
class position(Scene):
    def construct(self):
        plane=NumberPlane(x_range=(-2,2,1),y_range=(-2,2,1))
        curve=plane.plot(lambda x: x**2-4,color=RED)
        plane2=NumberPlane(x_range=(-4,4,1),y_range=(-4,4,1))
        self.play(FadeIn(plane),run_time=0.5)
        self.play(Create(curve),run_time=3)

class Animete(Scene):
    def construct(self):
        doz = Dot(point=(1, 0,0), fill_opacity=1, color=RED)
        doz2 = Dot(point=(0, 1,0), fill_opacity=1, color=RED)
        doz1 = Dot(point=(0, 0,1), fill_opacity=1, color=RED)
        dotz = VGroup(doz1, doz2, doz)
        a=Text("Welcome to Trapa")
        self.add(dotz) 
        self.play(Rotate(dotz, angle=PI),Write(a), run_time=2)
        self.play(Wait(1))
        self.play(Unwrite(a))
        self.play(Wait(1))
        plane=NumberPlane()
        curve=plane.plot(lambda x: x**2-4,color=RED)
        self.play(FadeOut(dotz))
        self.play(FadeIn(plane),run_time=0.5)
        self.play(Create(curve),run_time=3)
        M=MathTex(r"x")
        N=MathTex(r"f(x)")
        M.move_to((5,0.2,0))
        N.move_to((0.5,3,0))
        self.play(Write(M),Write(N),run_time=2)

class testytesty(Scene):
    def construct(self):
        bluesq=Square(color=BLUE,fill_opacity=0.5)
        greenhexa=Circle(color=GREEN,fill_opacity=0.5)
        bluesq.next_to(greenhexa)
        self.play(DrawBorderThenFill(bluesq),DrawBorderThenFill(greenhexa))
        sqcirc=VGroup(bluesq,greenhexa)
        sqcirc.generate_target()
        sqcirc.target.shift(10*RIGHT)
        introtext=MathTex(r"\mathrm{Shr\ddot{o}dinger's \; Wavefunction}")
        introtext.generate_target()
        introtext.target.shift(10*UP)
        mob_1=NumberPlane()
        mob_1.move_to(10*DOWN)
        self.add(mob_1)
        mob_1.generate_target()
        mob_1.target.shift(10*UP)
        self.play(Rotate(sqcirc,2*PI))
        self.play(MoveToTarget(sqcirc))
        self.play(Write(introtext))
        self.play(Wait(1))
        self.play(MoveToTarget(introtext),MoveToTarget(mob_1),run_time=1,rate_func=smooth)
        curve_1=mob_1.plot(lambda x:(x-2)*(x+2)*x/2,color=BLUE)
        self.play(Create(curve_1,run_time=6))
class Rota(Scene):
    def construct(self):
        polys=VGroup([RegularPolygon(5) for i in range(5)]).arrange(RIGHT)
        self.add(polys)