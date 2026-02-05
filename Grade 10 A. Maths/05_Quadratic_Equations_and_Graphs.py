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

class Quadratic1(Scene):
    def construct(self):
        Topic=Tex(r"\textbf{Graphing Quadratic Functions}")
        NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
        self.add(NameLabel)
        self.play(Write(Topic))
        self.play(Topic.animate.to_edge(UP))
        self.play(Wait(1))
        k=ValueTracker(0) 
        x_coords=dict(zip([i for i in range(-4,5)],[i for i in range(-4,5)]))
        y_coords=dict(zip([i for i in range(-4,5)],[i for i in range(-4,5)]))
        Plane1 = always_redraw(lambda: NumberPlane(x_range=[-5+k.get_value(),5+k.get_value()],y_range=[-5+k.get_value(),5+k.get_value()],x_axis_config={"label_direction":DL},y_axis_config={"label_direction":DL}).scale(0.6).to_edge(LEFT).add_coordinates(x_coords,y_coords))
        background_rectangle=Rectangle(width=Plane1.height,height=Plane1.height,color=YELLOW,fill_opacity=0).move_to(Plane1.get_center())
        y_label=MathTex(r"y").scale(0.9).move_to(Plane1.c2p(-0.5,4.5))
        x_label=MathTex(r"x").scale(0.9).move_to(Plane1.c2p(4.5,-0.5))
        Plane1_Stuff=VGroup(background_rectangle,y_label,x_label).to_edge(LEFT)
        Tab=Table([[f"{x}" for x in range(-2,3)],[f"{x**2}" for x in range(-2,3)]],include_outer_lines=True, line_config={"stroke_width": 0.5}, row_labels=[MathTex(r"x").scale(1.5),MathTex(r"y").scale(1.5)]).scale(0.4).next_to(Graph,RIGHT)
        Tab.get_entries().set_opacity(0)
        Points=Group(*[GlowingDot(Plane1.c2p(i,i**2),color=YELLOW_B) for i in range(-2,3)]).set_z_index(5)
        self.play(FadeIn(Plane1),FadeIn(background_rectangle))
        self.play(Write(x_label),Write(y_label))
        self.play(FadeIn(Tab))
        cols=Tab.get_columns()
        self.play(cols[0].animate.set_opacity(1))
        cols=[*cols]
        cols.pop(0)
        for x in range(5):
            self.play(AnimationGroup(*[AnimationGroup(GrowFromCenter(Points[x]), cols[x].animate.set_opacity(1))],lag_ratio=0.5))
        
