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