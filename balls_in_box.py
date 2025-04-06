import turtle
import random

def color_func(value):
    # Hex codes for yellow and red
    yellow = (255, 255, 0)
    red = (255, 0, 0)

    # Interpolating the color
    ratio = value / 10.0
    r = int(red[0] * ratio + yellow[0] * (1 - ratio))
    g = int(red[1] * ratio + yellow[1] * (1 - ratio))
    b = int(red[2] * ratio + yellow[2] * (1 - ratio))

    # Returning the color as a hex string
    return f'#{r:02X}{g:02X}{b:02X}'

window=turtle.Screen()
window.bgcolor("black")
window.title("Bouncinc Balls Simulation")
window.tracer(1,0.1)

length=300
height=400
balls=[]
radius_of_balls=[]

gelb = (255, 255, 0)
colors=[]

# Erstellen einer Turtle
u_turtle = turtle.Turtle()
u_turtle.color("white")  # Farbe der Turtle auf Weiß setzen
u_turtle.pensize(3)

# Funktion zum Zeichnen eines eckigen U
def draw_u(turtle, width, height):
    turtle.right(90)  # Richtung nach unten
    turtle.forward(height)  # Linie nach unten
    turtle.left(90)  # Richtung nach rechts
    turtle.forward(length)  # Linie nach rechts
    turtle.left(90)  # Richtung nach oben
    turtle.forward(height)  # Linie nach oben


# Positionieren der Turtle zum Startpunkt
u_turtle.penup()
u_turtle.goto(-length/2, height/2)
u_turtle.pendown()

# Zeichnen des eckigen U
draw_u(u_turtle, length, height)


for i in range(0,5):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.shape("circle")
    ball.penup()
    ball.speed(0)
    radius_of_balls.append(random.uniform(1,4))
    ball.shapesize(radius_of_balls[-1])
    ball.weight=random.randint(1,10)
    ball.color(color_func(ball.weight))
    x=random.randint(50-length/2, -50+length/2)
    y=random.randint(length/10,length)
    ball.goto(x,y)
    ball.dx=random.uniform(-2, 2)
    ball.dy=0

gravity=0.1
damping=1

while True:
    window.update() 
    what_ball=0 
    for ball in balls:
        ball.dy -=gravity
        ball.dy*=damping
        ball.dx*=damping
        damping*=0.999999
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
        pixels_offset=int(10*radius_of_balls[what_ball])
        what_ball+=1
        
        for i in range (0, len(balls)):
            for j in range(i+1, len(balls)):
                dist=10*(radius_of_balls[i]+radius_of_balls[i])+1
                if balls[i].distance(balls[j]) <= dist:
                    # Berechne die Richtung des Verschiebungsvektors
                    dx = balls[j].xcor() - balls[i].xcor()
                    dy = balls[j].ycor() - balls[i].ycor()
                    distance = (dx**2 + dy**2)**0.5

                    # Normierter Vektor
                    nx = dx / distance
                    ny = dy / distance

                    vi = balls[i].dx * nx + balls[i].dy * ny
                    vj = balls[j].dx * nx + balls[j].dy * ny

                    # Berechnung der neuen Geschwindigkeiten nach der Kollision
                    mi = balls[i].weight
                    mj = balls[j].weight
                    vi_new = (vi * (mi - mj) + 2 * mj * vj) / (mi + mj)
                    vj_new = (vj * (mj - mi) + 2 * mi * vi) / (mi + mj)

                    # Neue Geschwindigkeiten in x- und y-Richtung zerlegen
                    balls[i].dx += (vi_new - vi) * nx
                    balls[i].dy += (vi_new - vi) * ny
                    balls[j].dx += (vj_new - vj) * nx
                    balls[j].dy += (vj_new - vj) * ny

                    overlap = dist - distance
                    shift_x = (dx / distance) * (overlap / 2)
                    shift_y = (dy / distance) * (overlap / 2)

                    # Verschiebe die Bälle
                    balls[i].setx(balls[i].xcor() - shift_x)
                    balls[i].sety(balls[i].ycor() - shift_y)
                    balls[j].setx(balls[j].xcor() + shift_x)
                    balls[j].sety(balls[j].ycor() + shift_y)

        if ball.ycor()-pixels_offset <-height/2:
            ball.dy *=-1
            ball.sety(ball.ycor()+ball.dy*1.1)

        if abs(ball.xcor())+pixels_offset >length/2:
            ball.dx*=-1
            ball.setx(ball.xcor()+ball.dx*1.1)



if __name__ == "__main__":
    window.mainloop()

