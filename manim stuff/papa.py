from manim import *
import numpy as np
from manim.opengl import *
from colour import Color
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
class Rota1(Scene):
    def construct(self):
        polys=VGroup([RegularPolygon(5,radius=1, fill_opacity=0.5,color=Color(hue=i/5,saturation=1,luminance=0.5)) for i in range(5)]).arrange(RIGHT)
        self.play(DrawBorderThenFill(polys))
        self.play(*[Rotate(polys[n],2*PI) for n in range(len(polys))])
        
class S(Scene):
    def construct(self):
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        vf = ArrowVectorField(
            lambda pos:pos, min_color_scheme_value=2, max_color_scheme_value=10, colors=colors
        )
        self.add(vf)

class CircularMotion(Scene):
    def construct(self):
        def revolve(planet,t):
            theta=2*PI*t
            radius=4
            planet.move_to([radius*np.cos(theta),radius*np.sin(theta),0])
        c=Dot(color=BLUE, fill_opacity=1)
        c.shift(6*LEFT)
        circ=Circle(radius=1,fill_opacity=0,color=WHITE)
        plane=NumberPlane(x_range=(0,8),y_range=(-2,2))
        ax=Axes(x_range=plane.x_range,y_range=plane.y_range,x_length=plane.x_length,y_length=plane.y_length,tips=None,axis_config={"include_numbers":True,})
        plane1=VGroup(plane,ax)
        curve=plane.plot(lambda x:-np.sin(x*PI/2), x_range=(0,8), color=[RED,ORANGE,YELLOW,GREEN,BLUE])
        circ.shift(5*LEFT)
        plane1.shift(1*RIGHT)
        self.add(plane1)
        curve.shift(1*RIGHT)
        owner_text = Text("Created by: Himalaya Satyal", font_size=24).move_to(DOWN*3.5 + LEFT * -5)
        self.add(owner_text)
        self.add(circ)
        self.play(Rotate(c,4*PI,about_point=LEFT*5),Create(curve),rate_func=linear,run_time=4)
        self.play(Wait(0.1))

class t(Scene):
    def construct(self):
        c=Dot(color=BLUE, fill_opacity=1)
        c.shift(6*LEFT)
        circ=Circle(radius=1,fill_opacity=0,color=WHITE)
        plane=NumberPlane(x_range=(0,8),y_range=(-2,2))
        ax=Axes(x_range=plane.x_range,y_range=plane.y_range,x_length=plane.x_length,y_length=plane.y_length,tips=None,axis_config={"include_numbers":True,})
        plane1=VGroup(plane,ax)
        curve=plane.plot(lambda x:-np.sin(x*PI/2), x_range=(0,8), color=[RED,ORANGE,YELLOW,GREEN,BLUE])
        circ.shift(5*LEFT)
        plane1.shift(1*RIGHT)
        self.add(plane1)
        curve.shift(1*RIGHT)
        owner_text = Text("Created by: Himalaya Satyal", font_size=24).move_to(DOWN*3.5 + LEFT * -5)
        self.add(owner_text)
        self.add(circ)
        self.play(Rotate(c,4*PI,about_point=LEFT*5),Create(curve),rate_func=linear,run_time=4)
        self.play(Wait(0.1))
        self.interactive_embed()

class Try(Scene):
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

class graph(Scene):
    def construct(self):
        plane_1=NumberPlane(x_range=(0,9),y_range=(0,7),x_length=10,y_length=6).to_corner(DL)
        rec_1=Rectangle(color=YELLOW,height=plane_1.height,width=plane_1.width).move_to(plane_1.get_center())
        plane_1.add_coordinates(None,None)
        self.add(plane_1,rec_1)
from manim import *
from colour import Color
from manim.opengl import *
import numpy as np
from math import *
class VectorTry(VectorScene):
    def construct(self):
        plane=NumberPlane()
        self.play(FadeIn(plane))
        vector=self.add_vector([-3,2],color=YELLOW)
        base=self.get_basis_vectors()
        self.add(base)
        self.vector_to_coords(vector=vector)
        vector1=self.add_vector([2,2])
        self.write_vector_coordinates(vector=vector1)
class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,show_coordinates=True,leave_ghost_vectors=True,show_basis_vectors=True)
    def construct(self):
        matrix=[[0,2],[0,-2]]
        matrix_text=MathTex(r"\begin{bmatrix}1&2\\2&1\end{bmatrix}").to_edge(UL)
        unit_square=self.get_unit_square()
        text=always_redraw(lambda: Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center()))
        vect=self.get_vector([1,-2],color=PURPLE)
        rect_1=Rectangle(height=2,width=1,color=BLUE,fill_opacity=0.5).shift(UL*2)
        circ1=Circle(radius=1, color=BLUE,fill_opacity=0.5).shift(DOWN*2)
        self.add_transformable_mobject(vect,unit_square,rect_1,circ1)
        self.add_background_mobject(matrix_text,text)
        self.apply_matrix(matrix)

class vectorsum(VectorScene):  
    def construct(self):
        x_labels=dict(zip([i for i in range(-7,7)],[i for i in range(-7,7)]))
        plane_1=self.add_plane().add_coordinates(x_labels,None)
        vec_B=self.add_vector([-1,3],color=BLUE)
        tex_B=MathTex(r"\vec{v}",color=BLUE).next_to(vec_B,RIGHT).scale(1.2)
        self.play(Write(tex_B))
        vec_C=Line(start=(plane_1.coords_to_point(-1,3)),end=(plane_1.coords_to_point(-3,-1)),color=RED).set_stroke(width=vec_B.get_stroke_width()).add_tip()
        vec_A=Line(start=(plane_1.coords_to_point(0,0)),end=(plane_1.coords_to_point(-2,-4)),color=RED).set_stroke(width=vec_B.get_stroke_width()).add_tip()
        tex_A=MathTex(r"\vec{u}",color=RED).next_to(vec_A,LEFT,buff=-0.2).scale(1.2)
        tex_A.add_updater(lambda tex_A:tex_A.become(MathTex(r"\vec{u}",color=RED).next_to(vec_A,LEFT,buff=-0.2).scale(1.2)))
        self.play(GrowFromPoint(vec_A,ORIGIN))
        self.play(Write(tex_A))
        self.play(ReplacementTransform(vec_A,vec_C))
        vec_D=self.add_vector((-3,-1)).set_color(YELLOW)
        tex_D=MathTex(r"\vec{u}+\vec{v}",color=YELLOW).next_to(vec_D,DOWN,buff=-0.1).scale(1.2)
        self.play(Write(tex_D))

class PiLabelAxis(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-2,4],
            y_range=[-3, 3,1]
        )
        x_pos=[i for i in range(-2,5)]
        x_vals = [
            MathTex(r"-\pi"), MathTex(r"-\frac{\pi}{2}"), MathTex(r"0"),
            MathTex(r"\frac{\pi}{2}"), MathTex(r"\pi"),
            MathTex(r"\frac{3\pi}{2}"), MathTex(r"2\pi")
        ]

        # Create a mapping dict
        x_dict = dict(zip(x_pos, x_vals))
        border = Rectangle(
            width=plane.width,
            height=plane.height,
            stroke_color=YELLOW,
            stroke_width=2
        )
        # Add labeled coordinates
        plane.add_coordinates(x_dict,None)
        ax=Axes(x_range=[-2,4],y_range=[-3, 3,1],x_length=plane.x_length,y_length=plane.y_length,tips=False)
        plane1=VGroup(plane,ax,border)
        Curve=plane.plot(lambda x:np.sin(x*PI/2),x_range=(-2,4),color=RED)
        self.play(FadeIn(plane1))
        self.play(Create(Curve))

class Matrix1(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,show_coordinates=True,show_basis_vectors=True)
    def construct(self):
        matrix=[[1,2],[2,1]]
        matrix_text=MathTex(r"\begin{bmatrix}1&2\\2&1\end{bmatrix}").to_edge(UL)
        unit_square=self.get_unit_square()
        rect_1=Rectangle(height=2,width=1,color=BLUE,fill_opacity=0.5).shift(UL*2)
        circ1=Circle(radius=1, color=BLUE,fill_opacity=0.5).shift(DOWN*2)
        self.add_transformable_mobject(unit_square,rect_1,circ1)
        self.add_background_mobject(matrix_text)
        self.apply_matrix(matrix)


class mat(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,show_basis_vectors=True,show_coordinates=True,leave_ghost_vectors=True)
    def construct(self):
        matrix_1=[[0,-1],[1,0]]
        self.get_basis_vectors()
        unit_square_1=self.get_unit_square()
        matrix_text=MathTex(r"A=\begin{bmatrix}0&-1\\1&0\end{bmatrix}").to_edge(UL)
        det_text=always_redraw(lambda: MathTex(r"\mathrm{det(A)}").scale(0.5).move_to(unit_square_1.get_center()))
        circle_1=Circle(radius=1,color=BLUE,fill_opacity=0.6).shift(RIGHT*2,UP*3)
        square_1=Square(side_length=2,color=BLUE,fill_opacity=0.6).shift(DOWN*1+LEFT*2)
        self.add(circle_1,square_1,matrix_text,unit_square_1,det_text)
        self.add_transformable_mobject(circle_1,square_1,unit_square_1)
        self.add_background_mobject(matrix_text,det_text)
        self.apply_matrix(matrix_1)

class VectorS(VectorScene):
    def construct(self):
        plane_1=self.add_plane(x_range=(-7,7),y_range=(-3,3))
        rec_1=Rectangle(width=plane_1.width,height=plane_1.height,fill_opacity=0,color=YELLOW)
        self.add(rec_1)
        vec_1_tex=MathTex(r"\vec{a}",color=RED)
        vec_2_tex=MathTex(r"\vec{b}",color=TEAL)
        vec_1plus2_tex=MathTex(r"\vec{a}+\vec{b}",color=GREEN)
        vec_1=Line(start=plane_1.coords_to_point(0,0),end=plane_1.coords_to_point(1,2),color=RED).add_tip()
        vec_2=Line(start=plane_1.coords_to_point(0,0),end=plane_1.coords_to_point(3,-3),color=TEAL).add_tip()
        vec_3=Line(start=plane_1.coords_to_point(1,2),end=plane_1.coords_to_point(4,-1),color=TEAL).add_tip()
        vec_1plus2=Line(start=plane_1.coords_to_point(0,0),end=plane_1.coords_to_point(4,-1),color=GREEN).add_tip()
        vecs=VGroup(vec_1,vec_2)
        self.play(AnimationGroup(*[GrowFromPoint(vec,plane_1.get_center()) for vec in vecs],lag_ratio=0))
        self.play(Write(vec_1_tex.next_to(vec_1,LEFT,buff=-0.2)))
        self.play(Write(vec_2_tex.next_to(vec_2,UP,buff=-1)))
        vec_2_tex.add_updater(lambda v:v.next_to(vec_2,UP,buff=-1))
        self.play(ReplacementTransform(vec_2,vec_3))
        self.play(GrowFromPoint(vec_1plus2,plane_1.get_center()))
        self.play(Write(vec_1plus2_tex.next_to(vec_1,DOWN*1.2+0.05*RIGHT,buff=0.5)))

class IntegrationReimannAnim(Scene):
    def construct(self):
        plane_1=NumberPlane(x_range=(-7,7),y_range=(-4,4),x_length=14,y_length=8)
        rec_1=Rectangle(width=plane_1.x_length,height=plane_1.y_length,fill_opacity=0,color=YELLOW)
        curve_1=plane_1.plot(lambda x:x*(x-2)*(x+2),color=GREEN)
        tex_1=MathTex(r"f(x)=\frac{1}{2}x(x-2)(x+2)",color=GREEN_A).to_edge((UL)).scale(0.8).add_background_rectangle(color=BLACK,opacity=1,buff=0.2,corner_radius=0.2)
        rec_2=RoundedRectangle(width=tex_1.width,height=tex_1.height,fill_opacity=0,color=GREEN,corner_radius=0.2).move_to(tex_1.get_center())
        self.add(plane_1,rec_1,curve_1,tex_1,rec_2)
        dx_list=[2**(-i) for i in range(1,9)]
        rects=VGroup(*[plane_1.get_riemann_rectangles(graph=curve_1,x_range=(-2,2),stroke_width=0.05,stroke_color=WHITE,dx=dX)for dX in dx_list])
        first_area=rects[0]
        for i in range(1,len(rects)):
            new_area=rects[i]
            self.play(Transform(first_area,new_area),run_time=2)
            self.wait(0.5)
        self.wait(1)

class Differentiation(Scene):
    def construct(self):
        plane_1=NumberPlane(x_range=(-7,7),y_range=(-4,4),x_length=14,y_length=8)
        rec_1=Rectangle(width=plane_1.x_length,height=plane_1.y_length,fill_opacity=0,color=YELLOW)
        def f(x):
            return x*(x-2)*(x+2)/2
        curve_1=plane_1.plot(lambda x:f(x),color=PURPLE,x_range=(-3,3))
        tex_1=MathTex(r"f(x)=\frac{1}{2}x(x-2)(x+2)",color=WHITE).to_edge((UL)).scale(0.8).add_background_rectangle(color=BLACK,opacity=1,buff=0.2,corner_radius=0.2)
        rec_2=RoundedRectangle(width=tex_1.width,height=tex_1.height,fill_opacity=0,color=PURPLE,corner_radius=0.2).move_to(tex_1.get_center())
        self.play(FadeIn(plane_1),DrawBorderThenFill(rec_1),Write(tex_1),Create(rec_2))
        self.play(Create(curve_1),run_time=3)
        dot_x_pos=ValueTracker(-3)
        doz = always_redraw(lambda: Dot(plane_1.coords_to_point(dot_x_pos.get_value(), f(dot_x_pos.get_value())),color=BLUE))
        self.add(doz)
        tangent_1=always_redraw(lambda: plane_1.get_secant_slope_group(x=dot_x_pos.get_value(),graph=curve_1,dx=0.01,secant_line_length=5))
        self.add(tangent_1)
        self.play(dot_x_pos.animate.set_value(3),run_time=6)

class Int(Scene):
    def construct(self):
        plane_1=NumberPlane(x_range=(-4,4.4),y_range=(-4,4),x_length=14,y_length=8)
        background_rectangle=Rectangle(width=plane_1.x_length,height=plane_1.y_length,color=YELLOW,fill_opacity=0).move_to(plane_1.center())
        curve_1=plane_1.plot(lambda x:2*np.sin(x*PI/2),x_range=(-1,2),color=PURPLE)
        tex_1=MathTex(r"f(x)=\mathrm{sin}(x),&-\frac{\pi}{2} \leqslant x\leqslant \pi",color=PURPLE).add_background_rectangle(color=BLACK,opacity=1,buff=0.2,corner_radius=0.2).to_edge(UL)
        bgrect_1=RoundedRectangle(corner_radius=0.2,color=PURPLE,fill_opacity=0,width=tex_1.width,height=tex_1.height).move_to(tex_1.get_center())
        plane_1.add_coordinates(dict(zip([i for i in range(-4,5)],[MathTex(a) for a in [r"-2\pi",r"-\frac{3\pi}{2}",r"-\pi",r"-\frac{\pi}{2}",r"0",r"\frac{\pi}{2}",r"\pi",r"\frac{3\pi}{2}",r"2\pi"]])))
        plane_stuff=VGroup(plane_1,background_rectangle)
        vec_1=Line(start=plane_1.coords_to_point(3,2),end=plane_1.coords_to_point(1.8,1),color=YELLOW).add_tip()
        dx_array=[2**(-i) for i in range(7)]
        reimrects=VGroup(*[plane_1.get_riemann_rectangles(graph=curve_1,x_range=(-1,2),dx=d,stroke_color=WHITE,stroke_width=0.05,color=[PURPLE,DARK_BLUE,BLUE]) for d in dx_array])
        FirstArea=reimrects[0]
        tex_2=MathTex(r"\int_{-\frac{\pi}{2}}^{\pi} \mathrm{sin}(x) \mathrm{d}x",
                                color=WHITE).to_edge(UR).add_background_rectangle(
                                    color=BLACK,opacity=1,buff=0.2,corner_radius=0.2)
        bgrect_2=RoundedRectangle(corner_radius=0.2,color=WHITE,fill_opacity=0,width=tex_2.width,height=tex_2.height).move_to(tex_2.get_center())
        self.play(FadeIn(plane_stuff))
        self.play(Write(tex_1),Create(bgrect_1))
        self.play(Create(curve_1),run_time=4)
        self.play(AnimationGroup(Write(tex_2),Create(bgrect_2),lag_ratio=0.4))
        self.play(Create(vec_1))
        self.play(FadeIn(FirstArea))
        for index in range(1,len(reimrects)):
            ReplaceArea=reimrects[index]
            self.play(Transform(FirstArea,ReplaceArea))

class DifferentiationOfSin(Scene):
    def construct(self):
        plane_1=NumberPlane(x_range=(-2,2),y_range=(-2.8,2.8),x_length=6.4,y_length=5)
        plane_1.to_edge(LEFT)
        plane_1_y_ax=MathTex(r"f(x)",color=YELLOW).scale(0.8).move_to(plane_1.get_center()+UP*2+LEFT*0.5)
        plane_1_x_ax=MathTex(r"x",color=YELLOW).scale(0.8).move_to(plane_1.get_center()+DOWN*0.25+RIGHT*2.7)
        background_rectangle=Rectangle(width=plane_1.x_length,height=plane_1.y_length,color=WHITE,fill_opacity=0).move_to(plane_1.get_center())
        curve_1=plane_1.plot(lambda x:2*np.sin(x*PI/2),x_range=(-2,2),color=PURPLE)
        plane_1.add_coordinates(dict(zip([i for i in range(-3,4)],[MathTex(a) for a in [r"-\frac{3\pi}{2}",r"-\pi",r"-\frac{\pi}{2}",r"0",r"\frac{\pi}{2}",r"\pi"]])))
        plane_stuff=VGroup(plane_1,background_rectangle,plane_1_y_ax,plane_1_x_ax)
        x1=ValueTracker(-2)
        dotty=always_redraw(lambda:Dot(plane_1.c2p(x1.get_value(),2*np.sin(x1.get_value()*PI/2)),color=BLUE))
        tangy=always_redraw(lambda:plane_1.get_secant_slope_group(x=x1.get_value(),graph=curve_1,dx=0.01,secant_line_length=2))
        tangy_tex=always_redraw(lambda:MathTex(r"m="+f"{np.cos(x1.get_value()*PI/2):.2f}",color=GREEN).next_to(dotty,buff=-0.1).scale(0.75))
        plane_2=NumberPlane(x_range=(-2,2),y_range=(-2.8,2.8),x_length=6.4,y_length=5)
        plane_2.to_edge(RIGHT)
        plane_2_y_ax=MathTex(r"\frac{d}{dx}[f(x)]",color=YELLOW).scale(0.8).move_to(plane_2.get_center()+UP*2+LEFT*1)
        plane_2_x_ax=MathTex(r"x",color=YELLOW).scale(0.8).move_to(plane_2.get_center()+DOWN*0.25+RIGHT*2.7)
        background_rectangleA=Rectangle(width=plane_2.x_length,height=plane_2.y_length,color=WHITE,fill_opacity=0).move_to(plane_2.get_center())
        curve_2=plane_2.plot(lambda x:2*np.cos(x*PI/2),x_range=(-2,1.9),color=GREEN)
        plane_2.add_coordinates(dict(zip([i for i in range(-2,3)],[MathTex(a) for a in [r"-\pi",r"-\frac{\pi}{2}",r"0",r"\frac{\pi}{2}",r"\pi"]])))
        plane_stuff2=VGroup(plane_2,background_rectangleA,plane_2_y_ax,plane_2_x_ax)
        x2=ValueTracker(-2)
        dotty2=always_redraw(lambda:Dot(plane_2.c2p(x2.get_value(),2*np.cos(x2.get_value()*PI/2)),color=BLUE))\
        
        texy_1=MathTex(r"f(x)=\sin x",color=PURPLE).add_background_rectangle(color=BLACK,buff=0.2).to_edge(UL).shift(RIGHT*1.5)
        texy_2=MathTex(r"f'(x)=\cos x",color=GREEN).add_background_rectangle(color=BLACK,buff=0.2).to_edge(UR).shift(LEFT*1.5)
        recA=RoundedRectangle(color=PURPLE,fill_opacity=0,height=texy_1.height,width=texy_1.width,corner_radius=0.2).move_to(texy_1.get_center())
        recB=RoundedRectangle(color=GREEN,fill_opacity=0,height=texy_2.height,width=texy_2.width,corner_radius=0.2).move_to(texy_2.get_center())
        texy1=VGroup(texy_1,recA)
        texy2=VGroup(texy_2,recB)
        self.play(FadeIn(plane_stuff))
        self.play(Create(curve_1),run_time=4)
        self.play(FadeIn(plane_stuff2))
        self.play(FadeIn(dotty2),FadeIn(dotty),FadeIn(tangy),FadeIn(tangy_tex))
        self.play(x1.animate.set_value(1.9),x2.animate.set_value(1.9),Create(curve_2),run_time=6,rate_func=linear)
        self.play(Write(texy1),Write(texy2))

class V(Scene):
    def construct(self):
        plane=NumberPlane()
        curve=plane.plot(lambda x:np.log2(x),color=RED)
        self.play(FadeIn(plane))
        self.play(Create(curve))
        self.interactive_embed()

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
        
class taylor(Scene):
    def construct(self):
        graph=NumberPlane()
        curve_to_approximate=graph.plot(lambda x: np.sin(x),color=GREEN)
        
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
        
        self.play(FadeIn(graph))
        self.play(Create(curve_to_approximate),run_time=3)
        poly_group=VGroup()
        for i in range(10):
            poly_group.add(*[graph.plot(lambda x : p(x,i+1),color=BLUE)])
            if i==0:
                self.play(Create(poly_group[0]),run_time=2)
            else:
                self.play(ReplacementTransform(poly_group[i-1],poly_group[i]),run_time=2)

class ThreeD(Scene):
    def construct(self):
        plane=ThreeDAxes()
        c=Line3D(start=(2,1,2),end=(0,1,-2))
        self.play(Create(plane),Create(c))
        a=MathTex(r"a").move_to(ORIGIN)
        self.play(Create(a))
        self.play(Indicate(a))
        self.interactive_embed()

from manim import *
import numpy as np
from manim.opengl import *
class Projectile_Motion1(Scene):
    def construct(self):
        theta=ValueTracker(45)
        plane=NumberPlane().shift(LEFT*5)
        curve=always_redraw(lambda:DashedVMobject(plane.plot(lambda x:x*np.tan(np.deg2rad(theta.get_value()))
                -(x**2)*(np.cos(np.deg2rad(theta.get_value())))**(-2)/20,
                x_range=(0,10*np.sin(2*np.deg2rad(theta.get_value())))),num_dashes=40))
        ball=Circle(radius=0.25,color=BLUE,fill_opacity=1).shift(LEFT*5)
        horizontal=DashedLine(start=ball.get_center(),end=ball.get_center()+RIGHT*1.3)
        velocity_vector=always_redraw(lambda:Line(start=ball.get_center(),
                    end=ball.get_center()+2*RIGHT*np.cos(np.deg2rad(theta.get_value()))+2*UP*np.sin(np.deg2rad(theta.get_value())),color=RED).add_tip().set_stroke(width=6))
        angle_arc=always_redraw(lambda:Arc(radius=0.6,arc_center=ball.get_center(),angle=np.deg2rad(theta.get_value()),color=YELLOW))
        start_point=ball.get_center()
        velocity_tex=always_redraw(lambda: MathTex(r"\vec{v}",color=RED).next_to(ball,UP,buff=0.06).rotate(angle=np.deg2rad(theta.get_value()+0.06*UP),about_point=ball.get_center()).shift(RIGHT*np.cos(np.deg2rad(theta.get_value()))+UP*np.sin(np.deg2rad(theta.get_value()))))
        self.play(DrawBorderThenFill(ball))
        self.play(AnimationGroup(*[Create(x) for x in [horizontal,angle_arc]],lag_ratio=1))
        self.play(Create(curve))
        self.play(GrowFromPoint(velocity_vector,point=ball.get_center()))
        self.play(Write(velocity_tex))
        self.wait(0.5)
        self.play(theta.animate.set_value(80))
        self.play(theta.animate.set_value(45))
        self.play(theta.animate.set_value(0.1))
        self.play(theta.animate.set_value(50))
        velocity_vector.clear_updaters()
        angle_arc.clear_updaters()
        velocity_tex.clear_updaters()
        curve.clear_updaters()
        theta_new_tex=MathTex(r"\theta=",f"{theta.get_value():.1f}",r"^\circ",color=YELLOW).set_color_by_tex(r"\theta=",WHITE).move_to(ball.get_center()+1.7*RIGHT+0.5*UP)
        self.play(Write(theta_new_tex))
        self.play(theta_new_tex.animate.to_edge(UL))
        theta_new_tex.add_background_rectangle(buff=0.2,color=BLACK,opacity=1)
        rect_1=RoundedRectangle(corner_radius=0.2,color=GREEN,height=theta_new_tex.height,width=theta_new_tex.width).move_to(theta_new_tex.get_center())
        self.play(Create(rect_1))
        x=ValueTracker(0)
        theta_0=theta.get_value()
        theta.add_updater(lambda theta:theta.set_value(np.rad2deg(np.arctan(np.tan(np.deg2rad(theta_0))-0.1*x.get_value()*(np.cos(np.deg2rad(theta_0)))**(-2)))))
        theta_new_tex.add_updater(lambda a:a.become(MathTex(r"\theta=",f"{np.abs(theta.get_value()):.1f}",r"^\circ",color=YELLOW).set_color_by_tex(r"\theta=",WHITE).to_edge(UL)).add_background_rectangle(buff=0.2,color=BLACK,opacity=1))
        ball.add_updater(lambda ball:ball.move_to((x.get_value()-5,x.get_value()*np.tan(np.deg2rad(theta_0))-(x.get_value()**2)*(np.cos(np.deg2rad(theta_0)))**(-2)/20,0)))
        horizontal.add_updater(lambda x:x.become(DashedLine(start=ball.get_center(),end=ball.get_center()+RIGHT*1.3)))
        velocity_vector.add_updater(lambda a:a.become(Line(start=ball.get_center(),
                    end=ball.get_center()+2*RIGHT*np.cos(np.deg2rad(theta.get_value()))+2*UP*np.sin(np.deg2rad(theta.get_value())),color=RED).add_tip().set_stroke(width=6)))
        angle_arc.add_updater(lambda a:a.become(Arc(radius=0.6,arc_center=ball.get_center(),angle=np.deg2rad(theta.get_value()),color=YELLOW)))
        velocity_tex.add_updater(lambda d:d.become(MathTex(r"\vec{v}",color=RED).next_to(ball,UP,buff=0.06).rotate(angle=np.deg2rad(theta.get_value()+0.06*UP),about_point=ball.get_center()).shift(RIGHT*np.cos(np.deg2rad(theta.get_value()))+UP*np.sin(np.deg2rad(theta.get_value())))))
        self.play(x.animate.set_value(10*np.sin(2*np.deg2rad(theta_0))),run_time=3,rate_func=linear)
        self.play(Wait(0.2))
        
        end_point=ball.get_center()
        br_x=BraceBetweenPoints(point_1=start_point,point_2=end_point,color=PURPLE)
        max_x=(10*np.sin(2*np.deg2rad(theta_0)))
        x_range=MathTex(r"R").next_to(br_x,DOWN)
        self.play(AnimationGroup(FadeIn(br_x),Write(x_range),lag_ratio=1))
        vertical_max=start_point+(0.5*max_x*np.tan(np.deg2rad(theta_0))-(0.5*max_x)**2/(20*(np.cos(np.deg2rad(theta_0)))**2))*UP
        br_y=BraceBetweenPoints(point_1=start_point,point_2=vertical_max+0.1*DOWN,direction=LEFT,color=PURPLE)
        y_range=MathTex(r"h").next_to(br_y,LEFT)
        self.play(FadeIn(br_y))
        self.play(Write(y_range))
        self.play(x.animate.set_value(0),run_time=3,rate_func=linear)
        self.wait(0.2)
        v_0_label=MathTex(r"v_0=",r"10.0\mathrm{\,m\,s}^{-1}",color=YELLOW).set_color_by_tex(r"v_0=",WHITE).add_background_rectangle(buff=0.2,color=BLACK,opacity=1).next_to(x_range,DOWN)
        rect_v_0_label=RoundedRectangle(corner_radius=0.2,color=PURPLE,height=v_0_label.height,width=v_0_label.width).move_to(v_0_label.get_center())
        rect_v_0_label.add_updater(lambda m: m.move_to(v_0_label.get_center()))
        self.play(Write(v_0_label))
        self.play(Create(rect_v_0_label))
        rect_1.add_updater(lambda m: m.move_to(theta_new_tex.get_center()))
        theta_new_tex.clear_updaters()
        self.wait(1)
        bg_stuff=VGroup(br_x,br_y,x_range,y_range,curve)
        for mob in bg_stuff:
            mob.clear_updaters()
        self.play(FadeOut(bg_stuff))
        self.play(v_0_label.animate.next_to(theta_new_tex,RIGHT))
        theta_on_diagram=MathTex(r"\theta",color=YELLOW).move_to(ball.get_center()+RIGHT*1.2+UP*0.6)
        vertical_component_of_v_0=Line(start=ball.get_center(),end=ball.get_center()+2*UP*np.sin(np.deg2rad(theta_0)),color=GREEN).add_tip().set_stroke(width=6)
        horizontal_component_of_v_0=Line(start=ball.get_center(),end=ball.get_center()+2*RIGHT*np.cos(np.deg2rad(theta_0)),color=YELLOW).add_tip().set_stroke(width=6)
        vertical_tex=MathTex(r"v_0\sin{\theta}",color=GREEN).next_to(vertical_component_of_v_0,LEFT)
        horizontal_tex=MathTex(r"v_0\cos{\theta}",color=YELLOW).next_to(horizontal_component_of_v_0,DOWN)
        self.play(GrowFromPoint(vertical_component_of_v_0,point=ball.get_center()),GrowFromPoint(horizontal_component_of_v_0,point=ball.get_center()))
        self.play(Write(theta_on_diagram))
        l0=MathTex(r"v=u+a\times t").next_to(v_0_label,DR)
        l1=MathTex(r"v_y=",r"v_0\sin{\theta}",r"-gt").next_to(l0,DOWN)
        l1[1].set_color(GREEN)
        self.play(Write(vertical_tex),Write(horizontal_tex))
        t=np.sin(np.deg2rad(theta_0))*10/9.81
        l2=MathTex(r"0=v_0\sin{\theta}-gt").next_to(l1,DOWN)
        l3=MathTex(r"v_0 \sin{\theta}=gt").next_to(l2,DOWN)
        l4=MathTex(r"9.81\times t=10\times \sin",f"{theta_0:.1f}",r"^\circ").next_to(l3,DOWN)
        l5=MathTex(r"t=\frac{10}{9.81} \times \sin",f"{theta_0:.1f}",r"^\circ}").next_to(l4,DOWN)
        l6=MathTex(r"\therefore t \approx",f"{t:.3g}",r"\, \mathrm{s}",color=YELLOW).set_color_by_tex(r"t \approx",WHITE).next_to(l5,DOWN)
        self.play(Write(l0))
        l1_1=l1[1].copy()
        self.play(TransformMatchingShapes(vertical_tex,l1_1))
        self.play(Write(l1))
        self.wait(0.5)
        self.play(TransformMatchingShapes(l1.copy(),l2))
        self.wait(0.5)
        self.play(TransformMatchingShapes(l2.copy(),l3))
        self.wait(0.5)
        self.play(TransformMatchingShapes(l3.copy(),l4))
        self.wait(0.5)
        self.play(TransformMatchingShapes(l4.copy(),l5))
        self.wait(0.5)
        self.play(TransformMatchingShapes(l5.copy(),l6))
        l6.add_background_rectangle(buff=0.2,color=BLACK,opacity=1)
        l6_border=always_redraw(lambda: RoundedRectangle(corner_radius=0.2,color=BLUE,height=l6.height,width=l6.width).move_to(l6.get_center()))
        self.play(Create(l6_border))
        self.wait(1)
        lines_without_6=VGroup(l2,l3,l4,l5)
        self.play(FadeOut(lines_without_6),FadeOut(l0),FadeOut(l1),FadeOut(l1_1))
        self.wait(0.2)
        self.play(l6.animate.become(MathTex(r"t \approx",f"{t:.3g}",r"\,\mathrm{s}",color=YELLOW).set_color_by_tex(r"t \approx",WHITE).next_to(l5,DOWN).add_background_rectangle(buff=0.2,color=BLACK,opacity=1)))
        self.play(l6.animate.next_to(v_0_label,RIGHT))
        R=10*np.cos(np.deg2rad(theta_0))*2*t
        h=10*np.sin(np.deg2rad(theta_0))*t-0.5*9.81*t**2
        m1=MathTex(r"v_0\cos \theta",r"\times T=R").next_to(v_0_label,DR)
        m1[0].set_color(YELLOW)
        m1_1=m1[0].copy()
        m2=MathTex(r"v_0\cos \theta",r"\times 2t=R").next_to(m1,DOWN)
        m3=MathTex(r"R=10 \times \cos",f"{theta_0:.1f}",r"^\circ \times 2 \times",f"{t:.3g}").next_to(m2,DOWN)
        m4=MathTex(r"\therefore R \approx",f"{R:.3g}",r"\;m",color=YELLOW).next_to(m3,DOWN)
        m4[0].set_color(WHITE)
        n1=MathTex(r"h=ut+\frac{1}{2}at^2").next_to(v_0_label,DR)
        n2=MathTex(r"h=v_0\sin \theta \times t-\frac{1}{2}\times g\times t^2")
        n3=MathTex(r"h=10\times \sin",f"{theta_0:.1f}", r"^\circ\times",f"{t:.3g}",r"-\frac{1}{2}\times 9.81\times",f"{t:.3g}",r"^2")
        n4=MathTex(r"\therefore h \approx",f"{h:.3g}",r"\,m",color=YELLOW)
        n4[0].set_color(WHITE)
        self.play(TransformMatchingShapes(horizontal_tex,m1_1))
        self.wait(0.5)
        self.play(Write(m1))
        self.wait(0.5)
        self.play(TransformMatchingShapes(m1.copy(),m2))
        self.wait(0.5)
        self.play(TransformMatchingShapes(m2.copy(),m3))
        self.wait(0.5)
        self.play(TransformMatchingShapes(m3.copy(),m4))
        m4.add_background_rectangle(buff=0.2,color=BLACK,opacity=1)
        m4_border=always_redraw(lambda: RoundedRectangle(corner_radius=0.2,color=RED,height=m4.height,width=m4.width).move_to(m4.get_center()))
        self.play(Create(m4_border))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in [m1,m2,m3,m1_1]])
        self.wait(0.2)
        self.play(m4.animate.next_to(l6,RIGHT))
        n_group=VGroup(n1,n2,n3,n4).arrange(DOWN)
        self.play(Write(n1))
        self.wait(0.5)
        self.play(TransformMatchingShapes(n1.copy(),n2))
        self.wait(0.5)
        self.play(TransformMatchingShapes(n2.copy(),n3))
        self.wait(0.5)
        self.play(TransformMatchingShapes(n3.copy(),n4))
        n4.add_background_rectangle(buff=0.2,color=BLACK,opacity=1)
        n4_border=always_redraw(lambda: RoundedRectangle(corner_radius=0.2,color=YELLOW,height=n4.height,width=n4.width).move_to(n4.get_center()))
        self.play(Create(n4_border))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in [n1,n2,n3]])
        self.wait(0.2)
        self.play(n4.animate.next_to(m4,DOWN))
        self.wait(1)
        ball_stuff=VGroup(ball,horizontal,velocity_vector,velocity_tex,angle_arc,horizontal_component_of_v_0,vertical_component_of_v_0,theta_on_diagram)
        for mob in ball_stuff:
            mob.clear_updaters()
        bg_stuff.shift(DOWN*2)
        T=MathTex(r"T \approx",f"{2*t:.3g}",r"\,\mathrm{s}",color=YELLOW).set_color_by_tex(r"T \approx",WHITE).next_to(l6,DOWN,0.35).add_background_rectangle(buff=0.2,color=BLACK,opacity=1)
        T_border=always_redraw(lambda: RoundedRectangle(corner_radius=0.2,color=TEAL,height=T.height,width=T.width).move_to(T.get_center()))
        self.play(Write(T),Write(T_border))
        self.play(ball_stuff.animate.shift(DOWN*2))
        self.play(FadeIn(bg_stuff))
        self.interactive_embed()

class threed(ThreeDScene):
    def construct(self):
        plane=NumberPlane()
        Curve=plane.plot(lambda x:x**2-2,x_range=(-2,2),color=RED)
        self.add(plane)
        self.play(Create(Curve))
        self.interactive_embed()