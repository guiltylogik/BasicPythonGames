# Client side for a multiplayer game.
import pygame
from network import Network
from player import Player

# Global Variables
width = 650
height = 650

pygame.font.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
GREY = (128, 128, 128)

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 45)
        text = font.render(self.text, 1, WHITE)
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), (self.y + round(self.height/2) - round(text.get_height()/2))))

    def click(self, pos):
        x_one = pos[0]
        y_one = pos[1]

        if self.x <= x_one <= self.x + self.width and self.y <= y_one <= self.y + self.height:
            return True
        else:
            return False

def redraw_window(win, game, player):
    win.fill(GREY)

    if not (game.connected()):
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Wiating for player...", 1, RED, True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", 1, CYAN)
        win.blit(text, (80, 200))

        text = font.render("Opponent", 1, CYAN)
        win.blit(text, (380, 200))

        p_one_move = game.get_player_move(0)
        p_two_move = game.get_player_move(1)

        if game.both_p_moved():
            text_1 = font.render(p_one_move, 1, (0, 245, 200))
            text_2 = font.render(p_two_move, 1, (0, 245, 200))
        else:
            if game.p_one_moved and player == 0:
                text_1 = font.render(p_one_move, 1, (0,0,0))
            elif game.p_one_moved:
                text_1 = font.render("Locked", 1, (0,0,0))
            else:
                text_1 = font.render("Waiting...", 1, (0,0,0))

            if game.p_two_moved and player == 1:
                text_2 = font.render(p_two_move, 1, (0,0,0))
            elif game.p_two_moved:
                text_2 = font.render("Locked", 1, (0,0,0))
            else:
                text_2 = font.render("Waiting...", 1, (0,0,0))

        if player == 1:
            win.blit(text_2, (100, 350))
            win.blit(text_1, (400, 350))
        else:
            win.blit(text_1, (100, 350))
            win.blit(text_2, (400, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()

btns = [Button("Rock", 50, 500, RED),
        Button("Scissors", 250, 500, BLUE),
        Button("Paper", 450, 500, GREEN)]

def main():
    run = True
    clock = pygame.time.Clock()
    net = Network()
    player = int(net.get_plyr())
    print("You are player: ", player)

    while run:
        clock.tick(60)
        try:
            game = net.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.both_p_moved():
            redraw_window(win, game, player)
            pygame.time.delay(200)
            try:
                game = net.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 80)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, RED)
            elif game.winner() == -1:
                text = font.render("Tie Game", 1, RED)
            else:
                text = font.render("You Lost!", 1, RED)

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p_one_moved:
                                net.send(btn.text)
                        else:
                             if not game.p_two_moved:
                                 net.send(btn.text)

        redraw_window(win, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill(GREY)
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play", 1, RED)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
