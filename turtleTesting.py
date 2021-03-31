import turtle

#setup turtle screen

game_play = turtle.Screen()
#game.color("#5493FF")
game_play.bgcolor("black")
game_play.title("Welcome to my game")

#create player turtle
player = turtle.Turtle()
player.color("white")
player.shape("blank")

player.forward(100)

turtle.done()