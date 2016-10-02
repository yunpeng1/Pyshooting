import pygame
from random import randint
from math import sqrt

class BaseClass(pygame.sprite.Sprite):
    
    allsprites = pygame.sprite.Group()
    def __init__(self, x, y, image_string):
        
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)
        
        self.image = pygame.image.load(image_string)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def destroy(self, ClassName):
        
        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self

class Tri(BaseClass):
    
    List = pygame.sprite.Group()
    numplayer = 0.5; Pscore = [0,0]; Level_up = 0; Level_t = 0
    def __init__(self, x, y, image_string, gl):
        
        BaseClass.__init__(self, x, y, image_string)
        Tri.List.add(self)
        Tri.numplayer = int(Tri.numplayer) + 1
        self.nplay  = Tri.numplayer
        if gl in [0]:
            self.damage = 0 
        elif gl in [1]:
            self.damage = 2
        elif gl in [2]:
            self.damage = 3
        self.health = 6
        self.score  = 0
        self.life   = 3
    
    @staticmethod
    def update_all(sw,sh,game_restart,num_damaged):
        if not game_restart:
            for tri in Tri.List:
                if tri.health <= 0:
                    tri.life -= 1
                    tri.rect.x = sw/2-25
                    tri.rect.y = sh-50
                    tri.health = 6
                if tri.life == 0:
                    Tri.Pscore[tri.nplay-1] = tri.score
                    Tri.numplayer -= 1
                    tri.destroy(tri)   
                if Boss.Ifwin:
                    Tri.Pscore[tri.nplay-1] = tri.score
                if num_damaged == 10:
                    Cirfire.FM = 2; Tri.Level_up = 1
                if num_damaged == 25:
                    Trcfire.FM = 1; Tri.Level_up = 1
                if num_damaged == 38:
                    Cirfire.FM = 3; Tri.Level_up = 1
                if num_damaged == 52:
                    Trcfire.FM = 2; Tri.Level_up = 1
        else:
            Tri.numplayer = 0.5
            Tri.Pscore = [0,0]
            Tri.Level_up = 0
            Tri.Level_t = 0
            for tri in Tri.List:
                tri.destroy(tri)
                
class Rec(BaseClass):

    List = pygame.sprite.Group()
    Dnum = 0
    def __init__(self, x, y, image_string, gl):
        
        BaseClass.__init__(self, x, y, image_string)
        Rec.List.add(self)
        if gl in [0]:
            self.damage = 3
        elif gl in [1]:
            self.damage = 2
        elif gl in [2]:
            self.damage = 2
        self.health = 12
        self.speed  = randint(1,3)      # randint(2,5)
        self.CT     = 0
        self.FM     = randint(1,5)      # fire mode
        self.stime  = randint(30,50)
        
    def Move(self, sh, mod=1):
        if mod in [1]:
            if self.CT < 30:                    yspeed = 5
            elif self.CT > 30 and self.CT < 70: yspeed = 0
            else:                               yspeed = self.speed
            self.rect.y += yspeed
    
    @staticmethod
    def update_all(sh,game_restart):
        if not game_restart:
            for rec in Rec.List:
                if rec.health <= 0:
                    Exp(rec.rect.x+rec.rect.width/2-21,rec.rect.y+rec.rect.height/2-21,"image/e0.png")
                    Gld(rec.rect.x+rec.rect.width/2-5,rec.rect.y+rec.rect.height/2-9,"image/g1.png")
                    rec.destroy(rec)
                    Rec.Dnum += 1
                rec.CT += 1
                rec.Move(sh)
                if rec.rect.y > sh*1.1:
                    rec.destroy(rec)
                if rec.rect.y < -50:
                    rec.destroy(rec)
        else:
            Rec.Dnum = 0
            for rec in Rec.List:
                rec.destroy(rec)

class Boss(BaseClass):
    
    List = pygame.sprite.Group()
    appear = 0; Ifwin = 0; win_t = 0
    def __init__(self, x, y, image_string, gl):
        
        BaseClass.__init__(self, x, y, image_string)
        Boss.List.add(self)
        if gl in [0]:
            self.damage = 4
        elif gl in [1]:  
            self.damage = 2
        elif gl in [2]:  
            self.damage = 1
        self.health = 3000
        self.speed  = 1                 # randint(2,5)
        self.CT1    = 0
        self.CT2    = 0
        self.stage  = 0
        self.FM     = randint(1,5)      # fire mode
        self.stime  = 24
        
    def Move(self):
        if self.CT1 <= 50:                    
            yspeed = 5; xspeed = 0
            self.CT1 += 1
        elif self.CT1 > 50:
            if self.stage in [1,2,3]:
                TH = 50; self.CT2 += 1
                if self.CT2 < TH:  
                    yspeed = 0; xspeed = -2
                elif ((self.CT2 - TH) / (2*TH)) % 2 == 1:
                    yspeed = 0; xspeed = -2
                elif ((self.CT2 - TH) / (2*TH)) % 2 == 0:
                    yspeed = 0; xspeed = 2
                else:
                    yspeed = 0; xspeed = 0
        self.rect.x += xspeed
        self.rect.y += yspeed
    
    @staticmethod
    def update_all(game_restart):
        if not game_restart:
            for boss in Boss.List:
                if boss.health <= 0:
                    Gld(boss.rect.x+boss.rect.width/2-5,boss.rect.y+boss.rect.height/2-9,"image/g2.png")
                    Boss.Ifwin = 1; boss.destroy(boss)
                if boss.health <= 3000 and boss.health > 2000: 
                    boss.stage = 1
                if boss.health <= 2000 and boss.health > 1000: 
                    boss.stage = 2
                if boss.health <= 1000 and boss.health > 0: 
                    boss.stage = 3
                if boss.health <= 2000 and boss.health > 1950: 
                    Boss.appear = 2
                if boss.health <= 1000 and boss.health > 950: 
                    Boss.appear = 3
                boss.Move()
        else:
            Boss.appear = 0; Boss.Ifwin = 0; Boss.win_t = 0
            for boss in Boss.List:
                boss.destroy(boss)

class Gld(BaseClass):
    
    List = pygame.sprite.Group()
    def __init__(self, x, y, image_string):
        
        BaseClass.__init__(self, x, y, image_string)
        Gld.List.add(self)
        self.speed = randint(1,5)
    
    @staticmethod
    def update_all(sh,game_restart):
        if not game_restart:
            for gld in Gld.List:
                gld.rect.y += gld.speed
                if gld.rect.y > sh:
                    gld.destroy(gld)
        else:
            for gld in Gld.List:
                gld.destroy(gld)
                
class Exp(BaseClass):
    
    List = pygame.sprite.Group()
    def __init__(self, x, y, image_string):
        
        BaseClass.__init__(self, x, y, image_string)
        Exp.List.add(self)
        Exp.CT = 0
        
    @staticmethod
    def update_all(game_restart):
        if not game_restart:
            for exp in Exp.List:
                if exp.CT > 3 and exp.CT < 7: 
                    exp.image = pygame.image.load("image/e1.png")
                    exp.CT += 1
                elif exp.CT >= 5: exp.destroy(exp)
                else: exp.CT += 1
        else:
            for exp in Exp.List:
                exp.destroy(exp)
    
class Cirfire(pygame.sprite.Sprite):
    List = pygame.sprite.Group()
    CT   = 0; FM = 1
    
    def __init__(self, x, y, image_string):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image_string)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
        
        Cirfire.List.add(self)
        
        self.velx = 0
        self.vely = 0
    
    @staticmethod
    def update_all(game_restart):
        if not game_restart:
            for cfire in Cirfire.List:
                cfire.rect.x += cfire.velx
                cfire.rect.y += cfire.vely
                if cfire.rect.y < 0: 
                    Cirfire.List.remove(cfire)
        else:
            Cirfire.CT = 0; Cirfire.FM = 1
            for cfire in Cirfire.List:    
                Cirfire.List.remove(cfire)

class Trcfire(pygame.sprite.Sprite):
    List = pygame.sprite.Group()
    CT   = 0; FM = 0; obj = 0
    
    def __init__(self, x, y, image_string):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image_string)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
        
        Trcfire.List.add(self)
        self.CT_  = 0
        self.velx = 0
        self.vely = 0
    
    @staticmethod
    def update_all(game_restart):
        if not game_restart:
            for tfire in Trcfire.List:
                if Trcfire.obj != 0:
                    tol_ = 1.0e-8
                    abd = sqrt((Trcfire.obj.rect.x-tfire.rect.x)**2.0+(Trcfire.obj.rect.y-tfire.rect.y)**2.0+tol_)
                    tfire.velx = (Trcfire.obj.rect.x-tfire.rect.x+tol_)/abd*8.0
                    tfire.vely = (Trcfire.obj.rect.y-tfire.rect.y+tol_)/abd*8.0
                    tfire.rect.x += tfire.velx
                    tfire.rect.y += tfire.vely
                else: Trcfire.obj = 0
                if tfire.CT_ > 24*5: 
                    Trcfire.List.remove(tfire)
                tfire.CT_ += 1
        else:
            Trcfire.CT   = 0; Trcfire.FM = 0; Trcfire.obj = 0
            for tfire in Trcfire.List:
                Trcfire.List.remove(tfire)
                
class Recfire(pygame.sprite.Sprite):

    List = pygame.sprite.Group()
    def __init__(self, x, y, image_string):
         
        pygame.sprite.Sprite.__init__(self)
         
        self.image = pygame.image.load(image_string)
         
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
         
        Recfire.List.add(self)
         
        self.velx = 0
        self.vely = 0
     
    @staticmethod
    def update_all(sw,sh,game_restart):
        if not game_restart:
            for rfire in Recfire.List:
                rfire.rect.x += rfire.velx
                rfire.rect.y += rfire.vely
                if rfire.rect.y > sh-10: 
                    Recfire.List.remove(rfire)
                elif rfire.rect.y < 1: 
                    Recfire.List.remove(rfire)
                elif rfire.rect.x > sw-10: 
                    Recfire.List.remove(rfire)
                elif rfire.rect.x < 1: 
                    Recfire.List.remove(rfire)
        else:
            for rfire in Recfire.List:
                Recfire.List.remove(rfire)
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            