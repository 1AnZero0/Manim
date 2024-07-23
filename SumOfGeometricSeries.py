from audioop import reverse
from pdb import run
from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_rate = 120
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class PlayGround(Scene):

    def construct(self):
        
        self.MyName = Tex("ENG A.ALQARNI").set_color_by_gradient(RED, GOLD)
        self.play(Write(self.MyName), run_time=1.5)
        self.play(self.MyName.animate.to_edge(UP).scale(0.9))
        self.wait()

        ArabTexTemplate = TexTemplate(
        tex_compiler="xelatex",
        output_format='.xdv',
        preamble = r'''
        \usepackage{polyglossia}\setotherlanguage{arabic}\newfontfamily\arabicfont[Script=Arabic]{a-jannat-lt.ttf}
            '''
        )
        
        title = Tex(
            r"إيجاد مجموع المتتابعة الهندسية",
            tex_template=ArabTexTemplate,
            tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        
        sequence = MathTex(
            r"4 + 2 + 1 + \cdots + \frac{1}{16}"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        
        vgroup1 = VGroup(title, sequence ).arrange(DOWN, buff=0.5)
        box_union = SurroundingRectangle(vgroup1, buff=0.4, color=RED, corner_radius=0.2)
        vgroup1.add(box_union)
        self.play(Write(vgroup1[0]), run_time=2 , reverse = True)
        self.play(Write(vgroup1[1]), run_time=2)
        self.play(Create(box_union) , run_time = 2)
        self.wait(3)
        
        Text2 = Tex(
        r"نستخدم طريقة عبدالله الجهنمية",
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient(RED_C, GOLD).scale(0.9)
        
        self.play(ReplacementTransform(vgroup1 , Text2))
        self.wait(3)
        
        
        Text3 = Tex(
        r"\begin{minipage}{30em}"
        r"\begin{center}"
        r"الطريقة تقول لنا التالي : \\ بما ان المتتابعة الهندسية ذات حدود بسيطة \\ نستخرج النسبة المشتركة و نكمل الحدود الناقصة \\ بأنفسنا بشكل يدوي ."
        r"\end{center}"
        r"\end{minipage}",
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        
        self.play(ReplacementTransform(Text2 , Text3))
        self.wait(3)
        
        sequence2 = MathTex(r"4 + 2 + 1 + \cdots + \frac{1}{16}").set_color_by_gradient("#DFB885", GOLD).scale(0.9)        
        self.play(ReplacementTransform(Text3 , sequence2))
        self.play(sequence2.animate.to_edge(UP*5).scale(1))
        self.wait(2)
        
        Text4 = Tex(
        r"النسبة المشتركة : " ,
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        Fraction1 = MathTex(r"\frac{1}{2}").set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        group = VGroup(Fraction1, Text4).arrange(RIGHT)
        self.play(Write(group), run_time=2, reverse=True)
        self.wait(3)
        
        Text5 = Tex(
        r"نبدأ بالضرب في " ,
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        Fraction2 = MathTex(r"\frac{1}{2}").set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        Text6 = Tex(
        r"حتى نصل الي " ,
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        Fraction3 = MathTex(r"\frac{1}{16}").set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        group1 = VGroup(Fraction3, Text6 , Fraction2 , Text5).arrange(RIGHT)
        self.play(ReplacementTransform(group , group1), reverse=True)
        self.wait(3)
        self.play(FadeOut(group1))
        
        fractions = [
            "1",
            "\\frac{1}{2}",
            "\\frac{1}{4}",
            "\\frac{1}{8}",
            "\\frac{1}{16}"
        ]
        
        equations = VGroup()
        
        for i in range(len(fractions) - 1):
            eq = MathTex(
                fractions[i],
                "\\times \\frac{1}{2}",
                "=",
                fractions[i+1]
            )
            eq[0].set_color_by_gradient("#DFB885", GOLD)
            eq[3].set_color_by_gradient("#DFB885", GOLD)
            equations.add(eq)
        
        equations.arrange(DOWN, buff=0.8)
        
        self.play(Write(equations[0]))
        self.wait()
        
        for i in range(1, len(equations)):
            self.play(
                TransformFromCopy(equations[i-1][0], equations[i][0]),
                TransformFromCopy(equations[i-1][1], equations[i][1]),
                TransformFromCopy(equations[i-1][2], equations[i][2]),
                Write(equations[i][3])
            )
            self.wait()
        
        self.wait(3)
        
        Text7 = Tex(
        r"إذاً لدينا : " ,
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        Fraction4 = MathTex(r"\frac{1}{2} + \frac{1}{4} + \frac{1}{8}").set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        group2 = VGroup(Fraction4 , Text7).arrange(RIGHT)
        self.play(ReplacementTransform(equations , group2), reverse=True)
        self.wait(3)
        
        Text8 = Tex(
        r"لنقم الأن بإعادة كتابة السلسة بعد أن أوجدنا كل الحدود" ,
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.8)
        self.play(ReplacementTransform(group2 , Text8), reverse=True)
        self.wait(3)
        self.play(FadeOut(Text8))
        
        self.play(sequence2.animate.move_to(ORIGIN).scale(1.1))
        self.wait(3)
        sequence3 = MathTex(r"4 + 2 + 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16}").set_color_by_gradient("#DFB885", GOLD)
        self.play(ReplacementTransform(sequence2 , sequence3), reverse=True)
        self.wait(3)
        
        
        Text9 = Tex(
        r"لا تنسى أنه يريد المجموع ، لذلك نبدأ بالجمع" ,
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.8).to_edge(DOWN*2)
        self.play(Write(Text9) , reverse = True)
        self.wait(3)
        
        sequence4 = MathTex(r"7 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16}").set_color_by_gradient("#DFB885", GOLD)
        self.play(ReplacementTransform(sequence3 , sequence4), reverse=True)
        self.wait(2)
        
        sequence5 = MathTex(r"7 + \frac{15}{16}").set_color_by_gradient("#DFB885", GOLD)
        self.play(ReplacementTransform(sequence4 , sequence5), reverse=True)
        self.wait(2)
        
        sequence6 = MathTex(r"7\frac{15}{16}").set_color_by_gradient("#DFB885", GOLD)
        self.play(ReplacementTransform(sequence5 , sequence6), reverse=True)
        self.wait(2)
        
        sequence7 = MathTex(r"\frac{127}{16}").set_color_by_gradient("#DFB885", GOLD)
        self.play(ReplacementTransform(sequence6 , sequence7), reverse=True)
        self.wait(2)
        
        self.play(FadeOut(Text9))
        
        Text10 = Tex(
        r"إذاً الإجابة النهائية هي : " ,
        tex_template=ArabTexTemplate,
        tex_environment="Arabic"
        ).set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        Fraction10 = MathTex(r"\frac{127}{16}").set_color_by_gradient("#DFB885", GOLD).scale(0.9)
        group10 = VGroup(Fraction10 , Text10).arrange(RIGHT)
        self.play(ReplacementTransform(sequence7 , group10), reverse=True)
        self.wait(3)
        self.play(FadeOut(group10))
        self.wait(1)
        
        self.play(self.MyName.animate.move_to(ORIGIN).scale(1.1))
        self.wait(3)

        
        
        
        
        
        
        
        
        
        

      


        
        

        

        
        
        
        
        
    
        
        
        
        

        