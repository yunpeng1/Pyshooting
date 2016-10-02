import pygame,sys,time
from Game_class import *
from Process_class import *

def Run_Game():
    pygame.init()
    pygame.font.init()
    #Prestage
    SCREENWIDTH, SCREENHEIGHT = 360,640
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT),0,32)
    background  = pygame.image.load("image/background1.png")
    _,bh        = background.get_size()
    background_loc1 =  0
    background_loc2 = -bh
    myfont      = pygame.font.SysFont(None, 25)
    stfont      = pygame.font.SysFont(None, 50)
    endfont     = pygame.font.SysFont(None, 30)
    clock       = pygame.time.Clock()
    FPS         = 30
    totalframes = 0
    loc_xy      = 0
    start_list  = [(SCREENWIDTH/6,SCREENHEIGHT/8*1.8,SCREENWIDTH/3*2,80),
                   (SCREENWIDTH/6,SCREENHEIGHT/8*3.8,SCREENWIDTH/3*2,80),
                   (SCREENWIDTH/6,SCREENHEIGHT/8*5.8,SCREENWIDTH/3*2,80),
                   (SCREENWIDTH/12,SCREENHEIGHT/8*7.2,SCREENWIDTH/5,50)]
    
    Game_Exit = False; Game_Over = False; Game_start = False; Game_Restart = False; Game_Begin = True; Game_Level = False; Game_Instruction = False
    while not Game_Exit:
        
        while Game_Begin:
            totalframes += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if loc_xy != 0: loc_xy -= 1         
                        else: loc_xy = 2
                    elif event.key == pygame.K_DOWN:
                        if loc_xy != 2: loc_xy += 1         
                        else: loc_xy = 0                       
                    elif event.key == pygame.K_RETURN:
                        if loc_xy in [0]: Game_Begin = 0; Game_Level = 1
                        if loc_xy in [1]: Game_Begin = 0; Game_Instruction = 1
                        if loc_xy in [2]: pygame.quit(); sys.exit()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(); sys.exit()
            screen.fill((0,200,200)) # fill black
            for i in xrange(1,SCREENHEIGHT/10):
                pygame.draw.line(screen, (0,255,0),     (0,10*i),    (SCREENWIDTH,10*i))
            for i in xrange(1,SCREENWIDTH/10):
                pygame.draw.line(screen, (0,255,0),     (10*i,0),    (10*i,SCREENHEIGHT))
            screen.fill((0,125,125),(SCREENWIDTH/6,SCREENHEIGHT/8*1.8,SCREENWIDTH/3*2,80))
            screen.fill((0,125,125),(SCREENWIDTH/6,SCREENHEIGHT/8*3.8,SCREENWIDTH/3*2,80))
            screen.fill((0,125,125),(SCREENWIDTH/6,SCREENHEIGHT/8*5.8,SCREENWIDTH/3*2,80))
            screen.fill((0,100+totalframes/10%2*10,205+totalframes/10%2*10),start_list[loc_xy])
            stext0 = myfont.render("Programmer: Victor brid", 1, (255,255,255))
            stext5 = myfont.render("Version: 1.0.0", 1, (255,255,255))
            stext1 = stfont.render("Start", 1, (255,255,255))
            stext2 = stfont.render("Instruction", 1, (255,255,255))
            stext3 = stfont.render("Exit", 1, (255,255,255))
            screen.blit(stext1, (SCREENWIDTH/2.7, SCREENHEIGHT/8*2.1))
            screen.blit(stext2, (SCREENWIDTH/4.0, SCREENHEIGHT/8*4.1))
            screen.blit(stext3, (SCREENWIDTH/2.7, SCREENHEIGHT/8*6.1))
            screen.blit(stext0, (SCREENWIDTH/2.5, SCREENHEIGHT/8*0.5))
            screen.blit(stext5, (SCREENWIDTH/1.5, SCREENHEIGHT/8*7.3))
            pygame.display.flip()
            clock.tick(FPS)

        while Game_Instruction:
            totalframes += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Run_Game()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(); sys.exit()
                        
            screen.fill((0,0,0)) # fill black
            inslabel1 = endfont.render("Press 'Z' to shoot", 1, (255,255,255))
            inslabel2 = endfont.render("Press 'L_SHIFT' to accelerate", 1, (255,255,255))
            inslabel3 = endfont.render("Press 'ARROW' to move", 1, (255,255,255))
            inslabel4 = endfont.render("Press 'ESC' to exit", 1, (255,255,255))
            instext   = endfont.render("Press 'Enter' to go back", 1, (totalframes/10%2*255,totalframes/10%2*255,totalframes/10%2*255))
            screen.blit(inslabel1, (SCREENWIDTH/7, SCREENHEIGHT/3))
            screen.blit(inslabel2, (SCREENWIDTH/7, SCREENHEIGHT/5))
            screen.blit(inslabel3, (SCREENWIDTH/7, SCREENHEIGHT/2.1))
            screen.blit(inslabel4, (SCREENWIDTH/7, SCREENHEIGHT/1.6))
            screen.blit(instext, (SCREENWIDTH/5.5, SCREENHEIGHT/1.3))
            pygame.display.flip()
            clock.tick(FPS)
            
        while Game_Level:
            totalframes += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if loc_xy != 0: loc_xy -= 1         
                        else: loc_xy = 2
                    elif event.key == pygame.K_DOWN:
                        if loc_xy != 3: loc_xy += 1         
                        else: loc_xy = 0                       
                    elif event.key == pygame.K_RETURN:
                        if loc_xy in [0]: 
                            Game_Level = 0; GameLevel = 0; Game_start =1
                            tri         = Tri(SCREENWIDTH/2-25, SCREENHEIGHT-50, "image/t1.png", GameLevel)
                        if loc_xy in [1]: 
                            Game_Level = 0; GameLevel = 1; Game_start =1
                            tri         = Tri(SCREENWIDTH/2-25, SCREENHEIGHT-50, "image/t1.png", GameLevel)
                        if loc_xy in [2]: 
                            Game_Level = 0; GameLevel = 2; Game_start =1
                            tri         = Tri(SCREENWIDTH/2-25, SCREENHEIGHT-50, "image/t1.png", GameLevel)
                        if loc_xy in [3]: 
                            Game_Level = 0; Game_Begin = 1; loc_xy = 0
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(); sys.exit()
            screen.fill((0,200,200)) # fill black
            for i in xrange(1,SCREENHEIGHT/10):
                pygame.draw.line(screen, (0,255,0),     (0,10*i),    (SCREENWIDTH,10*i))
            for i in xrange(1,SCREENWIDTH/10):
                pygame.draw.line(screen, (0,255,0),     (10*i,0),    (10*i,SCREENHEIGHT))
            screen.fill((0,125,125),(SCREENWIDTH/6,SCREENHEIGHT/8*1.8,SCREENWIDTH/3*2,80))
            screen.fill((0,125,125),(SCREENWIDTH/6,SCREENHEIGHT/8*3.8,SCREENWIDTH/3*2,80))
            screen.fill((0,125,125),(SCREENWIDTH/6,SCREENHEIGHT/8*5.8,SCREENWIDTH/3*2,80))
            screen.fill((0,125,125),start_list[3])
            screen.fill((0,100+totalframes/10%2*10,205+totalframes/10%2*10),start_list[loc_xy])
            stext1 = stfont.render("Easy", 1, (255,255,255))
            stext2 = stfont.render("Normal", 1, (255,255,255))
            stext3 = stfont.render("Hard", 1, (255,255,255))
            stext4 = endfont.render("Back", 1, (255,255,255))
            screen.blit(stext1, (SCREENWIDTH/2.7, SCREENHEIGHT/8*2.1))
            screen.blit(stext2, (SCREENWIDTH/3.0, SCREENHEIGHT/8*4.1))
            screen.blit(stext3, (SCREENWIDTH/2.7, SCREENHEIGHT/8*6.1))
            screen.blit(stext4, (SCREENWIDTH/8.5, SCREENHEIGHT/8*7.4))
            pygame.display.flip()
            clock.tick(FPS)
        
        while Game_Over:
            totalframes += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Game_Restart = True
                        Tri.update_all(SCREENWIDTH, SCREENHEIGHT, Game_Restart, Rec.Dnum)
                        Rec.update_all(SCREENHEIGHT, Game_Restart)
                        Cirfire.update_all(Game_Restart)
                        Recfire.update_all(SCREENWIDTH, SCREENHEIGHT, Game_Restart)
                        Gld.update_all(SCREENHEIGHT, Game_Restart)
                        Exp.update_all(Game_Restart)
                        Boss.update_all(Game_Restart)
                        Trcfire.update_all(Game_Restart)
                        Run_Game()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(); sys.exit()
                        
            screen.fill((0,0,0)) # fill black
            if not Boss.Ifwin:
                endlabel = endfont.render("Game Over", 1, (255,255,255))
            else:
                endlabel = endfont.render("  You Win!", 1, (255,255,255))
            endtext  = endfont.render("Press 'Enter' to restart", 1, (totalframes/10%2*255,totalframes/10%2*255,totalframes/10%2*255))
            endscore = endfont.render("Score of Player 1 is: %d" % (Tri.Pscore[0]), 1, (0,255,0))
            screen.blit(endlabel, (SCREENWIDTH/3, SCREENHEIGHT/3))
            screen.blit(endtext, (SCREENWIDTH/5.5, SCREENHEIGHT/1.3))
            screen.blit(endscore, (SCREENWIDTH/6, SCREENHEIGHT/2))               
            pygame.display.flip()
            clock.tick(FPS)

        while Game_start:
            #time contral
            totalframes += 1
            background_loc1 += 1
            background_loc2 += 1
            if background_loc1 > bh: background_loc1 = -bh
            if background_loc2 > bh: background_loc2 = -bh
            # start processing
            process(SCREENWIDTH, SCREENHEIGHT, FPS, totalframes, GameLevel)
            label1 = myfont.render("Score is: %g"%tri.score, 1, (0,255,255))
            label2 = myfont.render("Life: %d"%tri.life, 1, (0,255,255))
            label3 = myfont.render("", 1, (255,255,255))
            ltext  = myfont.render("Level Up!", 1, (255,255,255))
            for rec in Rec.List:
                Trcfire.obj = rec
            for boss in Boss.List:
                if boss.stage in [1,2,3]:
                    label3 = myfont.render("Boss: %d"%boss.health, 1, (255,255,255))
                    Trcfire.obj = boss
            #LOGIC
            Tri.update_all(SCREENWIDTH, SCREENHEIGHT, Game_Restart, Rec.Dnum)
            Rec.update_all(SCREENHEIGHT, Game_Restart)
            Cirfire.update_all(Game_Restart)
            Recfire.update_all(SCREENWIDTH, SCREENHEIGHT, Game_Restart)
            Gld.update_all(SCREENHEIGHT, Game_Restart)
            Exp.update_all(Game_Restart)
            Boss.update_all(Game_Restart)
            Trcfire.update_all(Game_Restart)
            #LOGIC
            #DRAW
            screen.blit(background,(0,background_loc1))#screen.fill( screen_color )
            screen.blit(background,(0,background_loc2))
            BaseClass.allsprites.draw(screen)
            Cirfire.List.draw(screen)
            Recfire.List.draw(screen)
            Trcfire.List.draw(screen)
            screen.blit(label1, (240, 30))
            screen.blit(label2, (30, 30))
            screen.blit(label3, (130, 50))
            if Tri.numplayer == 0: Game_Over = 1; Game_start = 0; break
            if Tri.Level_up and Tri.Level_t < 30: 
                for tri in Tri.List:
                    screen.blit(ltext, (tri.rect.x, tri.rect.y-tri.rect.height/2))
                Tri.Level_t += 1
            else: Tri.Level_up = 0; Tri.Level_t = 0
            if Boss.Ifwin and Boss.win_t == 80: Game_Over = 1; Game_start = 0; break
            elif Boss.Ifwin and Boss.win_t < 80: Boss.win_t += 1
            pygame.display.flip()
            #DRAW
            clock.tick(FPS)

if __name__ == "__main__":
    Run_Game()