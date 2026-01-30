# from manim import *
# import numpy as np

# class Intro(Scene):
#     def construct(self):
#         Chapter=MathTex(r"\mathbf{UNIT\;8}")
#         Title=Tex("Co-ordinate Geometry").next_to(Chapter,DOWN)
#         self.play(FadeIn(Chapter))
#         self.play(Write(Title))
#         self.play(Wait(1))
#         self.play(FadeOut(Chapter),FadeOut(Title))

# class Part1(Scene):
#     def construct(self):
#         Topic1=MathTex(r"\mathbf{Angle\;between\;two\;straight\;lines}")
#         Subtopic1=Tex("Angle between two straight lines when slopes are known",color=WHITE).scale(0.8)
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         self.play(Write(Topic1))
#         self.play(Topic1.animate.to_edge(UP))
#         self.play(Wait(1))
#         self.play(Write(Subtopic1))
#         self.play(Wait(0.8))
#         self.play(Indicate(Subtopic1))
#         self.play(FadeOut(Subtopic1))
#         Plane1 = NumberPlane(x_range=[-11,11],y_range=[-2,8]).scale(0.6)
#         background_rectangle=Rectangle(width=Plane1.width,height=Plane1.height,color=YELLOW,fill_opacity=0).move_to(Plane1.get_center())
#         Plane1.axes.set_stroke(width=4)
#         y_label=MathTex(r"y").move_to([0.5*0.6,4.5*0.6,0]).scale(0.9)
#         x_label=MathTex(r"x").move_to([10.5*0.6,-2.5*0.6,0]).scale(0.9)
#         a=ValueTracker(2)
#         def f(x):
#             y=a.get_value()*x-0.5
#             return max(min(y,8),-2)
#         def g(x):
#             y=5-x
#             return max(min(y,8),-2)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: f(x),color=LIGHT_BROWN,x_range=[-11, 11]).set_stroke(width=3))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g(x),color=LIGHT_GRAY,x_range=[-11, 11]).set_stroke(width=3))
#         background_rectangle.set_z_index(4)
#         self.play(FadeIn(Plane1),FadeIn(background_rectangle),Write(NameLabel))
#         self.play(Write(x_label),Write(y_label))
#         self.play(Wait(0.1))
#         self.play(FadeIn(l1),run_time=1)
#         self.play(a.animate.set_value(1),run_time=1.7)
#         L1=Plane1.plot(lambda x: f(x),color=LIGHT_BROWN,x_range=[-11, 11]).set_stroke(width=3)
#         self.play(ReplacementTransform(l1,L1))
#         m1=Plane1.get_secant_slope_group(x=6,graph=L1,secant_line_length=3,dx=1,include_secant_line=False,dy_line_color=YELLOW).set_stroke(width=2)
#         m1.shift(5*LEFT)
#         self.play(FadeIn(l2),run_time=1)
#         self.wait(0.2)
#         l1_label=MathTex(r"l_1",color=LIGHT_BROWN).move_to([6*0.6,0.6,0]).scale(0.9)
#         l2_label=MathTex(r"l_2",color=LIGHT_GRAY).move_to([-2*0.6,3*0.6,0]).scale(0.9)
#         theta=ParametricFunction(lambda t: Plane1.c2p(np.cos(t)+2.75,np.sin(t)+2.25),t_range=(1.25*PI,1.75*PI),color=GREEN_C)
#         theta_label=MathTex(r"\theta",color=GREEN_C).next_to(theta,DOWN).scale(0.9)
#         self.play(AnimationGroup(Write(l1_label),Write(l2_label),lag_ratio=0.6))
#         alpha=ParametricFunction(lambda t: Plane1.c2p(np.cos(t)+5,np.sin(t)),t_range=(0,0.75*PI),color=RED)
#         alpha_label=MathTex(r"\alpha",color=RED).next_to(alpha,0.5*UR).scale(0.9)
#         beta=ParametricFunction(lambda t: Plane1.c2p(np.cos(t)+0.5,np.sin(t)),t_range=(0,0.25*PI),color=PURPLE)
#         beta_label=MathTex(r"\beta",color=PURPLE).next_to(beta,0.7*UL).scale(0.9)
#         self.play(Create(theta),Create(alpha),Create(beta),run_time=2.5)
#         self.play(Write(theta_label),Write(alpha_label),Write(beta_label),run_time=2.5)
#         static=[]
#         for mob in self.mobjects:
#             if mob!=NameLabel and mob!=Topic1:
#                 static.append(mob)
#         static_mobs=Group(*[mob for mob in static])
#         self.play(Wait(3))
#         self.play(static_mobs.animate.shift(5*LEFT))
#         t1=MathTex(r"\alpha=\theta+\beta").scale(0.7).next_to(background_rectangle,RIGHT,buff=0.5).to_edge(UP).shift(DOWN)
#         t2=MathTex(r"\Rightarrow \theta=\alpha-\beta").scale(0.7)
#         t3=MathTex(r"\Rightarrow \tan\theta=\tan(\alpha-\beta)").scale(0.7)
#         t4=MathTex(r"=\frac{\tan\alpha-\tan\beta}{1+\tan\alpha\cdot \tan\beta}").scale(0.7)
#         t5=MathTex(r"\Rightarrow \tan\theta=\pm\frac{m_1-m_2}{1+m_1 m_2}").scale(0.7)
#         t6=MathTex(r"\therefore \theta=\tan^{-1}\bigg(\pm \frac{m_1-m_2}{1+m_1 m_2}\bigg)").scale(0.7)
#         tGroup=Group(t2,t3,t4,t5,t6)
#         tanimGroup=Group(t2,t3,t4)
#         referencet=t1
#         AngleGroup=Group(theta_label,alpha_label,beta_label)
#         for t in tGroup:
#             t.next_to(referencet,DOWN).align_to(t1,LEFT)
#             referencet=t
#         self.play(TransformMatchingShapes(AngleGroup.copy(),t1),run_time=1.5)
#         self.play(Wait(0.8))
#         self.play(AnimationGroup(*[Write(t) for t in tanimGroup],lag_ratio=2))
#         m2=Plane1.get_secant_slope_group(x=0,graph=l2,secant_line_length=3,dx=1,include_secant_line=False,dy_line_color=YELLOW).set_stroke(width=2)
#         m1_label=MathTex(r"m_1",color=YELLOW).next_to(m1,RIGHT).scale(0.7)
#         m2_label=MathTex(r"m_2",color=YELLOW).next_to(m2,RIGHT).scale(0.7)
#         self.play(Wait(0.8))
#         self.play(Create(m1),Create(m2))
#         self.play(Write(m1_label),Write(m2_label))
#         mGroup=Group(m1_label,m2_label)
#         self.play(TransformMatchingShapes(mGroup.copy(),t5))
#         mobs_to_disappear=[]
#         for mob in self.mobjects:
#             if mob!=NameLabel and mob!=Topic1:
#                 mobs_to_disappear.append(mob)
#         self.play(Write(t6))
#         theta_prime=ParametricFunction(lambda t: Plane1.c2p(np.cos(t)+2.75,np.sin(t)+2.25),t_range=(1.75*PI,2.25*PI),color=DARK_BLUE)
#         self.play(Create(theta_prime))
#         theta_prime_label=MathTex(r"180^{\circ}-\theta",color=BLUE).next_to(theta_prime,RIGHT,buff=-0.2).scale(0.7)
#         self.play(Write(theta_prime_label))
#         mobs_to_disappear.append(theta_prime)
#         mobs_to_disappear.append(theta_prime_label)
#         bg_rect=RoundedRectangle(color=PURPLE,fill_opacity=0,corner_radius=0.2,height=t6.height+0.2,width=t6.width+0.2).move_to(t6.get_center())
#         self.play(Create(bg_rect))
#         formula=VGroup(bg_rect,t6)
#         self.play(Wait(0.8))
#         self.play(*[FadeOut(mob) for mob in mobs_to_disappear])
#         for mob in self.mobjects:
#             mob.clear_updaters()
#         self.play(Wait(0.8))
#         self.play(formula.animate.to_corner(UL).shift(DOWN))

# class Part2(Scene):
#      def construct(self):
#         Topic1=MathTex(r"\mathbf{Angle\;between\;two\;straight\;lines}").to_edge(UP)
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         t6=MathTex(r"\therefore \theta=\tan^{-1}\bigg(\pm \frac{m_1-m_2}{1+m_1 m_2}\bigg)").scale(0.7)
#         bg_rect=RoundedRectangle(color=PURPLE,fill_opacity=0,corner_radius=0.2,height=t6.height+0.2,width=t6.width+0.2).move_to(t6.get_center())
#         formula1=VGroup(bg_rect,t6).to_corner(UL).shift(DOWN)
#         self.add(formula1,Topic1,NameLabel)
#         Subtopic2=Tex("1. Condition for Parallelism",color=WHITE).scale(0.7)
#         Subtopic3=Tex("2. Condition for Perpendicularity",color=WHITE).scale(0.7).next_to(Subtopic2,DOWN).align_to(Subtopic2,LEFT)
#         self.play(Write(Subtopic2))
#         self.play(Wait(0.8))
#         self.play(Write(Subtopic3))
#         subtopics=VGroup(Subtopic2,Subtopic3)
#         self.play(Wait(0.8))
#         self.play(subtopics.animate.next_to(formula1,DOWN).to_edge(LEFT))   
#         self.play(Wait(1))
#         self.play(Indicate(Subtopic2))
#         t6_copy=MathTex(r"\theta=\tan^{-1}\bigg(\pm \frac{m_1-m_2}{1+m_1 m_2}\bigg)").scale(0.7).shift(UP+RIGHT)
#         self.play(TransformMatchingShapes(t6.copy(),t6_copy))
#         text_1=MathTex(r"\Rightarrow \tan 0^\circ = \frac{m_1-m_2}{1+m_1 m_2}\;\; [\,\because l_1||l_2 \Rightarrow \theta=0^\circ\,]").scale(0.7).next_to(t6_copy,DOWN).align_to(t6_copy,LEFT)
#         text_2=MathTex(r"\Rightarrow 0 = \frac{m_1-m_2}{1+m_1 m_2}").scale(0.7).next_to(text_1,DOWN).align_to(text_1,LEFT)
#         text_3=MathTex(r"\Rightarrow 0 \cdot (1+m_1 m_2)= m_1-m_2").scale(0.7).next_to(text_2,DOWN).align_to(text_1,LEFT)
#         text_4=MathTex(r"\Rightarrow 0= m_1-m_2").scale(0.7).next_to(text_3,DOWN).align_to(text_1,LEFT)
#         text_5=MathTex(r"\therefore m_1=m_2").scale(0.7).next_to(text_4,DOWN).align_to(text_1,LEFT)
#         text_6=MathTex(r"l_1||l_2 \Rightarrow m_1=m_2").scale(0.7).move_to(text_5.get_center()).align_to(text_1,LEFT)
#         texts=Group(text_1,text_2,text_3,text_4,text_5)
#         for text in texts:
#             self.play(Write(text))
#             self.play(Wait(0.8))
#         self.play(Wait(1))
#         self.play(TransformMatchingShapes(text_5,text_6))
#         text_6_bg=RoundedRectangle(color=BLUE,fill_opacity=0,corner_radius=0.2,height=text_6.height+0.3,width=text_6.width+0.3).move_to(text_6.get_center())
#         formula2=VGroup(text_6,text_6_bg)
#         self.play(Create(text_6_bg))
#         self.play(Wait(1.5))
#         keep_mobs = Group(NameLabel, Topic1, formula1, text_6, text_6_bg, subtopics)
#         mobs_to_disappear = Group(*[mob for mob in self.mobjects if mob not in keep_mobs])
#         self.play(FadeOut(mobs_to_disappear))
#         self.play(Wait(0.8))
#         self.play(formula2.animate.next_to(formula1,RIGHT))
#         self.play(Wait(0.8))
#         self.play(Indicate(Subtopic3))
#         self.play(TransformMatchingShapes(t6.copy(),t6_copy))
#         Text_1=MathTex(r"\Rightarrow \tan 90^\circ = \frac{m_1-m_2}{1+m_1 m_2}\;\; [\,\because l_1 \perp l_2 \Rightarrow \theta=90^\circ\,]").scale(0.7).next_to(t6_copy,DOWN).align_to(t6_copy,LEFT)
#         Text_2=MathTex(r"\Rightarrow \frac{1}{\tan 90^\circ} = \frac{1+m_1 m_2}{m_1-m_2}").scale(0.7).next_to(text_1,DOWN).align_to(text_1,LEFT)
#         Text_3=MathTex(r"\Rightarrow \cot 90^\circ \cdot (m_1-m_2)= 1+m_1 m_2").scale(0.7).next_to(text_2,DOWN).align_to(text_1,LEFT)
#         Text_4=MathTex(r"\Rightarrow 0=1+m_1 m_2").scale(0.7).next_to(text_3,DOWN).align_to(text_1,LEFT)
#         Text_5=MathTex(r"\therefore m_1=-\frac{1}{m_2}").scale(0.7).next_to(text_4,DOWN).align_to(text_1,LEFT)
#         Text_6=MathTex(r"l_1 \perp l_2 \Rightarrow m_1=-\frac{1}{m_2}").scale(0.7).next_to(Text_5,DOWN,buff=-0.5).align_to(text_1,LEFT)
#         Text_6_bg=RoundedRectangle(color=GREEN,fill_opacity=0,corner_radius=0.2,height=Text_6.height+0.3,width=Text_6.width+0.3).move_to(Text_6.get_center())
#         formula3=VGroup(Text_6,Text_6_bg)
#         Texts=Group(Text_1,Text_2,Text_3,Text_4,Text_5)
#         for Text in Texts:
#             self.play(Write(Text))
#             self.play(Wait(0.8))
#         self.play(Wait(1))
#         self.play(TransformMatchingShapes(Text_5,Text_6))
#         self.play(Create(Text_6_bg))
#         self.play(Wait(1.5))
#         Keep_mobs = Group(NameLabel, Topic1, formula1, formula2,Text_6_bg, Text_6, subtopics)
#         Mobs_to_disappear = Group(*[mob for mob in self.mobjects if mob not in Keep_mobs])
#         self.play(FadeOut(Mobs_to_disappear))
#         self.play(Wait(0.8))
#         self.play(formula3.animate.next_to(formula2,RIGHT))
#         self.wait(1)
#         self.play(FadeOut(subtopics))
#         final_group=Group(formula1,formula2,formula3)
#         self.play(final_group.animate.move_to(ORIGIN))
#         self.play(Wait(1))
#         self.play(AnimationGroup(*[Indicate(Mob) for Mob in final_group],lag_ratio=1.1),run_time=3.5)
#         self.play(FadeOut(final_group))

# class Part3(Scene):
#     def construct(self):
#         Topic1=MathTex(r"\mathbf{Angle\;between\;two\;straight\;lines}").to_edge(UP)
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         self.add(Topic1,NameLabel)
#         self.play(FadeOut(Topic1))
#         Topic2_1=MathTex(r"\mathbf{Angle\;between\;two\;lines\;in\;the\;form\;of}")
#         Topic2_2=MathTex(r"\mathbf{a_1x+b_1y+c_1=0\;and\;a_2x+b_2x+c2=0}").next_to(Topic2_1,DOWN)
#         Topic2=VGroup(Topic2_1,Topic2_2)
#         self.play(Write(Topic2),run_time=2)
#         self.play(Wait(0.8))
#         self.play(Topic2.animate.to_edge(UP),run_time=1.5)
#         f = [MathTex(r"ax + by + c = 0").scale(0.7).next_to(Topic2,DOWN).set_color(BLUE),
#             MathTex(r"\Rightarrow y = \frac{c}{b} - \frac{a}{b}x"),
#             MathTex(r"\text{Comparing to } y = mx + k:"),
#             MathTex(r"m = -\frac{a}{b}")]
#         g=[MathTex(r"l_1:\,a_1x + b_1y + c_1 = 0").scale(0.7).next_to(Topic2,DOWN).set_color(YELLOW),
#             MathTex(r"l_2:\,a_2x + b_2y + c_2 = 0"),
#             MathTex(r"\Rightarrow m_1 = -\frac{a_1}{b_1}"),
#             MathTex(r"\Rightarrow m_2 = -\frac{a_2}{b_2}")]
#         i=[MathTex(r"l_1 \parallel l_2 \Rightarrow m_1 = m_2").scale(0.7).next_to(g[-1],DOWN),
#             MathTex(r"\Rightarrow -\frac{a_1}{b_1} = -\frac{a_2}{b_2}"),
#             MathTex(r"\therefore \frac{a_1}{a_2} = \frac{b_1}{b_2}")]
#         h=[MathTex(r"l_1 \perp l_2 \Rightarrow m_1 m_2 = -1").scale(0.7).next_to(g[-1],DOWN),
#             MathTex(r"\Rightarrow \left(-\frac{a_1}{b_1}\right)\cdot\left(-\frac{a_2}{b_2}\right) = -1"),
#             MathTex(r"\Rightarrow \frac{a_1}{b_1} = -\frac{b_2}{a_2}"),
#             MathTex(r"\therefore a_1 a_2 + b_1 b_2 = 0")]
        
#         for x in range(1,len(f)):
#             f[x].scale(0.7).next_to(f[x-1],DOWN).align_to(f[0],LEFT).set_color(BLUE)
#         for x in range(1,len(g)):
#             g[x].scale(0.7).next_to(g[x-1],DOWN).align_to(g[0],LEFT).set_color(YELLOW)
#         for x in range(1,len(i)):
#             i[x].scale(0.7).next_to(i[x-1],DOWN).align_to(i[0],LEFT)
#         for x in range(1,len(h)):
#             h[x].scale(0.7).next_to(h[x-1],DOWN).align_to(h[0],LEFT)
#         for x in range(0,len(f)):
#             self.play(Write(f[x]))
#             self.play(Wait(0.8))
#         self.play(Wait(1.5))
#         self.play(*[Unwrite(f[x]) for x in range(0,len(f))])
#         self.wait(1)
#         for x in range(0,len(g)):
#             self.play(Write(g[x]))
#             self.play(Wait(0.8))
#         self.play(Wait(1.5))
#         for x in range(0,len(i)):
#             self.play(Write(i[x]))
#             self.play(Wait(0.8))
#         self.play(Wait(1.5))
#         i_bg=always_redraw(lambda:RoundedRectangle(color=GREEN,fill_opacity=0,corner_radius=0.2,height=i[-1].height+0.2,width=i[-1].width+0.2).move_to(i[-1].get_center()))
#         self.play(Create(i_bg))
#         self.play(Wait(0.8))
#         self.play(i[-1].animate.next_to(Topic2,DOWN).to_edge(LEFT))
#         self.play(Wait(0.8))
#         self.play(*[FadeOut(i[x]) for x in range(0,len(i)-1)])
#         for x in range(0,len(h)):
#             self.play(Write(h[x]))
#             self.play(Wait(0.8))
#         self.play(Wait(1.5))
#         self.play(*[FadeOut(h[x]) for x in range(0,len(h)-1)])
#         h_bg=always_redraw(lambda: RoundedRectangle(color=GREEN,fill_opacity=0,corner_radius=0.2,height=h[-1].height+0.2,width=h[-1].width+0.2).move_to(h[-1].get_center()))
#         self.play(Create(h_bg))
#         self.play(h[-1].animate.next_to(i[-1],RIGHT))
#         remove_from_scene_list=[]
#         for mob in self.mobjects:
#             if mob!=NameLabel:
#                 remove_from_scene_list.append(mob)
#         self.play(Wait(1.5))
#         self.play(*[FadeOut(mob) for mob in remove_from_scene_list]) 

# class Practice1(Scene):
#     def construct(self):
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         Topic=Tex("Example Questions")
#         k=ValueTracker(4)
#         Plane1 = NumberPlane(x_range=[-5+k.get_value(),5+k.get_value()],y_range=[-5+k.get_value(),5+k.get_value()]).scale(0.6).to_edge(LEFT)
#         Plane1.axes.set_opacity(0)
#         background_rectangle=Rectangle(width=Plane1.height,height=Plane1.height,color=YELLOW,fill_opacity=0).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         def f(x):
#             y=x-2
#             return max(min(y,9),-1)
#         def g(x):
#             y=10-3*x
#             return max(min(y,9),-1)
#         l1=Plane1.plot(lambda x: f(x), color=GRAY_BROWN)
#         l2=Plane1.plot(lambda x: g(x), color=BLUE_B)
#         l1.set_stroke(width=l1.stroke_width * 0.8)
#         l2.set_stroke(width=l2.stroke_width * 0.8)
#         l1_l=MathTex(r"l_1", color=GRAY_BROWN).scale(0.7).move_to(Plane1.c2p(8,7))
#         l2_l=MathTex(r"l_2", color=BLUE_B).scale(0.7).move_to(Plane1.c2p(1,8))
#         l1_lab=MathTex(r"l_1:\;2x-y+6=0", color=GRAY_BROWN).scale(0.7)
#         l2_lab=MathTex(r"l_2:\;3x+y+4=0", color=BLUE_B).scale(0.7)
#         self.add(NameLabel)
#         self.play(Write(Topic))
#         self.play(Wait(0.5))
#         self.play(FadeOut(Topic))
#         self.play(FadeIn(Plane1),FadeIn(background_rectangle))
#         self.play(Write(x_label),Write(y_label))
#         self.play(FadeIn(l1),FadeIn(l2))
#         self.play(Wait(1))
#         # write small labels near the lines (ls)
#         self.play(Write(l1_l), Write(l2_l))
#         self.play(Wait(1))
#         # Question at top-right next to the plane
#         Question=MathTex(r"\text{1. Find the acute angle between these two lines.}").scale(0.7).next_to(Plane1, RIGHT).to_edge(UP)
#         self.play(Write(Question))
#         # place the full equation labels (labs) below the question
#         l1_lab.next_to(Question, DOWN).align_to(Question, LEFT)
#         l2_lab.next_to(l1_lab, DOWN).align_to(Question, LEFT)
#         self.play(Write(l1_lab), Write(l2_lab))
#         self.play(Wait(1))
#         SolutionTex=MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(l2_lab,DOWN).align_to(l1_lab,LEFT)
#         angle_arc = ParametricFunction(lambda t: Plane1.c2p(np.cos(t)+3,np.sin(t)+1),t_range=[PI/4,1.892],color=YELLOW)
#         angle_arc.set_stroke(width=angle_arc.stroke_width * 0.8)
#         theta_label = MathTex(r"\theta",color=YELLOW).scale(0.7).next_to(angle_arc, UP, buff=0.1)
#         self.play(Create(angle_arc))
#         self.play(Wait(1))
#         self.play(Write(theta_label))
#         self.play(Wait(1))
#         t1=MathTex(r"\text{slope of }l_1\;(m_1)=-\frac{a}{b}=-\frac{2}{-1}=2").scale(0.7).next_to(SolutionTex,DOWN).align_to(l1_lab,LEFT)
#         t2=MathTex(r"\text{slope of }l_2\;(m_2)=-\frac{a}{b}=-\frac{3}{1}=-3").scale(0.7).next_to(t1,DOWN).align_to(l1_lab,LEFT)
#         t3=MathTex(r"\tan\theta = \left| \frac{m_1 - m_2}{1+m_1 m_2} \right| = \left| \frac{2 - (-3)}{1 + (2)(-3)} \right|").scale(0.7).next_to(t2,DOWN).align_to(l1_lab,LEFT)
#         t4=MathTex(r"= \left| \frac{5}{1 - 6} \right| = \left| \frac{5}{-5} \right| = 1").scale(0.7).next_to(t3,DOWN).align_to(l1_lab,LEFT)
#         t5=MathTex(r"\therefore \theta = \tan^{-1}(1) = 45^\circ").scale(0.7).next_to(t4,DOWN).align_to(l1_lab,LEFT)
#         self.play(Write(SolutionTex))
#         self.play(Write(t1))
#         self.play(Wait(1))
#         self.play(Write(t2))
#         self.play(Wait(1))
#         self.play(Write(t3))
#         self.play(Wait(1))
#         self.play(Write(t4))
#         self.play(Wait(1))
#         self.play(Write(t5))
#         self.play(Wait(2))
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if mob not in [NameLabel, Plane1, Plane1.axes, background_rectangle, l1, l2, l1_l, l2_l,theta_label,angle_arc,x_label,y_label]]
#         )

# class Practice2(Scene):
#     def construct(self): 
#         # self.camera.background_color = BLUE
#         k = ValueTracker(4)
#         Plane1 = NumberPlane(
#             x_range=[-5 + k.get_value(), 5 + k.get_value()],
#             y_range=[-5 + k.get_value(), 5 + k.get_value()]
#         ).scale(0.6).to_edge(LEFT)
#         Plane1.axes.set_opacity(0)
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         a=ValueTracker(-3)
#         b=ValueTracker(10)
#         def f_old(x):
#             y = x - 2
#             return max(min(y, 9), -1)
#         def g_old(x):
#             y = b.get_value() + a.get_value() * x
#             return max(min(y, 9), -1)
#         l1_old = always_redraw(lambda: Plane1.plot(lambda x: f_old(x), color=GRAY_BROWN))
#         l2_old = always_redraw(lambda: Plane1.plot(lambda x: g_old(x), color=BLUE_B))

#         l1_l = MathTex(r"l_1", color=GRAY_BROWN).scale(0.7).move_to(Plane1.c2p(8, 7))
#         l2_l = MathTex(r"l_2", color=BLUE_B).scale(0.7).move_to(Plane1.c2p(1, 8))

#         angle_arc_old = ParametricFunction(
#             lambda t: Plane1.c2p(np.cos(t) + 3, np.sin(t) + 1),
#             t_range=[PI/4, 1.892],
#             color=YELLOW,
#         )
#         angle_arc_old.set_stroke(width=angle_arc_old.stroke_width * 0.8)
#         theta_label_old = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(angle_arc_old, UP, buff=0.1)

#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         self.add(NameLabel, Plane1, background_rectangle)
#         self.add(Plane1.axes,x_label,y_label)
#         self.add(l1_old, l2_old, l1_l, l2_l, angle_arc_old, theta_label_old)
#         angle_arc=ParametricFunction(
#             lambda t: Plane1.c2p(np.cos(t) + 3, np.sin(t) + 1),
#             t_range=[1.892, 1.892+116.6*DEGREES],
#             color=GREEN,
#         ).set_stroke(width=angle_arc_old.stroke_width * 0.8)
#         theta180=MathTex(r"180^{\circ}-\theta", color=GREEN).scale(0.7).next_to(angle_arc, LEFT, buff=0.1)
#         self.play(Create(angle_arc),Write(theta180))
#         Question = Tex(r"2. Find the obtuse angle between $y-(2+\sqrt{3})x=5$ and $y-(2-\sqrt{3})x=10$.").scale(0.7)
#         Question.to_edge(UP).align_to(Plane1,LEFT)
#         self.play(Write(Question))
#         self.play(Wait(1))
#         l1_lab = MathTex(r"l_1:\;y-(2+\sqrt{3})x=5", color=GRAY_BROWN).scale(0.7)
#         l2_lab = MathTex(r"l_2:\;y-(2-\sqrt{3})x=10", color=BLUE_B).scale(0.7)
#         l1_lab.next_to(Plane1,RIGHT).shift(UP*2.5)
#         l2_lab.next_to(l1_lab, DOWN).align_to(l1_lab, LEFT)
#         self.play(Write(l1_lab), Write(l2_lab))
#         self.play(Wait(1))
#         SolutionTex=MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(l2_lab,DOWN).align_to(l1_lab,LEFT)
#         t1 = MathTex(r"m_1 = 2+\sqrt{3}").scale(0.7).next_to(SolutionTex, DOWN).align_to(l1_lab, LEFT)
#         t2 = MathTex(r"m_2 = 2-\sqrt{3}").scale(0.7).next_to(t1, DOWN).align_to(l1_lab, LEFT)
#         t3 = MathTex(r"\tan\theta = \left| \frac{m_1 - m_2}{1 + m_1 m_2} \right| = \left| \frac{(2+\sqrt{3}) - (2-\sqrt{3})}{1 + (2+\sqrt{3})(2-\sqrt{3})} \right|").scale(0.7).next_to(t2, DOWN).align_to(l1_lab, LEFT)
#         t4 = MathTex(r"= \left| \frac{2\sqrt{3}}{1 + (4 - 3)} \right| = \left| \frac{2\sqrt{3}}{2} \right| = \sqrt{3}").scale(0.7).next_to(t3, DOWN).align_to(l1_lab, LEFT)
#         t5 = MathTex(r"\theta = \tan^{-1}(\sqrt{3}) = 60^\circ").scale(0.7).next_to(t4, DOWN).align_to(l1_lab, LEFT)
#         t6 = MathTex(r"\text{Obtuse angle } = 180^\circ - 60^\circ = 120^\circ").scale(0.7).next_to(t5, DOWN).align_to(l1_lab, LEFT)
#         self.play(Write(SolutionTex))
#         self.play(Wait(1))
#         self.play(Write(t1))
#         self.play(Wait(0.8))
#         self.play(Write(t2))
#         self.play(Wait(0.8))
#         self.play(Write(t3),run_time=2.5)
#         self.play(Wait(0.8))
#         self.play(Write(t4),run_time=2.5)
#         self.play(Wait(0.8))
#         self.play(Write(t5),run_time=2.5)
#         self.play(Wait(0.8))
#         self.play(Write(t6))
#         self.play(Wait(2))
#         Plane2=Plane1.copy()
#         self.play(Transform(Plane1,Plane2))
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [y_label,x_label,background_rectangle,Plane1,l1_l,l2_l,l1_old,l2_old,NameLabel]])
#         self.play(a.animate.set_value(1),b.animate.set_value(2),run_time=4)
#         self.play(l2_l.animate.shift(2.4*RIGHT))

# class Practice3(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         # self.camera.background_color = GRAY
#         Question = MathTex(r"\text{3. Find the value of $k$ such that the lines $2x-5y+9=0$ and $6x+ky=0$ are parallel.}").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         k = ValueTracker(4)
#         Plane1 = NumberPlane(
#             x_range=[-5 + k.get_value(), 5 + k.get_value()],
#             y_range=[-5 + k.get_value(), 5 + k.get_value()]
#         ).scale(0.6).to_edge(LEFT)
#         Plane1.axes.set_opacity(0)
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         a=ValueTracker(1)
#         b=ValueTracker(2)
#         def f_old(x):
#             y = x - 2
#             return max(min(y, 9), -1)
#         def g_old(x):
#             y = b.get_value() + a.get_value() * x
#             return max(min(y, 9), -1)
#         l1= always_redraw(lambda: Plane1.plot(lambda x: f_old(x), color=GRAY_BROWN))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g_old(x), color=BLUE_B))
#         l1_l = MathTex(r"l_1", color=GRAY_BROWN).scale(0.7).move_to(Plane1.c2p(8, 7))
#         l2_l = MathTex(r"l_2", color=BLUE_B).scale(0.7).move_to(Plane1.c2p(1, 8)).shift(RIGHT*2.4)
#         self.add(y_label,x_label,background_rectangle,Plane1,l1,l2,l1_l,l2_l)
#         self.play(Write(Question),run_time=2)
#         self.play(Wait(0.8))
#         l1_lab = MathTex(r"l_1:\;2x-5y+9=0", color=GRAY_BROWN).scale(0.7)
#         l2_lab = MathTex(r"l_2:\;6x+ky=0", color=BLUE_B).scale(0.7)
#         l1_lab.next_to(Plane1, RIGHT).to_edge(UP,buff=1)
#         l2_lab.next_to(l1_lab, DOWN).align_to(l1_lab, LEFT)
#         self.play(Write(l1_lab), Write(l2_lab))
#         self.play(Wait(0.8))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(l2_lab, DOWN).align_to(l2_lab, LEFT)
#         self.play(Write(SolutionTex))
#         self.play(Wait(0.8))
#         t1 = MathTex(r"\text{slope of }l_1\;(m_1) = -\frac{a_1}{b_1} = -\frac{2}{-5} = \frac{2}{5}").scale(0.7).next_to(SolutionTex, DOWN).align_to(l2_lab, LEFT)
#         t2 = MathTex(r"\text{slope of }l_2\;(m_2) = -\frac{a_2}{b_2} = -\frac{6}{k}").scale(0.7).next_to(t1, DOWN).align_to(l2_lab, LEFT)
#         t3 = MathTex(r"m_1 = m_2\,[\;\because l_1||l_2\;]").scale(0.7).next_to(t2, DOWN).align_to(l2_lab, LEFT)
#         t4 = MathTex(r"\Rightarrow \frac{2}{5} = -\frac{6}{k}").scale(0.7).next_to(t3, DOWN).align_to(l2_lab, LEFT)
#         t5 = MathTex(r"\Rightarrow 2k = -30").scale(0.7).next_to(t4, DOWN).align_to(l2_lab, LEFT)
#         t6 = MathTex(r"\therefore k = -15").scale(0.7).next_to(t5, DOWN).align_to(l2_lab, LEFT)
#         self.play(Write(t1))
#         self.wait(0.5)
#         self.play(Write(t2))
#         self.wait(0.5)
#         self.play(Write(t3))
#         self.wait(0.5)
#         self.play(Write(t4))
#         self.wait(0.5)
#         self.play(Write(t5))
#         self.wait(0.5)
#         self.play(Write(t6))
#         self.wait(1)
#         keep_mobs = [NameLabel]
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if mob not in keep_mobs]
#         )

# class Practice4(Scene): 
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = Tex(r"\text{4. Find the equation of the line passing through }(5,0)\text{ and parallel to the join of }(5,1)").scale(0.7).to_edge(UP)
#         Questionb = Tex(r"\text{and }(-2,8)\text{.}").scale(0.7).next_to(Question,DOWN).shift(RIGHT*0.35)
#         self.add(NameLabel)
#         k = ValueTracker(4)
#         Plane1 = NumberPlane(
#             x_range=[-5 + k.get_value(), 5 + k.get_value()],
#             y_range=[-5 + k.get_value(), 5 + k.get_value()]
#         ).scale(0.6).to_edge(LEFT)
#         Plane1.axes.set_opacity(0)
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         a=ValueTracker(-1)
#         b=ValueTracker(7)
#         def f(x):
#             y = a.get_value()*x + b.get_value()-2
#             return max(min(y, 9), -1)
#         def g(x):
#             y = b.get_value() + a.get_value() * x
#             return max(min(y, 9), -1)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: f(x), color=GRAY_BROWN))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g(x), color=BLUE_B))
#         l1_l = MathTex(r"l_2", color=GRAY_BROWN).scale(0.7).move_to(Plane1.c2p(0,4))
#         l2_l = MathTex(r"l_1", color=BLUE_B).scale(0.7).move_to(Plane1.c2p(0,8))
#         ADot=Dot(color=RED).move_to(Plane1.c2p(0,7))
#         BDot=Dot(color=RED).move_to(Plane1.c2p(7,0))
#         CDot=Dot(color=RED).move_to(Plane1.c2p(0,5))
#         ACoord=MathTex(r"A(5,1)").next_to(ADot,RIGHT).scale(0.7)
#         BCoord=MathTex(r"B(-2,8)").next_to(BDot,UP).scale(0.7)
#         CCoord=MathTex(r"C(5,0)").next_to(CDot,UP).scale(0.7)
#         BCoord.rotate(-45*DEGREES,about_point=(BCoord.get_center()))
#         CCoord.rotate(-45*DEGREES,about_point=(CCoord.get_center()))
#         self.play(FadeIn(Group(y_label,x_label,background_rectangle,Plane1,l1,l2,l1_l,l2_l)))
#         self.play(Create(ADot))
#         self.play(Write(ACoord))
#         self.play(Create(BDot))
#         self.play(Write(BCoord))
#         self.play(Create(CDot))
#         self.play(Write(CCoord))
#         self.play(Write(Question),run_time=3.3)
#         self.play(Write(Questionb))
#         self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(Questionb, DOWN).align_to(Questionb, LEFT)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"\text{slope of }l_1\;(m_1) = \frac{\Delta x}{\Delta y}=\frac{8-1}{-2-5}=-1").scale(0.7).next_to(SolutionTex, DOWN).align_to(Questionb, LEFT)
#         t2 = MathTex(r"\text{slope of }l_2\; = m_2 ").scale(0.7).next_to(t1, DOWN).align_to(Questionb, LEFT)
#         t3 = MathTex(r"m_1 = m_2\,[\;\because l_1||l_2\;]").scale(0.7).next_to(t2, DOWN).align_to(Questionb, LEFT)
#         t4 = MathTex(r"\Rightarrow y-y_1=m(x-x_1)").scale(0.7).next_to(t3, DOWN).align_to(Questionb, LEFT)
#         t5 = MathTex(r"\Rightarrow y-0=-1(x-5)").scale(0.7).next_to(t4, DOWN).align_to(Questionb, LEFT)
#         t6 = MathTex(r"\therefore x+y=5").scale(0.7).next_to(t5, DOWN).align_to(Questionb, LEFT)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t2))
#         self.wait(1)
#         self.play(Write(t3),run_time=1.5)
#         self.wait(1)
#         self.play(Write(t4),run_time=1.5)
#         self.wait(1)
#         self.play(Write(t5),run_time=1.5)
#         self.wait(1)
#         self.play(Write(t6),run_time=1.5)
#         self.wait(2)
#         keep_mobs = [NameLabel]
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if mob not in keep_mobs]
#         )

# class Practice5(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         self.add(NameLabel)
#         Question = MathTex(r"\text{5. Find the equation of the line }\perp\text{ to }3x-8y=6\text{ and making y-intercept \text{equal to }4.").scale(0.7).to_edge(UP)
#         k = ValueTracker(4)
#         Plane1 = NumberPlane(
#             x_range=[-5 + k.get_value(), 5 + k.get_value()],
#             y_range=[-5 + k.get_value(), 5 + k.get_value()]
#         ).scale(0.6).to_edge(LEFT)
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         a=ValueTracker(-1)
#         b=ValueTracker(4)
#         def f(x):
#             y = x+1
#             return max(min(y, 9), -1)
#         def g(x):
#             y = b.get_value() + a.get_value() * x
#             return max(min(y, 9), -1)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: f(x), color=GRAY_BROWN))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g(x), color=BLUE_B))
#         p1=Line(start=Plane1.c2p(1,3),end=Plane1.c2p(1.5,3.5),color=YELLOW).set_z_index(-1)
#         p2=Line(start=Plane1.c2p(1.48,3.52),end=Plane1.c2p(2,3),color=YELLOW).set_z_index(-1)
#         ADot=Dot(color=RED).move_to(Plane1.c2p(0,4))
#         ACoord=MathTex(r"C(0,4)").next_to(ADot,RIGHT,buff=-0.1).scale(0.7)
#         self.play(FadeIn(Group(y_label,x_label,background_rectangle,Plane1,l1,l2)))
#         self.play(Create(ADot))
#         self.play(Write(ACoord))
#         self.wait(0.5)
#         self.play(Write(Question),run_time=2)
#         self.wait(0.5)
#         self.play(Create(p1))
#         self.play(Create(p2))
#         self.wait(0.5)
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(Question,DOWN).shift(RIGHT*0.05)
#         self.play(Write(SolutionTex))
#         self.wait(0.5)
#         m1=Tex(r"Method I:",color=YELLOW).scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         l1_tex=MathTex(r"3x-8y=6\cdots\cdots(i)",color=GRAY_BROWN).scale(0.7).next_to(m1, DOWN).align_to(SolutionTex, LEFT)
#         ll=MathTex(r"3x-8y",color=GRAY_BROWN).scale(0.7).move_to(l1_tex.get_center()).align_to(l1_tex,LEFT)
#         t1 = Tex("Line perpendicular to (i) passing through $(0,4)$:").scale(0.7).next_to(l1_tex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"8x+3y=8\times0+3\times4").scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         tt = MathTex(r"8x+3y").scale(0.7).move_to(t2.get_center()).align_to(t2,LEFT)
#         t3 = MathTex(r"\therefore 8x+3y=12").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         m2=Tex(r"Method II:",color=YELLOW).scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         T1=MathTex(r"m_1=\frac{-a}{b}=\frac{3}{8}").scale(0.7).next_to(m2, DOWN).align_to(SolutionTex, LEFT)
#         T2=MathTex(r"m_2=\frac{1}{-m_1}=-\frac{8}{3}").scale(0.7).next_to(T1, DOWN).align_to(SolutionTex, LEFT)
#         T3=MathTex(r"y-y_1=m(x-x_1)").scale(0.7).next_to(T2, DOWN).align_to(SolutionTex, LEFT)
#         T4=MathTex(r"\Rightarrow y-4=-\frac{8}{3}(x-0)").scale(0.7).next_to(T1, RIGHT).shift(RIGHT)
#         T5=MathTex(r"\therefore 8x+3y=12").scale(0.7).next_to(T4, DOWN).align_to(T4, LEFT)
#         self.play(Write(m1))
#         self.play(Write(l1_tex))
#         self.wait(0.5)
#         self.play(Write(t1),run_time=1.5)
#         self.wait(0.5)
#         self.play(TransformMatchingShapes(ll,tt))
#         self.play(Wait(0.2))
#         self.play(Write(t2),run_time=1.5)
#         self.wait(0.5)
#         self.play(Write(t3),run_time=1.5)
#         self.wait(0.5)
#         self.play(Write(m2),run_time=1.5)
#         self.wait(0.5)
#         self.play(Write(T1),run_time=1.5)
#         self.wait(0.5)
#         self.play(Write(T2),run_time=1.5)
#         self.wait(0.5)
#         self.play(Write(T3),run_time=1.5)
#         self.wait(0.5)
#         self.play(Write(T4),run_time=1.5)
#         self.wait(0.5)
#         self.play(Write(T5),run_time=1.5)
#         self.wait(2)
#         keep_mobs = [NameLabel]
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if mob not in keep_mobs])

# class Practice6(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         self.add(NameLabel)
#         Question = MathTex(r"\text{6. Find the equation of the line } || \text{ to }3x-8y=6\text{ and making y-intercept \text{equal to }4.").scale(0.7).to_edge(UP)
#         k = ValueTracker(4)
#         Plane1 = NumberPlane(
#             x_range=[-5 + k.get_value(), 5 + k.get_value()],
#             y_range=[-5 + k.get_value(), 5 + k.get_value()]
#         ).scale(0.6).to_edge(LEFT)
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         a=ValueTracker(1)
#         b=ValueTracker(4) 
#         def f(x):
#             y = x+1
#             return max(min(y, 9), -1)
#         def g(x):
#             y = b.get_value() + a.get_value() * x
#             return max(min(y, 9), -1)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: f(x), color=GRAY_BROWN))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g(x), color=BLUE_B))
#         ADot=Dot(color=RED).move_to(Plane1.c2p(0,4))
#         ACoord=MathTex(r"C(0,4)").next_to(ADot,RIGHT,buff=-0.1).scale(0.7)
#         self.play(FadeIn(Group(y_label,x_label,background_rectangle,Plane1,l1,l2)))
#         self.play(Create(ADot))
#         self.play(Write(ACoord))
#         self.wait(0.8)
#         self.play(Write(Question))
#         self.wait(0.8)
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(Question,DOWN).shift(RIGHT*0.05)
#         self.play(Write(SolutionTex))
#         self.wait(0.8)
#         m1=Tex(r"Method I:",color=YELLOW).scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         l1_tex=MathTex(r"3x-8y=6\cdots\cdots(i)",color=GRAY_BROWN).scale(0.7).next_to(m1, DOWN).align_to(SolutionTex, LEFT)
#         ll=MathTex(r"3x-8y",color=GRAY_BROWN).scale(0.7).move_to(l1_tex.get_center()).align_to(l1_tex,LEFT)
#         t1 = Tex("Line $||$ to (i) passing through $(0,4)$:").scale(0.7).next_to(l1_tex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"3x-8y=3\times0-8\times4").scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         tt = MathTex(r"3x-8y").scale(0.7).move_to(t2.get_center()).align_to(t2,LEFT)
#         t3 = MathTex(r"\therefore 3x-8y+32=0").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         m2=Tex(r"Method II:",color=YELLOW).scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         T1=MathTex(r"m_1=\frac{-a}{b}=\frac{3}{8}").scale(0.7).next_to(m2, DOWN).align_to(SolutionTex, LEFT)
#         T2=MathTex(r"m_2=m_1=\frac{3}{8}").scale(0.7).next_to(T1, DOWN).align_to(SolutionTex, LEFT)
#         T3=MathTex(r"y-y_1=m(x-x_1)").scale(0.7).next_to(T2, DOWN).align_to(SolutionTex, LEFT)
#         T4=MathTex(r"\Rightarrow y-4=\frac{3}{8}(x-0)").scale(0.7).next_to(T1, RIGHT).shift(RIGHT)
#         T5=MathTex(r"\therefore 3x-8y+32=0").scale(0.7).next_to(T4, DOWN).align_to(T4, LEFT)
#         self.play(Write(m1))
#         self.wait(0.8)
#         self.play(Write(l1_tex))
#         self.wait(0.8)
#         self.play(Write(t1))
#         self.wait(0.8)
#         self.play(TransformMatchingShapes(ll,tt))
#         self.play(Wait(0.2))
#         self.play(Write(t2))
#         self.wait(0.5)
#         self.play(Write(t3))
#         self.wait(0.5)
#         self.play(Write(m2))
#         self.wait(0.5)
#         self.play(Write(T1))
#         self.wait(0.5)
#         self.play(Write(T2))
#         self.wait(0.5)
#         self.play(Write(T3))
#         self.wait(0.5)
#         self.play(Write(T4))
#         self.wait(0.5)
#         self.play(Write(T5))
#         self.wait(2)
#         keep_mobs = [NameLabel]
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if mob not in keep_mobs])
    
# class Practice7(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         self.add(NameLabel)
#         rhombus = Polygon(
#             [-1, 0, 0],   
#             [0, 2, 0],    
#             [1, 0, 0],    
#             [0, -2, 0],   
#             color=BLUE
#         )
#         rhombus.set_fill(BLUE, opacity=0.5).to_edge(LEFT).shift(RIGHT*0.1)
#         P=MathTex(r"P(2,4)").scale(0.7).next_to(rhombus,UP)
#         Q=MathTex(r"Q").scale(0.7).next_to(rhombus,RIGHT)
#         R=MathTex(r"R(8,10)").scale(0.7).next_to(rhombus,DOWN)
#         S=MathTex(r"S").scale(0.7).next_to(rhombus,LEFT)
#         Question = MathTex(r"\text{7. }P(2,4)\text{ and }R(8,10)\text{ are opposite sides of rhombus }PQRS.\text{ Find the eq}^{\text{n}} \text{of diagonal QS.}").scale(0.7).to_edge(UP)
#         self.play(DrawBorderThenFill(rhombus),run_time=2)
#         self.play(AnimationGroup(Write(P),Write(Q),Write(R),Write(S),lag_ratio=0.6),run_time=3)
#         self.play(Write(Question),run_time=3)
#         PR=Line(color=BLUE,start=rhombus.get_top(),end=rhombus.get_bottom()).set_z_index(1)
#         QS=Line(color=BLUE,start=rhombus.get_left(),end=rhombus.get_right()).set_z_index(1)
#         self.play(Create(PR))
#         self.play(Create(QS))
#         perp_angle=Square(side_length=0.3,color=YELLOW,fill_opacity=0.6).move_to(rhombus.get_center()+UR*0.15)
#         self.play(Create(perp_angle))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(Question,DOWN).shift(LEFT*2)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"\text{Mid-point of }PR=\text{Mid-point of }QS").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"=\bigg(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\bigg)=\bigg(\frac{2+8}{2},\frac{4+10}{2}\bigg)=(5,7)").scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         t2copy=MathTex(r"(5,7)").scale(0.7).move_to(t2.get_center()).align_to(t2, RIGHT)
#         t3 = MathTex(r"m_{PR}}=\frac{\Delta y}{\Delta x}=\frac{10-4}{8-2}=1").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         t4 = MathTex(r"m_{QS}=-\frac{1}{m_{PR}}=-1\;\;[\,\because PR \perp QS\,]").scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         t5 = MathTex(r"y-y_1=m(x-x_1)").scale(0.7).next_to(t4, DOWN).align_to(SolutionTex, LEFT)
#         t6 = MathTex(r"y-7=-1(x-5)").scale(0.7).next_to(t4, DOWN).align_to(SolutionTex, LEFT)
#         t7 = MathTex(r"\therefore x+y=12").scale(0.7).next_to(t6, DOWN).align_to(SolutionTex, LEFT)
#         self.play(Write(t1),run_time=2.5)
#         self.wait(1)
#         self.play(Write(t2),run_time=2.5)
#         self.wait(1)
#         self.play(t2copy.animate.next_to(rhombus.get_center(),DR).shift(UL*0.1).shift(LEFT*0.1))
#         self.play(Write(t3),run_time=2.5)
#         self.wait(0.8)
#         self.play(Write(t4),run_time=2.5)
#         self.wait(0.8)
#         self.play(Write(t5),run_time=2.5)
#         self.wait(0.8)
#         self.play(Transform(t5,t6))
#         self.wait(0.8)
#         self.play(Write(t7))
#         self.wait(2)
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob != NameLabel])
        
# class Practice8(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         self.add(NameLabel)
#         Question = MathTex(r"\text{8. Find the equation of the line making an angle of }45^{\circ}\text{ with }2x+3y+5=0").scale(0.7).to_edge(UP)
#         Questionb = Tex(r"\text{ and passing through }(1,-4).").scale(0.7).next_to(Question,DOWN).shift(RIGHT*1.6)
#         Plane1 = NumberPlane(
#             x_range=[-1,9],
#             y_range=[-9,1]
#         ).scale(0.6).to_edge(LEFT)
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,0.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-8.5)).scale(0.9)
#         def f(x):
#             y = (x-21)/5
#             return max(min(y, 1), -9)
#         def g(x):
#             y = (-5-2*x)/3
#             return max(min(y, 1), -9)
#         def h(x):
#             y = 1-5*x
#             return max(min(y, 1), -9)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: g(x), color=GRAY_BROWN))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: f(x), color=BLUE_B))
#         l3=always_redraw(lambda: Plane1.plot(lambda x: h(x), color=RED))
#         self.play(FadeIn(Group(y_label,x_label,background_rectangle,Plane1)))
#         self.play(Create(l1))
#         l1_tex=MathTex(r"l_1:\;2x+3y+5=0",color=GRAY_BROWN).scale(0.7).next_to(Questionb, DOWN).align_to(Questionb, LEFT)
#         l1_label=MathTex(r"l_1",color=GRAY_BROWN).scale(0.7).move_to(Plane1.c2p(3,-3))
#         self.play(Write(l1_tex))
#         alpha=ParametricFunction(lambda t: Plane1.c2p(0.6*np.cos(t)+0.62,0.6*np.sin(t)-2.08),t_range=[np.arctan(-5),np.arctan(-2/3)],color=YELLOW)
#         beta=ParametricFunction(lambda t: Plane1.c2p(0.6*np.cos(t+PI)+2.92,0.6*np.sin(t+PI)-3.62),t_range=[np.arctan(-2/3),np.arctan(1/5)],color=YELLOW)
#         alpha_tex=MathTex(r"45^{\circ}",color=YELLOW).scale(0.6).next_to(alpha,DR,buff=-0.15).shift(DOWN*0.1)
#         beta_tex=MathTex(r"45^{\circ}",color=YELLOW).scale(0.6).next_to(beta,LEFT,buff=-0.001)
#         self.play(Wait(0.8))
#         self.play(Write(l1_label))
#         self.play(Create(l2))
#         self.play(AnimationGroup(Create(l3),Write(Question),lag_ratio=0.7),run_time=6)
#         self.play(Write(Questionb))
#         self.play(Wait(0.8))
#         self.play(Create(alpha))
#         self.play(Write(alpha_tex))
#         self.play(Create(beta))
#         self.play(Write(beta_tex))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(l1_tex,DOWN).align_to(Questionb,LEFT)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"m_1=\frac{-2}{3}").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"\tan 45^{\circ}=\pm \frac{m_1-m_2}{1+m_1 m_2}").scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         tt = MathTex(r"\Rightarrow 1=\pm\frac{-2/3-m_2}{1+(-2/3)m_2}").scale(0.7).next_to(t2, DOWN).align_to(t2,LEFT)
#         T1=Tex("Taking positive:",color=YELLOW).scale(0.7).next_to(tt, DOWN).align_to(SolutionTex, LEFT)
#         t3 = MathTex(r"1-\frac{2}{3}m_2=-\frac{2}{3}-m_2").scale(0.7).next_to(T1, DOWN).align_to(SolutionTex, LEFT)
#         t4=MathTex(r"\therefore m_2=-5",color=RED).scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         T2=Tex("Taking negative:",color=YELLOW).scale(0.7).next_to(T1, RIGHT).shift(RIGHT)
#         t5=MathTex(r"1-\frac{2}{3}m_2=\frac{2}{3}+m_2").scale(0.7).next_to(T2, DOWN).align_to(T2, LEFT)
#         t6=MathTex(r"\therefore m_2=1/5",color=BLUE).scale(0.7).next_to(t5, DOWN).align_to(t5, LEFT)
#         self.play(Write(t1))
#         self.wait(0.5)
#         self.play(Write(t2))
#         self.wait(0.5)
#         self.play(Write(tt))
#         self.wait(0.5)
#         self.play(Write(T1))
#         self.wait(0.5)
#         self.play(Write(t3))
#         self.wait(0.5)
#         self.play(Write(t4))
#         self.wait(0.5)
#         self.play(Write(T2))
#         self.wait(0.5)
#         self.play(Write(t5))
#         self.wait(0.5)
#         self.play(Write(t6))
#         self.wait(0.5)
#         fade_mobs = [SolutionTex,t1,t2,tt,T1,T2,t3,t5]
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if mob in fade_mobs])
#         self.play(t4.animate.next_to(l1_tex,DOWN).align_to(l1_tex,LEFT))
#         self.play(t6.animate.next_to(t4,RIGHT,buff=1.8))
#         t7=MathTex(r"y-y_1=m(x-x_1)").scale(0.7).next_to(t4, DOWN).align_to(t4, LEFT)
#         t8=MathTex(r"\Rightarrow y+4=-5(x-1)").scale(0.7).next_to(t4, DOWN).align_to(t4, LEFT)
#         t9=MathTex(r"\Rightarrow y+4=\frac{1}{5}(x-1)").scale(0.7).next_to(t7,RIGHT,buff=1.2)
#         t10=MathTex(r"\therefore 5x+y=1 \text{ or } x-5y=21").scale(0.7).next_to(t8, DOWN).align_to(t8, LEFT)
#         self.play(Write(t7))
#         self.wait(0.5)
#         self.play(Transform(t7,t8),Transform(t7.copy(),t9))
#         self.wait(0.5)
#         self.play(Write(t10))
#         self.play(Wait(2))
#         keep_mobs = [NameLabel]
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if mob not in keep_mobs])
#         Notice=Tex(r"NOTE",color=YELLOW).to_edge(UP)
#         Note1 = Tex(
#             "When you are given the equations or slopes of two lines and have to find the acute angle, use "
#             "$\\tan \\theta = \\big|\\frac{m_1 - m_2}{1 + m_1 m_2}\\big|$. "
#             "If you are asked to find the obtuse angle, just subtract the acute value you get from "
#             "$180^{\\circ}$."
#         ).scale(0.7).shift(UP*2)

#         Note2 = Tex(
#             "When you are given the angle between two lines, the slope of one of the lines, "
#             "and have to find the equation of the unknown line, use "
#             "$\\tan \\theta = \\pm \\frac{m_1 - m_2}{1 + m_1 m_2}$.").scale(0.7).next_to(Note1, DOWN)
#         self.play(Write(Notice),run_time=1)
#         self.play(Write(Note1),run_time=6)
#         self.play(Write(Note2),run_time=6)
#         self.wait(2)
#         self.play(*[FadeOut(mob) for mob in self.mobjects])

# class homogeneousA(Scene):
#     def construct(self):
#         self.play(Wait(1))
#         Topic=MathTex(r"\mathbf{Pair\;of\;straight\;lines}")
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         self.play(Write(Topic))
#         self.play(Wait(0.7))
#         self.play(Topic.animate.to_edge(UP))
#         self.play(Wait(1))
#         k=ValueTracker(4)
#         Plane1 = NumberPlane(x_range=[-5+k.get_value(),5+k.get_value()],y_range=[-5+k.get_value(),5+k.get_value()]).scale(0.6).to_edge(LEFT)
#         background_rectangle=Rectangle(width=Plane1.height,height=Plane1.height,color=YELLOW,fill_opacity=0).move_to(Plane1.get_center())
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         a=ValueTracker(2)
#         b=ValueTracker(-4.5)
#         m=ValueTracker(1/2)
#         c=ValueTracker(1.5)
#         def f(x):
#             y=a.get_value()*x+b.get_value()
#             return max(min(y,9),-1) 
#         def g(x):
#             y=m.get_value()*x+c.get_value()
#             return max(min(y,9),-1)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: f(x),color=LIGHT_BROWN,x_range=[-5+k.get_value(),5+k.get_value()]).set_stroke(width=3))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g(x),color=LIGHT_GRAY,x_range=[-5+k.get_value(),5+k.get_value()]).set_stroke(width=3))
#         background_rectangle.set_z_index(1)
#         self.play(Write(NameLabel),FadeIn(Plane1),FadeIn(background_rectangle))
#         self.play(Write(x_label),Write(y_label))
#         self.play(Wait(0.1))
#         self.play(FadeIn(l1),FadeIn(l2),run_time=2)
#         self.play(Wait(0.1))
#         l1_label=MathTex(r"l_1",color=LIGHT_BROWN).move_to(Plane1.c2p(7,8)).scale(0.9)
#         l2_label=MathTex(r"l_2",color=LIGHT_GRAY).move_to(Plane1.c2p(8,4.7)).scale(0.9)
#         self.play(Write(l1_label),Write(l2_label))
#         self.play(Wait(0.5))
#         Text1=MathTex(r"l_1: a_1x+b_1y+c_1=0",color=LIGHT_BROWN).scale(0.7).next_to(Plane1,RIGHT).shift(UP*2.5)
#         Text2=MathTex(r"l_2: a_2x+b_2y+c_2=0",color=LIGHT_GRAY).scale(0.7).next_to(Text1,DOWN).align_to(Text1,LEFT)
#         self.play(AnimationGroup(Write(Text1),Write(Text2),lag_ratio=1))
#         self.play(Wait(1))
#         Text3=MathTex(r"\text{Multiplying the equations of }l_1\text{ and }l_2\text{,}").scale(0.7).next_to(Text2,DOWN).align_to(Text2,LEFT)
#         Text4=MathTex(r"(a_1x+b_1y+c_1)(a_2x+b_2y+c_2)=0").scale(0.7).next_to(Text3,DOWN).align_to(Text2,LEFT)
#         Text5a = MathTex(r"\Rightarrow a_1a_2x^2 + (a_1b_2 + a_2b_1)xy + b_1b_2y^2").scale(0.7).next_to(Text4, DOWN).align_to(Text2, LEFT)
#         Text5b = MathTex(r"+ (a_1c_2 + a_2c_1)x + (b_1c_2 + b_2c_1)y + c_1c_2 = 0").scale(0.7).next_to(Text5a, DOWN).align_to(Text2, LEFT)
#         Text6a = MathTex(r"\text{This is in the form of } ax^2 + 2hxy + by^2 + gx + ").scale(0.7).next_to(Text5b, DOWN).align_to(Text2, LEFT)
#         Text6b = MathTex(r"fy + k = 0\text{, which represents both } l_1 \text{ and } l_2.").scale(0.7).next_to(Text6a, DOWN).align_to(Text2, LEFT)
#         self.play(AnimationGroup(
#             Write(Text3),
#             Write(Text4),
#             lag_ratio=2
#         ))
#         self.play(Wait(1))
#         self.play(Write(Text5a),run_time=3.5)
#         self.play(Write(Text5b),run_time=3.5)
#         self.play(Wait(1))
#         self.play(Write(Text6a),run_time=2.5)
#         self.play(Write(Text6b),run_time=2.5)
#         self.play(Wait(2.5))
#         self.play(FadeOut(Group(Text3,Text4,Text6a,Text6b)))
#         Text7=MathTex(r"\text{Now, if both lines pass through the origin:}").scale(0.7).next_to(Text2,DOWN).align_to(Text2,LEFT)
#         cTex=MathTex(r"c_1=c_2=0", color=PURPLE).scale(0.7).shift(DOWN+RIGHT)
#         self.play(Write(Text7))
#         self.play(Wait(1))
#         self.play(Text5a.animate.shift(UP*0.7),Text5b.animate.shift(UP*0.7))
#         text1=MathTex(r"l_1: a_1x+b_1y=0",color=LIGHT_BROWN).scale(0.7).next_to(Plane1,RIGHT).shift(UP*2.5) 
#         text2=MathTex(r"l_2: a_2x+b_2y=0",color=LIGHT_GRAY).scale(0.7).next_to(Text1,DOWN).align_to(Text1,LEFT)
#         text5a = MathTex(r"=0").scale(0.7).next_to(Text4, DOWN).align_to(Text2, LEFT).shift(UP*0.7)
#         text5b = MathTex(r"+ (a_1 \cdot 0 + a_2 \cdot 0)x + (b_1 \cdot 0 + b_2 \cdot 0)y + 0 \cdot 0 = 0").scale(0.7).next_to(Text5a, DOWN).align_to(Text2, LEFT)
#         cTexbg=RoundedRectangle(color=PURPLE,fill_opacity=0,corner_radius=0.1,height=cTex.height+0.2,width=cTex.width+0.2).move_to(cTex.get_center())
#         self.play(Write(cTex),Create(cTexbg))
#         self.play(Wait(0.6))
#         self.play(AnimationGroup(Indicate(Text1),Indicate(Text2),Indicate(Text5a),Indicate(Text5b),lag_ratio=0.4))
#         self.play(Wait(0.5))
#         self.play(FadeOut(Group(cTex,cTexbg)))
#         self.play(ReplacementTransform(Text1,text1),ReplacementTransform(Text2,text2))
#         self.play(Wait(1))
#         self.play(ReplacementTransform(Text5b,text5b))
#         self.play(Wait(1))
#         self.play(FadeOut(text5b),Write(text5a.next_to(Text5a,RIGHT,buff=-0.00001)))
#         self.play(Wait(0.5))
#         self.play(c.animate.set_value(0),b.animate.set_value(0),l1_label.animate.move_to(Plane1.c2p(4.5,8)),l2_label.animate.move_to(Plane1.c2p(8,3.2)),run_time=3)
#         Text8 = MathTex(r"\text{This is known as a homogeneous eq}^n \text{ of degree } 2").scale(0.7).next_to(Text5a, DOWN).align_to(Text2, LEFT)
#         Text9=MathTex(r"\text{as each term in this expression is of }2^{nd}\text{ order.}").scale(0.7).next_to(Text8,DOWN).align_to(Text2,LEFT)
#         Text10=MathTex(r"\text{It is in the form of }ax^2+2hxy+by^2=0.").scale(0.7).next_to(Text9,DOWN).align_to(Text2,LEFT)
#         self.play(Write(Text8))
#         self.play(Wait(1))
#         self.play(Write(Text9))
#         self.play(Wait(1))
#         self.play(Write(Text10))
#         self.play(Wait(1))
#         Text11a=MathTex(r"\text{Finding the angle between the lines represented}").scale(0.7).next_to(Text5a,DOWN).align_to(Text2,LEFT)
#         Text11b=MathTex(r"\text{by a homogeneous eq}^n \text{ of degree } 2.").scale(0.7).next_to(Text11a,DOWN).align_to(Text2,LEFT)
#         Text12a=MathTex(r"m_1=-\frac{a_1}{b_1}").scale(0.7).next_to(Text11b,DOWN).align_to(Text2,LEFT)
#         Text12b=MathTex(r"a_1=-m_1b_1").scale(0.7).next_to(Text11b,DOWN).align_to(Text2,LEFT)
#         Text13a=MathTex(r"m_2=-\frac{a_2}{b_2}").scale(0.7).next_to(Text12a,DOWN).align_to(Text2,LEFT)
#         Text13b=MathTex(r"a_2=-m_2b_2").scale(0.7).next_to(Text12a,DOWN).align_to(Text2,LEFT)
#         Text14=MathTex(r"\Rightarrow m_1b_1 m_2b_2x^2 - (m_1b_1 b_2+m_2b_2 b_1)xy+b_1b_2y^2").scale(0.7).next_to(Text5a,DOWN).align_to(Text2,LEFT)
#         Text14s=MathTex(r"=0").scale(0.7).next_to(Text14,DOWN).align_to(Text2,LEFT)
#         Text15=MathTex(r"\Rightarrow b_1b_2(m_1m_2x^2-(m_1+m_2)xy+y^2)=0").scale(0.7).next_to(Text14s,DOWN).align_to(Text14,LEFT)
#         Text15s=MathTex(r"\Rightarrow m_1m_2x^2-(m_1+m_2)xy+y^2=0 \; \cdots \cdots (i)").scale(0.7).next_to(Text14s,DOWN).align_to(Text14,LEFT)
#         Text16=MathTex(r"ax^2 + 2hxy + by^2=0").scale(0.7).next_to(Text15,DOWN).align_to(Text15,LEFT)
#         Texty=MathTex(r"\text{Divide both sides by b,}").scale(0.7).next_to(Text16,DOWN).align_to(Text15,LEFT)
#         Text17=MathTex(r"\Rightarrow \frac{a}{b}x^2+\frac{2h}{b}xy+y^2=0 \; \cdots \cdots (ii)").scale(0.7).next_to(Texty,DOWN).align_to(Text16,LEFT)
#         angle_arc=always_redraw(lambda: ParametricFunction(lambda t: Plane1.c2p(1.5*np.cos(t),1.5*np.sin(t)),color=YELLOW, t_range=[np.arctan(m.get_value()),np.arctan(a.get_value())]))
#         theta_label=always_redraw(lambda: MathTex(r"\theta",color=YELLOW).scale(0.7).next_to(angle_arc,UR,buff=-0.08))
#         m1=Plane1.get_secant_slope_group(dx=1,graph=l1, x=3, dy_line_color=YELLOW, dx_line_color=YELLOW, include_secant_line=False)
#         m2=Plane1.get_secant_slope_group(dx=1,graph=l2, x=4, dy_line_color=YELLOW, dx_line_color=YELLOW, include_secant_line=False)
#         m1_label=MathTex(r"m_1", color=YELLOW).scale(0.7).next_to(m1,RIGHT)
#         m2_label=MathTex(r"m_2", color=YELLOW ).scale(0.7).next_to(m2,RIGHT)
#         self.play(Wait(1))
#         self.play(FadeOut(Text8),FadeOut(Text9),FadeOut(Text10))
#         self.play(Write(Text11a))
#         self.play(Wait(1))
#         self.play(Write(Text11b))
#         self.play(Wait(1))
#         self.play(Indicate(Text11a),Indicate(Text11b))
#         self.play(Wait(0.5))
#         self.play(Create(m1),Create(m2))
#         self.play(Wait(1))
#         self.play(Write(m1_label),Write(m2_label))
#         self.play(Wait(0.5))
#         self.play(TransformMatchingShapes(m1_label.copy(),Text12a),TransformMatchingShapes(m2_label.copy(),Text13a))
#         self.play(Wait(1.4))
#         self.play(Transform(Text12a,Text12b),Transform(Text13a,Text13b))
#         self.play(FadeOut(Text11a,Text11b))
#         self.play(Wait(1))
#         TextB=Group(Text12a,Text13a)
#         self.play(Write(Text14),run_time=3)
#         self.play(Wait(1))
#         self.play(Write(Text14s))
#         self.play(Wait(1))
#         self.play(FadeOut(TextB))
#         self.play(Wait(1))
#         self.play(Write(Text15),run_time=3)
#         self.play(Wait(1))
#         self.play(ReplacementTransform(Text15,Text15s),run_time=1.5)
#         self.play(Wait(1))
#         self.play(Write(Text16),run_time=3)
#         self.play(Wait(1))
#         self.play(Write(Texty))
#         self.play(Wait(1))
#         self.play(Write(Text17),run_time=3)
#         self.play(Wait(1))
#         disappearTexts=Group(Text14,Text14s,Texty,Text16)
#         self.play(FadeOut(disappearTexts))
#         self.play(Create(angle_arc),Create(theta_label))
#         self.play(Wait(1))
#         self.play(Text15s.animate.shift(UP*1.2),Text17.animate.shift(UP*2.7))
#         Text18=MathTex(r"\frac{a}{b}=m_1m_2,\;m_1+m_2=-\frac{2h}{b}",color=YELLOW).scale(0.7).next_to(Text17,DOWN).align_to(Text2,LEFT)
#         Text19=MathTex(r"\tan\theta=\frac{m_1-m_2}{1+m_1 m_2}=\frac{\sqrt{(m_1-m_2)^2}}{1+m_1 m_2}").scale(0.7).next_to(Text18,DOWN).align_to(Text2,LEFT)
#         Text21=MathTex(r"\tan\theta=\frac{\sqrt{(m_1+m_2)^2-4m_1m_2}}{1+m_1 m_2}").scale(0.7).next_to(Text19,DOWN).align_to(Text2,LEFT)
#         self.play(Write(Text18),run_time=3)
#         self.play(Wait(1))
#         self.play(Write(Text19),run_time=3)
#         self.play(Wait(1))
#         self.play(Write(Text21),run_time=3)
#         self.play(Wait(2))
#         keep_mobs = Group(NameLabel, l1_label, l2_label, m1_label, m2_label, Text18, Text19, Text21,background_rectangle,Plane1,l1,l2,y_label,x_label,Topic,m2,m1,theta_label,angle_arc)
#         mobs_to_disappear = Group(*[mob for mob in self.mobjects if mob not in keep_mobs])
#         self.play(FadeOut(mobs_to_disappear))
#         self.play(Wait(1))
#         self.play(Group(Text18, Text19, Text21).animate.shift(UP*3.8))
#         self.play(Wait(1))
#         Text22=MathTex(r"\tan\theta=\frac{\sqrt{(-\frac{2h}{b})^2-4\frac{a}{b}}}{1+\frac{a}{b}}=\frac{\sqrt{\frac{4h^2}{b^2}-4\frac{a}{b}}}{\frac{b+a}{b}}").scale(0.7).next_to(Text21,DOWN).align_to(Text2,LEFT)
#         Text23=MathTex(r"\tan\theta=\frac{\sqrt{\frac{4h^2-4ab}{b^2}}}{\frac{b+a}{b}}=\frac{\sqrt{\frac{4(h^2-ab)}{b^2}}}{\frac{b+a}{b}}").scale(0.7).next_to(Text22,DOWN).align_to(Text2,LEFT)
#         Text24=MathTex(r"\tan\theta=\frac{\frac{2}{b}\sqrt{(h^2-ab)}}{\frac{b+a}{b}}").scale(0.7).next_to(Text23,DOWN).align_to(Text2,LEFT)
#         Text27=MathTex(r"\therefore \tan\theta=\frac{2\sqrt{h^2-ab}}{a+b}").scale(0.7).move_to(Text24.get_center()).align_to(Text24,LEFT)
#         Text27bg=RoundedRectangle(color=PURPLE,fill_opacity=0,corner_radius=0.2,height=Text27.height+0.2,width=Text27.width+0.2).move_to(Text27.get_center())
#         self.play(Write(Text22,run_time=5))
#         self.play(Wait(1))
#         self.play(Write(Text23),run_time=6)
#         self.play(Wait(1))
#         self.play(Write(Text24),run_time=5)
#         self.play(Wait(1))
#         self.play(Transform(Text24,Text27))
#         self.play(Wait(1))
#         self.play(Create(Text27bg))
#         self.play(Wait(2))
#         keep_mobs1 = Group(NameLabel, l1_label, l2_label, m1_label, m2_label,background_rectangle,Plane1,l1,l2,y_label,x_label,Topic,m2,m1,Text27bg,Text24,Text27)
#         self.play(*[FadeOut(mob) for mob in self.mobjects if not mob in keep_mobs1])

# class homogeneous2(Scene):
#     def construct(self):
#         Topic=MathTex(r"\mathbf{Pair\;of\;straight\;lines}").to_edge(UP)
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         k=ValueTracker(4)
#         Plane1 = NumberPlane(x_range=[-5+k.get_value(),5+k.get_value()],
#                              y_range=[-5+k.get_value(),5+k.get_value()]).scale(0.6).to_edge(LEFT)
#         background_rectangle=Rectangle(width=Plane1.height,height=Plane1.height,
#                                        color=YELLOW,fill_opacity=0).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         a=ValueTracker(2)
#         b=ValueTracker(0)
#         m=ValueTracker(1/2)
#         c=ValueTracker(0)
#         def f(x):
#             y=a.get_value()*x+b.get_value()
#             return max(min(y,9),-1)
#         def g(x):
#             y=m.get_value()*x+c.get_value()
#             return max(min(y,9),-1)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: f(x),color=LIGHT_BROWN,
#                                              x_range=[-5+k.get_value(),5+k.get_value()]).set_stroke(width=3))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g(x),color=LIGHT_GRAY,
#                                              x_range=[-5+k.get_value(),5+k.get_value()]).set_stroke(width=3))
#         l1_label=MathTex(r"l_1",color=LIGHT_BROWN).move_to(Plane1.c2p(4.5,8)).scale(0.9)
#         l2_label=MathTex(r"l_2",color=LIGHT_GRAY).move_to(Plane1.c2p(8,3.2)).scale(0.9)
#         m1=Plane1.get_secant_slope_group(dx=1,graph=l1, x=3, dy_line_color=YELLOW,
#                                          dx_line_color=YELLOW, include_secant_line=False)
#         m2=Plane1.get_secant_slope_group(dx=1,graph=l2, x=4, dy_line_color=YELLOW,
#                                          dx_line_color=YELLOW, include_secant_line=False)
#         m1_label=MathTex(r"m_1", color=YELLOW).scale(0.7).next_to(m1,RIGHT)
#         m2_label=MathTex(r"m_2", color=YELLOW ).scale(0.7).next_to(m2,RIGHT)
#         Text27=MathTex(r"\therefore \tan\theta=\frac{2\sqrt{h^2-ab}}{a+b}").scale(0.7).next_to(Plane1,RIGHT).shift(DOWN*3.4)
#         Text27bg=RoundedRectangle(color=PURPLE,fill_opacity=0,corner_radius=0.2,
#                                   height=Text27.height+0.2,width=Text27.width+0.2).move_to(Text27.get_center())
#         Formula=Group(Text27bg,Text27)
#         angle_arc=always_redraw(lambda: ParametricFunction(lambda  t: Plane1.c2p(1.5*np.cos(t),1.5*np.sin(t)),color=YELLOW, t_range=[np.arctan(m.get_value()),np.arctan(a.get_value())]))
#         theta_label=always_redraw(lambda: MathTex(r"\theta",color=YELLOW).scale(0.7).next_to(angle_arc,UR,buff=-0.08))
#         self.add(NameLabel,Topic,Plane1,background_rectangle,y_label,x_label,
#                  l1,l2,l1_label,l2_label,m1,m2,m1_label,m2_label,Formula,angle_arc,theta_label)
#         self.play(Wait(1))
#         self.play(Formula.animate.shift(UP*5.8))
#         self.play(FadeOut(Group(m1,m2,m1_label,m2_label)))
#         self.play(a.animate.set_value(8),m.animate.set_value(-1/8),l1_label.animate.shift(LEFT*0.6*3),l2_label.animate.shift(DOWN*0.6*3.5),run_time=2)
#         self.play(Wait(1))
#         perp_label=MathTex(r"90^\circ",color=YELLOW).scale(0.7).move_to(theta_label.get_center())
#         self.play(ReplacementTransform(theta_label,perp_label))
#         self.play(Wait(1))
#         Text28=MathTex(r"l_1\perp l_2 \Rightarrow \tan\theta=\tan 90^\circ = \frac{2\sqrt{h^2-ab}}{a+b}").scale(0.7).next_to(Text27,DOWN).align_to(Text27,LEFT)
#         Text29=MathTex(r"\Rightarrow \frac{1}{\tan 90^\circ} = \frac{a+b}{2\sqrt{h^2-ab}}").scale(0.7).next_to(Text28,DOWN).align_to(Text27,LEFT)
#         Text30=MathTex(r"\Rightarrow \cot 90^\circ \cdot 2\sqrt{h^2-ab}=a+b").scale(0.7).next_to(Text29,DOWN).align_to(Text27,LEFT)
#         Text31=MathTex(r"\Rightarrow 0 = a+b").scale(0.7).next_to(Text30,DOWN).align_to(Text27,LEFT)
#         Text32a=MathTex(r"\therefore a+b=0").scale(0.7).next_to(Text31,DOWN).align_to(Text27,LEFT)
#         Text32b=MathTex(r"l_1\perp l_2 \Rightarrow a+b=0").scale(0.7).next_to(Text31,DOWN).align_to(Text27,LEFT)
#         self.play(Write(Text28))
#         self.play(Wait(1))
#         self.play(Write(Text29))
#         self.play(Wait(1))
#         self.play(Write(Text30))
#         self.play(Wait(1))
#         self.play(Write(Text31))
#         self.play(Wait(1))
#         self.play(Write(Text32a))
#         self.play(Wait(1))
#         self.play(Transform(Text32a, Text32b))
#         self.play(Wait(2))
#         self.play(FadeOut(Group(Text28, Text29, Text30, Text31)))
#         Text32bg = RoundedRectangle(color=GREEN, fill_opacity=0, corner_radius=0.2,
#                                     height=Text32b.height+0.2, width=Text32b.width+0.2).move_to(Text32b.get_center())
#         self.play(Create(Text32bg))
#         self.play(Wait(1))
#         Formula2 = Group(Text32a, Text32bg)
#         self.play(Formula2.animate.next_to(Formula, RIGHT))
#         self.play(FadeOut(perp_label))
#         self.play(a.animate.set_value(1), m.animate.set_value(1),
#                   l1_label.animate.shift(RIGHT*4*0.6), l2_label.animate.shift(UP*0.6*6), run_time=2)
#         PText1 = MathTex(r"l_1||l_2 \Rightarrow \tan\theta=\tan 0^\circ = \frac{2\sqrt{h^2-ab}}{a+b}").scale(0.7).next_to(Text27, DOWN).align_to(Text27, LEFT)
#         PText2 = MathTex(r"\Rightarrow 0=\frac{2\sqrt{h^2-ab}}{a+b}").scale(0.7).next_to(PText1, DOWN).align_to(Text27, LEFT)
#         PText3 = MathTex(r"\Rightarrow 0\cdot(a+b)=2\sqrt{h^2-ab}").scale(0.7).next_to(PText2, DOWN).align_to(Text27, LEFT)
#         PText4 = MathTex(r"\Rightarrow 0=2\sqrt{h^2-ab}").scale(0.7).next_to(PText3, DOWN).align_to(Text27, LEFT)
#         PText5 = MathTex(r"\therefore h^2=ab").scale(0.7).next_to(PText4, DOWN).align_to(Text27, LEFT)
#         PText6 = MathTex(r"l_1||l_2 \Rightarrow h^2=ab").scale(0.7).move_to(PText5.get_center()).align_to(Text27, LEFT)
#         self.play(Write(PText1))
#         self.play(Wait(1))
#         self.play(Write(PText2))
#         self.play(Wait(1))
#         self.play(Write(PText3))
#         self.play(Wait(1))
#         self.play(Write(PText4))
#         self.play(Wait(1))
#         self.play(Write(PText5))
#         self.play(Wait(1))
#         self.play(Transform(PText5, PText6))
#         self.play(Wait(2))
#         self.play(FadeOut(Group(PText1, PText2, PText3, PText4)))
#         PTextbg = RoundedRectangle(color=BLUE, fill_opacity=0, corner_radius=0.2,
#                                    height=PText6.height+0.2, width=PText6.width+0.2).move_to(PText6.get_center())
#         self.play(Create(PTextbg))
#         Formula3 = Group(PText5, PTextbg)
#         self.play(Formula3.animate.next_to(Formula2, DOWN))
#         graph_mobs = [
#             Plane1,
#             background_rectangle,
#             x_label,
#             y_label,
#             l1,
#             l2,
#             l1_label,
#             l2_label,
#             angle_arc,
#         ]
#         self.play(*[FadeOut(mob) for mob in graph_mobs])
#         self.play(
#             Formula.animate.to_corner(UL),
#             Formula3.animate.to_corner(UR),
#             Formula2.animate.next_to(Topic,DOWN)
#         )

#         TextEq1 = MathTex(r"ax^2+2hxy+by^2=0").scale(0.7)
#         TextEq2 = MathTex(r"ax^2+2hxy+by^2+gx+fy+c=0").scale(0.7).next_to(TextEq1, DOWN)
#         TextEq1.move_to(ORIGIN)
#         TextEq2.next_to(TextEq1, DOWN)
#         self.play(Write(TextEq1), Write(TextEq2),run_time=2)
#         self.play(Wait(1))
#         NoteText = Tex("These formulae work regardless of whether the given equation represents lines passing through the origin or not.").scale(0.7).next_to(TextEq2, DOWN, buff=0.5)
#         self.play(Write(NoteText),run_time=4)
#         self.play(Indicate(Formula))
#         self.play(Wait(0.5))
#         self.play(Indicate(Formula2))
#         self.play(Wait(0.5))
#         self.play(Indicate(Formula3))
#         self.play(Wait(2))
#         keep_only = Group(NameLabel)
#         fade_out_group = Group(*[mob for mob in self.mobjects if mob not in keep_only])
#         self.play(FadeOut(fade_out_group))

# class homoPractice1(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = Tex(r"\text{1. Find the single equation representing both $x-y+1=0$ and $3x+y=2$. ").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         Plane1 = NumberPlane(
#             x_range=[-3,7],
#             y_range=[-4,6]
#         ).scale(0.6).to_edge(LEFT)
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,5.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(6.5,-0.5)).scale(0.9)
#         def f(x):
#             y = x+1
#             return max(min(y, 6), -4)
#         def g(x):
#             y = 2-3*x
#             return max(min(y, 6), -4)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: f(x), color=BLUE_B))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g(x), color=GRAY_BROWN))
#         l1_l = MathTex(r"l_1", color=BLUE_B).scale(0.7).move_to(Plane1.c2p(1,3))
#         l2_l = MathTex(r"l_2", color=GRAY_BROWN).scale(0.7).move_to(Plane1.c2p(-1,4))
#         self.play(FadeIn(Group(y_label,x_label,background_rectangle,Plane1,l1,l2,l1_l,l2_l)))
#         self.play(Write(Question),run_time=3.3)
#         self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(Question, DOWN).shift(RIGHT*1.1)
#         self.play(Write(SolutionTex))
#         l1_tex=MathTex(r"l_1:\;x-y+1=0\cdots\cdots(i)", color=BLUE_B).scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         l2_tex=MathTex(r"l_2:\;3x+y=2", color=GRAY_BROWN).scale(0.7).next_to(l1_tex, DOWN).align_to(SolutionTex, LEFT)
#         l2_tex_b=MathTex(r"l_2:\;3x+y-2=0\cdots\cdots(ii)", color=GRAY_BROWN  ).scale(0.7).next_to(l1_tex, DOWN).align_to(SolutionTex, LEFT)
#         t1 = Tex("Multiply (i) and (ii):").scale(0.7).next_to(l2_tex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"(x-y+1)(3x+y-2)=0").scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         t3 = MathTex(r"\Rightarrow 3x^2+xy-2x-3xy-y^2+2y+3x+y-2").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         t3b = MathTex(r"=0").scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         t4 = MathTex(r"\therefore 3x^2-2xy-y^2+x+3y-2=0").scale(0.7).next_to(t3b, DOWN).align_to(SolutionTex, LEFT)
#         self.play(Write(l1_tex))
#         self.wait(1)
#         self.play(Write(l2_tex))
#         self.wait(1)
#         self.play(Transform(l2_tex,l2_tex_b))
#         self.wait(1)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t2))
#         self.wait(1)
#         self.play(Write(t3),run_time=4)
#         self.wait(1)
#         self.play(Write(t3b))
#         self.wait(1)
#         self.play(Write(t4),run_time=3.5)
#         self.wait(2 )
#         fade_mobs = [t1, t2, t3, t4, t3b,SolutionTex,l1_tex,l2_tex,Question]
#         self.play(*[FadeOut(mob) for mob in fade_mobs])
        
# class homoPractice2(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = Tex(r"\text{2. Find the separate equations representing $x^2-5xy+4y^2=0$.").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         Plane1 = NumberPlane(
#             x_range=[-3,7],
#             y_range=[-4,6]
#         ).scale(0.6).to_edge(LEFT)
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,5.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(6.5,-0.5)).scale(0.9)
#         a=ValueTracker(1)
#         b=ValueTracker(1)
#         m=ValueTracker(-3)
#         c=ValueTracker(2)
#         def f(x):
#             y = a.get_value()*x+b.get_value()
#             return max(min(y, 6), -4)
#         def g(x):
#             y = m.get_value()*x+c.get_value()
#             return max(min(y, 6), -4)
#         l1=always_redraw(lambda: Plane1.plot(lambda x: f(x), color=BLUE_B))
#         l2=always_redraw(lambda: Plane1.plot(lambda x: g(x), color=GRAY_BROWN))
#         l1_l = MathTex(r"l_1", color=BLUE_B).scale(0.7).move_to(Plane1.c2p(1,3))
#         l2_l = MathTex(r"l_2", color=GRAY_BROWN).scale(0.7).move_to(Plane1.c2p(-1,4))
#         plane_stuff=(Group(y_label,x_label,background_rectangle,Plane1,l1,l2,l1_l,l2_l))
#         self.add(plane_stuff)
#         self.play(Write(Question),run_time=3.3)
#         self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(Question, DOWN).shift(RIGHT*2)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"x^2-5xy+4y^2=0").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"\Rightarrow x^2-4xy-xy+4y^2=0").scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         t3 = MathTex(r"\Rightarrow x(x-4y)-y(x-4y)=0").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         t4 = MathTex(r"\Rightarrow(x-4y)(x-y)=0").scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         t5 = MathTex(r"\therefore y=\frac{1}{4}x\text{ and }y=x").scale(0.7).next_to(t4, DOWN).align_to(SolutionTex, LEFT)
#         self.play(b.animate.set_value(0),c.animate.set_value(0))
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t2))
#         self.wait(1)
#         self.play(Write(t3))
#         self.wait(1)
#         self.play(TransformMatchingShapes(t3.copy(),t4))
#         self.wait(1)
#         self.play(Write(t5))
#         self.wait(2)
#         keep_mobs = [NameLabel]
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if mob not in keep_mobs]
#         )
      
# class homoPractice3(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = Tex(r"\text{3. Find the separate equations representing $4x^2+4xy+y^2+6x+3y-4=0$.").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         self.play(Write(Question), run_time=3.3)
#         self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(Question, DOWN)
#         t1 = MathTex(r"4x^2+4xy+y^2+6x+3y-4=0",color=BLUE_B).scale(0.7).to_corner(UL).shift(DOWN)
#         SolutionTex.align_to(t1,LEFT)
#         self.play(Write(SolutionTex))
#         t2 = MathTex(r"\text{Treat as a quadratic in }x:\;4x^2+(4y+6)x+(y^2+3y-4)=0",color=GOLD).scale(0.7)
#         t3a = MathTex(r"x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}").scale(0.7)
#         t3 = MathTex(r"x=\dfrac{-(4y+6)\pm\sqrt{(4y+6)^2-16(y^2+3y-4)}}{8}").scale(0.7)
#         t4a = MathTex(r"\Rightarrow x=\frac{-(4y+6)\pm\sqrt{16y^2-16y^2+36+48y-48y+64}}{8}").scale(0.7)
#         t4 = MathTex(r"\Rightarrow x=\dfrac{-(4y+6)\pm\sqrt{100}}{8}").scale(0.7)
#         t5 = MathTex(r"\Rightarrow x=\dfrac{-(4y+6)\pm10}{8}").scale(0.7)
#         t6 = MathTex(r"\Rightarrow x=\dfrac{-4y-6+10}{8}\quad\text{or}\quad x=\dfrac{-4y-6-10}{8}").scale(0.7)
#         t7 = MathTex(r"\Rightarrow x=\dfrac{4-4y}{8}\quad\text{or}\quad x=\dfrac{-16-4y}{8}").scale(0.7)
#         t8 = MathTex(r"\Rightarrow x=\dfrac{1-y}{2}\quad\text{or}\quad x=-\dfrac{y+4}{2}").scale(0.7)
#         t9 = MathTex(r"\therefore\;2x+y-1=0\text{, }2x+y+4=0",color=RED_B).scale(0.7)
#         t2.next_to(t1, DOWN).align_to(t1,LEFT)
#         t3a.next_to(t2, DOWN).align_to(t1,LEFT)
#         t3.next_to(t2, DOWN).align_to(t1,LEFT)
#         t4.next_to(t3, DOWN).align_to(t1,LEFT)
#         t4a.next_to(t3, DOWN).align_to(t1,LEFT)
#         t5.next_to(t4, DOWN).align_to(t1,LEFT)
#         t6.next_to(t5, DOWN).align_to(t1,LEFT)
#         t7.next_to(t3, RIGHT)
#         t8.next_to(t7, DOWN).align_to(t7,LEFT)
#         t9.next_to(t8, DOWN).align_to(t7,LEFT)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t2))
#         self.wait(1)
#         self.play(Write(t3a),run_time=3)
#         self.wait(1)
#         self.play(Transform(t3a,t3),run_time=2)
#         self.wait(1)
#         self.play(Write(t4a),run_time=4)
#         self.wait(1)
#         self.play(Transform(t4a,t4),run_time=2.5)
#         self.wait(1)
#         self.play(Write(t5))
#         self.wait(1)
#         self.play(Write(t6))
#         self.wait(1)
#         self.play(Write(t7))
#         self.wait(1)
#         self.play(Write(t8))
#         self.wait(1)
#         self.play(Write(t9))
#         self.wait(2)
#         self.play(
#             *[FadeOut(mob) for mob in [t1, t2, t3, t4, t5, t6, t7, t8, t9, t3a, Question, SolutionTex,t4a]]
#         )

# class homoPractice4(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = Tex("4. Find the separate equations representing $x^2 - 2\sec \\theta \\,xy + y^2 = 0$.}").scale(0.7).to_corner(UL)
#         eq = MathTex(r"x^2 - 2\sec\theta\,xy + y^2 = 0", color=BLUE_B).scale(0.7).next_to(Question, DOWN).align_to(Question, LEFT)
#         self.add(NameLabel)
#         self.play(Write(Question))
#         self.play(Write(eq))
#         self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(eq, DOWN).align_to(eq, LEFT)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"\text{Treat as a quadratic in }x:\;x^2 + (-2\sec\theta\,y)x + y^2 = 0").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"\text{Quadratic formula: }x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}", color=GOLD).scale(0.7).next_to(t1, DOWN).align_to(t1, LEFT)
#         t3 = MathTex(r"\Rightarrow x=\dfrac{2\sec\theta\,y \pm \sqrt{4\sec^2\theta\,y^2-4y^2}}{2}").scale(0.7).next_to(t2, DOWN).align_to(t1, LEFT)
#         t4 = MathTex(r"\Rightarrow x=\dfrac{2y(\sec\theta\pm\sqrt{\sec^2\theta-1})}{2}").scale(0.7).next_to(t3, DOWN).align_to(t1, LEFT)
#         t5 = MathTex(r"\Rightarrow x=y(\sec\theta\pm\tan\theta)").scale(0.7).next_to(t4, DOWN).align_to(t1, LEFT)
#         t6 = MathTex(r"\therefore x-y(\sec\theta+\tan\theta)=0\quad\text{and}\quad x-y(\sec\theta-\tan\theta)=0", color=RED_B).scale(0.7).next_to(t5, DOWN).align_to(t1, LEFT)
#         for t in [t1, t2, t3, t4, t5, t6]:
#             self.play(Write(t))
#             self.play(Wait(1))
#         self.play(Wait(1))
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [NameLabel]])

# class homoPractice5(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{5. Find the angle between the lines }x^2 +3xy+2y^2=0.").scale(0.7).to_corner(UL)
#         eq = MathTex(r"x^2 +3xy+2y^2=0 ", color=BLUE_B).scale(0.7).next_to(Question, DOWN).align_to(Question, LEFT)
#         self.add(NameLabel)
#         self.play(Write(Question)); self.play(Write(eq)); self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(eq, DOWN).align_to(eq, LEFT)
#         t1 = MathTex(r"\text{Compare with }ax^2+2hxy+by^2=0:").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"a=1,\;2h=3\Rightarrow h=\tfrac{3}{2},\;b=2").scale(0.7).next_to(t1, DOWN).align_to(t1, LEFT)
#         f1 = MathTex(r"\tan\theta=\pm\frac{2\sqrt{h^2-ab}}{a+b}", color=GOLD).scale(0.7).next_to(t2, DOWN).align_to(t1, LEFT)
#         t3 = MathTex(r"\tan\theta=\pm\frac{2\sqrt{\tfrac{9}{4}-2}}{1+2}=\pm\frac{1}{3}").scale(0.7).next_to(f1, DOWN).align_to(f1, LEFT)
#         ans = MathTex(r"\therefore \theta=\tan^{-1}\!\left(\pm\frac{1}{3}\right)", color=RED_B).scale(0.7).next_to(t3, DOWN).align_to(t3, LEFT)
#         for t in [SolutionTex, t1, t2, f1, t3, ans]:
#             self.play(Write(t))
#             self.play(Wait(1))
#         self.play(Wait(2))
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [NameLabel]])

# class homoPractice6(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{6. Find the angle between the lines }x^2 - 5xy + 4y^2 + x + 2y - 2 = 0.").scale(0.7).to_corner(UL)
#         eq = MathTex(r"x^2 - 5xy + 4y^2 + x + 2y - 2 = 0", color=BLUE_B).scale(0.7).next_to(Question, DOWN).align_to(Question, LEFT)
#         self.add(NameLabel)
#         self.play(Write(Question),run_time=4); self.play(Write(eq)); self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(eq, DOWN).align_to(eq, LEFT)
#         t1 = MathTex(r"\text{Compare with }ax^2+2hxy+by^2+\cdots=0:").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"\Rightarrow a=1,\;2h=-5\Rightarrow h=-\tfrac{5}{2},\;b=4").scale(0.7).next_to(t1, DOWN).align_to(t1, LEFT)
#         f1 = MathTex(r"\tan\theta=\pm\dfrac{2\sqrt{h^2-ab}}{a+b}", color=GOLD).scale(0.7).next_to(t2, DOWN).align_to(t1, LEFT)
#         t3 = MathTex(r"\tan\theta=\pm\dfrac{2\sqrt{\tfrac{25}{4}-4}}{1+4}=\pm\frac{3}{5}").scale(0.7).next_to(f1, DOWN).align_to(f1, LEFT)
#         ans = MathTex(r"\therefore \theta=\tan^{-1}\!\left(\pm\frac{3}{5}\right)", color=RED_B).scale(0.7).next_to(t3, DOWN).align_to(t3, LEFT)
#         for t in [SolutionTex, t1, t2, f1, t3, ans]:
#             self.play(Write(t),run_time=3); self.play(Wait(1))
#         self.play(Wait(2))
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [NameLabel]])

# class homoPractice7(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{7. Show the lines represented by }x^2 - 2xy\cot\theta - y^2 = 0\text{ are perpendicular.}").scale(0.7).to_corner(UL)
#         eq = MathTex(r"x^2 - 2xy\cot\theta - y^2 = 0", color=BLUE_B).scale(0.7).next_to(Question, DOWN).align_to(Question, LEFT)

#         self.add(NameLabel)
#         self.play(Write(Question),run_time=4.5); self.play(Write(eq)); self.play(Wait(1))

#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(eq, DOWN).align_to(eq, LEFT)
#         t1 = MathTex(r"\text{Compare to }ax^2+2hxy+by^2=0:").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"a=1,\;b=-1").scale(0.7).next_to(t1, DOWN).align_to(t1, LEFT)
#         f1 = MathTex(r"a+b=-1+1=0\Rightarrow l_1 \perp l_2", color=GOLD).scale(0.7).next_to(t2, DOWN).align_to(t2, LEFT)
#         for t in [SolutionTex, t1, t2, f1]:
#             self.play(Write(t)); self.play(Wait(1))
#         self.play(Wait(2)); self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [NameLabel]])

# class homoPractice8(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{8. Show the lines represented by }x^2 - xy + \tfrac{y^2}{4} = 0\text{ are coincident.}").scale(0.7).to_corner(UL)
#         eq = MathTex(r"x^2 - xy + \frac{y^2}{4} = 0", color=BLUE_B).scale(0.7).next_to(Question, DOWN).align_to(Question, LEFT)
#         self.add(NameLabel)
#         self.play(Write(Question),run_time=4.5); self.play(Write(eq)); self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(eq, DOWN).align_to(eq, LEFT)
#         t1 = MathTex(r"\text{Compare to }ax^2+2hxy+by^2=0:").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"a=1,\;b=\tfrac{1}{4},\;2h=-1\Rightarrow h=-\tfrac{1}{2}").scale(0.7).next_to(t1, DOWN).align_to(t1, LEFT)
#         f1 = MathTex(r"h^2-ab=\bigg(-\frac{1}{2}\bigg)^2-\frac{1}{4}=0\Rightarrow l_1 || l_2", color=GOLD).scale(0.7).next_to(t2, DOWN).align_to(t2, LEFT)
#         for t in [SolutionTex, t1, t2, f1]:
#             self.play(Write(t)); self.play(Wait(1))

#         self.play(Wait(2)); self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [NameLabel]])

# class homoPracticeIX(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{9. Find }\lambda\text{ so that the pair }\lambda x^2 - 5xy - 6y^2 = 0\text{ is perpendicular.}").scale(0.65).to_corner(UL)
#         eq = MathTex(r"\lambda x^2 - 5xy - 6y^2 = 0", color=BLUE_B).scale(0.7).next_to(Question, DOWN).align_to(Question, LEFT)
#         self.add(NameLabel)
#         self.play(Write(Question),run_time=3);self.play(Wait(1));self.play(Write(eq)); self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(eq, DOWN).align_to(eq, LEFT)
#         t1 = MathTex(r"\text{Compare to }ax^2+2hxy+by^2=0: ").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"a=\lambda,\;b=-6").scale(0.7).next_to(t1, DOWN).align_to(t1, LEFT)
#         f1 = MathTex(r"a+b=0\;[\,\because\;l_1\perp l_2\,]", color=GOLD).scale(0.7).next_to(t2, DOWN).align_to(t2, LEFT)
#         t3 = MathTex(r"\lambda-6=0\Rightarrow \lambda=6").scale(0.7).next_to(f1, DOWN).align_to(f1, LEFT)
#         t4 = MathTex(r"6x^2 - 5xy - 6y^2 = 0").scale(0.7).next_to(t3, DOWN).align_to(t3, LEFT)
#         t5 = MathTex(r"\Rightarrow 6x^2 - 9xy + 4xy - 6y^2=0").scale(0.7).next_to(t4, DOWN).align_to(t4, LEFT)
#         t6 = MathTex(r"\Rightarrow 3x(2x-3y)+2y(2x-3y)=0").scale(0.7).next_to(t5, DOWN).align_to(t4, LEFT)
#         t7 = MathTex(r"\Rightarrow (2x-3y)(3x+2y)=0").scale(0.7).next_to(t6, DOWN).align_to(t4, LEFT)
#         ans = MathTex(r"\therefore 2x-3y=0 \;\;\text{and}\;\; 3x+2y=0", color=RED_B).scale(0.7).next_to(t7, RIGHT)
#         for t in [SolutionTex, t1, t2, f1, t3, t4, t5, t6, t7, ans]:
#             self.play(Write(t),run_time=2.5); self.play(Wait(1))
#         self.play(Wait(2)); self.play(*[FadeOut(mob) for mob in self.mobjects])

# class ExampleQuestionsTitle(Scene):
#     def construct(self):
#         Topic=Tex("Example Questions")
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         self.add(NameLabel)
#         self.play(Write(Topic))
#         self.play(Wait(1))
#         self.play(FadeOut(Topic))

# class ConicSectionP1(ThreeDScene):
#     def construct(self):
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         Topic=MathTex(r"\textbf{Conic Sections}").shift(UR*2)
#         self.add_fixed_in_frame_mobjects(NameLabel)
#         axes = ThreeDAxes(x_range=[-5, 5, 1],
#             y_range=[-5, 5, 1],
#             z_range=[-5, 5, 1],
#             x_length=10,
#             y_length=10,
#             z_length=10)
#         cone1 = Cone(
#             direction=OUT,
#             base_radius=2,
#             height=4,
#             fill_opacity=0.5,
#             color=BLUE,
#             resolution=(32, 32),
#             show_base=True,
#             stroke_opacity=0)
#         cone2=Cone(base_radius=2,
#                    direction=IN,
#                    show_base=True,
#                    color=BLUE,
#                    fill_opacity=0.5,
#                    height=4,
#                    resolution=(32, 32),
#                    stroke_opacity=0)
#         self.play(FadeIn(cone1),FadeIn(cone2))
#         height=ValueTracker(-4)
#         self.play(FadeIn(axes))
#         self.play(AnimationGroup(Write(Topic),Write(NameLabel),lag_ratio=0.4))
#         Text1=Tex("If a plane intersects a right cone parallel to the base or perpendicular").scale(0.8).to_corner(UR).set_opacity(0)
#         Text2=Tex("to the vertial axis of the cone, the section formed is a circle.").scale(0.8).next_to(Text1,DOWN).set_opacity(0)
#         Text3=Tex("If a plane intersects a right cone parallel to the generator").scale(0.8).to_edge(UP).set_opacity(0)
#         Text4=Tex("of the cone, the section formed is a parabola.").next_to(Text3,DOWN).scale(0.8).set_opacity(0)
#         self.add_fixed_in_frame_mobjects(Text1,Text2,Text3,Text4)
#         plane1=always_redraw(lambda: Rectangle(width=5,height=5,color=YELLOW,fill_opacity=0.5).shift(OUT*height.get_value()))
#         self.move_camera(phi=60 * DEGREES, theta=240 * DEGREES,run_time=4)
#         circ=always_redraw(lambda: Circle(radius=np.abs(height.get_value()*0.5),color=YELLOW,fill_opacity=0.5).shift(OUT*height.get_value()))
#         self.play(Wait(1))
#         self.play(Text1.animate.set_opacity(1))
#         self.play(Text2.animate.set_opacity(1))
#         self.play(Wait(2))
#         self.play(FadeIn(plane1),FadeIn(circ))
#         self.play(height.animate.set_value(2),run_time=3)
#         self.play(Wait(2.5))
#         self.play(FadeOut(plane1),FadeOut(circ),FadeOut(Text2),FadeOut(Text1))
#         a = ValueTracker(-4)
#         k=2
#         plane2=always_redraw(lambda: Surface(
#             lambda u, v: axes.c2p(u, v, k*v + a.get_value()),
#             u_range=[-3, 3],
#             v_range=[-3, 3],
#             resolution=(1, 1),   
#             fill_opacity=0.2,
#             stroke_opacity=1,
#             stroke_width=4, 
#             shade_in_3d=False).set_color(YELLOW).set_stroke(YELLOW, width=4))
#         curve = always_redraw(lambda: ParametricFunction(
#             lambda t: axes.c2p(
#                 t,
#                 (0.5*k/a.get_value()) * t**2 - a.get_value()/(2*k),
#                 k*((0.5*k/a.get_value()) * t**2 - a.get_value()/(2*k))+a.get_value()
#             ),
#             t_range=[-3, 3],
#             color=YELLOW,
#             fill_opacity=0.5))
#         self.play(Text3.animate.set_opacity(1))
#         self.play(Text4.animate.set_opacity(1))
#         self.play(Wait(2))
#         self.play(FadeIn(curve), FadeIn(plane2))
#         self.play(Wait(1))
#         self.play(a.animate.set_value(3),run_time=4)
#         self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES,run_time=4)
#         generator_text=Tex("Generator").shift(RIGHT+UP).scale(0.8).rotate(angle=62*DEGREES)
#         self.add_fixed_in_frame_mobjects(generator_text)
#         self.play(Write(generator_text))
#         self.play(Wait(2.5))
#         self.play(FadeOut(curve),FadeOut(plane2),FadeOut(generator_text),FadeOut(Text3),FadeOut(Text4))
 
# class ConicSectionP2(ThreeDScene):
#     def construct(self):
#         axes = ThreeDAxes(
#         x_range=[-5, 5, 1],
#         y_range=[-5, 5, 1],
#         z_range=[-5, 5, 1],
#         x_length=10,
#         y_length=10,
#         z_length=10,
#         )
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         self.add_fixed_in_frame_mobjects(NameLabel)
#         cone1 = Cone(
#             direction=OUT,
#             base_radius=2,
#             height=4,
#             fill_opacity=0.5,
#             color=BLUE,
#             resolution=(32, 32),
#             show_base=True,
#             stroke_opacity=0)
#         cone2=Cone(base_radius=2,
#             direction=IN,
#             show_base=True,
#             color=BLUE,
#             fill_opacity=0.5,
#             height=4,
#             resolution=(32, 32),
#             stroke_opacity=0)
#         Text1=MathTex(r"\text{If the angle formed by the plane with the vertical axis of the cone }").scale(0.8).to_edge(UP).set_opacity(0).set_z_index(1)
#         Text2=MathTex(r"\text{equals to the semi-vertical angle of the cone (}\theta\text{),}").scale(0.8).next_to(Text1,DOWN).set_opacity(0).set_z_index(1)
#         Text3=MathTex(r"\text{the section formed is a parabola.}").scale(0.8).next_to(Text2,DOWN).set_opacity(0).set_z_index(1)
#         Text4 = MathTex(r"\text{If the angle formed by the plane with the vertical axis of the cone }").scale(0.8).to_edge(UP).set_opacity(0)
#         Text5 = MathTex(r"\text{is greater than the semi-vertical angle of the cone (}\theta\text{),}").scale(0.8).next_to(Text4, DOWN).set_opacity(0)
#         Text6 = MathTex(r"\text{the section formed is an ellipse.}").scale(0.8).next_to(Text5, DOWN).set_opacity(0)
#         Text7 = MathTex(r"\text{If the angle formed by the plane with the vertical axis of a conjoint double}").scale(0.8).to_edge(UP).set_opacity(0)
#         Text8 = MathTex(r"\text{right cone is less than the semi-vertical angle of the cone}").scale(0.8).next_to(Text7, DOWN).set_opacity(0)
#         Text9 = MathTex(r"\text{(}\theta\text{), the section formed is a hyperbola.}").scale(0.8).next_to(Text8, DOWN).set_opacity(0)
#         self.add_fixed_in_frame_mobjects(Text1,Text2,Text3,Text4,Text5,Text6,Text7,Text8,Text9)
#         self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES)
#         self.add(cone1,cone2,NameLabel)
#         self.add(axes)
#         a = ValueTracker(-2) 
#         k=ValueTracker(2)
#         plane1=always_redraw(lambda: Surface(
#             lambda u, v: axes.c2p(u, v, k.get_value()*v + a.get_value()),
#             u_range=[-3, 3],
#             v_range=[-8/np.sqrt(1+k.get_value()**2), 8/np.sqrt(1+k.get_value()**2)],
#             resolution=(1, 1),   
#             fill_opacity=0.2,
#             stroke_opacity=1,
#             stroke_width=4,
#             shade_in_3d=False).set_color(YELLOW).set_stroke(YELLOW, width=4))
#         line1=Line(start=cone2.get_top(),end=(cone2.get_bottom()+LEFT*2)).shift(DOWN*2)
#         line2=Line(start=cone2.get_top(),end=cone2.get_bottom()).shift(DOWN*2).set_z_index(1)
#         theta=ParametricFunction(lambda t: axes.c2p(np.cos(t),np.sin(t)),t_range=[-117*DEGREES,-90*DEGREES],color=YELLOW)
#         theta_label=MathTex(r"\theta",color=YELLOW).scale(0.8).next_to(theta,DOWN).shift(0.1*LEFT)
#         def param_curve(t):
#             c = k.get_value()
#             y = t
#             z = c * y + a.get_value()
#             x = np.sqrt((1/4) * z**2 - y**2) if (1/4)*z**2 - y**2 >= 0 else 0
#             return np.array([x, y, z])
#         def param_curve2(t):
#             c = k.get_value()
#             y = t
#             z = c * y + a.get_value()
#             x = -np.sqrt((1/4) * z**2 - y**2) if (1/4)*z**2 - y**2 >= 0 else 0
#             return np.array([x, y, z])
#         curve1=always_redraw(
#             lambda: ParametricFunction(lambda t:
#                 param_curve(t),
#                 t_range=[-2, 1.7],
#                 color=YELLOW,
#                 stroke_width=4
#             )
#         )
#         curve2 = always_redraw(
#             lambda: ParametricFunction(lambda t:
#                 param_curve2(t),
#                 t_range=[-2, 1.7],
#                 color=YELLOW,
#                 stroke_width=4
#             )
#         )
#         curve=VGroup(curve1,curve2)
#         alpha_line_1=always_redraw(lambda: Line(start=plane1.get_edge_center(UP+OUT),end=plane1.get_edge_center(DOWN+IN)).set_z_index(1))
#         alpha=always_redraw(lambda: ParametricFunction(lambda t: axes.c2p(0,np.cos(t),np.sin(t)+a.get_value()),t_range=[-PI+np.arctan(k.get_value()),-90*DEGREES],color=YELLOW))
#         fixed_mobs=Group(line1.set_opacity(0),line2.set_opacity(0),theta.set_opacity(0),theta_label.set_opacity(0))
#         self.add_fixed_in_frame_mobjects(fixed_mobs)
#         self.play(fixed_mobs[0].animate.set_opacity(1),fixed_mobs[1].animate.set_opacity(1))
#         self.play(Wait(1))
#         self.play(fixed_mobs[2].animate.set_opacity(1),fixed_mobs[3].animate.set_opacity(1))
#         self.play(FadeIn(plane1),FadeIn(curve),FadeIn(alpha_line_1))
#         self.play(Wait(0.8))
#         self.play(Create(alpha))
#         self.play(Wait(1))
#         fade_out_group=Group(alpha,line1,line2,theta,theta_label)
#         self.play(Text1.animate.set_opacity(1))
#         self.play(Wait(0.8))
#         self.play(Text2.animate.set_opacity(1))
#         self.play(Wait(0.8))
#         self.play(Text3.animate.set_opacity(1)) 
#         self.play(Wait(1))
#         self.play(FadeOut(Text1),FadeOut(Text2),FadeOut(Text3))
#         self.play(FadeOut(fade_out_group))
#         self.play(Wait(1))
#         self.move_camera(phi=65*DEGREES,theta=30*DEGREES,run_time=2)
#         self.play(Wait(0.7))
#         self.move_camera(phi=90*DEGREES,theta=0,run_time=2)
#         self.play(FadeIn(fade_out_group))
#         self.play(Text4.animate.set_opacity(1))
#         self.play(Wait(0.8))
#         self.play(Text5.animate.set_opacity(1))
#         self.play(Wait(0.8))
#         self.play(Text6.animate.set_opacity(1))
#         self.play(Wait(1))
#         self.play(k.animate.set_value(0.5),run_time=3)
#         self.play(FadeOut(fade_out_group))
#         self.play(Wait(0.5))
#         self.move_camera(phi=65*DEGREES,theta=30*DEGREES,run_time=2)
#         self.play(Wait(0.7))
#         self.play(FadeOut(Text4),FadeOut(Text5),FadeOut(Text6))
#         self.move_camera(phi=90*DEGREES,theta=0,run_time=2)
#         self.play(FadeIn(fade_out_group))
#         self.play(Text7.animate.set_opacity(1))
#         self.play(Wait(0.8))
#         self.play(Text8.animate.set_opacity(1))
#         self.play(Wait(0.8))
#         self.play(Text9.animate.set_opacity(1))
#         self.play(Wait(1))
#         self.play(k.animate.set_value(10),run_time=4)
#         self.play(FadeOut(fade_out_group))
#         self.play(Wait(0.5))
#         self.move_camera(phi=65*DEGREES,theta=30*DEGREES,run_time=2)
#         self.play(Wait(0.7))
#         self.play(FadeOut(Text7),FadeOut(Text8),FadeOut(Text9))
#         self.move_camera(phi=90*DEGREES,theta=0,run_time=2)
#         self.play(Wait(0.6))
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=NameLabel])
#         self.play(Wait(1))

# class CircularGeometry1(Scene):
#     def construct(self):
#         Topic=MathTex(r"\mathbf{Circles}")
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         self.add(NameLabel)
#         self.play(Write(Topic))
#         self.play(Topic.animate.to_edge(UP))
#         self.play(Wait(1))
#         k=ValueTracker(0)
#         Plane1 = always_redraw(lambda: NumberPlane(x_range=[-5+k.get_value(),5+k.get_value()],y_range=[-5+k.get_value(),5+k.get_value()]).scale(0.6).to_edge(LEFT))
#         background_rectangle=Rectangle(width=Plane1.height,height=Plane1.height,color=YELLOW,fill_opacity=0).move_to(Plane1.get_center())
#         y_label=MathTex(r"y").scale(0.9).move_to(Plane1.c2p(0.5,4.5))
#         x_label=MathTex(r"x").scale(0.9).move_to(Plane1.c2p(4.5,-0.5))
#         Plane1_Stuff=VGroup(background_rectangle,y_label,x_label).to_edge(LEFT)
#         self.play(FadeIn(Plane1),FadeIn(background_rectangle))
#         self.play(Write(x_label),Write(y_label))
#         theta=ValueTracker(45)
#         O=Dot(Plane1.c2p(0,0),color=GRAY)
#         A=always_redraw(lambda: Dot(Plane1.c2p(3*np.cos(theta.get_value()*DEGREES),3*np.sin(theta.get_value()*DEGREES)),color=BLUE))
#         B=always_redraw(lambda: Dot(Plane1.c2p(3*np.cos(theta.get_value()*DEGREES),0),color=BLUE))
#         A_label = always_redraw(lambda: MathTex("A").next_to(A, RIGHT, buff=0.1))
#         B_label = always_redraw(lambda: MathTex("B").next_to(B, DOWN, buff=0.1))
#         O_label = MathTex("O").next_to(O, DL,buff=-0.0005)
#         A.set_z_index(2)
#         B.set_z_index(2)
#         O.set_z_index(2)
#         triangle = always_redraw(lambda: Polygon(
#             (Plane1.c2p(0,0)),
#             (Plane1.c2p(3*np.cos(theta.get_value()*DEGREES),3*np.sin(theta.get_value()*DEGREES))),
#             (Plane1.c2p(3*np.cos(theta.get_value()*DEGREES),0)),
#             color=YELLOW,
#             fill_opacity=0.5))
#         y_coord_label=always_redraw(lambda: MathTex(r"y").scale(0.8).move_to(triangle.get_right()+0.2*RIGHT))
#         x_coord_label=always_redraw(lambda: MathTex(r"x").scale(0.8).move_to(triangle.get_bottom()+0.2*DOWN))
#         self.play(Wait(0.5))
#         self.play(Create(O),Write(O_label))
#         Text1=MathTex(r"\mathrm{Let\;}A(x, y)\mathrm{\;be\;a\;point\;in\;the\;Cartesian\;plane.}").scale(0.7).next_to(Plane1,RIGHT).to_edge(UP).shift(DOWN)
#         Text2=MathTex(r"\mathrm{The\;distance\;from\;the\;origin\;to\;A\;is\;equal\;to}").scale(0.7).next_to(Text1,DOWN).align_to(Text1,LEFT)
#         Text3=MathTex(r"\mathrm{the\;length\;of\;the\;hypotenuse\;OA\;of\;right\;} \Delta OAB.").scale(0.7).next_to(Text2,DOWN).align_to(Text1,LEFT)
#         self.play(AnimationGroup(Write(Text1),Create(A),Write(A_label),Create(B),Write(B_label),Write(Text2),Write(Text3),DrawBorderThenFill(triangle),lag_ratio=1))
#         self.play(Write(x_coord_label),Write(y_coord_label))
#         radius = always_redraw(lambda: Line(O.get_center(), A.get_center()))
#         radius_label = always_redraw(lambda: MathTex(r"r",color=YELLOW).scale(0.8).rotate(theta.get_value()*DEGREES).move_to(Plane1.c2p(1.5 * np.cos(theta.get_value() * DEGREES+17*DEGREES), 1.5 * np.sin(theta.get_value() * DEGREES+17*DEGREES))))
#         self.play(Write(radius_label))
#         self.play(Wait(1))
#         Text4=MathTex(r"\mathrm{Now,\;consider\;all\;points\;that\;are\;the\;same}").scale(0.7).next_to(Text3,DOWN).align_to(Text1,LEFT)
#         Text5=MathTex(r"\mathrm{distance\;away\;from\;the\;origin.}").scale(0.7).next_to(Text4,DOWN).align_to(Text1,LEFT)
#         self.play(Write(Text4))
#         self.play(Write(Text5))
#         path = TracedPath(A.get_center, stroke_color=PURPLE_A, stroke_width=4)
#         self.add(path)
#         self.play(theta.animate.set_value(405),run_time=8,rate_func=linear)
#         self.play(Wait(0.5))
#         Texts=Group(Text1,Text2,Text3,Text4,Text5)
#         self.play(FadeOut(Texts))
#         Text6=MathTex(r"\mathrm{The\;path\;traced\;by\;point\;A\;is\;called\;a\;locus.}").scale(0.7).next_to(Plane1,RIGHT).to_edge(UP).shift(DOWN)
#         self.play(Write(Text6))
#         self.play(Wait(0.5))
#         self.play(FadeOut(Text6))
#         self.play(Wait(0.5))
#         Text7=MathTex(r"\mathrm{A\;circle\;is\;a\;locus\;of\;points\;that\;are\;equidistant}").scale(0.7).next_to(Plane1,RIGHT).to_edge(UP).shift(DOWN)
#         Text8=MathTex(r"\mathrm{from\;a\;fixed\;point,\;called\;its\;center.}").scale(0.7).next_to(Text7,DOWN).align_to(Text1,LEFT)
#         self.play(Write(Text7))
#         self.play(Write(Text8))
#         self.play(Wait(0.5))
#         self.play(FadeOut(Text7),FadeOut(Text8))
#         Text9=MathTex(r"\text{Using the Pythagorean theorem, we have}").scale(0.7).next_to(Plane1,RIGHT).to_edge(UP).shift(DOWN)
#         Text10=MathTex(r"x^2 + y^2 = r^2\; \text{where } r \text{ is a constant." ).scale(0.7).next_to(Text9,DOWN).align_to(Text9,LEFT)
#         Text11=MathTex(r"\text{This is the equation of a circle of radius }r").scale(0.7).next_to(Text10,DOWN).align_to(Text9,LEFT)
#         Text12=MathTex(r"\text{ centered at (0,0).}").scale(0.7).next_to(Text11,DOWN).align_to(Text9,LEFT)
#         self.play(Write(Text9))
#         self.play(Write(Text10))
#         self.play(Write(Text11))
#         self.play(Write(Text12))
#         self.wait(1)
#         Textz=Group(Text9,Text10,Text11,Text12)
#         self.play(FadeOut(Textz))
#         fade_out_stuff=Group(radius_label,x_coord_label,y_coord_label,A,B,O,triangle,path,O_label,A_label,B_label)
#         self.play(FadeOut(fade_out_stuff))
#         self.play(k.animate.set_value(4),x_label.animate.shift(0.6*4*DOWN),y_label.animate.shift(4*0.6*LEFT),run_time=3)
#         self.play(Wait(0.5))

# class CircularGeometry2(Scene):
#     def construct(self):
#         Topic=MathTex(r"\mathbf{Circles}").to_edge(UP)
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         k=ValueTracker(4)
#         Plane1 = always_redraw(lambda: NumberPlane(x_range=[-5+k.get_value(),5+k.get_value()],y_range=[-5+k.get_value(),5+k.get_value()]).scale(0.6).to_edge(LEFT))
#         background_rectangle=Rectangle(width=Plane1.height,height=Plane1.height,color=YELLOW,fill_opacity=0).move_to(Plane1.
#         get_center())
#         background_rectangle.set_z_index(1)
#         y_label=MathTex(r"y").scale(0.9).move_to(Plane1.c2p(0.5,8.5))
#         x_label=MathTex(r"x").scale(0.9).move_to(Plane1.c2p(8.5,-0.5))
#         Plane1_Stuff=VGroup(background_rectangle,y_label,x_label).to_edge(LEFT)
#         self.add(NameLabel,Topic,Plane1_Stuff,Plane1)
#         Circ=ParametricFunction(lambda t: Plane1.c2p(3*np.cos(t)+4,3*np.sin(t)+4),t_range=[0,2*PI],color=PURPLE)
#         A=Dot(Plane1.c2p(3*np.cos(PI/4)+4,3*np.sin(PI/4)+4),color=BLUE)
#         C=Dot(Plane1.c2p(4,4),color=BLUE)
#         A.set_z_index(1)
#         C.set_z_index(1)
#         radius=Line(start=Plane1.c2p(4,4),end=Plane1.c2p(3*np.cos(PI/4)+4,3*np.sin(PI/4)+4),color=WHITE)
#         Center_tex=MathTex(r"C(h,k)").scale(0.8).next_to(C,DOWN)
#         self.play(Wait(1.2))
#         A_tex=MathTex(r"A(x,y)").scale(0.8).move_to(Plane1.c2p(7,7))
#         self.play(Create(Circ),run_time=2)
#         self.play(Wait(0.5))
#         self.play(Create(C),Write(Center_tex),run_time=2)
#         self.play(Create(A),Write(A_tex),run_time=2)
#         self.play(Wait(0.8))
#         self.play(Create(radius))
#         Text1=MathTex(r"\mathrm{Similarly,\;for\;a\;circle\;centered\;at\;}C(h,k),").scale(0.7).next_to(Plane1,RIGHT).to_edge(UP).shift(DOWN)
#         Text2=MathTex(r"\mathrm{we\;can\;use\;the\;distance\;formula\;to\;deduce\;the}").scale(0.7).next_to(Text1,DOWN).align_to(Text1,LEFT)
#         Text3=MathTex(r"\mathrm{equation\;of\;the\;circle\;to\;be:}").scale(0.7).next_to(Text2,DOWN).align_to(Text1,LEFT)
#         Text4=MathTex(r"(x-h)^2 + (y-k)^2 = r^2").scale(0.7).next_to(Text3,DOWN).align_to(Text1,LEFT)
#         self.play(Write(Text1))
#         self.play(Write(Text2))
#         self.play(Write(Text3))
#         self.play(Write(Text4))
#         fade_group = Group(*[mob for mob in self.mobjects if mob not in [Topic, NameLabel]])
#         self.play(Wait(1.5))
#         self.play(FadeOut(fade_group))

# class CircularGeometry3(Scene):
#     def construct(self):
#         Topic=MathTex(r"\mathbf{Circles}").to_edge(UP)
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         SubTopic=MathTex(r"\text{Special Cases}").scale(0.8)
#         Plane1 = NumberPlane(x_range=[-1,9],y_range=[-1,9]).scale(0.6).move_to(ORIGIN+2*LEFT)
#         y_label=MathTex(r"y").scale(0.9).move_to(Plane1.c2p(0.5,8.5))
#         x_label=MathTex(r"x").scale(0.9).move_to(Plane1.c2p(8.5,-0.5))
#         xaxisline=Line(start=Plane1.c2p(-1,0,0),end=Plane1.c2p(9,0,0),color=WHITE,stroke_width=4)
#         yaxisline=Line(start=Plane1.c2p(0,-1,0),end=Plane1.c2p(0,9,0),color=WHITE,stroke_width=4)
#         axeslines=Group(xaxisline,yaxisline)
#         background_rectangle1=Rectangle(width=Plane1.height,height=Plane1.height,color=YELLOW,fill_opacity=0).set_z_index(1).move_to(Plane1.get_center())
#         Circ1=ParametricFunction(lambda t: Plane1.c2p(3*np.cos(t)+3,3*np.sin(t)+4),t_range=[0,2*PI],color=PURPLE)
#         Plane1_Stuff=VGroup(background_rectangle1,Plane1,Circ1).scale(0.2).next_to(Topic,DOWN,buff=1).to_edge(LEFT)
#         Plane3 = NumberPlane(x_range=[-1,9],y_range=[-1,9]).scale(0.6).move_to(ORIGIN+2*LEFT)
#         background_rectangle3=Rectangle(width=Plane3.height,height=Plane3.height,color=YELLOW,fill_opacity=0).set_z_index(1).move_to(Plane3.get_center())
#         Circ3=ParametricFunction(lambda t: Plane3.c2p(3*np.cos(t)+3,3*np.sin(t)+3),t_range=[0,2*PI],color=PURPLE)
#         Plane3_Stuff=VGroup(background_rectangle3,Plane3,Circ3).scale(0.2).next_to(NameLabel,UP,buff=1).to_edge(LEFT)
#         Plane2 = NumberPlane(x_range=[-1,9],y_range=[-1,9]).scale(0.6).move_to(ORIGIN+2*LEFT)
#         background_rectangle2=Rectangle(width=Plane2.height,height=Plane2.height,color=YELLOW,fill_opacity=0).set_z_index(1).move_to(Plane2.get_center())
#         Circ2=ParametricFunction(lambda t: Plane2.c2p(3*np.cos(t)+4,3*np.sin(t)+3),t_range=[0,2*PI],color=PURPLE)
#         Plane2_Stuff=VGroup(background_rectangle2,Plane2,Circ2).scale(0.2).move_to((Plane1.get_center()+Plane3.get_center())/2)
#         self.add(NameLabel,Topic)
#         self.play(Write(SubTopic))
#         self.play(Wait(1))
#         self.play(Indicate(SubTopic))
#         self.play(FadeOut(SubTopic))
#         self.play(FadeIn(Plane1_Stuff))
#         self.play(FadeIn(Plane2_Stuff))
#         self.play(FadeIn(Plane3_Stuff))
#         Case1=MathTex(r"\text{Equation of a circle touching the }y\text{ axis}").scale(0.7)
#         Case2=MathTex(r"\text{Equation of a circle touching the }x\text{ axis}").scale(0.7)
#         Case3=MathTex(r"\text{Equation of a circle touching both axes").scale(0.7)
#         self.play(Write(Case1))
#         self.play(Indicate(Plane1_Stuff))
#         self.play(FadeOut(Case1))
#         self.play(Plane1_Stuff.animate.scale(5).move_to(ORIGIN+2*LEFT))
#         center1=Dot(color=RED).move_to(Circ1.get_center()).set_z_index(1)
#         center_text_1=MathTex(r"C(h,k)").scale(0.8).next_to(center1,RIGHT)
#         radius1=Line(start=Plane1.c2p(0,4),end=Plane1.c2p(3,4),stroke_width=4,color=GRAY)
#         radius1_label=MathTex(r"r=h").scale(0.8).next_to(radius1,UP)
#         radius2=Line(start=Plane1.c2p(4,0),end=Plane1.c2p(4,3),stroke_width=4,color=GRAY)
#         radius2_label=MathTex(r"r=k").scale(0.8).next_to(radius2,RIGHT)
#         radius3A=Line(start=Plane1.c2p(0,3),end=Plane1.c2p(3,3),stroke_width=4,color=GRAY)
#         radius3B=Line(start=Plane1.c2p(3,0),end=Plane1.c2p(3,3),stroke_width=4,color=GRAY)
#         radius3_label=MathTex(r"r=k=h").scale(0.8).next_to(radius3A,UP)
#         self.play(Write(x_label),Write(y_label),FadeIn(axeslines))
#         self.play(Create(center1))
#         self.play(Write(center_text_1))
#         self.play(GrowFromEdge(radius1,RIGHT))
#         self.play(Write(radius1_label))
#         Atext1=MathTex(r"(x-h)^2+(y-k)^2=r^2").scale(0.8)
#         Atext1.next_to(Plane1_Stuff, RIGHT, buff=0.7).shift(UP*1.5)
#         Atext2=MathTex(r"\Rightarrow(x-h)^2+(y-k)^2=h^2").scale(0.8).next_to(Atext1,DOWN).align_to(Atext1, LEFT)
#         Atext2.next_to(Atext1, DOWN, buff=0.3).align_to(Atext1, LEFT)
#         Btext1 = MathTex(r"(x-h)^2+(y-k)^2=r^2").scale(0.8)
#         Btext1.next_to(Plane1_Stuff, RIGHT, buff=0.7).shift(UP*1.5)
#         Btext2 = MathTex(r"\Rightarrow(x-h)^2+(y-k)^2=k^2").scale(0.8).next_to(Btext1,DOWN).align_to(Atext1, LEFT)
#         Btext2.next_to(Btext1, DOWN, buff=0.3).align_to(Btext1, LEFT)
#         Ctext1 = MathTex(r"(x-h)^2+(y-k)^2=r^2").scale(0.8)
#         Ctext1.next_to(Plane1_Stuff, RIGHT, buff=0.7).shift(UP*1.5)
#         Ctext2 = MathTex(r"\Rightarrow(x-h)^2+(y-h)^2=h^2").scale(0.8).next_to(Ctext1,DOWN).align_to(Atext1, LEFT)
#         Ctext2.next_to(Ctext1, DOWN, buff=0.3).align_to(Ctext1, LEFT)
#         self.play(Write(Atext1))
#         self.play(Write(Atext2))
#         self.play(Wait(1.5))
#         self.play(FadeOut(Atext1), FadeOut(Atext2))
#         Plane1_Stuff.add(center1, radius1, radius1_label)  
#         self.play(
#             FadeOut(x_label),
#             FadeOut(y_label),
#             FadeOut(axeslines),
#             FadeOut(center_text_1)
#         )
#         self.play(
#             Plane1_Stuff.animate.scale(0.2).next_to(Topic,DOWN,buff=1).to_edge(LEFT)
#         )
#         self.play(Write(Case2))
#         self.play(Indicate(Plane2_Stuff))
#         self.play(FadeOut(Case2))
#         self.play(Plane2_Stuff.animate.scale(5).move_to(ORIGIN+2*LEFT))
#         center2=Dot(color=RED).move_to(Circ2.get_center()).set_z_index(1)
#         center_text_1.next_to(center2,RIGHT)
#         radius2=Line(start=Plane2.c2p(4,0),end=Plane2.c2p(4,3),stroke_width=4,color=GRAY)
#         radius2_label=MathTex(r"r=k").scale(0.8).next_to(radius2,RIGHT)
#         self.play(Write(x_label),Write(y_label),FadeIn(axeslines))
#         self.play(Create(center2))
#         self.play(Write(center_text_1))
#         self.play(GrowFromEdge(radius2,UP))
#         self.play(Write(radius2_label))
#         self.play(Write(Btext1))
#         self.play(Write(Btext2))
#         self.play(Wait(1.5))
#         self.play(FadeOut(Btext1), FadeOut(Btext2))
#         Plane2_Stuff.add(center2, radius2, radius2_label)  
#         self.play(
#             FadeOut(x_label),
#             FadeOut(y_label),
#             FadeOut(axeslines),
#             FadeOut(center_text_1)
#         )
#         self.play(
#             Plane2_Stuff.animate.scale(0.2).move_to((Plane1.get_center()+Plane3.get_center())/2)
#         )
#         self.play(Write(Case3))
#         self.play(Indicate(Plane3_Stuff))
#         self.play(FadeOut(Case3))
#         self.play(Plane3_Stuff.animate.scale(5).move_to(ORIGIN+2*LEFT))
#         center3=Dot(color=RED).move_to(Circ3.get_center()).set_z_index(1)
#         center_text_2=MathTex(r"C(h,h)").scale(0.8).next_to(center3,RIGHT)
#         radius3A=Line(start=Plane3.c2p(0,3),end=Plane3.c2p(3,3),stroke_width=4,color=GRAY)
#         radius3B=Line(start=Plane3.c2p(3,0),end=Plane3.c2p(3,3),stroke_width=4,color=GRAY)
#         radius3_label=MathTex(r"r=k=h").scale(0.8).next_to(radius3A,UP).shift(RIGHT*0.1)
#         self.play(Write(x_label),Write(y_label),FadeIn(axeslines))
#         self.play(Create(center3))
#         self.play(Write(center_text_2))
#         self.play(GrowFromEdge(radius3A,RIGHT))
#         self.play(GrowFromEdge(radius3B,UP))
#         self.play(Write(radius3_label))
#         self.play(Write(Ctext1))
#         self.play(Write(Ctext2))
#         self.play(Wait(1.5))
#         self.play(FadeOut(Ctext1), FadeOut(Ctext2))
#         Plane3_Stuff.add(center3, radius3A, radius3B, radius3_label)  
#         self.play(
#             FadeOut(x_label),
#             FadeOut(y_label),
#             FadeOut(axeslines),
#             FadeOut(center_text_2)
#         )
#         self.play(
#             Plane3_Stuff.animate.scale(0.2).next_to(NameLabel,UP,buff=1).to_edge(LEFT)
#         )
#         self.play(Wait(2))
#         self.play(FadeOut(Group(*[mobject for mobject in self.mobjects if mobject!=NameLabel and mobject!=Topic])))

# class CircularGeometry4(Scene):
#     def construct(self):
#         Topic=MathTex(r"\mathbf{Circles}").to_edge(UP)
#         NameLabel=Tex("Created by Himalaya Satyal",font_size=30).to_corner(DL)
#         self.add(NameLabel,Topic)
#         k=ValueTracker(4)
#         Plane1 = NumberPlane(x_range=[-5+k.get_value(),5+k.get_value()],y_range=[-5+k.get_value(),5+k.get_value()]).scale(0.6).to_edge(LEFT).set_z_index(-1)
#         O_tex=MathTex(r"O").scale(0.9).move_to(Plane1.c2p(-0.5,-0.5))
#         background_rectangle=Rectangle(width=Plane1.height,height=Plane1.height,color=YELLOW,fill_opacity=0).move_to(Plane1.
#         get_center())
#         background_rectangle.set_z_index(1)
#         y_label=MathTex(r"y").scale(0.9).move_to(Plane1.c2p(-0.5,8.5))
#         x_label=MathTex(r"x").scale(0.9).move_to(Plane1.c2p(8.5,-0.5))
#         Plane1_Stuff=VGroup(background_rectangle,y_label,x_label).to_edge(LEFT)
#         Circ=ParametricFunction(lambda t: Plane1.c2p(3*np.cos(t)+4,3*np.sin(t)+4),t_range=[0,2*PI],color=PURPLE)
#         C=Dot(Plane1.c2p(4,4),color=BLUE)
#         C.set_z_index(1)
#         radius=Line(start=Plane1.c2p(4,4),end=Plane1.c2p(3*np.cos(PI/4)+4,3*np.sin(PI/4)+4),color=WHITE)
#         Center_tex=MathTex(r"C(h,k)").scale(0.8).next_to(C,DOWN)
#         self.play(Wait(1.2))
#         r_tex=MathTex(r"r").scale(0.8).move_to(radius.get_center()+UL*0.6*0.3)
#         r_tex.rotate(angle=45*DEGREES,about_point=r_tex.get_center())
#         self.play(FadeIn(Group(radius,Center_tex,Circ,C,r_tex,Plane1_Stuff,Plane1,O_tex)))
#         Text1=MathTex(r"(x-h)^2+(y-k)^2=r^2",color=RED_C).scale(0.7).next_to(Plane1,RIGHT).to_edge(UP).shift(DOWN*0.7+LEFT*0.08)
#         Text2=MathTex(r"\Rightarrow x^2+y^2-2hx-2ky+(h^2+k^2-r^2)=0").scale(0.7).next_to(Text1,DOWN).align_to(Text1,LEFT)
#         Text3=MathTex(r"\text{This is in the form, }x^2+y^2+2gx+2fy+c=0.",color=GOLD).scale(0.7).next_to(Text2,DOWN).align_to(Text1,LEFT)
#         Text4=MathTex(r"2g=-2h").scale(0.7).next_to(Text3,DOWN).align_to(Text1,LEFT)
#         Text4s=MathTex(r"\therefore h=-g",color=BLUE_B).scale(0.7).next_to(Text3,DOWN).align_to(Text1,LEFT)
#         Text5=MathTex(r"2f=-2k").scale(0.7).next_to(Text4s,DOWN).align_to(Text1,LEFT)
#         Text5s=MathTex(r"\therefore k=-f",color=BLUE_B).scale(0.7).next_to(Text4s,DOWN).align_to(Text1,LEFT)
#         Text6=MathTex(r"c=h^2+k^2-r^2").scale(0.7).next_to(Text5s,DOWN).align_to(Text1,LEFT)
#         Text6s=MathTex(r"\therefore r=\sqrt{h^2+k^2-c}.",color=BLUE_B).scale(0.7).next_to(Text5s,DOWN).align_to(Text1,LEFT)
#         Texty1=Tex("So, if the equation of a circle is given in the").scale(0.7).next_to(Text6s,DOWN).align_to(Text1,LEFT)
#         Texty2=Tex("general form, its center is ","$(-g,-f)$"," and its").scale(0.7).next_to(Texty1,DOWN).align_to(Text1,LEFT)
#         Texty3=Tex("radius is ","$\sqrt{g^2+f^2-c}$"," .").scale(0.7).next_to(Texty2,DOWN).align_to(Text1,LEFT)
#         Texty2[1].set_color(GOLD_D)
#         Texty3[1].set_color(GOLD_D)
#         self.play(Write(Text1))
#         self.play(Wait(1))
#         self.play(Write(Text2))
#         self.play(Wait(1))
#         self.play(Write(Text3)) 
#         self.play(Wait(1))
#         self.play(Write(Text4))
#         self.play(Wait(1))
#         self.play(TransformMatchingShapes(Text4,Text4s))
#         self.play(Wait(1))
#         self.play(Write(Text5))
#         self.play(Wait(1))
#         self.play(TransformMatchingShapes(Text5,Text5s))
#         self.play(Wait(1))
#         self.play(Write(Text6))
#         self.play(Wait(1))
#         self.play(TransformMatchingShapes(Text6,Text6s))
#         self.play(Wait(1))
#         self.play(Write(Texty1))
#         self.play(Write(Texty2))
#         self.play(Write(Texty3))

#         fade_group = Group(*[mob for mob in self.mobjects if mob not in [Topic, NameLabel]])
#         self.play(Wait(2))
#         self.play(FadeOut(fade_group))

# class CircularGeometry5(Scene):
#     def construct(self):
#         theta=ValueTracker(270)
#         alpha=ValueTracker(90)
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Topic1 = MathTex(r"\textbf{Circles}").to_edge(UP)
#         Topic2 = MathTex(r"\textbf{Equation of a circle in its diameter form}",color=GOLD).scale(0.7).next_to(Topic1,DOWN).to_edge(RIGHT)
#         self.add(NameLabel,Topic1)
#         h=ValueTracker(4)
#         k=ValueTracker(4)
#         r=ValueTracker(3)
#         m=ValueTracker(-1)
#         n=ValueTracker(9)
#         def f(t):
#             return max(-1,min(9,r.get_value()*np.cos(t)+h.get_value()))
#         def g(t):
#             return max(m.get_value(),min(n.get_value(),r.get_value()*np.sin(t)+k.get_value()))
#         Plane1 = NumberPlane( 
#             x_range=[-1,9],
#             y_range=[m.get_value(),n.get_value()],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": DL},
#             x_axis_config={"label_direction": DL}
#         ).scale(0.6).to_edge(LEFT)
#         O_tex=MathTex(r"O").move_to(Plane1.c2p(-0.5,-0.5)).scale(0.9)
#         Circ=always_redraw(lambda: ParametricFunction(lambda t: Plane1.c2p(f(t),g(t)),t_range=[0,2*PI],color=PURPLE))
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height , color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         self.play(FadeIn(*[y_label,x_label,background_rectangle,Plane1,O_tex]))
#         self.play(Write(Topic2),run_time=2.5)
#         self.play(Wait(0.5))
#         A=Dot(color=GRAY_C,point=Plane1.c2p(7,4)).set_z_index(1)
#         B=Dot(color=GRAY_C,point=Plane1.c2p(1,4)).set_z_index(1)
#         t=ValueTracker(30)
#         C=always_redraw(lambda: Dot(color=RED,point=Plane1.c2p(f(t.get_value()*DEGREES),g(t.get_value()*DEGREES))).set_z_index(1))
#         A_tex=MathTex(r"A(x_1,y_1)").scale(0.6).next_to(A,DOWN).set_z_index(1)
#         B_tex=MathTex(r"B(x_2,y_2)").scale(0.6).next_to(B,DOWN).set_z_index(1)
#         C_tex=always_redraw(lambda: MathTex(r"C(x,y)").scale(0.6).next_to(C,UP)).set_z_index(1)
#         triangle=always_redraw(lambda: Polygon(
#             (Plane1.c2p(7,4)),
#             (Plane1.c2p(1,4)),
#             (Plane1.c2p(f(t.get_value()*DEGREES),g(t.get_value()*DEGREES))),
#             color=BLUE_B,
#             fill_opacity=0))
#         self.play(Wait(1))
#         self.play(GrowFromCenter(A),Write(A_tex))
#         self.play(GrowFromCenter(B),Write(B_tex))
#         self.play(GrowFromCenter(C),Write(C_tex))
#         self.play(Create(Circ),run_time=2)
#         self.play(Wait(0.5))
#         self.play(FadeIn(triangle),run_time=1.5)
#         i=ValueTracker(0)
#         j=ValueTracker(0)
#         i.add_updater(lambda m: m.set_value(1/np.sqrt((7-f(t.get_value()*DEGREES))**2+(4-g(t.get_value()*DEGREES))**2)))
#         j.add_updater(lambda m: m.set_value(1/np.sqrt((1-f(t.get_value()*DEGREES))**2+(4-g(t.get_value()*DEGREES))**2)))
#         self.wait(2)
#         def right_angle_marker(A, B, C, size=0.3, color=YELLOW):
#             v1 = (A - C) / np.linalg.norm(A - C)
#             v2 = (B - C) / np.linalg.norm(B - C)
#             v1 = v1 * size
#             v2 = v2 * size
#             return Polygon(
#                 C + v1,
#                 C + v1 + v2,
#                 C + v2,
#                 C,
#                 color=color,
#                 fill_opacity=0.3
#             )
#         perp_angle = always_redraw(lambda: right_angle_marker(
#             Plane1.c2p(7, 4),
#             Plane1.c2p(1, 4),
#             Plane1.c2p(f(t.get_value()*DEGREES), g(t.get_value()*DEGREES)),
#             size=0.3,
#             color=YELLOW
#         ))
#         self.play(FadeIn(perp_angle))   
#         self.wait(1)
#         self.play(t.animate.set_value(10),run_time=2)
#         self.play(t.animate.set_value(135),run_time=3)
#         self.play(Wait(0.5))
#         self.play(t.animate.set_value(60),run_time=3)
#         t1 = MathTex(r"\text{Diametrically Opposite End-Points:",color=BLUE_B).scale(0.7).next_to(background_rectangle, RIGHT).shift(UP*2.2)
#         t2 = MathTex(r"A(x_1,y_1)\text{ and }B(x_2,y_2)",color=BLUE_B).scale(0.7).next_to(t1, DOWN).align_to(t1, LEFT)
#         t3 = MathTex(r"m_{AC}=\frac{y-y_1}{x-x_1}").scale(0.7).next_to(t2, DOWN).align_to(t1, LEFT)
#         t4 = MathTex(r"m_{BC}=\frac{y-y_2}{x-x_2}").scale(0.7).next_to(t3, DOWN).align_to(t1, LEFT)
#         t5 = MathTex(r"m_{AC}=-\frac{1}{m_{BC}}\;[\,\because \angle ACB=90^{\circ}\,]").scale(0.7).next_to(t4, DOWN).align_to(t1, LEFT)
#         t6 = MathTex(r"\Rightarrow\frac{y-y_1}{x-x_1}=-\frac{x-x_2}{y-y_2}").scale(0.7).next_to(t5, DOWN).align_to(t1, LEFT)
#         t7 = MathTex(r"\Rightarrow (y-y_1)(y-y_2)=-(x-x_1)(x-x_2)").scale(0.7).next_to(t6, DOWN).align_to(t1, LEFT)
#         t8 = MathTex(r"\therefore(x-x_1)(x-x_2)+(y-y_1)(y-y_2)=0", color=GOLD).scale(0.7).next_to(t7, DOWN).align_to(t1, LEFT)
#         self.wait(1)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t2))
#         self.wait(1)
#         self.play(Write(t3))
#         self.wait(1)
#         self.play(Write(t4))
#         self.wait(1)
#         self.play(Write(t5))
#         self.wait(1)
#         self.play(Write(t6))
#         self.wait(1)
#         self.play(Write(t7))
#         self.wait(1)
#         self.play(Write(t8))
#         self.wait(2)
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [NameLabel]])

# class NameLabelEnter(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         self.play(Write(NameLabel))

# class CircPractice1(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{1. Find the equation of the circle with center $(3,5)$ and radius $=$ $2$.}").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         theta=ValueTracker(180)
#         alpha=ValueTracker(0)
#         Plane1 = NumberPlane(
#             x_range=[-1,9],
#             y_range=[-1,9],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": LEFT+DOWN},
#             x_axis_config={"label_direction": LEFT+DOWN}
#         ).scale(0.6).to_edge(LEFT)
#         A=Dot(color=RED,point=Plane1.c2p(3,5)).set_z_index(1)
#         rad=Line(start=Plane1.c2p(3,5),end=Plane1.c2p(1,5))
#         A_tex=MathTex(r"(3,5)").scale(0.6).next_to(A,RIGHT)
#         x_dash=DashedLine(start=Plane1.c2p(3,0),end=Plane1.c2p(3,5))
#         y_dash=DashedLine(start=Plane1.c2p(0,5),end=Plane1.c2p(3,5))
#         x_labels=[r"0",r"1",r"2",r"3",r"4",r"5",r"6",r"7",r"8"]
#         x_coords=[0,1,2,3,4,5,6,7,8]
#         y_labels=[r"1",r"2",r"3",r"4",r"5",r"6",r"7",r"8"]
#         y_coords=[1,2,3,4,5,6,7,8]
#         Plane1.add_coordinates(dict(zip(x_coords,x_labels)),dict(zip(y_coords,y_labels)))
#         Circ=ParametricFunction(lambda t: Plane1.c2p(2*np.cos(t)+3,2*np.sin(t)+5),t_range=[0,2*PI],color=PURPLE)
#         r_tex=always_redraw(lambda: MathTex(r"r=2").scale(0.6).rotate(alpha.get_value()*DEGREES).move_to(Plane1.c2p(0.5*2*np.cos(theta.get_value()*DEGREES-17*DEGREES)+3,0.5*2*np.sin(theta.get_value()*DEGREES-17*DEGREES)+5)))
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         self.play(FadeIn(Group(y_label,x_label,background_rectangle,Plane1)))
#         self.play(Write(Question),run_time=3.3)
#         self.play(Create(x_dash),Create(y_dash),run_time=2)
#         self.play(GrowFromCenter(A),Write(A_tex))
#         self.play(Wait(1))
#         self.play(Create(Circ),run_time=2)
#         self.play(Wait(1))
#         self.play(FadeOut(x_dash,y_dash))
#         self.play(Create(rad))
#         self.play(Write(r_tex))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(Question, DOWN).shift(RIGHT*1.4)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"C(h,k)=(3,5),\;r=2",color=BLUE_B).scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"(x-h)^2+(y-k)^2=r^2", color=GOLD).scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         t3 = MathTex(r"\Rightarrow(x-3)^2+(y-5)^2=2^2").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         t3b = MathTex(r"\Rightarrow x^2-6x+9+y^2-10y+25=4").scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         t4 = MathTex(r"\therefore x^2+y^2-6x-10y+30=0", color=RED_C).scale(0.7).next_to(t3b, DOWN).align_to(SolutionTex, LEFT)
#         self.wait(1)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t2))
#         self.wait(1)
#         self.play(Write(t3),run_time=1.5)
#         self.wait(1)
#         self.play(Write(t3b))
#         self.wait(1)
#         self.play(Write(t4),run_time=1.5)
#         self.wait(2)
#         fade_mobs = [t1, t2, t3, t4, t3b,SolutionTex,Question]
#         self.play(*[FadeOut(mob) for mob in fade_mobs])

# class CircPractice2(Scene):
#     def construct(self):
#         theta=ValueTracker(180)
#         alpha=ValueTracker(0)
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{2. Find the equation of the circle with center $(5,3)$ and touching the x-axis.}").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         h=ValueTracker(3)
#         k=ValueTracker(5)
#         r=ValueTracker(2)
#         Plane1 = NumberPlane(
#             x_range=[-1,9],
#             y_range=[-1,9],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": LEFT+DOWN},
#             x_axis_config={"label_direction": LEFT+DOWN}
#         ).scale(0.6).to_edge(LEFT)
#         A=always_redraw(lambda: Dot(color=RED,point=Plane1.c2p(h.get_value(),k.get_value())).set_z_index(1))
#         rad=always_redraw(lambda: Line(start=Plane1.c2p(h.get_value(),k.get_value()),end=Plane1.c2p(h.get_value()-r.get_value(),k.get_value())))
#         A_tex=always_redraw(lambda: MathTex(r"(",f"{h.get_value():.2g}",r",",f"{k.get_value():.2g}",r")").scale(0.6).next_to(A,RIGHT))
#         x_labels=[r"0",r"1",r"2",r"3",r"4",r"5",r"6",r"7",r"8"]
#         x_coords=[0,1,2,3,4,5,6,7,8]
#         y_labels=[r"1",r"2",r"3",r"4",r"5",r"6",r"7",r"8"]
#         y_coords=[1,2,3,4,5,6,7,8]
#         Plane1.add_coordinates(dict(zip(x_coords,x_labels)),dict(zip(y_coords,y_labels)))
#         Circ=always_redraw(lambda: ParametricFunction(lambda t: Plane1.c2p(r.get_value()*np.cos(t)+h.get_value(),r.get_value()*np.sin(t)+k.get_value()),t_range=[0,2*PI],color=PURPLE))
#         r_tex=always_redraw(lambda: MathTex(r"r=",f"{r.get_value():.2g}").scale(0.6).rotate(alpha.get_value()*DEGREES).move_to(Plane1.c2p(0.5*r.get_value()*np.cos(theta.get_value()*DEGREES-17*DEGREES)+h.get_value(),0.5*r.get_value()*np.sin(theta.get_value()*DEGREES-17*DEGREES)+k.get_value())))
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         self.add(y_label,x_label,background_rectangle,Plane1,A,A_tex,Circ,rad,r_tex)
#         self.play(Write(Question),run_time=3.3)
#         self.play(r.animate.set_value(3),run_time=2)
#         self.play(h.animate.set_value(5),k.animate.set_value(3),run_time=3.5)
#         rad_1=always_redraw(lambda: Line(start=Plane1.c2p(h.get_value(),k.get_value()),end=Plane1.c2p(r.get_value()*np.cos(theta.get_value()*DEGREES)+h.get_value(),r.get_value()*np.sin(theta.get_value()*DEGREES)+k.get_value())))
#         self.play(ReplacementTransform(rad,rad_1),run_time=0.5)
#         self.play(theta.animate.set_value(270),alpha.animate.set_value(90),run_time=2.5)
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(background_rectangle, RIGHT).shift(UP*2.5)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"C(h,k)=(5,3),\;r=3",color=BLUE_B).scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"(x-h)^2+(y-k)^2=r^2", color=GOLD).scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         t3 = MathTex(r"\Rightarrow(x-5)^2+(y-3)^2=3^2").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         t3b = MathTex(r"\Rightarrow x^2-10x+25+y^2-6y+9=9").scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         t4 = MathTex(r"\therefore x^2+y^2-10x-6y+25=0", color=RED_C).scale(0.7).next_to(t3b, DOWN).align_to(SolutionTex, LEFT)
#         self.wait(1)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t2))
#         self.wait(1)
#         self.play(Write(t3),run_time=1.5)
#         self.wait(1)
#         self.play(Write(t3b))
#         self.wait(1)
#         self.play(Write(t4),run_time=1.5)
#         self.wait(2)
#         fade_mobs = [t1, t2, t3, t4, t3b,SolutionTex,Question]
#         self.play(*[FadeOut(mob) for mob in fade_mobs])

# class CircPractice3(Scene):
#     def construct(self):
#         theta=ValueTracker(270)
#         alpha=ValueTracker(90)
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{3. Find the equation of the circle touching both axes at $(5,0)$ and $(0,5)$.}").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         h=ValueTracker(5)
#         k=ValueTracker(3)
#         r=ValueTracker(3)
#         def f(t):
#             return max(-1,min(9,r.get_value()*np.cos(t)+h.get_value()))
#         def g(t):
#             return max(-1,min(9,r.get_value()*np.sin(t)+k.get_value()))
        
#         Plane1 = NumberPlane(
#             x_range=[-1,9],
#             y_range=[-1,9],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": LEFT+DOWN},
#             x_axis_config={"label_direction": LEFT+DOWN}
#         ).scale(0.6).to_edge(LEFT)
#         A=always_redraw(lambda: Dot(color=RED,point=Plane1.c2p(h.get_value(),k.get_value())).set_z_index(1))
#         rad=always_redraw(lambda: Line(start=Plane1.c2p(h.get_value(),k.get_value()),end=Plane1.c2p(max(-1,min(9,r.get_value()*np.cos(theta.get_value()*DEGREES)+h.get_value())),max(-1,min(9,r.get_value()*np.sin(theta.get_value()*DEGREES)+k.get_value())))))
#         A_tex=always_redraw(lambda: MathTex(r"(",f"{h.get_value():.2g}",r",",f"{k.get_value():.2g}",r")").scale(0.6).next_to(A,RIGHT))
#         x_labels=[r"0",r"1",r"2",r"3",r"4",r"5",r"6",r"7",r"8"]
#         x_coords=[0,1,2,3,4,5,6,7,8]
#         y_labels=[r"1",r"2",r"3",r"4",r"5",r"6",r"7",r"8"]
#         y_coords=[1,2,3,4,5,6,7,8]
#         Plane1.add_coordinates(dict(zip(x_coords,x_labels)),dict(zip(y_coords,y_labels)))
#         Circ=always_redraw(lambda: ParametricFunction(lambda t: Plane1.c2p(f(t),g(t)),t_range=[0,2*PI],color=PURPLE))
#         r_tex=always_redraw(lambda: MathTex(r"r=",f"{r.get_value():.2g}").scale(0.6).rotate(alpha.get_value()*DEGREES).move_to(Plane1.c2p(0.5*r.get_value()*np.cos(theta.get_value()*DEGREES-17*DEGREES)+h.get_value(),0.5*r.get_value()*np.sin(theta.get_value()*DEGREES-17*DEGREES)+k.get_value())))
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         self.add(y_label,x_label,background_rectangle,Plane1,A,A_tex,Circ,rad,r_tex)
#         self.play(Write(Question),run_time=3.3)
#         self.play(r.animate.set_value(5),run_time=2)
#         self.play(h.animate.set_value(5),k.animate.set_value(5),run_time=3.5)
#         rad_2=always_redraw(lambda: Line(start=Plane1.c2p(h.get_value(),k.get_value()),end=Plane1.c2p(r.get_value()*np.cos(180*DEGREES)+h.get_value(),r.get_value()*np.sin(180*DEGREES)+k.get_value())))
#         r_tex_2=always_redraw(lambda: MathTex(r"r=",f"{r.get_value():.2g}").scale(0.6).move_to(Plane1.c2p(0.5*r.get_value()*np.cos((180-17)*DEGREES)+h.get_value(),0.5*r.get_value()*np.sin((180-17)*DEGREES)+k.get_value())))
#         self.play(Write(r_tex_2),Create(rad_2),run_time=2.5)
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(background_rectangle, RIGHT).shift(UP*2.5)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"C(h,k)=(5,5),\;r=5",color=BLUE_B).scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"(x-h)^2+(y-k)^2=r^2", color=GOLD).scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         t3 = MathTex(r"\Rightarrow(x-5)^2+(y-5)^2=5^2").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         t3b = MathTex(r"\Rightarrow x^2-10x+25+y^2-10y+25=25").scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         t4 = MathTex(r"\therefore x^2+y^2-10x-10y+25=0", color=RED_C).scale(0.7).next_to(t3b, DOWN).align_to(SolutionTex, LEFT)
#         self.wait(1)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t2))
#         self.wait(1)
#         self.play(Write(t3),run_time=1.5)
#         self.wait(1)
#         self.play(Write(t3b))
#         self.wait(1)
#         self.play(Write(t4),run_time=1.5)
#         self.wait(2)
#         fade_mobs = [t1, t2, t3, t4, t3b,SolutionTex,Question]
#         self.play(*[FadeOut(mob) for mob in fade_mobs])

# class CircPractice4(Scene):
#     def construct(self):
#         theta=ValueTracker(270)
#         alpha=ValueTracker(90)
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{4. Find the eq}^{\text{n}}\text{ of the circle with $(3,6)$ and $(7,-2)$ as the end-points of its diameter.}").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         h=ValueTracker(5)
#         k=ValueTracker(5)
#         r=ValueTracker(5)
#         m=ValueTracker(-1)
#         n=ValueTracker(9)
#         def f(t):
#             return max(-1,min(9,r.get_value()*np.cos(t)+h.get_value()))
#         def g(t):
#             return max(m.get_value(),min(n.get_value(),r.get_value()*np.sin(t)+k.get_value()))
#         def i(t):
#             return max(m.get_value(),min(n.get_value()+2,r.get_value()*np.sin(t)+k.get_value()+2))
#         x_labels=[r"0",r"1",r"2",r"3",r"4",r"5",r"6",r"7",r"8"]
#         x_coords=[0,1,2,3,4,5,6,7,8]
#         y_labels=[r"1",r"2",r"3",r"4",r"5",r"6",r"7",r"8"]
#         y_coords=[1,2,3,4,5,6,7,8]
#         Plane1 = NumberPlane( 
#             x_range=[-1,9],
#             y_range=[m.get_value(),n.get_value()],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": DL},
#             x_axis_config={"label_direction": DL}
#         ).scale(0.6).to_edge(LEFT).add_coordinates(dict(zip(x_coords,x_labels)),dict(zip(y_coords,y_labels)))
#         A=always_redraw(lambda: Dot(color=RED,point=Plane1.c2p(h.get_value(),k.get_value())).set_z_index(1))
#         rad=always_redraw(lambda: Line(start=Plane1.c2p(h.get_value(),k.get_value()),end=Plane1.c2p(r.get_value()*np.cos(theta.get_value()*DEGREES)+h.get_value(),r.get_value()*np.sin(theta.get_value()*DEGREES)+k.get_value())))
#         A_tex=always_redraw(lambda: MathTex(r"(",f"{h.get_value():.2g}",r",",f"{k.get_value():.2g}",r")").scale(0.6).next_to(A,RIGHT))
#         Circ=always_redraw(lambda: ParametricFunction(lambda t: Plane1.c2p(f(t),g(t)),t_range=[0,2*PI],color=PURPLE))
#         r_tex=always_redraw(lambda: MathTex(r"r=",f"{r.get_value():.2g}").scale(0.6).rotate(alpha.get_value()*DEGREES).move_to(Plane1.c2p(0.5*r.get_value()*np.cos(theta.get_value()*DEGREES-17*DEGREES)+h.get_value(),0.5*r.get_value()*np.sin(theta.get_value()*DEGREES-17*DEGREES)+k.get_value())))
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height , color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         y_label=always_redraw(lambda: MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9))
#         x_label=always_redraw(lambda: MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9))
#         rad_2=always_redraw(lambda: Line(start=Plane1.c2p(h.get_value(),k.get_value()),end=Plane1.c2p(r.get_value()*np.cos(180*DEGREES)+h.get_value(),r.get_value()*np.sin(180*DEGREES)+k.get_value())))
#         r_tex_2=always_redraw(lambda: MathTex(r"r=",f"{r.get_value():.2g}").scale(0.6).move_to(Plane1.c2p(0.5*r.get_value()*np.cos((180-17)*DEGREES)+h.get_value(),0.5*r.get_value()*np.sin((180-17)*DEGREES)+k.get_value())))
#         self.add(y_label,x_label,background_rectangle,Plane1,A,A_tex,Circ,rad,r_tex,rad_2,r_tex_2)
#         Plane2=always_redraw(lambda: NumberPlane(
#             x_range=[-1,9],
#             y_range=[m.get_value(),n.get_value()],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": DL},
#             x_axis_config={"label_direction": DL}
#         ).scale(0.6).to_edge(LEFT))
#         self.play(Write(Question),run_time=3.3)
#         self.play(FadeOut(Plane1),FadeIn(Plane2),FadeOut(rad_2,rad,r_tex,r_tex_2,A,A_tex,Circ),run_time=2)
#         self.play(Wait(0.5))
#         self.play(m.animate.set_value(-3),n.animate.set_value(7),run_time=2)
#         A=always_redraw(lambda: Dot(color=RED,point=Plane2.c2p(3,8)).set_z_index(1))
#         B=always_redraw(lambda: Dot(color=RED,point=Plane2.c2p(7,0)).set_z_index(1))
#         A_tex=MathTex(r"(3,6)").scale(0.6).next_to(A,RIGHT)
#         h.set_value(5)
#         k.set_value(2)
#         r.set_value(2*np.sqrt(5))
#         diameter=Line(start=A.get_center(),end=B.get_center(),color=BLUE)
#         Circ_1=always_redraw(lambda: ParametricFunction(lambda t: Plane1.c2p(f(t),i(t)),t_range=[0,2*PI],color=PURPLE))
#         B_tex=MathTex(r"(7,-2)").scale(0.6).next_to(B,LEFT)
#         Plane3=NumberPlane(
#             x_range=[-1,9],
#             y_range=[m.get_value(),n.get_value()],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": DL},
#             x_axis_config={"label_direction": DL}
#         ).scale(0.6).to_edge(LEFT).add_coordinates(dict(zip([i for i in range(0,9)],[i for i in range(0,9)])),dict(zip([i for i in range(-2,7)],[i for i in range(-2,7)])))
#         self.play(FadeIn(Plane3),FadeOut(Plane2))
#         self.play(Wait(1))
#         self.play(GrowFromCenter(A),Write(A_tex))
#         self.play(GrowFromCenter(B),Write(B_tex))
#         self.play(Create(Circ_1),run_time=2)
#         self.play(Wait(0.5))
#         self.play(Create(diameter),run_time=1.5)
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(background_rectangle, RIGHT).shift(UP*2.5)
#         self.play(Write(SolutionTex))
#         t1 = MathTex(r"\text{Diametrically Opposite End-Points:",color=BLUE_B).scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t1s = MathTex(r"(3,6)\text{ and }(7,-2)",color=BLUE_B).scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"(x-x_1)(x-x_2)+(y-y_1)(y-y_2)=0", color=GOLD).scale(0.7).next_to(t1s, DOWN).align_to(SolutionTex, LEFT)
#         t3 = MathTex(r"\Rightarrow(x-3)(x-7)+(y-6)(y+2)=0").scale(0.7).next_to(t2, DOWN).align_to(SolutionTex, LEFT)
#         t3b = MathTex(r"\Rightarrow x^2-10x+21+y^2-4y-12=0").scale(0.7).next_to(t3, DOWN).align_to(SolutionTex, LEFT)
#         t4 = MathTex(r"\therefore x^2+y^2-10x-4y+9=0", color=RED_C).scale(0.7).next_to(t3b, DOWN).align_to(SolutionTex, LEFT)
#         self.wait(1)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(Write(t1s))
#         self.wait(1)
#         self.play(Write(t2),run_time=2.5)
#         self.wait(1)
#         self.play(Write(t3),run_time=2.5)
#         self.wait(1)
#         self.play(Write(t3b),run_time=2.5)
#         self.wait(1)
#         self.play(Write(t4),run_time=2)
#         self.wait(2)
#         fade_mobs = [t1, t2, t3, t4, t3b, SolutionTex, Question, t1s,Circ_1,A,B,B_tex,A_tex,diameter]
#         self.play(*[FadeOut(mob) for mob in fade_mobs])

# class CircPractice5(Scene):
#     def construct(self):
#         theta=ValueTracker(270)
#         alpha=ValueTracker(90)
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{5. Find the eq}^{\text{n}}\text{ of the circle passing through $A(3,1)$,$B(1,-1)$ and $C(3,-3)$.}").scale(0.7).to_corner(UL)
#         h=ValueTracker(3)
#         k=ValueTracker(-1)
#         r=ValueTracker(2)
#         m=ValueTracker(-3)
#         n=ValueTracker(7)
#         def f(t):
#             return max(-1,min(9,r.get_value()*np.cos(t)+h.get_value()))
#         def g(t):
#             return max(m.get_value(),min(n.get_value(),r.get_value()*np.sin(t)+k.get_value()))
#         Plane1 = NumberPlane( 
#             x_range=[-1,9],
#             y_range=[m.get_value(),n.get_value()],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": DL},
#             x_axis_config={"label_direction": DL}
#         ).scale(0.6).to_edge(LEFT).add_coordinates(dict(zip([i for i in range(0,9)],[i for i in range(0,9)])),dict(zip([i for i in range(-2,7)],[i for i in range(-2,7)])))
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,6.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-2.5)).scale(0.9)
#         background_rectangle = Rectangle(
#              width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#          ).move_to(Plane1.get_center()).set_z_index(1)
#         self.add(NameLabel,Plane1,y_label,x_label,background_rectangle) 
#         A=always_redraw(lambda: Dot(color=RED,point=Plane1.c2p(h.get_value(),k.get_value())).set_z_index(1))
#         A_tex=always_redraw(lambda: MathTex(r"(",f"{h.get_value():.2g}",r",",f"{k.get_value():.2g}",r")").scale(0.6).next_to(A,RIGHT))
#         Circ=always_redraw(lambda: ParametricFunction(lambda t: Plane1.c2p(f(t),g(t)),t_range=[0,2*PI],color=PURPLE))
#         self.add(y_label,x_label,background_rectangle,Plane1)
#         self.play(Write(Question),run_time=3.3)
#         self.play(Wait(0.5))
#         A=always_redraw(lambda: Dot(color=RED,point=Plane1.c2p(3,1)).set_z_index(1))
#         B=always_redraw(lambda: Dot(color=RED,point=Plane1.c2p(1,-1)).set_z_index(1))
#         C=always_redraw(lambda: Dot(color=RED,point=Plane1.c2p(3,-3)).set_z_index(1))
#         A_tex=MathTex(r"(3,1)").scale(0.6).next_to(A,RIGHT)
#         B_tex=MathTex(r"(1,-1)").scale(0.6).next_to(B,LEFT)
#         C_tex=MathTex(r"(3,-3)").scale(0.6).next_to(C,UP)
#         self.play(Wait(1))
#         self.play(GrowFromCenter(A),Write(A_tex))
#         self.play(GrowFromCenter(B),Write(B_tex))
#         self.play(GrowFromCenter(C),Write(C_tex))
#         self.play(Wait(0.5))
#         self.play(Create(Circ),run_time=2.5)
#         t=[None]*17
#         t[0] = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.6).next_to(background_rectangle, RIGHT).shift(UP*2.8)
#         self.play(Write(t[0]))
#         t[1] = MathTex(r"\text{Suppose $O(h,k)$ is the center,}")
#         t[2] = MathTex(r"r^2=OA^2=OC^2", color=GOLD)
#         t[3] = MathTex(r"\Rightarrow (h-3)^2+(k-1)^2=(h-3)^2+(k+3)^2")
#         t[4] = MathTex(r"\Rightarrow k^2-2k+1=k^2+6k+9")
#         t[5] = MathTex(r"\Rightarrow 8k=-8")
#         t[6] = MathTex(r"\therefore k=-1", color=RED_C)
#         t[7] = MathTex(r"OA^2=OB^2",color=GOLD)
#         t[8] = MathTex(r"\Rightarrow (h-3)^2+(k-1)^2=(h-1)^2+(k+1)^2")
#         t[9] = MathTex(r"\Rightarrow (h-3)^2+(-1-1)^2=(h-1)^2+(-1+1)^2")
#         t[10] = MathTex(r"\Rightarrow h^2-6h+9+4=h^2-2h+1")
#         t[11] = MathTex(r"\Rightarrow 4h=12")
#         t[12] = MathTex(r"\therefore h=3", color=RED_C)
#         t[13] = MathTex(r"\therefore r^2=(3-3)^2+(-1-1)^2=4",color=RED_C)
#         t[14] = MathTex(r"(x-3)^2+(y+1)^2=4")
#         t[15] = MathTex(r"\Rightarrow x^2-6x+9+y^2+2y+1=4")
#         t[16] = MathTex(r"\therefore x^2+y^2-6x+2y-12=0", color=RED_C)
#         for i in range(1,13):
#             t[i].scale(0.6).next_to(t[i-1], DOWN).align_to(t[0], LEFT)
#             self.play(Write(t[i]))
#             self.wait(1)
#         self.play(*[FadeOut(t[i]) for i in range(2,6)],*[FadeOut(t[i]) for i in range(7,12)])
#         self.wait(1)
#         self.play(t[6].animate.next_to(t[1],DOWN).align_to(t[1],LEFT))
#         self.play(t[12].animate.next_to(t[6],RIGHT))
#         self.wait(1)
#         for i in range(13,17):
#             t[i].scale(0.6).next_to(t[i-1], DOWN).align_to(t[0], LEFT)
#             self.play(Write(t[i]))
#             self.wait(1)
#         self.wait(2)
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=NameLabel])

# class CircPractice6(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{6. Find the center and radius of $2x^2+2y^2+4x-2y+1=0$.").scale(0.7).to_corner(UL)
#         eq = MathTex(r"2x^2+2y^2+4x-2y+1=0", color=BLUE_B).scale(0.7).next_to(Question, DOWN).align_to(Question, LEFT)
#         self.add(NameLabel)
#         self.play(Write(Question),run_time=3); self.play(Write(eq)); self.play(Wait(1))
#         SolutionTex = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(eq, DOWN).align_to(eq, LEFT)
#         t1 = MathTex(r"2\bigg(x^2+y^2+2x-y+\frac{1}{2}\bigg)=0").scale(0.7).next_to(SolutionTex, DOWN).align_to(SolutionTex, LEFT)
#         t1s = MathTex(r"\Rightarrow x^2+y^2+2x-y+\frac{1}{2}=0").scale(0.7).next_to(t1, DOWN).align_to(SolutionTex, LEFT)
#         t2 = MathTex(r"\text{Compare to }x^2+y^2+2gx+2fy+c=0:",color=GOLD).scale(0.7).next_to(t1s, DOWN).align_to(t1, LEFT)
#         t3 = MathTex(r"2g=2\Rightarrow g=1,\;2f=-1\Rightarrow f=-\frac{1}{2},\;c=\frac{1}{2}").scale(0.7).next_to(t2, DOWN).align_to(t2, LEFT)
#         t4 = MathTex(r"\therefore \text{Center}(-g,-f)=(-1,\frac{1}{2}),", color=RED_C).scale(0.7).next_to(t3, DOWN).align_to(t2, LEFT)
#         f1 = MathTex(r"r=\sqrt{g^2+f^2-c}=\sqrt{(1)^2+\bigg(-\frac{1}{2}\bigg)^2-\frac{1}{2}}=\frac{\sqrt{3}}{2}", color=RED_C).scale(0.7).next_to(t4, RIGHT)
#         self.play(Write(SolutionTex)); self.play(Wait(1))
#         for t in [t1, t1s, t2, t3, t4, f1]:
#             self.play(Write(t),run_time=2.5); self.play(Wait(1))
#         self.play(Wait(1)); self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [NameLabel]])

# class CircPractice7(Scene): 
#     def construct(self):
#         h=ValueTracker(3)
#         k=ValueTracker(4)
#         r=ValueTracker(np.sqrt(10))
#         m=ValueTracker(-1)
#         n=ValueTracker(9)
#         def f(t):
#             return max(-1,min(9,r.get_value()*np.cos(t)+h.get_value()))
#         def g(t):
#             return max(m.get_value(),min(n.get_value(),r.get_value()*np.sin(t)+k.get_value()))
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = Tex(r"\text{7. Find the equation of the circle passing through $(4,1)$ and $(6,5)$ having its center on}").scale(0.7).to_corner(UL)
#         self.add(NameLabel)
#         k = ValueTracker(4)
#         Plane1 = NumberPlane(
#             x_range=[-5 + k.get_value(), 5 + k.get_value()],
#             y_range=[-5 + k.get_value(), 5 + k.get_value()],
#             axis_config={"include_tip": True},
#             y_axis_config={"label_direction": DL},
#             x_axis_config={"label_direction": DL}
#         ).scale(0.6).to_edge(LEFT).add_coordinates(dict(zip([i for i in range(0,9)],[i for i in range(0,9)])),dict(zip([i for i in range(0,9)],[i for i in range(0,9)])))
#         background_rectangle = Rectangle(
#             width=Plane1.height, height=Plane1.height, color=YELLOW, fill_opacity=0
#         ).move_to(Plane1.get_center()).set_z_index(1)
#         Questionb = Tex(r"\text{the line $4x+y=16$.}").scale(0.7).next_to(background_rectangle,RIGHT).to_edge(UP).shift(DOWN*0.5)
#         def i(x):
#             y = 16-4*x
#             return max(min(y, 9), -1)
#         l1=Plane1.plot(lambda x: i(x), color=BLUE_B)
#         l1_l = MathTex(r"4x+y=16", color=BLUE_B).scale(0.7).move_to(Plane1.c2p(4,8))
#         y_label=MathTex(r"y").move_to(Plane1.c2p(-0.5,8.5)).scale(0.9)
#         x_label=MathTex(r"x").move_to(Plane1.c2p(8.5,-0.5)).scale(0.9)
#         ADot=Dot(color=RED).move_to(Plane1.c2p(6,5)).set_z_index(1)
#         BDot=Dot(color=RED).move_to(Plane1.c2p(4,1)).set_z_index(1)
#         CDot=Dot(color=GRAY).move_to(Plane1.c2p(3,4)).set_z_index(1)
#         ACoord=MathTex(r"A(6,5)").next_to(ADot,RIGHT*0.5).scale(0.7).set_z_index(1)
#         BCoord=MathTex(r"B(4,1)").next_to(BDot,RIGHT*0.5).scale(0.7).set_z_index(1)
#         CCoord=MathTex(r"C(h,k)").next_to(CDot,LEFT*0.5).scale(0.7).set_z_index(1)
#         Circ=always_redraw(lambda: ParametricFunction(lambda t: Plane1.c2p(f(t),g(t)),t_range=[0,2*PI],color=GRAY_BROWN))
#         self.play(FadeIn(Group(y_label,x_label,background_rectangle,Plane1)))
#         self.play(Write(Question),run_time=3.3)
#         self.play(Write(Questionb))
#         self.play(GrowFromCenter(ADot))
#         self.play(Write(ACoord))
#         self.play(GrowFromCenter(BDot))
#         self.play(Write(BCoord))
#         self.play(GrowFromCenter(CDot))
#         self.play(Write(CCoord))
#         self.play(Wait(1))
#         self.play(Create(Circ),run_time=3)
#         self.play(FadeIn(l1),Write(l1_l,run_time=2.5))
#         t=[None]*17
#         t[0] = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.6).next_to(background_rectangle, 0.7*RIGHT).shift(UP*2.4)
#         self.play(Write(t[0]))
#         t[1] = MathTex(r"\text{Suppose $C(h,k)$ is the center,}")
#         t[2] = MathTex(r"r^2=AC^2=BC^2", color=GOLD)
#         t[3] = MathTex(r"\Rightarrow (4-h)^2+(1-k)^2=(6-h)^2+(5-k)^2")
#         t[4] = MathTex(r"\Rightarrow 16-8h+h^2+1-2k+k^2=36-12h+h^2+25-10k+k^2")
#         t[5] = MathTex(r"\Rightarrow 4h+8k=44\cdots\cdots(i)")
#         t[6] = MathTex(r"\text{$C$ also lies on $4x+y=16$:}", color=GOLD)
#         t[7] = MathTex(r"4h+k=16")
#         t[8] = MathTex(r"\Rightarrow 44-8k+k=16\;\;\;[\,\text{From }(i)\,]")
#         t[9] = MathTex(r"\Rightarrow 28=7k")
#         t[10] = MathTex(r"\therefore k=4", color=RED_C)
#         t[11] = MathTex(r"h=\tfrac{16-k}{4}=\tfrac{12}{4}")
#         t[12] = MathTex(r"\therefore h=3", color=RED_C)
#         t[13] = MathTex(r"\therefore r=AC=\sqrt{(4-3)^2+(1-4)^2}=\sqrt{10}",color=RED_C)
#         t[14] = MathTex(r"(x-3)^2+(y-4)^2=10")
#         t[15] = MathTex(r"\Rightarrow x^2-6x+9+y^2-8y+16=10")
#         t[16] = MathTex(r"\therefore x^2+y^2-6x-8y+15=0", color=RED_C)
#         for i in range(1,13):
#             t[i].scale(0.55).next_to(t[i-1], DOWN).align_to(t[0], LEFT)
#             self.play(Write(t[i]))
#             self.wait(1)
#         self.play(*[FadeOut(t[i]) for i in range(2,10)],FadeOut(t[11]))
#         self.wait(1)
#         self.play(t[10].animate.next_to(t[1],DOWN).align_to(t[1],LEFT))
#         self.play(t[12].animate.next_to(t[10],RIGHT))
#         self.wait(1)
#         for i in range(13,17):
#             t[i].scale(0.55).next_to(t[i-1], DOWN).align_to(t[0], LEFT)
#             self.play(Write(t[i]))
#             self.wait(1)
#         self.wait(2)
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=NameLabel])

# class CircPractice8(Scene):
#     def construct(self):
#         NameLabel = Tex("Created by Himalaya Satyal", font_size=30).to_corner(DL)
#         Question = MathTex(r"\text{8. Show that circles $x^2+y^2=36$ and $(x-6)^2+(y-8)^2=16$ touch externally.").scale(0.7).to_corner(UL)
#         eq = MathTex(r"\omega_1:\;x^2+y^2=36,\;\omega_2:\;(x-6)^2+(y-8)^2=16", color=BLUE_B).scale(0.7).next_to(Question, DOWN).align_to(Question, LEFT)
#         self.add(NameLabel)
#         self.play(Write(Question),run_time=3.5); self.play(Write(eq),run_time=2.5); self.play(Wait(1.5))
#         t=[None]*17
#         t[0] = MathTex(r"\text{Sol}^{\text{n}}\text{:}").scale(0.7).next_to(eq, DOWN).align_to(eq,LEFT)
#         self.play(Write(t[0]))
#         t[1] = MathTex(r"\text{Center of $\omega_1=A(0,0)$, radius of $\omega_1$$(r_1)=\sqrt{36}=6$}", color=GOLD)
#         t[2] = MathTex(r"\text{Center of $\omega_2=B(6,8)$, radius of $\omega_1$$(r_2)=\sqrt{16}=4$}", color=GOLD)
#         t[3] = MathTex(r"AB=\sqrt{(6-0)^2+(8-0)^2}=10")
#         t[4] = MathTex(r"r_1+r_2=6+4=10")
#         t[5] = MathTex(r"\text{$\therefore r_1+r_2=AB$, so the two circles touch externally.}", color=RED)
#         for i in range(1,6):
#             t[i].scale(0.7).next_to(t[i-1], DOWN).align_to(t[0], LEFT)
#         circ_1=Circle(radius=2.5*0.6,fill_opacity=0.1,color=BLUE).next_to(t[2],RIGHT)
#         circ_2=Circle(radius=2*0.6,fill_opacity=0.1,color=BLUE).rotate(angle=180*DEGREES,about_point=ORIGIN).next_to(circ_1,RIGHT,buff=0)
#         omega_1_tex=MathTex(r"\omega_1",color=BLUE_B).scale(0.6).next_to(circ_1,UP*0.3)
#         omega_2_tex=MathTex(r"\omega_2",color=BLUE_B).scale(0.6).next_to(circ_2,UP*0.3)
#         self.play(DrawBorderThenFill(circ_1),run_time=2.5)
#         self.play(Write(omega_1_tex))
#         self.play(Wait(0.5))
#         self.play(DrawBorderThenFill(circ_2),run_time=2.5)
#         self.play(Write(omega_2_tex))
#         self.play(Wait(0.5))
#         A=Dot(color=RED).move_to(circ_1.get_center()).set_z_index(1)
#         B=Dot(color=RED).move_to(circ_2.get_center()).set_z_index(1)
#         A_tex=MathTex(r"A",color=RED).scale(0.6).next_to(A,DOWN*0.3)
#         B_tex=MathTex(r"B",color=RED).scale(0.6).next_to(B,DOWN*0.3)
#         self.play(GrowFromCenter(A))
#         self.play(Write(A_tex))
#         self.play(Wait(0.5))
#         self.play(GrowFromCenter(B))
#         self.play(Write(B_tex))
#         self.play(Wait(0.5))
#         r_1=Line(color=GOLD_C,start=circ_1.get_center(),end=circ_1.get_center()+RIGHT*2.5*0.6)
#         r_2=Line(color=YELLOW,start=circ_2.get_center(),end=circ_2.get_center()+LEFT*2*0.6)
#         r_1_tex=MathTex(r"r_1",color=GOLD_C).scale(0.6).next_to(r_1,DOWN*0.3)
#         r_2_tex=MathTex(r"r_2",color=YELLOW).scale(0.6).next_to(r_2,DOWN*0.3)
#         self.play(Create(r_1))
#         self.play(Write(r_1_tex))
#         self.play(Wait(0.5))
#         self.play(Create(r_2))
#         self.play(Write(r_2_tex))
#         self.play(Wait(0.5))
#         br=BraceBetweenPoints(point_1=circ_1.get_center()+UP*0.1,point_2=circ_2.get_center()+UP*0.2,direction=UP)
#         AB_tex=MathTex(r"AB").scale(0.6).next_to(br,UP*0.3)
#         self.play(FadeIn(br),Write(AB_tex))
#         self.play(Wait(0.5))
#         for i in range(1,6): 
#             self.play(Write(t[i]),run_time=3)
#             self.wait(1)
#         self.wait(1)
#         self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=NameLabel])