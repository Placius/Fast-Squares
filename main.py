import pygame
import sys, time

pygame.init()
# rozmiar okna
win = pygame.display.set_mode((500, 500))
# nazwa gry
pygame.display.set_caption("Fast Squares")
# kolor tła
win.fill((230,214,144))
# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
BIALY = (255, 255, 255)
CURRY = (157, 145, 1)
ROZOWY = (255,182,193)
CZARNY = (0, 0, 0)

# plansza widok uproszczony, roboczy
plansza = [0, 0, 0,
           0, 0, 0,
           0, 0, 0]

# aktualna liczba zdobytych punktów
points = 0

# import funkcji pokazującej punkty na ekranie
from funkcje import pokaz_punkty

# zmiana kolorów/aktualny kolor kwadracików
pygr = 0

# aktualna liczba kolorowych kwadracików wyświetlancyh na ekranie
color_squares = 3

# losowanie indeksów dla kolorych kwadracików
from funkcje import losuj_indexy
indexy = losuj_indexy()
for i in indexy:
    plansza[i] = 1

# w przypadku gdy równa się 1 pokazuje wynik zdobyty podczas rozgrywki (dana pomocnicza)
show_score = 0

# muzyka w tle
import pyglet

def music_play():
    music = pyglet.resource.media('music.mp3')
    music.play()

music_play()
kolor_tlo = (30,30,30)
from funkcje import nowa_plansza, Kwadrat
tlo = Kwadrat(win, kolor_tlo, 0, 0, 500)

# pętla główna działająca aż do wyjścia z programu  przy użyciu X
while 1:
    if show_score == 1:
        # nałożenie tła
        win.fill((230,214,144))
        # tło 
        tlo.actual()
        # wynik końcowy
        font_points = pygame.font.SysFont('comicsansms', 60)
        label_points = font_points.render('Score: ' + str(points), 1, (0, 0, 0))
        win.blit(label_points, (80, 200))
        # powrót do menu
        font = pygame.font.SysFont('comicsansms', 20)
        label_back = font.render('back to menu', 1, (0,0,0))
        win.blit(label_back, (190, 470))

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    # powrót do menu
                    if mx > 180 and mx < 320:
                        if my > 475 and my < 495:
                            try:
                                with open("Ranking.txt" ,"a+", encoding='utf8') as file:
                                    file.write(str(points) + "\n")

                            except FileNotFoundError:
                                with open("Ranking.txt" ,"w+", encoding='utf8') as file:
                                    file.write(str(points) + "\n")
                            points = 0
                            run = False
            pygame.display.update()

    # zaimportowanie funkcji menu
    from funkcje import menu
    menu(win)

    # nadanie kolejnej warstwy tła
    win.fill((230,214,144))
    tlo.actual()

    # stworzenie pierwszej planszy
    # zaimportowanie modułu nowej planszy
    from funkcje import nowa_plansza, Kwadrat
    k1, k2, k3, k4, k5, k6, k7, k8, k9 = nowa_plansza(pygr, win, plansza)

    # logo gry - label
    font = pygame.font.SysFont('comicsans', 40)
    label = font.render('Fast Squares', 1, FIOLETOWY)
    win.blit(label, (157, 435))

    # powrót do menu - label
    font = pygame.font.SysFont('comicsansms', 20)
    label = font.render('back to menu', 1, CZARNY)
    win.blit(label, (190, 470))

    # label punkty - label
    pokaz_punkty(win, points)

    #pobranie tickow startowych
    start_ticks=pygame.time.get_ticks()

    # pętla wykonuje się aż do powrotu do menu bądz przekroczenia limitu czasowego dla rozgrywki
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
                
            # timer
            # obliczenie ile sekund 
            sekundy=(pygame.time.get_ticks()-start_ticks)/1000        
            font = pygame.font.SysFont('comicsans', 30)
            deadline = 60 - sekundy
            label = font.render('Time: ' + str(deadline) + "      ", 1, (0, 0, 0), (255, 255, 255))
            win.blit(label, (360, 465))

            # operacje wykonywane pokliknięciu myszką
            if event.type == pygame.MOUSEBUTTONDOWN:
                # aktualna pozycja myszki
                mx, my = pygame.mouse.get_pos()
                if mx > 50 and mx < 150:
                    if my > 20 and my < 120:
                        if k1.color == ZOLTY or k1.color == ROZOWY or k1.color == ZIELONY or k1.color == CZERWONY:
                            points += 100
                            k1.color = BIALY
                            k1.actual()
                            plansza[0] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (60, 60))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (50, 60))
                            points -= 10
                            pokaz_punkty(win, points)

                    elif my > 170 and my < 270:
                        if k4.color == ZOLTY or k4.color == ROZOWY or k4.color == ZIELONY or k4.color == CZERWONY:
                            points += 100
                            k4.color = BIALY
                            k4.actual()
                            plansza[3] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (60, 210))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (50, 210))
                            points -= 10
                            pokaz_punkty(win, points)

                    elif my > 320 and my < 420:
                        if k7.color == ZOLTY or k7.color == ROZOWY or k7.color == ZIELONY or k7.color == CZERWONY:
                            points += 100
                            k7.color = BIALY
                            k7.actual()
                            plansza[6] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (60, 360))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (50, 360))
                            points -= 10
                            pokaz_punkty(win, points)

                    else:
                        print('PUSTE POLE')
                
                elif mx > 200 and mx < 350:
                    if my > 20 and my < 120:
                        if k2.color == ZOLTY or k2.color == ROZOWY or k2.color == ZIELONY or k2.color == CZERWONY:
                            points += 100
                            k2.color = BIALY
                            k2.actual()
                            plansza[1] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (210, 60))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (200, 60))
                            points -= 10
                            pokaz_punkty(win, points)

                    elif my > 170 and my < 270:
                        if k5.color == ZOLTY or k5.color == ROZOWY or k5.color == ZIELONY or k5.color == CZERWONY:
                            points += 100
                            k5.color = BIALY
                            k5.actual()
                            plansza[4] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (210, 210))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (200, 210))
                            points -= 10
                            pokaz_punkty(win, points)

                    elif my > 320 and my < 420:
                        if (k8.color == ZOLTY or k8.color == ROZOWY or k8.color == ZIELONY or k8.color == CZERWONY):
                            points += 100
                            k8.color = BIALY
                            k8.actual()
                            plansza[7] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (210, 360))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (200, 360))
                            points -= 10
                            pokaz_punkty(win, points)

                    else:
                        print('PUSTE POLE')
                
                elif mx > 350 and mx < 450:
                    if my > 20 and my < 120:
                        if k3.color == ZOLTY or k3.color == ROZOWY or k3.color == ZIELONY or k3.color == CZERWONY:
                            points += 100
                            k3.color = BIALY
                            k3.actual()
                            plansza[2] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (360, 60))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (350, 60))
                            points -= 10
                            pokaz_punkty(win, points)


                    elif my > 170 and my < 270:
                        if k6.color == ZOLTY or k6.color == ROZOWY or k6.color == ZIELONY or k6.color == CZERWONY:
                            points += 100
                            k6.color = BIALY
                            k6.actual()
                            plansza[5] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (360, 210))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (350, 210))
                            points -= 10
                            pokaz_punkty(win, points)

                    elif my > 320 and my < 420:
                        if k9.color == ZOLTY or k9.color == ROZOWY or k9.color == ZIELONY or k9.color == CZERWONY:
                            points += 100
                            k9.color = BIALY
                            k9.actual()
                            plansza[8] = 0
                            color_squares -= 1
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('+100pkt', 1, ZIELONY)
                            win.blit(label_points, (360, 360))
                            pokaz_punkty(win, points)
                        else:
                            # label punkty jednorazowo pokazywane
                            font_points = pygame.font.SysFont('comicsans', 30)
                            label_points = font_points.render('   -10pkt   ', 1, CZERWONY)
                            win.blit(label_points, (350, 360))
                            points -= 10
                            pokaz_punkty(win, points)

                    else:
                        print('PUSTE POLE')
                
                else:
                    print('PUSTE POLE')

                # powrót do menu
                if mx > 180 and mx < 320:
                    if my > 475 and my < 495:
                        for i in range(0,9):
                            plansza[i]= 0
                        indexy = losuj_indexy()
                        for i in indexy:
                            plansza[i] = 1
                        k1, k2, k3, k4, k5, k6, k7, k8, k9 = nowa_plansza(pygr, win, plansza)
                        points = 0
                        color_squares = 3
                        pygr = 0
                        run = False

                if color_squares == 0:
                    pygr += 1
                    if pygr == 4:
                        pygr = 0
                    indexy = losuj_indexy()
                    for i in indexy:
                        plansza[i] = 1
                    k1, k2, k3, k4, k5, k6, k7, k8, k9 = nowa_plansza(pygr, win, plansza)
                    color_squares = 3

                if deadline <= 30:
                    for i in range(0,9):
                        plansza[i]= 0
                    indexy = losuj_indexy()
                    for i in indexy:
                        plansza[i] = 1
                    k1, k2, k3, k4, k5, k6, k7, k8, k9 = nowa_plansza(pygr, win, plansza)
                    show_score = 1
                    color_squares = 3
                    pygr = 0
                    run = False

        pygame.display.update()