#       Goals
# 1. Platform moves 
# 2. Create a ball + making it moves
# 3. Hitting ball mechanics
# 4. Lose-win conditions


from pygame import *

win = display.set_mode((700, 500))
win.fill((39, 137, 33))

paddle_height = 80

#create character
class Character(sprite.Sprite):
    #create init function takes in x, y, width, height, speed
    def __init__ (self, x, y, width, height, color, speed):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.speed = speed
        

    def draw(self):
        draw.rect(win, self.color, self.rect)


class Player1(Character):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys[K_DOWN] and self.rect.y < 500 - self.rect.height:
            self.rect.y += self.speed
            
        
class Player2(Character):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 500 - self.rect.height:
            self.rect.y += self.speed
            

class Ball(sprite.Sprite):
    def __init__ (self, x, y, color, radius, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speedx = speed
        self.speedy = speed
        self.rect = Rect(x, y, self.radius*2, self.radius*2)

        
    def draw(self):
        draw.circle(win, self.color, (self.rect.x, self.rect.y) , self.radius, 0)
        

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x <= 0 or self.rect.x >= 700:
            self.speedx *= (-1)

        if self.rect.y <= 0 or self.rect.y >= 500:
            self.speedy *= (-1)

        
        




# class wall(sprite.Sprite):
#     def __init__(self,x, y, width, height,  color):
#         super().__init__()
#         self.color = color
#         self.rect = Rect(x, y, width, height)

#     def draw(self):
#         draw.rect(win, self.color, self.rect)

font.init()
font1 = font.Font(None, 45)
player1_score_txt = font1.render("Score 1: ", True, (255, 255, 255))
player2_score_txt = font1.render("Score 2: ", True, (255, 255, 255))
level_txt = font1.render("Level: ", True, (255, 255, 255))


player1_winning = font1.render("Player 1 wins!", True, (255, 255, 255))
player2_winning = font1.render("Player 2 wins!", True, (255, 255, 255))

player1_score = 0
player2_score = 0


paddle1 = Player1(670, 250, 10, 80, (240, 240, 122), 50)
paddle2 = Player2(30, 250, 10, 80, (240, 240, 122), 50)
ball = Ball(350, 250, (255, 255, 255), 10, 15)


# wall1 = wall(0, 0, 700, 1, (39, 137, 33))
run = True
finish = True
level = 0
clock = time.Clock()

win.fill((0, 0, 0))
text1 = font1.render("Press 'space' to start", True, (255, 255, 255))
text2 = font1.render("Use the arrow keys + WASD to move", True, (255, 255, 255))
text3 = font1.render("Press 'p' to pause and 'r' to unpause", True, (255, 255, 255))
level_txt = font1.render("Level: {}".format(level), True, (255, 255, 255))


win.blit(text1, (180, 100))
win.blit(text2, (85, 200))
win.blit(text3, (85, 300))
# win.blit(level_txt, (300, 10))
display.update()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


        if e.type == KEYDOWN:
            if e.key == K_SPACE and finish:
                finish = False
                player1_score_txt = font1.render("Score 1: ", True, (255, 255, 255))
                player2_score_txt = font1.render("Score 2: ", True, (255, 255, 255))
                player1_score = 0
                player2_score = 0
                ball.speedx += 5
                ball.speedy += 5
                ball.rect.x = 350
                ball.rect.y = 250
                # level_txt = 0
                level += 1
                level_txt = font1.render("Level: {}".format(level), True, (255, 255, 255))
                win.blit(level_txt, (300, 10))
                if level == 5:
                    paddle_height = paddle_height / 2
                    paddle1 = Player1(670, 250, 10, paddle_height, (240, 240, 122), 50)
                    paddle2 = Player2(30, 250, 10, paddle_height, (240, 240, 122), 50)

                

        
    #pause funtion
        if e.type == KEYDOWN:
            if e.key == K_p:
                finish = True
        
        if e.type == KEYDOWN:
            if e.key == K_r:
                finish = False


    

    win.fill((39, 137, 33))

    win.blit(player1_score_txt, (50, 50))
    win.blit(player2_score_txt, (500, 50))
    win.blit(level_txt, (300, 10))
    

    paddle1.draw()
    paddle2.draw()

    ball.draw()
    paddle1.update()
    paddle2.update()
    ball.update()
    if not finish:
        if sprite.collide_rect(paddle1, ball):
            ball.speedx *= (-1)
        if sprite.collide_rect(paddle2, ball):
            ball.speedx *= (-1)

    #player 1
        if ball.rect.x <= 0:
            player2_score += 1
            player2_score_txt = font1.render("Score 2: " + str(player2_score), True, (255, 255, 255))
        #player 2
        if  ball.rect.x >= 700:
            player1_score += 1
            player1_score_txt = font1.render("Score 1: " + str(player1_score), True, (255, 255, 255))

        #winning condition
        if player1_score >= 5:
            finish = True
            win.blit(player1_winning, (250, 250))
            

        if player2_score >= 5:
            finish = True
            win.blit(player2_winning, (250, 250))
            
        #how many frame refresh per second
        clock.tick(15) #15 frames per second

        display.update()