from turtle import Screen, Turtle

turtle = Turtle()

turtle.color('white')
turtle.shape("square")
turtle.shapesize(stretch_wid=20, stretch_len=100)
turtle.goto(x=350,y=0)

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Right_Paddle:
    def create_paddle(self):
        self.Turtle("square")
        self.color('white')
        self.shapesize(stretch_wid=20, stretch_len=100)
        turtle.goto(x=350,y=0)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def up(self):
        self.setheading(UP)
        
    def down(self):
        self.setheading(DOWN)
        
turtle.onkey("")