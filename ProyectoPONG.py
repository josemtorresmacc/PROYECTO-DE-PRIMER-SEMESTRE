# -*- coding: utf-8 -*-
import pygame
import sys 
import random
import time 

        #INICIO DE PIGAME 
mainclock = pygame.time.Clock()
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

# APARTADO DE COLORES BIBLIOTECAS RANDOM Y PYGAME
rng=random.Random()
Time=time.clock()
COLOR = rng.randrange(0,255)
COLOOR = rng.randrange(0,255)
COLOOOR = rng.randrange(0,255)
black = (0, 0, 0)
ligth_grey = (250, 250, 250)
bg_color = pygame.Color("dark slate gray")
white = (255, 255, 255)
    
    #SE DEVINEN LAS VAIRABLES PARA BATTLE
#POSICIONES
xheroe=100
yheroe=100
xheroe2 = 600
yheroe2 = 300
xzombie = 600
yzombie = 300

#BALAS
xbala=xheroe+30
ybala=yheroe
xbala2=xheroe2+30
ybala2=yheroe2

#VIDA
vidaz=15
vidah=1
vida2=1
vida1=1

#ANGULOS
angulo=0
angulo1=0
angulo2=180

def texto(text , fuente, color, surface, x, y): #SE DEFINE LA FUNCIÓN PARA PODER PINTAR TEXTO PARA EL MENÚ
    textobj = fuente.render(text, 1, color)
    recttext = textobj.get_rect()
    recttext.topleft = (x, y)
    surface.blit(textobj, recttext)

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
          
def plt_restart(): #REINICIA LA PELATO ALTERANDO DE FORMA ALEATORIA LA DIRECCIÓN DE SALIDA
    global plt_speed_x,plt_speed_y
    plt.center = (screen_width/2, screen_height/2)
    plt_speed_y *= random.choice((1,-1))
    plt_speed_x *= random.choice((1,-1))
      
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
               
def PONG(): #INICIO DEL JUEGO PONG PARA UN SOLO JUGADOR
    global screen_height, screen_width
    running = True 
    #CICLO REPETIRIVO DEL JUEGO
    while running:
        global player1_speed, COLOR, COLOOR, COLOOOR
        texto("PONG", fuente, ligth_grey, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
        mainclock.tick(60)
                
def PONG_1vs1(): #INICIO DEL JUEGO PONG PARA DOS PERSONAS
    global screen_height, screen_width    
    running = True 
    #CICLO REPETIRIVO DEL JUEGO
    while running:
        global player1_speed, player2_speed, COLOR, COLOOR, COLOOOR
        texto("PONG 1vs1", fuente, ligth_grey, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
        mainclock.tick(60)
           
#ACÁ COMIENZAN LAS DEFINICIONES PARA BATTLE
def INDICADOR(font2,screen,vidaz): #SIRVE PARA QUE AL FINAL DEL JUEGO SE IMPRIMA EN PANTALLA EL RESULTADO FINAL EL CUAL PUEDE SER QUE HAYAS GANADO O PERDIDO
    global running
    
    if  vidaz== 0:
       text_surface = font2.render("ganaste", True, (0,0,0))
       screen.blit(text_surface,(500 ,325))
       pygame.display.flip()
       time.sleep(3)
       running=False
    if  vidah== 0:
       text_surface = font2.render("perdiste", True, (0,0,0))
       screen.blit(text_surface,(500 ,325))
       pygame.display.flip()
       time.sleep(3)
       running=False
             
def yzombieIA(): #SE DEFINE EL MOVIMIENTO DEL ZOMBIE EN EL EJE y, ES DECIR, ESTE VA A SEGUIR AL HEROE EN ESTE EJE
    global yzombie,xheroe,yheroe,xzombie,zombie,vidah
    
    if yzombie <  yheroe:
        yzombie += 1
    if yzombie >yheroe:
        yzombie -= 1
    if yzombie == yheroe:
        yzombie = yzombie
    if yzombie >= 650:
        yzombie = 650   
    
def xzombiIA():#SE DEFINE EL MOVIMIENTO DEL ZOMBIE EN EL EJE x, ES DECIR, ESTE VA A SEGUIR AL HEROE EN ESTE EJE
    global yzombie,xheroe,yheroe,xzombie,zombie,vidah
    
    if xzombie <  xheroe:
        xzombie += 1
    if xzombie >xheroe:
        xzombie -= 1
    if xzombie == xheroe:
        xzombie = xzombie
    if xzombie >= 1300:
        xzombie = 1300 
        
def idd():#ES PARA QUE LA VIDA DEL HEROE BAJE CADA VEZ QUE EL ZOMBIE LO TOCA
    global yzombie,xheroe,yheroe,xzombie,zombie,vidah
    
    if xzombie==xheroe  and yzombie==yheroe :
        vidah-=1
       
def balas(): #SIRVE PARA DARLE MOVIMIENTO AL PROYECTIL; HACIENDO QUE CADA VEZ QUE TOQUE AL ZOMBIE LE BAJE VIDA
    global xbala,ybala,angulo,bala,vidaz,xzombie,yzombie,yheroe,xheroe
    
    if angulo==0: #ESTA CONDICION ES CUANDO EL ANGULO ES = 0
        xbala+=10
        if xbala>=1300:
            xbala=xheroe
            ybala=yheroe
        if (xzombie<=xbala and xbala<=xzombie+11) and( yzombie<=ybala and ybala<=yzombie+40)  :
            xbala=xheroe
            ybala=yheroe
            vidaz-=1
    elif angulo==90:#ESTA CONDICION ES CUANDO EL ANGULO ES = 90
        ybala-=10
        if ybala<=0:
            ybala=yheroe
            xbala=xheroe 
        if (yzombie<=ybala and ybala<=yzombie+11) and( xzombie-20<=xbala and xbala<=xzombie+40)  :
            xbala=xheroe
            ybala=yheroe
            vidaz-=1
    elif angulo==180:#ESTA CONDICION ES CUANDO EL ANGULO ES = 180
        xbala-=10
        if xbala<=0:
            xbala=xheroe
            ybala=yheroe
        if (xzombie-11<=xbala and xbala<=xzombie) and( yzombie<=ybala and ybala<=yzombie+40)  :
            xbala=xheroe
            ybala=yheroe
            vidaz-=1
    elif angulo==270:#ESTA CONDICION ES CUANDO EL ANGULO ES = 270
        ybala+=10
        if ybala>=650:
            ybala=yheroe
            xbala=xheroe 
        if (yzombie<=ybala and ybala<=yzombie+11) and( xzombie-20<=xbala and xbala<=xzombie+40)  :
            xbala=xheroe
            ybala=yheroe
            vidaz-=1
    elif angulo==360:#ESTA CONDICION ES CUANDO EL ANGULO ES = 360
        xbala+=10    
        if xbala>=1300:
            xbala=xheroe  
            ybala=yheroe
        if (xzombie<=xbala and xbala<=xzombie+11) and( yzombie<=ybala and ybala<=yzombie+40)  :
            xbala=xheroe
            ybala=yheroe
            vidaz-=1
            
def BATTLE ():#ACÁ COMIENZA EL JUEGO 
    global screen_height,screen_width,yzombie,xheroe,yheroe,xzombie,zombie,vidah,angulo
    
    running = True 
    screen = pygame.display.set_mode((screen_width,screen_height))#SE DEFINE EL TAMAÑO DE LA PANTALLA
    heroe= pygame.image.load("mago.png")#IMAGEN DEL JUGADOR EL CUAL SERÁ EL HEROE 
    zombie= pygame.image.load("zombie0.png")#IMAGEN DEL ZOMBIE EL CUAL SERÁ EL ENEMIGO
    bala=pygame.image.load("bola de fuego.png")#IMAGEN DEL PROYECTIL
    
    #SE IMPRIME EN PANTALLA
    screen.fill((45,87,44), (0,0,1300,650))#COLOR DEL BACKGROUND
    screen.blit(zombie,(xzombie,yzombie))
    screen.blit(heroe,(xheroe,yheroe))
    clock = pygame.time.Clock()
    pygame.display.flip()   
    font2= pygame.font.Font(None,100)
    
    #CICLO REPETITIVO DEL VIDEOJUEGO
    while running:   
        texto("BATTLE", fuente, ligth_grey, screen, 20, 20)
        
        screen.fill((45,87,44), (0,0,1300,650))  
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running= False
            #SE TIENEN EN CUENTA LOS EVENTOS QUE OCURREN EN EL TECLADO Y MOUSE
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    yheroe += 15
                elif evento.key == pygame.K_w:
                    yheroe -= 15
                elif evento.key == pygame.K_d:
                    xheroe += 15
                elif evento.key == pygame.K_a:
                    xheroe -= 15
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 3:
                    angulo += 90
                    if angulo ==360:
                        angulo=0
        #SE REEIMPRIMEN LAS IMÁGENES               
        INDICADOR(font2,screen,vidaz)
        heroe=pygame.transform.rotate(heroe, angulo)
        screen.blit(bala,(xbala+30,ybala+25))
        
        #SE LLAMAN A LAS FUNCIONES QUE CREAN LOS MOVIMIENTOS 
        balas() 
        yzombieIA()
        xzombiIA()
        idd()
        
        screen.blit(zombie,(xzombie,yzombie))
        screen.blit(heroe, (xheroe, yheroe))
        
        #SE DIBUJA LA VIDA DEL ZOMBIE 
        vidazz = font2.render("vida del zombie: "+ str(vidaz), True, (200,200,200))
        screen.blit(vidazz,(350,0))
        #SE ROTA LA IMAGEN DEL JUGADOR 
        pygame.transform.rotate(heroe, angulo)  
        
        pygame.display.update()
        clock.tick(60)

#ACÁ COMIENZAN LAS DEFINICIONES PARA BATTLE2
def marcador(font2,screen,vida1,vida2):
    global running
    
    if vida2== 0:
       text_surface = font2.render("ganaste jugador 1", True, (0,0,0))
       screen.blit(text_surface,(400 ,325))
       pygame.display.flip()
       time.sleep(3)
       running=False
    if  vida1== 0:
       text_surface = font2.render("ganaste jugador 2", True, (0,0,0))
       screen.blit(text_surface,(400 ,325))
       pygame.display.flip()
       time.sleep(3)
       running=False  
          
def balas1(): #SIRVE PARA DARLE MOVIMIENTO AL PROYECTIL; HACIENDO QUE CADA VEZ QUE TOQUE JUAGADOR 2 hHACE QUE ESTE MUERA AL INSTANTE ENTRE TERRIBE DOLOR Y SUFRIMIENTO  
    global xbala,ybala,angulo1,bala2,vida2,xheroe2,xheroe,yheroe2,yheroe
    
    if angulo1==0:
        xbala+=10
        if xbala>=1300:
            xbala=xheroe
            ybala=yheroe
        if (xheroe2<=xbala and xbala<=xheroe2+11) and( yheroe2<=ybala and ybala<=yheroe2+40)  :
            xbala=xheroe
            ybala=yheroe
            vida2-=1
    elif angulo1==90:
        ybala-=10
        if ybala<=0:
            ybala=yheroe
            xbala=xheroe 
        if (yheroe2<=ybala and ybala<=yheroe2+11) and( xheroe2-40<=xbala and xbala<=xheroe2+40)  :
            xbala=xheroe
            ybala=yheroe
            vida2-=1
    elif angulo1==180:
        xbala-=10
        if xbala<=0:
            xbala=xheroe
            ybala=yheroe
        if (xheroe2-11<=xbala and xbala<=xheroe2) and( yheroe2<=ybala and ybala<=yheroe2+40)  :
            xbala=xheroe
            ybala=yheroe
            vida2-=1
    elif angulo1==270:
        ybala+=10
        if ybala>=650:
            ybala=yheroe
            xbala=xheroe 
        if (yheroe2<=ybala and ybala<=yheroe2+11) and( xheroe2-40<=xbala and xbala<=xheroe2+40)  :
            xbala=xheroe
            ybala=yheroe
            vida2-=1
    elif angulo1==360:
        xbala+=10    
        if xbala>=1300:
            xbala=xheroe  
            ybala=yheroe
        if (xheroe2<=xbala and xbala<=xheroe2+11) and( yheroe2<=ybala and ybala<=yheroe2+40)  :
            xbala=xheroe
            ybala=yheroe
            vida2-=1
            
def balas2():#SIRVE PARA DARLE MOVIMIENTO AL PROYECTIL; HACIENDO QUE CADA VEZ QUE TOQUE JUAGADOR 1 hHACE QUE ESTE MUERA AL INSTANTE ENTRE TERRIBE DOLOR Y SUFRIMIENTO 
    global xbala2,ybala2,angulo2,bala2,vida1,xheroe2,xheroe,yheroe2,yheroe
   
    if angulo2==0:
        xbala2+=10
        if xbala2>=1300:
            xbala2=xheroe2
            ybala2=yheroe2
        if (xheroe<=xbala2 and xbala2<=xheroe+11) and( yheroe<=ybala2 and ybala2<=yheroe+40)  :
            xbala2=xheroe2
            ybala2=yheroe2
            vida1-=1
    elif angulo2==90:
        ybala2-=10
        if ybala2<=0:
            ybala2=yheroe2
            xbala2=xheroe2
        if (yheroe<=ybala2 and ybala2<=yheroe+11) and( xheroe-40<=xbala2 and xbala2<=xheroe+40)  :
            xbala2=xheroe2
            ybala2=yheroe2
            vida1-=1
    elif angulo2==180:
        xbala2-=10
        if xbala2<=0:
            xbala2=xheroe2
            ybala2=yheroe2
        if (xheroe-11<=xbala2 and xbala2<=xheroe) and( yheroe-20<=ybala2 and ybala2<=yheroe+40)  :
            xbala2=xheroe2
            ybala2=yheroe2
            vida1-=1
    elif angulo2==270:
        ybala2+=10
        if ybala2>=650:
            ybala2=yheroe2
            xbala2=xheroe2 
        if (yheroe<=ybala2 and ybala2<=yheroe+11) and( xheroe-40<=xbala2 and xbala2<=xheroe+40)  :
            xbala2=xheroe2
            ybala2=yheroe2
            vida1-=1
    elif angulo2==360:
        xbala2+=10    
        if xbala2>=1300:
            xbala2=xheroe2  
            ybala2=yheroe2
        if (xheroe<=xbala2 and xbala2<=xheroe+11) and( yheroe<=ybala2 and ybala2<=yheroe+40)  :
            xbala2=xheroe2
            ybala2=yheroe2
            vida1-=1
            
def BATTLEPARADOS():#ACÁ INICIA EL JUEGO 
    global xbala2,ybala2,angulo2,vida1,xheroe2,xheroe,yheroe2,yheroe,angulo1,xbala1,ybala1,angulo1,bala2
    heroe= pygame.image.load("mago.png")
    heroe2= pygame.image.load("mago 2.png")
    bala=pygame.image.load("bola de fuego.png")
    bala2=pygame.image.load("bola de fuego.png")
    screen.fill((128,64,0), (0,0,1300,650))
    screen.blit(heroe2,(xheroe2,yheroe2))
    screen.blit(heroe,(xheroe,yheroe))
    pygame.display.flip()   
    font2= pygame.font.Font(None,100)
    clock = pygame.time.Clock()
    running=True
    
    while running:    
        texto("BATTLE PARA DOS", fuente, ligth_grey, screen, 20, 20)
        screen.fill((125,64,0), (0,0,1300,650))
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running=False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    yheroe += 15
                elif evento.key == pygame.K_w:
                    yheroe -= 15
                elif evento.key == pygame.K_d:
                    xheroe += 15
                elif evento.key == pygame.K_a:
                    xheroe -= 15
                elif evento.key == pygame.K_e:
                    angulo1 += 90
                    if angulo1 ==360:
                        angulo1=0
            #SE TIENE EN CUENTA LOS EVENTOS QUE OCURREN EN EL TECLADO PARA MOVER AL JUGADOR 2
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    yheroe2 += 15
                elif evento.key == pygame.K_UP:
                    yheroe2 -= 15
                elif evento.key == pygame.K_RIGHT:
                    xheroe2 += 15
                elif evento.key == pygame.K_LEFT:
                    xheroe2 -= 15
                elif evento.key == pygame.K_n:
                    angulo2 += 90
                    if angulo2 ==360:
                        angulo2=0
  
        #SE PINTA EN PANTALLA 
        marcador(font2,screen,vida1,vida2)
        heroe=pygame.transform.rotate(heroe, angulo1)
        heroe2=pygame.transform.rotate(heroe2, angulo2)
        screen.blit(bala,(xbala2+30,ybala2+25))
        screen.blit(bala,(xbala+30,ybala+25))
        #SE LLAMAN A LAS FUNCIONES QUE CREAN LOS MOVIMIENTOS 
        balas1() 
        balas2()
        
        screen.blit(heroe2,(xheroe2,yheroe2))
        screen.blit(heroe, (xheroe, yheroe))
        pygame.display.update()
        clock.tick(60)
        
def MENÚPREINCIPAL():#SERÁ EL MENÚ DE OPCIONES
    while True:
        global click,font2
        screen.fill(black)
        texto("PROYECTO ARCADEMY", fuente, bg_color, screen, 20, 20)
        font2= pygame.font.Font(None,100)
        mx, my = pygame.mouse.get_pos()

        Boton1 = pygame.Rect(50,100,450,80)
        Boton2 = pygame.Rect(50,200,450,80)
        Boton3 = pygame.Rect(50,300,450,80)
        Boton4 = pygame.Rect(50,400,450,80)
#        Boton4 = pygame.Rect(50,500,200,50)
        if Boton1.collidepoint((mx, my)):
            if click:
                PONG()
        if Boton2.collidepoint((mx, my)):
            if click:    
                PONG_1vs1()
        if Boton3.collidepoint((mx, my)):
            if click:
                BATTLE()
        if Boton4.collidepoint((mx, my)): 
            if click:
                BATTLEPARADOS()
#        if Boton5.collidepoint((mx, my)):
#            if click:
#                 snake()
        pygame.draw.rect(screen,black,Boton1)
        text_surface2 = font2.render("PONG", True, bg_color)
        screen.blit(text_surface2,( 50,100))
        pygame.draw.rect(screen,black,Boton2)
        text_surface3 = font2.render("PONG 1vs1", True, bg_color)
        screen.blit(text_surface3,( 50,200))
        pygame.draw.rect(screen,black,Boton3)
        text_surface4 = font2.render("BATTLE", True, bg_color)
        screen.blit(text_surface4,( 50,300))
        pygame.draw.rect(screen,black,Boton4)
        text_surface2 = font2.render("BATTLE 1vs1", True, bg_color)
        screen.blit(text_surface2,( 50,400))
        
        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==  pygame.KEYDOWN:
                if event.type ==  pygame.K_ESCAPE:
                    pygame.exit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        pygame.display.update()
        mainclock.tick(60)
        
MENÚPREINCIPAL()