import turtle as t
import random


def main():
    # variables
    x, y = (
        300,
        100
    )
    n_squares = 10
    square_size = 10
    layers = 3
    # player bots
    colors = [
        "green",
        "blue",
        "red",
        "yellow",
        "purple"
    ]
    # - - -
    screen = t.Screen()
    # build finsish line
    builder = t.Turtle()
    builder.hideturtle()
    builder.speed(-1)
    builder.penup()
    builder.right(90)
    for i in range(layers):
        builder.goto((x, y + square_size * (i % 2)))
        builder.left(90)
        builder.forward(square_size * i)
        builder.right(90)
        builder.pendown()
        for _ in range(n_squares + (i % 2)):
            # black square
            builder.pendown()
            builder.begin_fill()
            for _ in range(4):
                builder.forward(square_size)
                builder.right(90)
            builder.end_fill()
            builder.penup()
            builder.forward(square_size * 2)

    bots = []
    n_colors = len(colors)
    for i, color in enumerate(colors):
        bot = t.Turtle()
        bot.shape("turtle")
        bot.penup()
        bot.color(color)
        bot.speed(-1)
        bot.left(180)
        bot.forward(x)
        bot.right(90)
        bot.backward(round(square_size / 2) +
                     round(square_size * 1.5))  # remove half cell
        bot.forward(y)
        bot.backward(square_size * i * round(n_squares / n_colors) * 2)
        bot.right(90)
        bot.speed(1)
        bot.pendown()
        bots.append((bot, 0, color))  # make tuple

    # start race
    winner_color = "[NONE]"
    finished = False
    while not finished:
        for i in range(len(bots)):
            bot, num, color = bots[i]  # unpack
            # if random.randint(1, 3) == 1:
            #    continue
            dist = random.randint(0, 7)
            num += dist
            bot.forward(dist)
            if num >= (x * 2 + (square_size * layers) - square_size):
                winner_color = color
                finished = True
            else:
                bots[i] = bot, num, color  # pack
    builder.goto((0, square_size * n_colors * 2 + square_size))
    builder.write(winner_color.capitalize() + " won!",
                  align="center", font=("Comic Sans MS", 80, "normal"))
    screen.mainloop()


if __name__ == "__main__":
    main()
