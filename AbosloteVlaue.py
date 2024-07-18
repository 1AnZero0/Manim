from manim import *
from networkx import center

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_rate = 120
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class AnimatedCounter(VMobject):
    def __init__(self, start, end, duration, **kwargs):
        super().__init__(**kwargs)
        self.start = start
        self.end = end
        self.duration = duration
        self.counter = DecimalNumber(start, color=WHITE)
        self.add(self.counter)

    def start_count(self):
        self.counter.add_updater(self.update_counter)

    def update_counter(self, m, dt):
        self.elapsed_time = self.elapsed_time + dt
        value = self.end + (self.start - self.end) * (1 - self.elapsed_time / self.duration)
        self.counter.set_value(max(value, self.end))
        if self.elapsed_time >= self.duration:
            self.counter.remove_updater(self.update_counter)

class PlayGround(Scene):
    def construct(self):
        self.MyName = Tex("ENG A.ALQARNI").set_color_by_gradient(RED, GOLD)
        self.play(Write(self.MyName), run_time=1.5)
        self.play(self.MyName.animate.to_edge(UP).scale(0.9))
        self.wait()

        FirstText = Tex("Let's solve a math question!").set_color_by_gradient(RED, GOLD).scale(0.8)
        SecText = Tex("Ready?!").set_color_by_gradient(RED, GOLD).scale(1)
        self.play(Write(FirstText))
        self.wait(2)
        self.play(ReplacementTransform(FirstText, SecText))
        self.wait(3)

        question = MathTex(r"|x^2 - 12| = 13").set_color(WHITE)
        question_options = VGroup(
            question,
            Tex("A) x = ±5").set_color(YELLOW),
            Tex("B) x = ±7").set_color(YELLOW),
            Tex("C) x = ±1 or x = ±5").set_color(YELLOW),
            Tex("D) x = ±i or x = ±5").set_color(YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        question_options.scale(0.9)
        self.play(ReplacementTransform(SecText, question_options))

        # Create and start the timer
        timer = AnimatedCounter(15, 0, 15)
        timer.to_corner(DOWN)
        self.add(timer)
        timer.start_count()
        timer.elapsed_time = 0
        self.wait(15)

        ThirdText = Tex("Have you finished thinking?").set_color_by_gradient(RED, GOLD).scale(1)
        self.play(ReplacementTransform(question_options, ThirdText), FadeOut(timer))
        self.wait(3)

        FourthText = Tex("The correct answer is: D) x = ±i or x = ±5").set_color_by_gradient(RED, GOLD).scale(0.8)
        self.play(ReplacementTransform(ThirdText, FourthText))
        self.wait(3)

        explanation = VGroup(
            Tex("Explanation:").set_color(BLUE),
            MathTex(r"|x^2 - 12| = 13"),
            Tex("Case 1: ").set_color(GREEN),
            MathTex(r"x^2 - 12 = 13 \Rightarrow x^2 = 25 \Rightarrow x = \pm 5"),
            Tex("Case 2: ").set_color(GREEN),
            MathTex(r"x^2 - 12 = -13 \Rightarrow x^2 = -1 \Rightarrow x = \pm i")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.7)

        self.play(ReplacementTransform(FourthText, explanation))
        self.wait(5)

        FiveText = Tex(
            "Math is not about memorizing formulas,\\\\it's about understanding concepts.",
            tex_to_color_map={
            "Math is not about memorizing formulas,": RED,
            "it's about understanding concepts.": GOLD}).scale(0.9)

        self.play(ReplacementTransform(explanation, FiveText))
        self.wait(3)
        self.play(FadeOut(FiveText))

        self.play(self.MyName.animate.move_to(ORIGIN))
        self.wait(3)
