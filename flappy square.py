#Mengimport library yang diperlukan
import pygame
from random import*


#Membuat display game
pygame.init()




disp_size = 600,550
window = pygame.display.set_mode(disp_size)
disp_title = pygame.display.set_caption('Flappy Square')
bg = pygame.image.load('background1.jpg')
run = False
clock = pygame.time.Clock()


#Membuat fungsi untuk menunjang game

def color (warna):
    if warna == 'red' :
        return 255,0,0

    elif warna == 'black' :
        return 0,0,0

    elif warna == 'blue' :
        return 0,0,255

    elif warna == 'white':
        return 255,255,255

    elif warna == 'green':
        return 0,255,0

def kotak (x,y):
    pygame.draw.rect(window,color('red'),(x,y,40,40))

def text_kalah ():
    text = pygame.font.SysFont(None, 50, bold = True , italic = True)
    disp_text = text.render("Kamu sudah kalah",True, color('black'))
    window.blit(disp_text,(150,270))
    

def rintangan(x_loc, y_loc , width , height):
    pygame.draw.rect(window,color('green'),(x_loc,y_loc,width,height))
    pygame.draw.rect(window,color('green'),(x_loc,int(jarak+height),width,550))


def text_score (score):
    text = pygame.font.SysFont(None, 50, bold = True , italic = True)
    disp_text = text.render("Score Kamu " +str(score),True, color('blue'))
    window.blit(disp_text,(0,0))
    

#Membuat variabel yang dibutuhkan

    
x,y = 300,300
x_speed, y_speed = 0,0
ground = 530
x_loc, y_loc = 600,0
width = 110
height = randint(20,300)
obstacle = 3
jarak = 100
score = 0 




#Game_Looping
while not run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
            
    #Mengaktifkan button yang diperlukan dalam game
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_speed = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                y_speed = 2
                
                
#Menjalankan game


    window.blit(bg,(0,0))
    kotak(x,y)
    rintangan(x_loc, y_loc , width , height)
    text_score(score)
    
    y += y_speed
    x_loc -= obstacle

    if y > ground and y < 0:
        text_kalah()
        y_speed = 0
        obstacle = 0
    

    if x_loc < 90:
        x_loc = 700
        height = randint(20,300)

    if x_loc < x +40 < x_loc+width:
        if height < y < (jarak+height+40) :
            score += 1
      
        else :
            text_kalah()
            y_speed = 0
            obstacle = 0
        
        

  
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()



