from manim import *
import numpy as np
import math
# class QuadraticsIntro(Scene):
#     def construct(self):
#         Chapter=MathTex(r"\mathbf{UNIT\;5}")
#         Title=Tex("Quadratic Equations and Graphs").next_to(Chapter,DOWN)
#         self.play(FadeIn(Chapter))
#         self.play(Write(Title))
#         self.play(Wait(1))
#         self.play(FadeOut(Chapter),FadeOut(Title))

class GlowingDot(VGroup):
    def __init__(self, point=ORIGIN, color=WHITE, radius=0.025, glow_levels=10, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.color = color
        main_dot = Dot(point=point, radius=self.radius, color=self.color, fill_opacity=1)
        self.add(main_dot)

        # Add "glow" layers
        for i in range(1, glow_levels + 1):
            # Gradually increase radius and decrease opacity
            glow_radius = self.radius * (1 + i * 0.5)
            glow_opacity = 1 / (i * 1.5)
            glow_dot = Dot(point=point, radius=glow_radius, color=self.color, fill_opacity=glow_opacity)
            self.add(glow_dot)
            # Send glow dots to the background so the main dot is on top
            glow_dot.set_z_index(-i) 

# class Taylors(Scene):
#     def construct(self):
#         t=ValueTracker(0)
#         plane=NumberPlane(x_range=[-5,5],
#                           y_range=[-3,7],
#                           axis_config={"include_tip": True},
#                           y_axis_config={"label_direction": LEFT+DOWN},
#                           x_axis_config={"label_direction": LEFT+DOWN}).scale(0.6)
#         plane_bg=always_redraw(lambda: Rectangle(color=YELLOW,width=plane.width, height=plane.height).set_z_index(1).move_to(plane.get_center()))
#         self.play(FadeIn(plane),FadeIn(plane_bg))
#         def x(t):
#             x=5*np.exp(-t.get_value()/10)*np.cos(t.get_value())
#             return min(5,max(-5,x))
#         def y(t):
#             y=5*np.exp(-t.get_value()/10)*np.sin(t.get_value())
#             return min(7,max(-3,y))
#         A=always_redraw(lambda: GlowingDot(color=TEAL).move_to(plane.c2p(x(t),y(t))))
#         A_path=TracedPath(A.get_center).set_color(color=TEAL)
#         self.play(FadeIn(A))
#         self.add(A_path)
#         self.wait(1)
#         self.play(t.animate.set_value(10*PI),run_time=20)

class Taylor(Scene):
    def construct(self):
        plane=NumberPlane(x_range=[-5,5],
                          y_range=[-3,7],
                          axis_config={"include_tip": True},
                          y_axis_config={"label_direction": LEFT+DOWN},
                          x_axis_config={"label_direction": LEFT+DOWN}).scale(0.6).set_z_index(1)
        x_labs=[]
        def f(x):
            y=np.sin(x)
            return y
        def p(x,n):
            poly=0
            count=0
            for index in range(1,n+1):
                if index%2==1:
                    poly+=(x)**(index+count)/(math.factorial(index+count))
                else:
                    poly-=(x)**(index+count)/(math.factorial(index+count))
                count+=1
            return poly

        for i in range(-8,12,2):
            if i==0:
                x_labs.append(MathTex(f"O"))
            else:
                x_labs.append(MathTex(f"{i}a"))
        x_labels=dict(zip([i for i in range(-4,6)],x_labs))
        curve=plane.plot(lambda x: f(x), color=TEAL, x_range=[-5,5])
        curve.set_stroke(width=curve.width*0.7)
        plane_bg=always_redraw(lambda: Rectangle(color=YELLOW,width=plane.width, height=plane.height).set_z_index(2).move_to(plane.get_center()))
        plane.add_coordinates(x_labels)
        self.add(plane, plane_bg)
        self.play(Create(curve), run_time=4, rate_func=linear)
        poly_group=VGroup()
        for i in range(5):
            poly_group.add(*[plane.plot(lambda x : p(x,i+1),color=BLUE)])
            if i==0:
                self.play(Create(poly_group[0]),run_time=2)
            else:
                self.play(ReplacementTransform(poly_group[i-1],poly_group[i]),run_time=2)

# class Quadratic1(Scene):
#     def construct(self):
#         Topic=Tex(r"\textbf{Graphing Quadratic Functions}")
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         self.add(NameLabel)
#         self.play(Write(Topic))
#         self.play(Topic.animate.to_edge(UP))
#         self.play(Wait(1))
#         k=ValueTracker(0) 
#         Plane1 = always_redraw(lambda: NumberPlane(x_range=[-5+k.get_value(),5+k.get_value()],y_range=[-5+k.get_value(),5+k.get_value()]).scale(0.6).to_edge(LEFT))
#         background_rectangle=Rectangle(width=Plane1.height,height=Plane1.height,color=YELLOW,fill_opacity=0).move_to(Plane1.get_center())
#         y_label=MathTex(r"Y").scale(0.9).move_to(Plane1.c2p(0.5,4.5))
#         x_label=MathTex(r"x").scale(0.9).move_to(Plane1.c2p(4.5,-0.5))
#         Plane1_Stuff=VGroup(background_rectangle,y_label,x_label).to_edge(LEFT)
#         self.play(FadeIn(Plane1),FadeIn(background_rectangle))
#         self.play(Write(x_label),Write(y_label))
        
