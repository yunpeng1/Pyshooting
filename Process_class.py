import pygame,sys,random,Game_class
from math import sqrt

def process(sw, sh, FPS, totalframes, gl):
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LSHIFT]: speed = 3
    else: speed = 1

    for tri in Game_class.Tri.List:

        if keys[pygame.K_LEFT]:
            predicted_x = tri.rect.x - 0 * speed
            if predicted_x < 0: pass
            else: tri.rect.x += -5 * speed
        if keys[pygame.K_RIGHT]:
            predicted_x = tri.rect.x + 0 * speed
            if predicted_x + tri.rect.width> sw: pass
            else: tri.rect.x += 5 * speed
        if keys[pygame.K_UP]:
            predicted_y = tri.rect.y - 5 * speed
            if predicted_y < 0: pass
            else: tri.rect.y += -5 * speed
        if keys[pygame.K_DOWN]:
            predicted_y = tri.rect.y + 5 * speed
            if predicted_y + tri.rect.height> sh: pass
            else:tri.rect.y += 5 * speed
        
        if keys[pygame.K_z]:
            if totalframes - Game_class.Cirfire.CT > FPS/8:
                fire_mode(tri,Game_class.Cirfire.FM)
                Game_class.Cirfire.CT = totalframes
            if totalframes - Game_class.Trcfire.CT > FPS:
                tfire_mode(tri,Game_class.Trcfire.FM)
                Game_class.Trcfire.CT = totalframes
        
        collisions_tri(tri)
        collected(tri)
        recshoot(tri)
        collisions(tri)
        collisions_boss(tri)
        bossfire(tri)
    if Game_class.Boss.appear == 0: 
        spawn(FPS, totalframes, sw, gl)
    elif Game_class.Boss.appear == 1:
        Game_class.Boss(sw/2-62, -200, "image/s1.png", gl)
        Game_class.Boss.appear = -1
    elif Game_class.Boss.appear == 2:
        for boss in Game_class.Boss.List:
            boss.image = pygame.image.load("image/s2.png")
        Game_class.Boss.appear = -1
    elif Game_class.Boss.appear == 3:
        for boss in Game_class.Boss.List:
            boss.image = pygame.image.load("image/s3.png")
        Game_class.Boss.appear = -1
        
def spawn(FPS, totalframes, sw, gl):
    
    if Game_class.Rec.Dnum < 21:   one_second = FPS
    elif Game_class.Rec.Dnum < 41:   one_second = FPS/2
    elif Game_class.Rec.Dnum < 61:   one_second = FPS/4
    elif Game_class.Rec.Dnum < 81:   one_second = FPS/6
    else: one_second = FPS/8
    if Game_class.Rec.Dnum < 101 and gl in [0,1]:
        if totalframes % one_second == 0:
            loc = random.randint(0,15)
            Game_class.Rec(sw/15*loc, -50, "image/r1.png", gl)
    elif Game_class.Rec.Dnum < 201 and gl in [2]:
        if totalframes % (one_second/2) == 0:
            loc = random.randint(0,15)
            Game_class.Rec(sw/15*loc, -50, "image/r1.png", gl)
    else: Game_class.Boss.appear = 1
        
def collisions(tri):
    for rec in Game_class.Rec.List:
        rec_proj = pygame.sprite.spritecollide(rec, Game_class.Cirfire.List, True)
        if len(rec_proj) > 0:
            for _ in rec_proj:
                rec.health -= rec.damage
                tri.score += 1
        rec_proj = pygame.sprite.spritecollide(rec, Game_class.Trcfire.List, True)
        if len(rec_proj) > 0:
            for _ in rec_proj:
                rec.health -= 2 * rec.damage
                tri.score += 2
        rec_proj = pygame.sprite.spritecollide(rec, Game_class.Tri.List, False)
        if len(rec_proj) > 0:
            for _ in rec_proj:
                rec.health -= 10*rec.damage
                tri.score += 0

def collisions_tri(tri):
    tri_proj = pygame.sprite.spritecollide(tri, Game_class.Recfire.List, True)
    if len(tri_proj) > 0:
        for _ in tri_proj:
            tri.health -= tri.damage
    tri_proj = pygame.sprite.spritecollide(tri, Game_class.Rec.List, False)
    if len(tri_proj) > 0:
        for _ in tri_proj:
            tri.health -= 10*tri.damage

def collisions_boss(tri):
    for boss in Game_class.Boss.List:
        boss_proj = pygame.sprite.spritecollide(boss, Game_class.Cirfire.List, True)
        if len(boss_proj) > 0:
            for _ in boss_proj:
                boss.health -= boss.damage
                tri.score += 1
        boss_proj = pygame.sprite.spritecollide(boss, Game_class.Trcfire.List, True)
        if len(boss_proj) > 0:
            for _ in boss_proj:
                boss.health -= 2 * boss.damage
                tri.score += 2

def recshoot(tri):
    for rec in Game_class.Rec.List:
        if rec.CT > 24: fire_mode_e(rec,tri,rec.CT)


def bossfire(tri):
    for boss in Game_class.Boss.List:
        if boss.stage == 1: boss.stime  = 12; boss.FM = random.randint(1,5); fire_mode_e(boss,tri,boss.CT2)
        elif boss.stage == 2: boss.stime  = 6; boss.FM = random.randint(1,5); fire_mode_e(boss,tri,boss.CT2)
        elif boss.stage == 3: boss.stime  = 6; boss.FM = random.randint(6,9); fire_mode_e(boss,tri,boss.CT2)

def collected(tri):
    tri_col = pygame.sprite.spritecollide(tri, Game_class.Gld.List, True)
    if len(tri_col) > 0:
        for _ in tri_col:
            tri.score += 50
    
def fire_mode(tri,FM):
    if FM in [1]:
        p1 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p1.vely = -10
        p2 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p2.velx = -3
        p2.vely = -10
        p3 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p3.velx = 3
        p3.vely = -10
    if FM in [2]:
        p1 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p1.vely = -10
        p2 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p2.velx = -3
        p2.vely = -10
        p3 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p3.velx = 3
        p3.vely = -10
        p4 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p4.velx = -6
        p4.vely = -10
        p5 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p5.velx = 6
        p5.vely = -10
    if FM in [3]:
        p1 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p1.vely = -10
        p2 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p2.velx = -2
        p2.vely = -10
        p3 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p3.velx = 2
        p3.vely = -10
        p4 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p4.velx = -4
        p4.vely = -10
        p5 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p5.velx = 4
        p5.vely = -10
        p6 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p6.velx = -6
        p6.vely = -10
        p7 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p7.velx = 6
        p7.vely = -10
        p8 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p8.velx = -8
        p8.vely = -10
        p9 = Game_class.Cirfire(tri.rect.x+tri.rect.width/2-5, tri.rect.y, "image/f1.png")
        p9.velx = 8
        p9.vely = -10

def tfire_mode(tri,FM):
    if FM in [1]:
        Game_class.Trcfire(tri.rect.x+tri.rect.width/2-10-20, tri.rect.y+10, "image/f10.png")
        Game_class.Trcfire(tri.rect.x+tri.rect.width/2-10+20, tri.rect.y+10, "image/f10.png")
    elif FM in [2]:
        Game_class.Trcfire(tri.rect.x+tri.rect.width/2-10-20, tri.rect.y+10, "image/f10.png")
        Game_class.Trcfire(tri.rect.x+tri.rect.width/2-10+20, tri.rect.y+10, "image/f10.png")
        Game_class.Trcfire(tri.rect.x+tri.rect.width/2-10-40, tri.rect.y+20, "image/f10.png")
        Game_class.Trcfire(tri.rect.x+tri.rect.width/2-10+40, tri.rect.y+20, "image/f10.png")
    
def fire_mode_e(obj,tri,CT):
        if obj.FM in [1]:
            if CT % obj.stime == 0:
                p1 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.vely = 5
        elif obj.FM in [2]:
            if CT % obj.stime == 0:
                abd = sqrt((obj.rect.x-tri.rect.x)**2.0+(obj.rect.y-tri.rect.y)**2.0)
                p1  = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.velx = -(obj.rect.x-tri.rect.x)/abd*8.0
                p1.vely = -(obj.rect.y-tri.rect.y)/abd*8.0
        elif obj.FM in [3]:
            if CT % obj.stime == 0:
                p1 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.velx = 3.5
                p1.vely = 5
                p2 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p2.vely = 5
                p3 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p3.velx = -3.5
                p3.vely = 5
        elif obj.FM in [4]:
            if CT % (obj.stime * 2) == 0:
                p1 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.velx = 0.0
                p1.vely = sqrt(2.0)
                p2 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p2.velx = 0.0
                p2.vely =-sqrt(2.0)+1
                p3 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p3.velx =-sqrt(2.0)+1
                p3.vely = 0.0
                p4 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p4.velx = sqrt(2.0)
                p4.vely = 0.0
                p5 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p5.velx = 1
                p5.vely = 1
                p6 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p6.velx = 1
                p6.vely =-1
                p7 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p7.velx =-1
                p7.vely = 1
                p8 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p8.velx =-1
                p8.vely =-1
        elif obj.FM in [5]:
            if CT > obj.stime and CT < obj.stime+10:
                abd = sqrt((obj.rect.x-tri.rect.x)**2.0+(obj.rect.y-tri.rect.y)**2.0)
                p1  = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.velx = -(obj.rect.x-tri.rect.x)/abd*8.0
                p1.vely = -(obj.rect.y-tri.rect.y)/abd*8.0
        elif obj.FM in [6]:
            if CT % obj.stime == 0:
                abd = sqrt((obj.rect.x-tri.rect.x)**2.0+(obj.rect.y-tri.rect.y)**2.0)
                p1  = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.velx = -(obj.rect.x-tri.rect.x)/abd*8.0*2.0
                p1.vely = -(obj.rect.y-tri.rect.y)/abd*8.0*2.0
        elif obj.FM in [7]:
            if CT % obj.stime == 0:
                p1 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.velx = 3.5*2.0
                p1.vely = 5*2.0
                p2 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p2.vely = 5*2.0
                p3 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p3.velx = -3.5*2.0
                p3.vely = 5*2.0
        elif obj.FM in [8]:
            if CT % (obj.stime * 2) == 0:
                p1 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.velx = 0.0
                p1.vely = sqrt(2.0)*2.0
                p2 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p2.velx = 0.0
                p2.vely =-sqrt(2.0)*2.0+1
                p3 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p3.velx =-sqrt(2.0)*2.0+1
                p3.vely = 0.0*2.0
                p4 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p4.velx = sqrt(2.0)*2.0
                p4.vely = 0.0*2.0
                p5 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p5.velx = 1*2.0
                p5.vely = 1*2.0
                p6 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p6.velx = 1*2.0
                p6.vely =-1*2.0
                p7 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p7.velx =-1*2.0
                p7.vely = 1*2.0
                p8 = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p8.velx =-1*2.0
                p8.vely =-1*2.0
        elif obj.FM in [9]:
            if CT > obj.stime and CT < obj.stime+10:
                abd = sqrt((obj.rect.x-tri.rect.x)**2.0+(obj.rect.y-tri.rect.y)**2.0)
                p1  = Game_class.Recfire(obj.rect.x+obj.rect.width/2-5, obj.rect.y+obj.rect.height, "image/f2.png")
                p1.velx = -(obj.rect.x-tri.rect.x)/abd*8.0*2.0
                p1.vely = -(obj.rect.y-tri.rect.y)/abd*8.0*2.0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        