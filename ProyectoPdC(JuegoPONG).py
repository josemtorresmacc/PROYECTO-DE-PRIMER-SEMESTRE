import pygame, sys, random, time
form tkinter import*
raiz=Tk()
raiz.title("Arcademy")
raiz.iconbitmap("Joistic.ico")
#raiz.geometry("800x650")
raiz.config(bg="black")
raiz.config(bd=25)
raiz.config(relief="sunken")
raiz.config(cursor="pirate")

miframe = Frame()
miframe.pack(side="top")
miframe.config(bg= "blue")
miframe.config(width="500", height="200")
miframe.config(bd=15)
miframe.config(relief="groove")
miframe.config(cursor="star")

milabel = Label(miframe, text="Arcademy", fg="purple", font=("Castellar", 32))
milabel.place(x="100", y="70")

raiz.mainloop()

rng=random.Random()
COLOR= rng.randrange(0,250)
COLOOR= rng.randrange(0,250)
COLOOOR=rng.randrange(0,250)


def pltantmon():
    global plt_speed_x,plt_speed_y,marcadorj1,marcadorj2ia
    plt.x += plt_speed_x 
    plt.y += plt_speed_y
    if plt.top <= 0 or plt.bottom >= screen_height:
        plt_speed_y *= -1
    if plt.left <= 0:
        marcadorj1 += 1
        text_surface = font.render(u'punto a favor', True, (COLOR,COLOOR,COLOOOR))
        screen.blit(text_surface,(screen_width/2 + 10,screen_height/2 - 40))
        pygame.display.flip()
        time.sleep(2)
        plt_restart()
    if plt.right >= screen_width:
        marcadorj2ia += 1
        text_surface = font.render(u'punto en contra', True, (COLOR,COLOOR,COLOOOR))
        screen.blit(text_surface,(screen_width/2 - 170,screen_height/2 + 40))
        pygame.display.flip()
        time.sleep(2)
        plt_restart()
    if plt.colliderect(player1) or plt.colliderect(player2):
        plt_speed_x += 1
        plt_speed_x *= -1
    if marcadorj1== 10:
        text_surface = font2.render(u'Felicidades ganaste', True, (COLOR,COLOOR,COLOOOR))
        screen.blit(text_surface,(screen_width/2 -350 ,screen_height/2 -20))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
    if marcadorj2ia== 10:
        text_surface = font2.render(u"Perdiste", True, (COLOR,COLOOR,COLOOOR))
        screen.blit(text_surface,(screen_width/2 -120 ,screen_height/2 -20))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
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

def player2IA():
    if player2.top < plt.y:
        player2.top += IA_speed
    if player2.bottom > plt.y:
        player2.bottom -= IA_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def plt_restart():
    global plt_speed_x,plt_speed_y
    plt.center = (screen_width/2, screen_height/2)
    plt_speed_y *= random.choice((1,-1))
    plt_speed_x *= random.choice((1,-1))

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
font2= pygame.font.Font(None,100)

#P4NTA/L%A
screen_width = 1300
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PONG")

#Gam7
plt = pygame.Rect(screen_width/2 - 20, screen_height/2 - 20, 40, 40)
player1 = pygame.Rect(screen_width - 40,screen_height/2 - 70, 20,140)
player2 = pygame.Rect(20, screen_height/2 - 70, 20, 140)

#sp33dm4cs
plt_speed_x = 7 * random.choice((1,-1))
plt_speed_y = 7 * random.choice((1,-1))
player1_speed = 0
player2_speed = 0
IA_speed = 7

#c0l03
bg_color = pygame.Color("black")
ligth_grey = (200, 200, 200)

#Punt3
marcadorj1 = 0
marcadorj2ia = 0
fuente = pygame.font.Font("freesansbold.ttf",20)

#l0000p
while True:
    for event in pygame.event.get():
        COLOR= rng.randrange(0,250)
        COLOOR= rng.randrange(0,250)
        COLOOOR=rng.randrange(0,250)
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

    pltantmon()
    player1antmon()
    player2IA()

    screen.fill(bg_color)
    pygame.draw.rect(screen,ligth_grey,player1)
    pygame.draw.rect(screen,ligth_grey,player2)
    pygame.draw.polygon(screen,(COLOR,COLOOR,COLOOOR),[(40,325),(650,0),(1260,325),(650,650)],4)
    pygame.draw.ellipse(screen,ligth_grey,plt)
    pygame.draw.aaline(screen,ligth_grey,(screen_width/2,0),(screen_width/2,screen_height))
   
    
    
    Jugador_1 = fuente.render(str(marcadorj1),True,ligth_grey)
    screen.blit(Jugador_1,(screen_width/2 + 20,screen_height/2))
    
    Jugador_2_ia = fuente.render(str(marcadorj2ia),True,ligth_grey)
    screen.blit(Jugador_2_ia,(screen_width/2 - 30,screen_height/2))
    
    pygame.display.flip()
    clock.tick(60)
