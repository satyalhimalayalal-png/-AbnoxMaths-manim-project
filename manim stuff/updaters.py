from manim import *
from manim.opengl import *
import numpy as np
config.pixel_width = 720  # or 1080 or more
config.pixel_height = 1280
config.frame_width = 16
config.frame_height = 9
class t(Scene):
    def construct(self):
        sq=Square(side_length=0.5,color=BLUE,fill_opacity=0.7)
        sq.shift(LEFT*3)
        doz=Dot(fill_opacity=1,color=RED)
        doz.add_updater(lambda dxoz:doz.next_to(sq,RIGHT))

        def shifter(mob,dt):
            mob.shift(2*RIGHT*dt)
        sq.add_updater(shifter)

        def scaler(dt):
            for mob in self.mobjects:
                mob.set(width=2/(1+np.linalg.norm(mob.get_center())))
        self.add_updater(scaler)
        self.add(doz,sq)
        self.update_self(0)
        self.play(Wait(4))
class a(Scene):
    def construct(self):
        ax=Axes(x_range=(-6,6,1),y_range=(-10,10,1),x_length=8,y_length=6,tips=None)
        parabola=ax.plot(lambda x:x**2, color=YELLOW,x_range=(-3,3))
        a=ValueTracker(1)
        parabola.add_updater(lambda parabola:parabola.become(ax.plot(lambda x:a.get_value()*x**2, color=BLUE,x_range=(-3,3))))
        a_numb=DecimalNumber(a.get_value(),color=GOLD,num_decimal_places=2,show_ellipsis=True)
        a_numb.add_updater(lambda a_number:a_number.set_value(a.get_value()).next_to(parabola,RIGHT))
        self.add(ax,parabola,a_numb)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))
        self.wait(0.1)

class g(Scene):
    def construct(self):
        # Create objects
        circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.8)
        plane = NumberPlane(
            y_range=(-5, 1, 1),
            x_range=(0, 3, 1),
            background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.shift(ORIGIN)

        # Tracker for time
        time = ValueTracker(0)

        # Update circle position using kinematic equation: y = -0.5 * g * t^2
        circle.add_updater(lambda mob: mob.move_to(UP * (1 - 0.5 * 9.81 * time.get_value()**2)))

        # Add labels and objects to the scene
        time_label = always_redraw(lambda: Tex(f"t = {time.get_value():.2f}s").next_to(circle, RIGHT))
        self.add(plane, circle, time_label)

        # Animate the fall
        self.play(time.animate.set_value(0.6), run_time=2, rate_func=linear)
        self.wait()

class O(Scene):
    def construct(self):
        hello_text=Tex("Hello World")
        self.play(Write(hello_text))
        self.play(self.camera.animate.set_euler_angles(theta=-10*DEGREES,phi=50*DEGREES))
        self.play(FadeOut(hello_text))
        surface=OpenGLSurface(lambda u,v:(u,v,u*np.sin(v)+v*np.cos(u)),u_range=(-3,3),v_range=(-3,3))
        A=OpenGLSurfaceMesh(surface)
        self.play(Create(A))
        self.play(FadeTransform(A,surface))
        self.wait()
        light=self.camera.light_source
        self.play(light.animate.shift([0,0,-20]))
        self.play(light.animate.shift([0,0,10]))
        self.play(self.camera.animate.set_euler_angles(theta=90*DEGREES))
        self.interactive_embed()
        
