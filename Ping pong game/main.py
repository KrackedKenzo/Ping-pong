from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_game_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_game_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def Player1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def Player2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 600
win_height = 500
back = transform.scale(image.load('eilzykidspacebackground.jpeg'), (win_width,win_height))
window = display.set_mode((win_width, win_height))
window.blit(back, (0,0))

game = True
finish = False
clock = time.Clock()
fps = 60

Player_1 = Player('pong rod.png', 30, 200, 4, 50, 150)
Player_2 = Player('pong rod.png', 520, 200, 4, 50, 150)
Ball = GameSprite('pong boll.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(back, (0,0))
        Player_1.Player1()
        Player_2.Player2()
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y
        
        if sprite.collide_rect(Player_1, Ball) or sprite.collide_rect(Player_2, Ball):
            speed_x *= -1
            speed_y *= 1

        if Ball.rect.y > win_height - 50 or Ball.rect.y < 0:
            speed_y *= -1
        
        if Ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
            game_over = True

        if Ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True
        
        Player_1.reset()
        Player_2.reset()
        Ball.reset()

    display.update()
    clock.tick(fps)