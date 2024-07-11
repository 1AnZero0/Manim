from manim import *


config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_rate = 120
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class PlayGround(Scene):
    def construct(self):
        ArabTexTemplate = TexTemplate(
            tex_compiler="xelatex",   
            output_format='.xdv',            
            preamble = r'''
            \usepackage{polyglossia}\setotherlanguage{arabic}\newfontfamily\arabicfont[Script=Arabic]{a-jannat-lt.ttf}
            '''
        )
        arabicText = Tex(
            r"عبدالوهاب القرني",
            tex_template=ArabTexTemplate,
            tex_environment="Arabic"
        ).set_color_by_gradient(RED, GOLD)
        self.play(Write(arabicText , reverse=True) , run_time = 2)
        self.play(arabicText.animate.to_edge(UP))
        self.wait(3)
