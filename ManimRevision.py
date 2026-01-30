from manim import *
import numpy as np
class SquareCircle(Scene):
    def construct(self):
        C=Circle(radius=1.2,color=GREEN).move_to(ORIGIN)
        S=Square(side_length=2,color=BLUE).move_to(ORIGIN)
        D=Dot(radius=0.1).move_to(LEFT*2)
        self.play(FadeIn(S))
        self.play(ReplacementTransform(S,C))
        self.play(Create(D))
        self.play(D.animate.move_to(RIGHT*2))
        self.play(FadeOut(C,D))

class GraphAndArea(Scene):
    def construct(self):
        Axes1=Axes(x_range=(-2*np.pi,2*np.pi,np.pi),y_range=(-1.5,1.5,0.5))
        self.add(Axes1)
        x_labels = [MathTex(r"-2\pi"), MathTex(r"-\pi"), MathTex(r"\pi"), MathTex(r"2\pi")]
        x_coords=[-2*np.pi,-np.pi,np.pi,2*np.pi]
        y_labels=[MathTex(r"-1.5"),MathTex(r"-1.0"),MathTex(r"-0.5"),MathTex(r"0"),MathTex(r"0.5"),MathTex(r"1.0"),MathTex(r"1.5")]
        y_coords=[i*0.5 for i in range(-3,4)]
        Axes1.add_coordinates(dict(zip(x_coords,x_labels)),dict(zip(y_coords,y_labels)))
        curve=Axes1.plot(lambda x: np.sin(x))
        area=Axes1.get_area(curve, x_range=[-np.pi,np.pi],color=YELLOW, opacity=1)
        self.play(FadeIn(Axes1))
        self.play(AnimationGroup(Create(curve),FadeIn(area),lag_ratio=1),run_time=2)

class DynamicParabola(Scene):
    def construct(self):
        plane1=NumberPlane(x_range = (-4, 4), y_range = (-5, 5))
        a=ValueTracker(1)
        parabola=always_redraw(lambda: plane1.plot(lambda x:a.get_value()*x**2,color=YELLOW_B))
        label=always_redraw(lambda: MathTex(r"y=",f"{a.get_value():.1f}",r"x^2").to_corner(UL))
        self.play(AnimationGroup(FadeIn(plane1),FadeIn(parabola),FadeIn(label),lag_ratio=1))
        self.play(a.animate.set_value(2))
        self.wait(0.5)
        self.play(a.animate.set_value(-1))
        self.wait(0.5)
        self.play(a.animate.set_value(0.5))

class Exercise4(Scene):
    def construct(self):
        S=Square(side_length=1.5,color=BLUE,fill_opacity=0.7).move_to(LEFT*4)
        D=Dot(color=RED,radius=0.1)
        D.add_updater(lambda x : x.move_to(S.get_center()+RIGHT))
        self.play(AnimationGroup(FadeIn(S),FadeIn(D),lag_ratio=0.8))
        def shifter(mob,dt):
            mob.shift(2*RIGHT*dt)
        S.add_updater(shifter)
        def scaler(dt):
            for mob in self.mobjects:
                mob.set(width=2/(1+np.linalg.norm(mob.get_center())))
        self.add_updater(scaler)
        self.play(Wait(4))