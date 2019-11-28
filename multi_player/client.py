# Client side for a multiplayer game.
import pygame
from network import Network
from player import Player

# Global Variables
width = 500
height = 500

# Colors
WHITE = (255, 255, 255)

def redraw_window(win, player, player2):
    win.fill(WHITE)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    net = Network()
    pl_one = net.get_plyr()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        pl_two = net.send(pl_one)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        pl_one.move()
        redraw_window(win, pl_one, pl_two)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

main()
