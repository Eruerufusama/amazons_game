from classes import GameManager
import tkinter as tk


# Create board of size (4, 6, 8, or 10)
game = GameManager(size=10)

game.players[0].pieces[0].move()