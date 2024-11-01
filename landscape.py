import random
import pygame

bat_animation_counter = 0
moon_radius = 200
lights = (196, 181, 45)

eyes_radius = 2
eyes_appear = False

lightning_chance = 50

window_light_left = (0, 0, 0)
window_light_right = lights
light_animation_counter = 0

class Bat():
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.top = self.y - random.randint(10, 30) # Original values 20
        self.bottom = self.y + random.randint(10, 30) # Original values 20

    def move(self):
        self.x += self.vel_x

        if self.x > 800:
            self.vel_x *= -1
        if self.x < 0:
            self.vel_x *= -1
        
        self.y += self.vel_y

        if self.y > self.top:
            self.vel_y *= -1
        if self.y < self.bottom:
            self.vel_y *= -1

    def add_ears(self):
        self.ear1_points = [(self.x - 10, self.y - 10), (self.x - 5, self.y - 20), (self.x, self.y - 10)]
        self.ear2_points = [(self.x + 10, self.y - 10), (self.x + 5, self.y - 20), (self.x, self.y - 10)]

        return self.ear1_points, self.ear2_points
    
    def add_wings(self):
        self.wing1_points_up = [(self.x - 10, self.y), (self.x - 30, self.y - 10), (self.x - 10, self.y + 10)]
        self.wing2_points_up = [(self.x + 10, self.y), (self.x + 30, self.y - 10), (self.x + 10, self.y + 10)]
        self.wing1_points_down = [(self.x - 10, self.y), (self.x - 30, self.y + 10), (self.x - 10, self.y - 10)]
        self.wing2_points_down = [(self.x + 10, self.y), (self.x + 30, self.y + 10), (self.x + 10, self.y - 10)]

        return self.wing1_points_up, self.wing2_points_up, self.wing1_points_down, self.wing2_points_down

class Cloud():
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def draw(self):

        pygame.draw.circle(screen, (77, 69, 68), (self.x + 50, self.y + 5), 50)
        pygame.draw.circle(screen, (77, 69, 68), (self.x + 100, self.y + 5), 50)
        pygame.draw.circle(screen, (77, 69, 68), (self.x + 150, self.y + 5), 50)

    def move(self):
        self.x += self.vel_x

        if self.x > 800:
            self.x = -200

class Rain():
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def fall(self):

        self.x += self.vel_x

        self.y += self.vel_y

        if self.y > 600:
            self.y = 0

    def draw(self):
        pygame.draw.line(screen, (0, 100, 150), (self.x, self.y), (self.x - 10, self.y + 10), 2)

    def move(self):
        self.y += self.vel_y

        if self.y > 600:
            self.y = 0

class Pumpkin():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.ellipse(screen, (255, 50, 0), (self.x, self.y, 30, 40))
        pygame.draw.ellipse(screen, (255, 50, 0), (self.x + 10, self.y, 30, 40))
        pygame.draw.ellipse(screen, (255, 50, 0), (self.x + 20, self.y, 30, 40))
        pygame.draw.ellipse(screen, (255, 50, 0), (self.x + 30, self.y, 30, 40))
        pygame.draw.ellipse(screen, (255, 50, 0), (self.x + 40, self.y, 30, 40))

        pygame.draw.ellipse(screen, (0, 100, 0), (self.x + 30, self.y - 15, 10, 20))
        pygame.draw.ellipse(screen, (0, 100, 0), (self.x + 30, self.y - 15, 20, 10))

    def draw_face(self):
        pygame.draw.polygon(screen, (0, 0, 0), [(self.x + 20, self.y + 10), (self.x + 25, self.y + 15), (self.x + 15, self.y + 15)])
        pygame.draw.polygon(screen, (0, 0, 0), [(self.x + 45, self.y + 10), (self.x + 50, self.y + 15), (self.x + 40, self.y + 15)])

        
        pygame.draw.polygon(screen, (0, 0, 0), [(self.x + 15, self.y + 25), (self.x + 25, self.y + 25), (self.x + 20, self.y + 30)])
        pygame.draw.polygon(screen, (0, 0, 0), [(self.x + 25, self.y + 25), (self.x + 35, self.y + 25), (self.x + 30, self.y + 30)])
        pygame.draw.polygon(screen, (0, 0, 0), [(self.x + 35, self.y + 25), (self.x + 45, self.y + 25), (self.x + 40, self.y + 30)])
        pygame.draw.polygon(screen, (0, 0, 0), [(self.x + 45, self.y + 25), (self.x + 55, self.y + 25), (self.x + 50, self.y + 30)])

bat1 = Bat(300, 400, -10, -1)
bat2 = Bat(100, 100, -10, -1)
bat3 = Bat(500, 200, 10, -1)

cloud1 = Cloud(0, 25, 2, 2)
cloud2 = Cloud(200, 50, 2, 2)
cloud3 = Cloud(400, 25, 2, 2)
cloud4 = Cloud(600, 50, 2, 2)
cloud5 = Cloud(800, 25, 2, 2)

pumpkin = Pumpkin(450, 460)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((13, 34, 59))

    # Moon Glow  --------------------------------------------------------------------------------------------------------------
    n = 1
    quotient = 2 # Lower value = brighter moon
    for i in range(100, 0, -1):
        n += 1
        pygame.draw.circle(screen, (13 + n / quotient, 34 + n / quotient, 59 + n / quotient), (0, 0), moon_radius + i)

    # Lightning --------------------------------------------------------------------------------------------------------------
    if random.randint(0, lightning_chance) == 1:
        lightning_x = random.randint(0, 800)
        lightning_y = 75
        
        pygame.draw.line(screen, (255, 255, 255), (lightning_x, lightning_y), (lightning_x, lightning_y + 50), 5)
        pygame.draw.line(screen, (255, 255, 255), (lightning_x, lightning_y + 50), (lightning_x + 50, lightning_y + 100), 5)
        pygame.draw.line(screen, (255, 255, 255), (lightning_x + 50, lightning_y + 100), (lightning_x, lightning_y + 250), 5)
        pygame.draw.line(screen, (255, 255, 255), (lightning_x, lightning_y + 250), (lightning_x + 50, lightning_y + 425), 5)

        if lightning_chance == 50:
            lightning_chance = 100
        else:
            lightning_chance = 50 

    # Draw Ground  --------------------------------------------------------------------------------------------------------------
    ground = pygame.Rect(0, 500, 800, 100)
    pygame.draw.rect(screen, (43, 90, 3), ground)

    # Draw House  --------------------------------------------------------------------------------------------------------------

    # Front wall
    front_wall = pygame.Rect(200, 300, 200, 200)
    # Door
    door = pygame.Rect(275, 425, 50, 75)
    # Window 1 Outline
    window1_border = pygame.Rect(225, 350, 55, 55)
    window1_verticle = pygame.Rect(250, 350, 5, 55)
    window1_horizontal = pygame.Rect(225, 375, 55, 5)
    
    window1_top_left = pygame.Rect(230, 355, 20, 20)
    window1_bottom_left = pygame.Rect(230, 380, 20, 20)
    window1_top_right = pygame.Rect(255, 355, 20, 20)
    window1_bottom_right = pygame.Rect(255, 380, 20, 20)
    
    # Window 2 Outline 
    window2_border = pygame.Rect(325, 350, 55, 55)
    window2_verticle = pygame.Rect(350, 350, 5, 55)
    window2_horizontal = pygame.Rect(325, 375, 55, 5)

    window2_top_left = pygame.Rect(330, 355, 20, 20)
    window2_bottom_left = pygame.Rect(330, 380, 20, 20)
    window2_top_right = pygame.Rect(355, 355, 20, 20)
    window2_bottom_right = pygame.Rect(355, 380, 20, 20)


    pygame.draw.rect(screen, (107, 60, 29), front_wall)

    pygame.draw.rect(screen, (97, 50, 19), door)

    pygame.draw.rect(screen, (97, 50, 19), window1_border)
    pygame.draw.rect(screen, window_light_left, window1_top_left)
    pygame.draw.rect(screen, window_light_left, window1_bottom_left)
    pygame.draw.rect(screen, window_light_left, window1_top_right)
    pygame.draw.rect(screen, window_light_left, window1_bottom_right)

    pygame.draw.rect(screen, (97, 50, 19), window2_border)
    pygame.draw.rect(screen, window_light_right, window2_top_left)
    pygame.draw.rect(screen, window_light_right, window2_bottom_left)
    pygame.draw.rect(screen, window_light_right, window2_top_right)
    pygame.draw.rect(screen, window_light_right, window2_bottom_right)

    roof_points = [(180, 320), (420, 320), (300, 200)]
    pygame.draw.polygon(screen, (125, 30, 26), roof_points)
    


    # Draw Moon  --------------------------------------------------------------------------------------------------------------
    pygame.draw.circle(screen, (255, 255, 255), (0, 0), moon_radius)

    # Moon Details  --------------------------------------------------------------------------------------------------------------
    pygame.draw.circle(screen, (181, 177, 177), (80, 30), 30)
    pygame.draw.ellipse(screen, (181, 177, 177), (150, 40, 20, 60))
    pygame.draw.ellipse(screen, (181, 177, 177), (0, 130, 100, 50))
    pygame.draw.circle(screen, (181, 177, 177), (100, 100), 30)
    pygame.draw.circle(screen, (181, 177, 177), (170, 0), 30)
    pygame.draw.ellipse(screen, (181, 177, 177), (0, 5, 50, 120))

    # Clouds ----------------------------------------------------------------------------------------------------------------------

    cloud1.draw()
    cloud1.move()

    cloud2.draw()
    cloud2.move()

    cloud3.draw()
    cloud3.move()

    cloud4.draw()
    cloud4.move()

    cloud5.draw()
    cloud5.move()
    

    # Draw Bats  --------------------------------------------------------------------------------------------------------------
    pygame.draw.circle(screen, (0, 0, 0), (bat1.x, bat1.y), 12)

    pygame.draw.circle(screen, (0, 0, 0), (bat2.x, bat2.y), 12)

    pygame.draw.circle(screen, (0, 0, 0), (bat3.x, bat3.y), 12)

    # Draw Bat Ears  --------------------------------------------------------------------------------------------------------------
    bat1_ear1_points, bat1_ear2_points = bat1.add_ears()
    bat2_ear1_points, bat2_ear2_points = bat2.add_ears()
    bat3_ear1_points, bat3_ear2_points = bat3.add_ears()

    pygame.draw.polygon(screen, (0, 0, 0), bat1_ear1_points)
    pygame.draw.polygon(screen, (0, 0, 0), bat1_ear2_points)

    pygame.draw.polygon(screen, (0, 0, 0), bat2_ear1_points)
    pygame.draw.polygon(screen, (0, 0, 0), bat2_ear2_points)

    pygame.draw.polygon(screen, (0, 0, 0), bat3_ear1_points)
    pygame.draw.polygon(screen, (0, 0, 0), bat3_ear2_points)

    # Draw Bat Wings --------------------------------------------------------------------------------------------------------------

    bat1_wing1_points_up, bat1_wing2_points_up, bat1_wing1_points_down, bat1_wing2_points_down = bat1.add_wings()
    bat2_wing1_points_up, bat2_wing2_points_up, bat2_wing1_points_down, bat2_wing2_points_down = bat2.add_wings()
    bat3_wing1_points_up, bat3_wing2_points_up, bat3_wing1_points_down, bat3_wing2_points_down = bat3.add_wings()

    # Animate bat wings --------------------------------------------------------------------------------------------------------------
    if bat_animation_counter > 10 and bat_animation_counter < 20:
        bat1_current_animation1 = bat1_wing1_points_down
        bat1_current_animation2 = bat1_wing2_points_down

        bat2_current_animation1 = bat2_wing1_points_down
        bat2_current_animation2 = bat2_wing2_points_down

        bat3_current_animation1 = bat3_wing1_points_down
        bat3_current_animation2 = bat3_wing2_points_down

    elif bat_animation_counter <= 10 or bat_animation_counter == 20:
        bat1_current_animation1 = bat1_wing1_points_up
        bat1_current_animation2 = bat1_wing2_points_up

        bat2_current_animation1 = bat2_wing1_points_up
        bat2_current_animation2 = bat2_wing2_points_up

        bat3_current_animation1 = bat3_wing1_points_up
        bat3_current_animation2 = bat3_wing2_points_up

    else:
        bat_animation_counter = 0

    # Light Flicker Animation -------------------------------------------------------------------------------------------------------------------------------

    if light_animation_counter == 60 or light_animation_counter == 330:
        window_light_left = lights
        if light_animation_counter == 330:
            eyes_appear = False
        
    elif light_animation_counter == 90 or light_animation_counter == 360:
        window_light_left = (0, 0, 0)
        if light_animation_counter == 90:
            eyes_appear = True
    
    if eyes_appear == True:
        pygame.draw.circle(screen, (255, 0, 0), (243, 370), eyes_radius)
        pygame.draw.circle(screen, (255, 0, 0), (262, 370), eyes_radius)
    
    if light_animation_counter == 160 or light_animation_counter == 380:
        window_light_right = (0, 0, 0)

    elif light_animation_counter == 180 or light_animation_counter == 400:
        window_light_right = lights

    elif light_animation_counter == 185 or light_animation_counter == 405:
        window_light_right = (0, 0, 0)

    elif light_animation_counter == 190 or light_animation_counter == 410:
        window_light_right = lights

    elif light_animation_counter == 195 or light_animation_counter == 415:
        window_light_right = (0, 0, 0)

    elif light_animation_counter == 200 or light_animation_counter == 420:
        window_light_right = lights

    elif light_animation_counter == 205 or light_animation_counter == 425:
        window_light_right = (0, 0, 0)

    elif light_animation_counter == 210 or light_animation_counter == 430:
        window_light_right = lights

    elif light_animation_counter == 215 or light_animation_counter == 435:
        window_light_right = (0, 0, 0)

    elif light_animation_counter == 220 or light_animation_counter == 440:
        window_light_right = lights



    if light_animation_counter > 440:
        light_animation_counter = 0

    pygame.draw.polygon(screen, (0, 0, 0), bat1_current_animation1)
    pygame.draw.polygon(screen, (0, 0, 0), bat1_current_animation2)

    pygame.draw.polygon(screen, (0, 0, 0), bat2_current_animation1)
    pygame.draw.polygon(screen, (0, 0, 0), bat2_current_animation2)

    pygame.draw.polygon(screen, (0, 0, 0), bat3_current_animation1)
    pygame.draw.polygon(screen, (0, 0, 0), bat3_current_animation2)

    # Draw Pumpkin  --------------------------------------------------------------------------------------------------------------
    pumpkin.draw()
    pumpkin.draw_face()

    # Draw Rain  --------------------------------------------------------------------------------------------------------------

    for i in range(50):
        rain = Rain(random.randint(0, 800), random.randint(75, 600), 0, 5)
        rain.draw()
        rain.move()

    # Move Bats --------------------------------------------------------------------------------------------------------------

    bat1.move()
    bat2.move()
    bat3.move()

    bat_animation_counter += 1
    light_animation_counter += 1

    clock.tick(60)
    pygame.display.flip()