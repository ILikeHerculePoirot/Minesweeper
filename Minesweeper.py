import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode((450,450))
pygame.display.set_caption('Minesweeper')
font=pygame.font.SysFont('FreeSansbold.ttf',40)
flag=pygame.image.load('Assets/Flag.png').convert_alpha()
bomb=pygame.image.load('Assets/Bomb.png').convert_alpha()
clicked_bomb=pygame.image.load('Assets/Clicked_bomb.png').convert_alpha()
pygame.display.set_icon(bomb)
screen.blit(flag,(175,0))
grid_color_state=[['lg','dg','lg','dg','lg','dg','lg','dg','lg','dg'],['dg','lg','dg','lg','dg','lg','dg','lg','dg','lg'],['lg','dg','lg','dg','lg','dg','lg','dg','lg','dg'],['dg','lg','dg','lg','dg','lg','dg','lg','dg','lg'],['lg','dg','lg','dg','lg','dg','lg','dg','lg','dg'],['dg','lg','dg','lg','dg','lg','dg','lg','dg','lg'],['lg','dg','lg','dg','lg','dg','lg','dg','lg','dg'],['dg','lg','dg','lg','dg','lg','dg','lg','dg','lg'],['lg','dg','lg','dg','lg','dg','lg','dg','lg','dg'],['dg','lg','dg','lg','dg','lg','dg','lg','dg','lg']]
grid_flag_state=[[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
grid_bomb_state=[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
random.shuffle(grid_bomb_state)
grid_number_state=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
i=0
while(i<(len(grid_bomb_state)-9)):
    grid_bomb_state[i]=[grid_bomb_state[i],grid_bomb_state[i+1],grid_bomb_state[i+2],grid_bomb_state[i+3],grid_bomb_state[i+4],grid_bomb_state[i+5],grid_bomb_state[i+6],grid_bomb_state[i+7],grid_bomb_state[i+8],grid_bomb_state[i+9]]
    del grid_bomb_state[i+1],grid_bomb_state[i+1],grid_bomb_state[i+1],grid_bomb_state[i+1],grid_bomb_state[i+1],grid_bomb_state[i+1],grid_bomb_state[i+1],grid_bomb_state[i+1],grid_bomb_state[i+1]
    i+=1
for i in range(10):
    for j in range(10):
        for x in range(abs(i-1),i+2):
            for y in range(abs(j-1),j+2):
                if(x<10 and y<10):
                    if((x,y)!=(i,j) and grid_bomb_state[x][y]):grid_number_state[i][j]+=1
def draw():
    for i in range(10):
        for j in range(10):
            if(grid_color_state[i][j]=='lg'):pygame.draw.rect(screen,(170,215,81),pygame.Rect(i*45,(j*45),45,45))
            elif(grid_color_state[i][j]=='dg'):pygame.draw.rect(screen,(162,209,73),pygame.Rect(i*45,(j*45),45,45))
            elif(grid_color_state[i][j]=='lg0'):pygame.draw.rect(screen,(229,194,159),pygame.Rect(i*45,(j*45),45,45))
            elif(grid_color_state[i][j]=='dg0'):pygame.draw.rect(screen,(215,184,153),pygame.Rect(i*45,(j*45),45,45))
            elif(grid_color_state[i][j]=='lgb' or grid_color_state[i][j]=='dgb'):screen.blit(bomb,(i*45,(j*45)))
            elif(grid_color_state[i][j]=='lgc' or grid_color_state[i][j]=='dgc'):screen.blit(clicked_bomb,(i*45,(j*45)))
            elif(grid_color_state[i][j]=='lgf' or grid_color_state[i][j]=='dgf'):screen.blit(flag,(i*45,(j*45)))
            elif(grid_color_state[i][j][-1]!='0'):screen.blit(font.render(str(grid_number_state[i][j]),True,(0,0,0)),((i*45)+15,(j*45)+15))
    pygame.display.update()
def check_win():
    for i in range(10):
        for j in range(10):
            if(bool(grid_bomb_state[i][j])!=grid_flag_state[i][j]):return False
            elif(grid_color_state[i][j][len(grid_color_state[i][j])-1]=='g'):return False
    return True
game=1
draw()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:exit()
        elif(event.type==pygame.MOUSEBUTTONDOWN):
            x,y=pygame.mouse.get_pos()
            if(event.button==pygame.BUTTON_LEFT):
                if(grid_bomb_state[x//45][y//45]):
                    game=0
                    for i in range(10):
                        for j in range(10):
                            if(i==(x//45) and j==(y//45)):grid_color_state[i][j]+='c'
                            elif(grid_bomb_state[i][j]):grid_color_state[i][j]+='b'
                else:
                    if(str(grid_number_state[x//45][y//45])!='0'):grid_color_state[x//45][y//45]+=str(grid_number_state[x//45][y//45])
                    else:
                        grid_color_state[x//45][y//45]+='0'
                        modifications=1
                        shown=[[x//45,y//45]]
                        while(modifications!=0):
                            modifications=0
                            for i in range(10):
                                for j in range(10):
                                    for x in range(abs(i-1),i+2):
                                        for y in range(abs(j-1),j+2):
                                            if(grid_number_state[i][j]==0 and shown.count([i,j]) and x<10 and y<10):
                                                if((x,y)!=(i,j) and grid_color_state[x][y][-1] not in ['0','1','2','3','4','5','6','7','8']):grid_color_state[x][y]+=str(grid_number_state[x][y]);modifications+=1;shown.append([x,y])
            elif(event.button==pygame.BUTTON_RIGHT):
                c=0
                for i in range(10):
                    for j in range(10):
                        if(grid_flag_state[i][j]):c+=1
                if(c<10 and grid_flag_state[(x//45)][y//45]==False):
                    grid_flag_state[(x//45)][y//45]=True
                    grid_color_state[(x//45)][y//45]+='f'
                elif(c>0 and grid_flag_state[(x//45)][y//45]==True):
                    grid_flag_state[(x//45)][y//45]=False
                    grid_color_state[(x//45)][y//45]=grid_color_state[(x//45)][y//45][0:2]
                time.sleep(1)
            draw()
            if(check_win()):game=2
    if(game==0):
        time.sleep(5)
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:exit()
            screen.fill((0,0,0))
            screen.blit(font.render('You lost!',True,(127,0,0)),(160,200))
            pygame.display.update()
    elif(game==2):
        time.sleep(5)
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:exit()
            screen.fill((0,0,0))
            screen.blit(font.render('You won!',True,(0,131,0)),(160,200))
            pygame.display.update()
    pygame.display.update()
