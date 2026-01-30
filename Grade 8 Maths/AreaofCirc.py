import numpy as np
from manim import *
class CircleAreaLimiting(Scene):
    def construct(self):
        Title=Tex("Area of circle")
        self.play(Write(Title))
        self.play(Wait(0.3))
        self.play(Title.animate.to_edge(UP))
        NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
        self.play(Write(NameLabel))
        circle = Circle(radius=1.5, color=BLUE).to_edge(LEFT)
        circle2 = Circle(radius=1.5, color=BLUE).to_edge(LEFT)
        circle.set_fill(BLUE, opacity=0.2)
        self.play(Create(circle),Create(circle2))
        self.wait(1)
        diameter=Line(start=circle.get_center()+LEFT*1.5,end=circle.get_center()+RIGHT*1.5,color=GREEN)
        radius=Line(start=circle.get_center(),end=circle.get_center()+DOWN*1.5,color=LOGO_WHITE)
        d1=Tex("diameter",color=GREEN).scale(0.7).next_to(diameter,UP)
        d2=MathTex(r"d",color=GREEN).scale(0.7).next_to(diameter,UP)
        r1=Tex("radius",color=LOGO_WHITE).scale(0.7).next_to(radius,RIGHT)
        r2=MathTex(r"r",color=LOGO_WHITE).scale(0.7).next_to(radius,RIGHT)
        exc=Line(start=ORIGIN,end=(3*PI,0,0),color=PURPLE).shift(LEFT*3)
        c1=Tex("circumference",color=BLUE).scale(0.7).next_to(circle,UR)
        c2=MathTex(r"c",color=BLUE).scale(0.7).next_to(circle,UR)
        d2r = MathTex(r"{d}", r"=", r"{2}", r"{r}").scale(0.7).next_to(circle, UP)
        d2r[0].set_color(GREEN)       
        d2r[1].set_color(WHITE)       
        d2r[2].set_color(LOGO_WHITE)  
        d2r[3].set_color(LOGO_WHITE)  
        pidef=MathTex(r"\therefore \pi=\frac{c}{d}").scale(0.7).to_edge(DOWN)
        pidef1=MathTex(r"\therefore \pi=\frac{c}{d}\approx 3.14").scale(0.7).to_edge(DOWN)
        bgrect=RoundedRectangle(corner_radius=0.2,color=PURPLE,height=pidef1.height+0.2,width=pidef1.width+0.2).move_to(pidef1.get_center())
        formula=VGroup(pidef1,bgrect)
        self.play(Create(radius))
        self.play(Write(r1))
        self.play(Wait(0.3))
        self.play(Transform(r1,r2))
        self.play(Create(diameter))
        self.play(Write(d1))
        self.play(Wait(0.3))
        self.play(Transform(d1,d2))
        self.play(Write(d2r))
        self.play(Wait(1))
        self.play(Transform(circle2,exc))
        self.play(Write(c1))
        self.play(Transform(c1,c2))
        self.play(c1.animate.set_color(PURPLE))
        self.play(c1.animate.next_to(exc,UP))
        circlez=[]
        for i in range(3):
            zirc=circle.copy()
            circlez.append(zirc)
        Circlez=VGroup(*[c for c in circlez])
        Circlez[0].move_to(exc.get_left(), aligned_edge=LEFT)
        Circlez[1].move_to(Circlez[0].get_right(), aligned_edge=LEFT)
        Circlez[2].move_to(Circlez[1].get_right(), aligned_edge=LEFT)
        self.play(AnimationGroup(*[TransformFromCopy(circle,Circlez[i]) for i in range(3)],lag_ratio=1))
        self.play(Indicate(c1))
        self.play(Indicate(d1))
        cd=VGroup(c1,d1)
        self.play(TransformMatchingShapes(cd.copy(),pidef))
        self.play(Transform(pidef,pidef1))
        self.play(Create(bgrect))
        self.play(Wait(1.5))
        self.play(FadeOut(Group(*[mob for mob in self.mobjects if mob not in [NameLabel, circle, Title]])))
        #First wedge transformation with n=12
        n = 12
        wedges = VGroup()
        for i in range(n):
            wedge = Sector(radius=1.5, angle=TAU/n, start_angle=i*TAU/n, color=BLUE, stroke_width=1)
            wedge.set_fill(BLUE, opacity=0.6)
            wedges.add(wedge)
        wedges.move_to(circle.get_center())
        self.play(LaggedStart(*[GrowFromCenter(w) for w in wedges], lag_ratio=0.05))
        self.wait(1)
        vedges = []
        for i in range(n):
            vedge = Sector(radius=1.5, angle=TAU/n, start_angle=0.5*((PI/2 - 2*PI/n) + PI/2), color=BLUE, stroke_width=1)
            vedge.set_fill(BLUE, opacity=0.6)
            if i % 2 == 1:
                vedge.rotate(PI, about_point=vedge.get_center())
            vedges.append(vedge)
        rects = VGroup(*vedges)
        rects.arrange(RIGHT, buff=-0.37)
        for i in range(n):
            if i%2==0:
                rects[i].shift(0.09*UP)
        rects.next_to(circle, RIGHT, buff=1)
        self.play(AnimationGroup(*[ReplacementTransform(wedges[i], rects[i]) for i in range(n)], lag_ratio=0))
        self.wait(1)
        self.play(FadeOut(rects))  
        # Second wedge transformation with n=24
        n = 24
        wedges = VGroup()
        for i in range(n):
            wedge = Sector(radius=1.5, angle=TAU/n, start_angle=i*TAU/n, color=BLUE, stroke_width=1)
            wedge.set_fill(BLUE, opacity=0.6)
            wedges.add(wedge)
        wedges.move_to(circle.get_center())
        self.play(LaggedStart(*[GrowFromCenter(w) for w in wedges], lag_ratio=0.05))
        self.wait(1)
        vedges = []
        for i in range(n):
            vedge = Sector(radius=1.5, angle=TAU/n, start_angle=0.5*((PI/2 - 2*PI/n) + PI/2), color=BLUE, stroke_width=1)
            vedge.set_fill(BLUE, opacity=0.6)
            if i % 2 == 1:
                vedge.rotate(PI, about_point=vedge.get_center())
            vedges.append(vedge)
        rects = VGroup(*vedges)
        rects.arrange(RIGHT, buff=-0.17)
        for i in range(n):
            if i%2==0:
                rects[i].shift(0.06*UP)
        rects.next_to(circle, RIGHT, buff=1)
        self.play(AnimationGroup(*[ReplacementTransform(wedges[i], rects[i]) for i in range(n)], lag_ratio=0))
        self.wait(1)
        self.play(FadeOut(rects))  
        # Third wedge transformation with n=48
        n = 48
        wedges = VGroup()
        for i in range(n):
            wedge = Sector(radius=1.5, angle=TAU/n, start_angle=i*TAU/n, color=BLUE, stroke_width=1)
            wedge.set_fill(BLUE, opacity=0.6)
            wedges.add(wedge)
        wedges.move_to(circle.get_center())
        self.play(LaggedStart(*[GrowFromCenter(w) for w in wedges], lag_ratio=0.05))
        self.wait(1)
        vedges = []
        for i in range(n):
            vedge = Sector(radius=1.5, angle=TAU/n, start_angle=0.5*((PI/2 - 2*PI/n) + PI/2), color=BLUE, stroke_width=1)
            vedge.set_fill(BLUE, opacity=0.6)
            if i % 2 == 1:
                vedge.rotate(PI, about_point=vedge.get_center())
            vedges.append(vedge)
        rects = VGroup(*vedges)
        rects.arrange(RIGHT, buff=-0.08)
        for i in range(n):
            if i%2==0:
                rects[i].shift(0.03*UP)
        rects.next_to(circle, RIGHT, buff=1)
        self.play(AnimationGroup(*[ReplacementTransform(wedges[i], rects[i]) for i in range(n)], lag_ratio=0))
        self.wait(1)
        self.play(FadeOut(rects))  
        # Fourth wedge transformation with n=96
        n = 96
        wedges = VGroup()
        for i in range(n):
            wedge = Sector(radius=1.5, angle=TAU/n, start_angle=i*TAU/n, color=BLUE, stroke_width=1)
            wedge.set_fill(BLUE, opacity=0.6)
            wedges.add(wedge)
        wedges.move_to(circle.get_center())
        self.play(LaggedStart(*[GrowFromCenter(w) for w in wedges], lag_ratio=0.05))
        self.wait(1)
        vedges = []
        for i in range(n):
            vedge = Sector(radius=1.5, angle=TAU/n, start_angle=0.5*((PI/2 - 2*PI/n) + PI/2), color=BLUE, stroke_width=1)
            vedge.set_fill(BLUE, opacity=0.6)
            if i % 2 == 1:
                vedge.rotate(PI, about_point=vedge.get_center())
            vedges.append(vedge)
        rects = VGroup(*vedges)
        rects.arrange(RIGHT, buff=-0.03)
        for i in range(n):
            if i%2==0:
                rects[i].shift(0.01*UP)
        rects.next_to(circle, RIGHT, buff=1)
        self.play(AnimationGroup(*[ReplacementTransform(wedges[i], rects[i]) for i in range(n)], lag_ratio=0))
        self.wait(1)
        self.play(FadeOut(rects))
        # Fifth wedge transformation with n=500
        n = 500
        wedges = VGroup()
        for i in range(n):
            wedge = Sector(radius=1.5, angle=TAU/n, start_angle=i*TAU/n, color=BLUE, stroke_width=1)
            wedge.set_fill(BLUE, opacity=0.6)
            wedges.add(wedge)
        wedges.move_to(circle.get_center())
        self.play(LaggedStart(*[GrowFromCenter(w) for w in wedges], lag_ratio=0.01))
        self.wait(1)
        vedges = []
        for i in range(n):
            vedge = Sector(radius=1.5, angle=TAU/n, start_angle=0.5*((PI/2 - 2*PI/n) + PI/2), color=BLUE, stroke_width=1)
            vedge.set_fill(BLUE, opacity=0.6)
            if i % 2 == 1:
                vedge.rotate(PI, about_point=vedge.get_center())
            vedges.append(vedge)
        rects = VGroup(*vedges)
        rects.arrange(RIGHT, buff=-0.005)
        for i in range(n):
            if i%2==0:
                rects[i].shift(0.002*UP)
        rects.next_to(circle, RIGHT, buff=1)
        self.play(AnimationGroup(*[ReplacementTransform(wedges[i], rects[i]) for i in range(n)], lag_ratio=0))
        self.wait(1)
        Tex1=MathTex(r"\text{Area}=l \times b").scale(0.7).next_to(rects,DOWN)
        Tex2a=MathTex(r"\Rightarrow \text{Area}= \frac{c}{2} \cdot r").scale(0.7).next_to(Tex1,DOWN)
        Tex2b=MathTex(r"\Rightarrow \text{Area}= (\pi \cdot r) \cdot r").scale(0.7).next_to(Tex2a,DOWN)
        Tex3=MathTex(r"\therefore \text{Area}= \pi r^2").scale(0.7).next_to(Tex2b,DOWN)
        bg=RoundedRectangle(corner_radius=0.2,color=PURPLE,height=Tex3.height+0.2,width=Tex3.width+0.2).move_to(Tex3.get_center())
        c2.next_to(circle,UP)
        self.play(FadeIn(r2),FadeIn(radius),FadeIn(c2))
        c3=MathTex(r"\frac{c}{2}",color=BLUE).scale(0.7).next_to(rects,UP)
        self.play(Wait(1))
        self.play(r2.animate.next_to(rects,LEFT))
        self.play(Transform(c2,c3)) 
        self.play(Wait(1))
        self.play(Write(Tex1))
        self.play(Write(Tex2a))
        self.play(Write(Tex2b))
        self.play(Write(Tex3))
        self.play(Create(bg))
        self.play(Wait(2))
        self.play(*[FadeOut(mob) for mob in self.mobjects])