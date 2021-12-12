import turtle
import winsound

# Configuração Janela do Jogo
wn = turtle.Screen()
wn.title("Pong by Ivan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Repetiçao do ínicio do Jogo

# Barra A
bar_a = turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
bar_a.shapesize(stretch_wid=5, stretch_len=1)
bar_a.color("red")
bar_a.penup()
bar_a.goto(-350, 0)

# Barra B
bar_b = turtle.Turtle()
bar_b.speed(0)
bar_b.shape("square")
bar_b.shapesize(stretch_wid=5, stretch_len=1)
bar_b.color("blue")
bar_b.penup()
bar_b.goto(350, 0)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jogador 1 - 0 x 0 - Jogador 2",
          align="center", font=("Courier", 20, "normal"))

# Funções
# ------------
# Movimento das Barras


# Barra A


def bar_a_up():
    y = bar_a.ycor()
    y += 20
    bar_a.sety(y)


def bar_a_down():
    y = bar_a.ycor()
    y -= 20
    bar_a.sety(y)


# Controles do Jogo
wn.listen()
wn.onkeypress(bar_a_up, "w")
wn.onkeypress(bar_a_down, "s")


# Barra B

def bar_b_up():
    y = bar_b.ycor()
    y += 20
    bar_b.sety(y)


def bar_b_down():
    y = bar_b.ycor()
    y -= 20
    bar_b.sety(y)


# Controles do Jogo
wn.listen()
wn.onkeypress(bar_b_up, "Up")
wn.onkeypress(bar_b_down, "Down")

while True:
    wn.update()

    # Movimento da Bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Controle de colisão com as laterais
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Jogador 1 - {} x {} - Jogador 2".format(score_a, score_b),
                  align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Jogador 1 - {} x {} - Jogador 2".format(score_a, score_b),
                  align="center", font=("Courier", 20, "normal"))

    # Colisão entre barra e bola
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bar_b.ycor() + 40
                                                      and ball.ycor() > bar_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bar_a.ycor() + 40
                                                        and ball.ycor() > bar_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
