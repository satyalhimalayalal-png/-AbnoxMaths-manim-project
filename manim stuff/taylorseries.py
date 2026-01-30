from manim import *
from manim.opengl import *
import numpy as np
from colour import Color
import math
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

        