import pygame

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
    BIALY = (255,255,255)
    ROZOWY = ((255,182,193))
    color = BIALY
    if pygr == 0:
        color = ROZOWY
    elif pygr == 1:
        color = ZOLTY
    elif pygr == 2:
        color = ZIELONY
    elif pygr == 3:
        color = CZERWONY

    plansza_na_9 = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

    # szerokość ekranu
    szer = win.get_width

    posX = 50
    posY = 20

    kwadrat_side = 100

    kwadrat_aktualny = 1
    rzad = 1

    indeks_planszy = 0

    for i in plansza:
        if i == 1:
            plansza_na_9[indeks_planszy] = Kwadrat(win, color, posX, posY, kwadrat_side)
            plansza_na_9[indeks_planszy].actual()
        else:
            plansza_na_9[indeks_planszy] = Kwadrat(win, BIALY, posX, posY, kwadrat_side)
            plansza_na_9[indeks_planszy].actual()
        # zmiana kwadratu
        kwadrat_aktualny += 1
        posX += 150

        # zmiana rzędu
        if kwadrat_aktualny == 4:
            rzad += 1
            posX = 50
            posY += 150

        if kwadrat_aktualny == 7:
            rzad += 1
            posX = 50
            posY += 150
    
    return plansza_na_9

pygame.init()
# rozmiar okna
win = pygame.display.set_mode((500, 500))
# nazwa gry
pygame.display.set_caption("Fast Squares")
# kolor tła
win.fill((230,214,144))

# plansza widok uproszczony, roboczy
plansza_na9 = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

mala_plansza = nowa_plansza(0, win, plansza_na9)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        # operacje wykonywane pokliknięciu myszką
        if event.type == pygame.MOUSEBUTTONDOWN:
            # aktualna pozycja myszki
            mx, my = pygame.mouse.get_pos()

            mala_plansza[0].color = (0,0,0)
            mala_plansza[0].actual()

    pygame.display.update() 