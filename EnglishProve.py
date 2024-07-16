from manim import *
from networkx import center 
 
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

        FirstText = Tex("Let's solve the hardest question in the world !!").set_color_by_gradient(RED, GOLD).scale(0.8)
        SecText = Tex("Ready ?!").set_color_by_gradient(RED, GOLD).scale(1)
        self.play(Write(FirstText)) 
        self.wait(2)
        self.play(ReplacementTransform(FirstText , SecText))
        self.wait(3)

        question_options = VGroup(
            Tex("She ...... waking up early for her new job.").set_color(WHITE),
            Tex("A ) Used to").set_color(YELLOW),
            Tex("B ) Gets used to").set_color(YELLOW),
            Tex("C ) Is used to").set_color(YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        question_options.scale(0.9)
        self.play(ReplacementTransform( SecText, question_options))
        self.wait(10)

        TherdText = Tex("Have you finished thinking?").set_color_by_gradient(RED, GOLD).scale(1)
        self.play(ReplacementTransform(question_options, TherdText))
        self.wait(3)

        ForthText = Tex("The Answer is (Gets used to)").set_color_by_gradient(RED, GOLD).scale(1)
        self.play(ReplacementTransform(TherdText, ForthText))
        self.wait(3)

        FiveText = Tex(
       "Do not fight to prove you are right,\\\\fight to find what is right.",
        tex_to_color_map={
        "Do not fight to prove you are right,": RED,
        "fight to find what is right.": GOLD}).scale(0.9)

        self.play(ReplacementTransform(ForthText, FiveText))
        self.wait(3)
        self.play(FadeOut(FiveText))

        self.play(self.MyName.animate.move_to(ORIGIN)) 
        self.wait(3)
