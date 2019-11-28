# Client side for a multiplayer game.

import pygame
from network import Network

# Global Variables
width = 500
height = 500

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

client_id = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redraw_window(win, player, player2):
    win.fill(WHITE)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    net = Network()
    start_pos = read_pos(net.get_pos())
    player = Player(start_pos[0], start_pos[1], 100, 100, GREEN)
    player_two = Player(0, 0, 100, 100, RED)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        p2_pos = read_pos(net.send(make_pos((player.x, player.y))))
        player_two.x = p2_pos[0]
        player_two.y = p2_pos[1]
        player_two.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move()
        redraw_window(win, player, player_two)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

main()
