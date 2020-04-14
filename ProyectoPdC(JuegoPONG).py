import pygame, sys 

def pltantmon():
    global plt_speed_x,plt_speed_y #Variable que se encontró en un video tutorial de Pygame
    plt.x += plt_speed_x
    plt.y += plt_speed_y
    if plt.top <= 0 or plt.bottom >= screen_height:
        plt_speed_y *= -1
    if plt.left <= 0 or plt.right >= screen_width:
        plt_speed_x *= -1
    if plt.colliderect(player1) or plt.colliderect(player2):
        plt_speed_x += 1
        plt_speed_x *= -1

def player1antmon():
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

def player2antmon():
    player2.y += player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height
        
#(esta acción es de la computadora donde se le dará al jugador la opción
# de poder jugar contra la computadora; donde se le da la "inteligencia" de mover la paleta
# en torno a "y" siguiendo la pelota
def player2IA():
    if player2.top < plt.y:
        player2.top += IA_speed
    if player2.bottom > plt.y:
        player2.bottom -= IA_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height
        
pygame.init()
clock = pygame.time.Clock()

#P4NTA/L%A
screen_width = 1300
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PONG")

#Gam
plt = pygame.Rect(screen_width/2 - 20, screen_height/2 - 20, 40, 40)
player1 = pygame.Rect(screen_width - 40,screen_height/2 - 70, 20,140)
player2 = pygame.Rect(20, screen_height/2 - 70, 20, 140)

bg_color = pygame.Color("black")
ligth_grey = (200, 200, 200)

#sp33dm4cs

plt_speed_x = 7
plt_speed_y = 7
player1_speed = 0
player2_speed = 0
IA_speed = 7
#l0000p
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 7
            elif event.key == pygame.K_UP:
                player1_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
            elif event.key == pygame.K_UP:
                player1_speed += 7
    #Un problema de pygame es el de hacer los ciclos y hasta no terminarlos no se puede 
    #hacer otro por esto mismo se hacen dos "event.type"
    pltantmon()
    player1antmon()
#    player2antmon()
    player2IA()
        
    screen.fill(bg_color)
    pygame.draw.rect(screen,ligth_grey,player1)
    pygame.draw.rect(screen,ligth_grey,player2)
    pygame.draw.ellipse(screen,ligth_grey,plt)
    pygame.draw.aaline(screen,ligth_grey,(screen_width/2,0),(screen_width/2,screen_height))
    
    pygame.display.flip()
    clock.tick(60)
