import pygame
import math


class Enemy:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.velocity = 3
        self.path = [(30, 150), (139, 150), (289, 150), (472, 150), (578, 150), (718, 152), (788, 232), (768, 307), (734, 364), (629, 390),(593, 432), (577, 475), (576, 514), (565, 565), (526, 600), (335, 620), (181, 620), (58, 619), (0, 619), (-10,619)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.imgs=[]
        self.path_pos = 0
        self.move_dis = 0
        self.dis = 0
        self.flipped= False
        self.max_health = 10

    def draw(self, win):
        #rysuje enemy - obrazek

        self.img= self.imgs[self.animation_count//3]
        self.animation_count +=1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0 


        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 30))
        self.draw_health_bar(win)
        self.move()
        pass

    def draw_health_bar(self, win):
        length=50
        moveBy= round(length / self.max_health)
        health_bar = moveBy * self.health

        pygame.draw.rect(win, (0,0,0), (self.x-32, self.y-76, length+3,12), 0, border_radius=20)

        pygame.draw.rect(win, (200,0, 0), (self.x-30, self.y-75, length, 10), 0, border_radius=20)
        pygame.draw.rect(win, (0,150, 0), (self.x-30, self.y-75, health_bar, 10), 0, border_radius=20)



    def collide(self, X, Y):

        if X < self.x + self.width and X>= self.x:
            if Y <= self.y + self.height and Y>= self.y:
                return True

        return False

    def move(self):
        #ruch wroga
        x1,y1= self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):  #jeśli jesteśmy na końcu iteracji przez ścieżkę
            x2, y2= (-50, 610)   #wróg ma wyjść poza widziany obszar jeśli jest już na końcu ścieżki
        else: 
            x2, y2 = self.path[self.path_pos + 1]   #w innym wypadku idziemy do kolejnego punktu

        #move_dis = math.sqrt((x2-x1)**2 + (y2- y1)**2)   #dystans jaki dzieli punkty 

         
        direction = ((x2-x1), (y2-y1))   #kierunek przesunięcia
        length = math.sqrt((direction[0])**2 + (direction[1])**2)   #długość jaką musi przejść do punktu
        direction = (direction[0]/length, direction[1]/length)

        
        if direction[0]<0 and not(self.flipped):   #jeśli wróg idzie w drugą stronę to musimy go odwrócić
            self.flipped= True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)


        move_x, move_y= (self.x + direction[0] , self.y + direction[1]  )
        # self.dis += math.sqrt((move_x - x1)**2 + (move_y - y1)**2)   #dystans o jaki chcemy przesunąć wroga
      
        self.x = move_x 
        self.y= move_y 

        #idzie do nastepnego punktu

        if direction[0] >= 0:  #idzie w prawo 
            if direction[1] >=0:  #idzie w dół
                if self.x >= x2 and self.y>=y2:
                    self.path_pos+=1
            else:  #idzie w górę
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:  #idzie w lewo
            if direction[1] >= 0:  #idzie w dół
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:  #idzie w górę i w lewo
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1


        

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True

        return False

