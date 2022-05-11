from turtle import Turtle
INCR = 1
FONT = ('Courier', 30, "bold")
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points1 = 0
        self.points2 = 0
        self.i = 0
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.score_write()

    def score_write(self):
        self.clear()
        for range1 in range(-290,290,40):
            self.dotted_line(range1)
        self.goto(-30,260)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(30,260)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def dotted_line(self,range1):
        self.goto(0,range1)
        self.write("|", align=ALIGNMENT, font=FONT)



    def pong1_add_points(self):
        self.l_score += INCR
        self.score_write()

    def pong2_add_points(self):
        self.r_score += INCR
        self.score_write()

    def game_over(self):
        self.goto(CORD1, CORD1)
        self.write("Game Over",  align = ALIGNMENT, font= FONT)
