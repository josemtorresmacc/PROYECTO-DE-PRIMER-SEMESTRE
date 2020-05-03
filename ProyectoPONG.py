# -*- coding: utf-8 -*-
import pygame
import random
import sys

        #INICIO DE PIGAME 
Principalclock = pygame.time.Clock()
pygame.init()  
pygame.display.set_caption("PROYECTO ARCADEMY")
        # DIMIECIONES DE LA PANTALLA
screen_width = 1300
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
fuente = pygame.font.Font("freesansbold.ttf",20)

        # RECTANGULOS DE JUEGO 
plt = pygame.Rect(screen_width/2 - 20, screen_height/2 - 20, 40, 40)
player1 = pygame.Rect(screen_width - 40,screen_height/2 - 70, 5,140)
player2 = pygame.Rect(20, screen_height/2 - 70, 5, 140)


        # CONTADORES 
plt_speed_x = 7 * random.choice((1,-1))
plt_speed_y = 7 * random.choice((1,-1))
player1_speed = 0
player2_speed = 0
IA_speed = 7
marcadorj1 = 0
marcadorj2ia = 0

    # APARTADO DE COLORES DE LAS
   #BIBLIOTECAS RANDOM Y PYGAME
rng=random.Random()
COLOR = rng.randrange(0,255)
COLOOR = rng.randrange(0,255)
COLOOOR = rng.randrange(0,255)
ligth_grey = (250, 250, 250)
bg_color = pygame.Color("dark slate gray")
white = (255, 255, 255)

def pltantmon(): #SE DEFINE EL MOVIMIENTO QUE VA A TENER LA PELOTA CUANDO SE ENCUENTRE CON UN RECTÁNGULO O CON UN BORDE DE LA VENTANA 
    #SE MUKTIPLICA POR -1 YA QUE ES EL QUE ALTERARÁ LA DIRECCIÓN DE LA PELOTA SIN AUNMENTARLA 
    global plt_speed_x, plt_speed_y, marcadorj1, marcadorj2ia, screen_width, screen_height
    plt.x += plt_speed_x 
    plt.y += plt_speed_y
    if plt.top <= 0 or plt.bottom >= screen_height:
        plt_speed_y *= -1
    if plt.left <= 0:
        marcadorj1 += 1
        plt_restart()
    if plt.right >= screen_width:
        marcadorj2ia += 1
        plt_restart()
    if plt.colliderect(player1) or plt.colliderect(player2): #CAMBIO DE DIRECCIÓN SI LA PELOTA CHOCA CON LOS RECTÁNGULOS DE LOS JUGADORES
        plt_speed_x *= -1
        
def player1antmon(): #SE DEFINEN LOS LÍMITES DE LAS PALETAS, ES DECIR, LAS PALETA DEL JUGADOR NO VA A PASAR DE LOS BORDES DE LA PANTALLA
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height
        
def player2antmon(): #SE DEFINEN LOS LÍMITES DE LAS PALETAS, ES DECIR LA PALETA DEL JUGADOR 2 NO VA A PASAR DE LOS BORDES DE LA PANTALLA
    #SOLO SIRVE PARA LA FUNCIÓN PONG2P
    player2.y += player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def player2IA(): #SE DEFINE EL MOVIMIENTO DE LA "MÁQUINA" LA CUAL SIGUE LA PELATA EN EL EJE y
    #SE DEFINEN LOS LÍMITES DE LAS PALETAS, ES DECIR LA PALETA DEL JUGADOR 2 NO VA A PASAR DE LOS BORDES DE LA PANTALLA
    #SOLO SIRVE PARA LA FUNCIÓN PONG
    if player2.top < plt.y:
        player2.top += IA_speed
    if player2.bottom > plt.y:
        player2.bottom -= IA_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def plt_restart(): #REINICIA LA PELATO ALTERANDO DE FORMA ALEATORIA LA DIRECCIÓN DE SALIDA
    global plt_speed_x,plt_speed_y
    plt.center = (screen_width/2, screen_height/2)
    plt_speed_y *= random.choice((1,-1))
    plt_speed_x *= random.choice((1,-1))
    
def texto(text , fuente, color, surface, x, y): #SE DEFINE LA FUNCIÓN DE PINTAR TEXT PARA EL MENÚ
    textobj = fuente.render(text, 1, color)
    recttext = textobj.get_rect()
    recttext.topleft = (x, y)
    surface.blit(textobj, recttext)

def MENÚPREINCIPAL():#SERÁ EL MENÚ DE OPCIONES
    while True:
        global click
        screen.fill(bg_color)
        texto("Menú principal", fuente, ligth_grey, screen, 20, 20)
        mx, my = pygame.mouse.get_pos()

        Boton1 = pygame.Rect(50,100,200,50)
        Boton2 = pygame.Rect(50,200,200,50)
#        Boton3 = pygame.Rect(50,300,200,50)
#        Boton4 = pygame.Rect(50,400,200,50)
#        Boton4 = pygame.Rect(50,500,200,50)
        if Boton1.collidepoint((mx, my)):
            if click:
                PONG()
        if Boton2.collidepoint((mx, my)):
            if click:
                PONG_1vs1()
#         if Boton3.collidepoint((mx, my)):
#             if click:
#                 Battle()
#         if Boton4.collidepoint((mx, my)): 
#             if click:
#                 Batlle_1vs1()
#        if Boton5.collidepoint((mx, my)):
#            if click:
#                 snake()
        pygame.draw.rect(screen,ligth_grey,Boton1)
        pygame.draw.rect(screen,ligth_grey,Boton2)
#        pygame.draw.rect(screen,ligth_grey,Boton3)
#        pygame.draw.rect(screen,ligth_grey,Boton4)
#        pygame.draw.rect(screen,ligth_grey,Boton5)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()
            if event.type ==  pygame.KEYDOWN:
                if event.type ==  pygame.K_ESCAPE:
                    pygame.exit()
                    sys.exit()
            if event.type == pygame.MOUSEBOTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        Principalclock.tick(60)

def PONG(): #INICIO DEL JUEGO PONG PARA UN SOLO JUGADOR
    global screen_height, screen_width
    running = True 
    #CICLO REPETIRIVO DEL JUEGO
    while running:
        global player1_speed, COLOR, COLOOR, COLOOOR
        texto("PONG", fuente, ligth_grey, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()
            if event.type ==  pygame.KEYDOWN:
                if event.type ==  pygame.K_ESCAPE:
                    running = False        
            COLOR= rng.randrange(0,255)
            COLOOR= rng.randrange(0,255)
            COLOOOR=rng.randrange(0,255)

        #SE COMIENZAN A OIR LOS EVENTOS DEL TECLADO PARA EL JUGADOR 1 
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
                    
        # SE LLAMAN A LASFUCIONES 
        pltantmon()
        player1antmon()
        player2IA()
        
        #SE COMIENZA A DIBUJAR EN PANTALLA 
        screen.fill(bg_color)
        pygame.draw.polygon(screen,(COLOR,COLOOR,COLOOOR),[(40,325),(650,0),(1260,325),(650,650)],3)
        pygame.draw.rect(screen,ligth_grey,player1)
        pygame.draw.rect(screen,ligth_grey,player2) 
        pygame.draw.ellipse(screen,white,plt)
        pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2,screen_height))
    
        #SE DIBUJA EL MARCADOR 
        Jugador_1 = fuente.render(str(marcadorj1),True,ligth_grey)
        screen.blit(Jugador_1,(screen_width/2 + 20,screen_height/2))
        #SE DIBUJA EL MARCADOR 
        IA = fuente.render(str(marcadorj2ia),True,ligth_grey)
        screen.blit(IA,(screen_width/2 - 30,screen_height/2))
        
        pygame.display.update()
        Principalclock.tick(60)
        
def PONG_1vs1(): #INICIO DEL JUEGO PONG PARA DOS PERSONAS
    global screen_height, screen_width    
    running = True 
    #CICLO REPETIRIVO DEL JUEGO
    while running:
        global player1_speed, player2_speed, COLOR, COLOOR, COLOOOR
        texto("PONG 1vs1", fuente, ligth_grey, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()
            if event.type ==  pygame.KEYDOWN:
                if event.type ==  pygame.K_ESCAPE:
                    running = False
            COLOR= rng.randrange(0,250)
            COLOOR= rng.randrange(0,250)
            COLOOOR=rng.randrange(0,250)
                #SE COMIENZAN A OIR LOS EVENTOS DEL TECLADO PARA EL JUGADOR 1     
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
                #SE COMIENZAN A OIR LOS EVENTOS DEL TECLADO PARA EL JUGADOR 2        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player2_speed += 7
                elif event.key == pygame.K_s:
                    player2_speed -= 7
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player2_speed -= 7
                elif event.key == pygame.K_s:
                    player2_speed += 7
                    
        # SE LLAMAN A LASFUCIONES PERTINENTES  
        pltantmon()
        player1antmon()
        player2antmon()
        
        #SE COMIENZA A DIBUJAR EN PANTALLA 
        screen.fill(bg_color)
        pygame.draw.polygon(screen,(COLOR,COLOOR,COLOOOR),[(40,325),(650,0),(1260,325),(650,650)],3)
        pygame.draw.rect(screen,ligth_grey,player1)
        pygame.draw.rect(screen,ligth_grey,player2) 
        pygame.draw.ellipse(screen,white,plt)
        pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2,screen_height))
    
        #SE DIBUJA EL MARCADOR 
        Jugador_1 = fuente.render(str(marcadorj1),True,ligth_grey)
        screen.blit(Jugador_1,(screen_width/2 + 20,screen_height/2))
        #SE DIBUJA EL MARCADOR 
        Jugador_2 = fuente.render(str(marcadorj2ia),True,ligth_grey)
        screen.blit(Jugador_2,(screen_width/2 - 30,screen_height/2))
        
        pygame.display.update()
        Principalclock.tick(60) 
