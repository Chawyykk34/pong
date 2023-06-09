from pygame import *
from random import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("PingPong")
background = transform.scale(image.load("FON.jpg"), (700, 500))


game = True
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 695:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 695:
            self.rect.y += self.speed

finish = False
game = True

rocket1 = Player("racket1.jpg", 520, 200, 150, 50, 4)
rocket2 = Player("racket1.jpg", 30, 200, 150, 50, 4)
ball = GameSprite("BALL.jpg", 200, 200, 50, 50, 4)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True,(180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True,(180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.blit(background,(0,0))
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += speed_x
        ball.rect.x += speed_y

        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > 680 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > 680:
            window.blit(lose1, (200, 200))
            finish = True
        
        rocket1.reset()
        rocket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
        



