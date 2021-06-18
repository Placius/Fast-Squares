# zaimportowanie standardowych modułów
import random, pygame, sys

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
BIALY = (255, 255, 255)
CURRY = (157, 145, 1)
ROZOWY = (255,182,193)
CZARNY = (0, 0, 0)

# funkcja losuje indexy kwadratów
def losuj_indexy():
    numery = []
    while len(numery) != 3:
        a = random.randint(0, 8)
        if a in numery:
            continue
        else:
            numery.append(a)
    return numery

# klasa tworzy obiekty (kwadraty)
class Kwadrat:
    def __init__(self, screen, color, posX, PosY, side):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = PosY
        self.side = side
        self.logo = "Placius"
        self.logoColor = (0,0,0)
        self.font_points = pygame.font.SysFont('comicsansms', 20)
        self.label_points = self.font_points.render('Placius', 1, self.logoColor) 

    # tło gradient
    def gradientRect(self, screen, left_colour, right_colour, target_rect):
        colour_rect = pygame.Surface( ( 2, 2 ) )                                  
        pygame.draw.line( colour_rect, left_colour,  ( 1,0 ), ( 2,1 ) )            
        pygame.draw.line( colour_rect, right_colour, ( 1,1 ), ( 1,1 ) )            
        colour_rect = pygame.transform.smoothscale( colour_rect, ( self.side, self.side ) ) 
        self.screen.blit( colour_rect, target_rect )

    def actual(self):
        if self.color != (255,255,255):   
            self.gradientRect(self.screen, self.color, (250,244,227), (self.posX, self.posY, self.side, self.side))
            if self.color == (230,214,144) or self.color == (30,30,30):
                pass
            else:
                self.screen.blit(self.label_points, (self.posX+20, self.posY+35))
        else:
            # pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.side, self.side))
            self.gradientRect(self.screen, self.color, (250,244,227), (self.posX, self.posY, self.side, self.side))

# funkcja tworząca planszę wraz z przypadkowo wylosowanymi kolorowymi kwadratami
def nowa_plansza(pygr, screen, plansza):
    # okno gry
    win = screen
    color = BIALY
    if pygr == 0:
        color = ROZOWY
    elif pygr == 1:
        color = ZOLTY
    elif pygr == 2:
        color = ZIELONY
    elif pygr == 3:
        color = CZERWONY

    los = 0
    for i in plansza:
        if  los == 0:
            if i == 1:
                k1 = Kwadrat(win, color, 50, 20, 100)
                k1.actual()
            else:
                k1 = Kwadrat(win, BIALY, 50, 20, 100)
                k1.actual()
        if  los == 1:
            if i == 1:
                k2 = Kwadrat(win, color, 200, 20, 100)
                k2.actual()
            else:
                k2 = Kwadrat(win, BIALY, 200, 20, 100)
                k2.actual()
        if  los == 2:
            if i == 1:
                k3 = Kwadrat(win, color, 350, 20, 100)
                k3.actual()
            else:
                k3 = Kwadrat(win, BIALY, 350, 20, 100)
                k3.actual()
        if  los == 3:
            if i == 1:
                k4 = Kwadrat(win, color, 50, 170, 100)
                k4.actual()
            else:
                k4 = Kwadrat(win, BIALY, 50, 170, 100)
                k4.actual()
        if  los == 4:
            if i == 1:
                k5 = Kwadrat(win, color, 200, 170, 100)
                k5.actual()
            else:
                k5 = Kwadrat(win, BIALY, 200, 170, 100)
                k5.actual()
        if  los == 5:
            if i == 1:
                k6 = Kwadrat(win, color, 350, 170, 100)
                k6.actual()
            else:
                k6 = Kwadrat(win, BIALY, 350, 170, 100)
                k6.actual()
        if  los == 6:
            if i == 1:
                k7 = Kwadrat(win, color, 50, 320, 100)
                k7.actual()
            else:
                k7 = Kwadrat(win, BIALY, 50, 320, 100)
                k7.actual()
        if  los == 7:
            if i == 1:
                k8 = Kwadrat(win, color, 200, 320, 100)
                k8.actual()
            else:
                k8 = Kwadrat(win, BIALY, 200, 320, 100)
                k8.actual()
        if  los == 8:
            if i == 1:
                k9 = Kwadrat(win, color, 350, 320, 100)
                k9.actual()
            else:
                k9 = Kwadrat(win, BIALY, 350, 320, 100)
                k9.actual()

        los += 1
    
    return k1, k2, k3, k4, k5, k6, k7, k8, k9

# funkcja menu głównego
def menu(win):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print(mx, my)
                    # new game
                    if mx > 78 and mx < 425:
                        if my > 22 and my < 106:
                            run = False
                    # options
                    if mx > 168 and mx < 323:
                        if my > 125 and my < 175:
                            pass
                    # ranking
                    if mx > 170 and mx < 325:
                        if my > 228 and my < 268:
                            run = True
                            while run:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit(0)
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mx, my = pygame.mouse.get_pos()
                                        # powrót do menu
                                        if mx > 180 and mx < 320:
                                            if my > 475 and my < 495:
                                                run = False
                                    # zmiana kursora myszki
                                    mx, my = pygame.mouse.get_pos()
                                    if mx > 180 and mx < 320:
                                            if my > 475 and my < 495:
                                                pygame.mouse.set_cursor(*pygame.cursors.diamond)
                                    else:
                                        pygame.mouse.set_cursor(*pygame.cursors.ball)

                                    ranking(win)
                                    # powrót do menu naklejka
                                    font = pygame.font.SysFont('comicsansms', 20)
                                    label_back = font.render('Break the record', 1, (0, 0, 0))
                                    win.blit(label_back, (167, 470))

                                pygame.display.update()
                    # contact
                    if mx > 174 and mx < 320:
                        if my > 330 and my < 371:
                            pass
                    # quit
                    if mx > 199 and mx < 296:
                        if my > 425 and my < 479:
                            sys.exit(0)

            win.fill((230,214,144))
            # tło
            kolor_tlo = (30,30,30)
            tlo = Kwadrat(win, kolor_tlo, 0, 0, 500)
            # tło 
            tlo.actual()

            kolo = (0,0,0)
            font = pygame.font.SysFont("comicsansms", 40)
            font_newGame  = pygame.font.SysFont("comicsansms", 70)
            new_game = font_newGame.render('New Game', 1, kolo)
            win.blit(new_game, (80, 20))
            new_game = font.render('Options', 1, kolo)
            win.blit(new_game, (172, 120))
            new_game = font.render('Ranking', 1, kolo)
            win.blit(new_game, (175, 220))
            new_game = font.render('Contact', 1, kolo)
            win.blit(new_game, (177, 320))
            new_game = font.render('Quit', 1, kolo)
            win.blit(new_game, (205, 420))

        pygame.display.update()

def pokaz_punkty(win, points):
    # punkty pokazane na ekranie
    font_points = pygame.font.SysFont('comicsans', 30)
    label_points = font_points.render('Score: ' + str(points) + "     ", 1, (0, 0, 0), (255, 255, 255))
    win.blit(label_points, (20, 465))

# wyświetlenie rankingu najlepszych wyników
def ranking(win):
    win.fill((230,214,144))
    kolor_tlo = (255,255,255)
    tlo = Kwadrat(win, kolor_tlo, 0, 0, 500)
    # tło 
    tlo.actual()
    # napis Best Scores
    font = pygame.font.SysFont('comicsansms', 40)
    label_back = font.render('Best scores', 1, (0, 0, 0))
    win.blit(label_back, (145, 5))
    wyniki = []

    with open("Ranking.txt", "r+", encoding='utf8') as file:
        scores = file.read().split("\n")
        for score in scores:
            try:
                if int(score) == 0:
                    continue
                else:
                    wyniki.append(int(score))
            except ValueError:
                continue

    wyniki.sort(reverse=True)

    position = 1

    x = 20
    y = 70

    for score in wyniki:
        pos = (str(position) + ": " + str(score))
        font = pygame.font.SysFont('comicsansms', 20)
        label = font.render(pos, 1, (0,0,0))
        win.blit(label, (x, y))
        y += 40
        if position == 10:
            y = 70
            x = 190
        if position == 20:
            y = 70
            x = 380
        if position == 30:
            break
        position += 1