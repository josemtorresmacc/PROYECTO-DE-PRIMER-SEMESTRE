import pygame
import sys
import random
#import time
import tkinter as tk
from tkinter import messagebox

def _P_O_N_G_():
    global PONG
    PONG()
    
wn = tk.Tk()
wn.title("PROYECTO ARCADEMY")
wn.configure(background="dark gray")
wn.iconbitmap("Arcademy.ico")
wn.geometry("1200x300")
wn.configure(bd = 15)
wn.configure(relief="groove")
wn.config(cursor="pirate")

Etiqueta = tk.Label(wn, text="ARCADEMY", fg ="black", font=("Castellar", 32))
Etiqueta.place(x="450", y="20")

opcion = tk.StringVar(wn)
opcion.set("OPCIONES")
opciones = [_P_O_N_G_]
opcione = tk.OptionMenu(wn, opcion, *opciones)
opcione.pack(side="left", padx = 500,pady = 0)

wn.mainloop()

        #Screen
screen_width = 1300
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PONG")
   
        #Rectangulos
plt = pygame.Rect(screen_width/2 - 20, screen_height/2 - 20, 40, 40)
player1 = pygame.Rect(screen_width - 40,screen_height/2 - 70, 5,140)
player2 = pygame.Rect(20, screen_height/2 - 70, 5, 140)
        #Punt3 y comentarios 
#sp33dm4cs
plt_speed_x = 7 * random.choice((1,-1))
plt_speed_y = 7 * random.choice((1,-1))
player1_speed = 0
player2_speed = 0
IA_speed = 7


marcadorj1 = 0
marcadorj2ia = 0

#font = pygame.font.Font("freesansbold.ttf", 30)
#font2= pygame.font.Font("freesansbold.ttf",80)

#c0l03
rng=random.Random()
COLOR = rng.randrange(0,255)
COLOOR = rng.randrange(0,255)
COLOOOR = rng.randrange(0,255)
bg_color = pygame.Color("dark slate gray")
ligth_grey = (250, 250, 250) 
white = (255, 255, 255)

def pltantmon():
    global plt_speed_x, plt_speed_y, marcadorj1, marcadorj2ia, screen_width, screen_height
    plt.x += plt_speed_x 
    plt.y += plt_speed_y
    if plt.top <= 0 or plt.bottom >= screen_height:
        plt_speed_y *= -1
    if plt.left <= 0:
        marcadorj1 += 1
#        text_surface = font.render(u'PUNTO A FAVOR', True, (255,255,255))
#        screen.blit(text_surface,(screen_width/2 - 135, screen_height/2 - 40))
#        pygame.display.flip()
#        time.sleep(1)
        plt_restart()
    if plt.right >= screen_width:
        marcadorj2ia += 1
#        text_surface = font.render(u'PUNTO EN CONTRA', True, (255,255,255))
#        screen.blit(text_surface,(screen_width/2 - 135, screen_height/2 + 40))
#        pygame.display.flip()
#        time.sleep(1)
        plt_restart()
    if plt.colliderect(player1) or plt.colliderect(player2):
        plt_speed_x *= -1
    if marcadorj1== 10:
#        text_surface = font2.render(u'¡YOU WIN!', True, (COLOR,COLOOR,COLOOOR))
#        screen.blit(text_surface,(screen_width/2 -300 ,screen_height/2 -20))
#        pygame.display.flip()
#        time.sleep(1)
        pygame.exit()
        sys.exit()
    if marcadorj2ia== 10:
#        text_surface = font2.render(u"¡GAME OVER!", True, (COLOR,COLOOR,COLOOOR))
#        screen.blit(text_surface,(screen_width/2 - 300 ,screen_height/2 -20))
#        pygame.display.flip()
#        time.sleep(1)
        pygame.exit()
        sys.exit()

def player1antmon():
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

def player2antmon(): #En proceso 
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

def PONG():
    global screen_height, screen_width
    pygame.init()
    clock = pygame.time.Clock()
    
    fuente = pygame.font.Font("freesansbold.ttf",20)
        
    #l0000p
    while True:
        global player1_speed
        for event in pygame.event.get():
            COLOR= rng.randrange(0,255)
            COLOOR= rng.randrange(0,255)
            COLOOOR=rng.randrange(0,255)
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
        pygame.draw.polygon(screen,(COLOR,COLOOR,COLOOOR),[(40,325),(650,0),(1260,325),(650,650)],3)
        pygame.draw.rect(screen,ligth_grey,player1)
        pygame.draw.rect(screen,ligth_grey,player2) 
        pygame.draw.ellipse(screen,white,plt)
        pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2,screen_height))
    
    
        Jugador_1 = fuente.render(str(marcadorj1),True,ligth_grey)
        screen.blit(Jugador_1,(screen_width/2 + 20,screen_height/2))
    
        Jugador_2_ia = fuente.render(str(marcadorj2ia),True,ligth_grey)
        screen.blit(Jugador_2_ia,(screen_width/2 - 30,screen_height/2))
    
        pygame.display.flip()
        clock.tick(60) 

PONG()