# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from pygame.locals import *
import sys
import time
import random

pygame.init()

def dajRecenicu():
    file = open("sentences.txt", "r")
    niz = [line.strip("\n") for line in file.readlines()]
    file.close()
    brojRecenica = len(niz)
    nasumicno = random.randint(0, brojRecenica-1)
    return niz[nasumicno]
# Press the green button in the gutter to run the script.

def prebrojRijeci(recenica):
    return len(recenica.split(" "))

def dajPreciznost(prva, druga):
    prviNiz = prva.split(" ")
    drugiNiz = druga.split(" ")
    i = 0
    tacni = 0
    for element in prviNiz:
        if drugiNiz[i] == element:
            tacni += 1
        i += 1
    return tacni / len(drugiNiz) * 100

def pohvala(wpm1, preciznost):
    wpm = float(wpm1)
    if(wpm >= 65 and preciznost >= 95):
        return "Wow bruda, zvijer si!"
    elif(wpm >= 60 and preciznost >= 85):
        return "Opa burke, svaka ćas!"
    elif(wpm >= 55 and preciznost >= 75):
        return "Nije lose braca"
    elif(preciznost <= 40):
        return "Mogao si nesto i pravilno napisati ocm"
    elif(wpm <=  40):
        return "Spor si ko mazga"
    else:
        return "Onako"

def main():
    (sirina, visina) = (1000, 600)
    screen = pygame.display.set_mode((sirina, visina))
    pygame.display.set_caption("Daj tekst brt")
    font = pygame.font.Font('freesansbold.ttf', 32)
    randomRecenica = dajRecenicu()
    brojSlova = len(randomRecenica)
    brojRijeci = prebrojRijeci(randomRecenica)
    recenica = font.render(randomRecenica, True, (0, 0, 128))
    recenicaRect = recenica.get_rect()
    recenicaRect.center = (sirina / 2, visina / 3)
    text = ""
    gotovo = False
    br = 0
    preciznost = 0

    screenOn = True
    while screenOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screenOn = False
            if event.type == pygame.KEYDOWN:
                if br == 0:
                    vrijemePocetka = time.time()
                    br = 1
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    vrijemeKraja = time.time()
                    konacniRezultat = vrijemeKraja - vrijemePocetka
                    gotovo = True
                    preciznost = dajPreciznost(text, randomRecenica)
                else:
                    text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                pozicija = event.pos
                if resetRect.collidepoint(pozicija):
                    screenOn = False
                    main()

        screen.fill(0)
        if gotovo:
            wpm = "{:.0f}".format(60 / (konacniRezultat / brojRijeci))
            rezultat = "Rezultat: " + "{:.2f}".format(konacniRezultat) + "s; Preciznost: " + "{:.2f}".format(preciznost) + "%; Riječi po minuti: " + wpm
            rezultatRender = font.render(rezultat, True, (255, 255, 255))
            rezultatRect = rezultatRender.get_rect()
            rezultatRect.center = (sirina / 2, visina / 1.5)
            pohvalaRender = font.render(pohvala(wpm, preciznost), True, (255, 255, 255))
            pohvalaRect = pohvalaRender.get_rect()
            pohvalaRect.top = rezultatRect.bottom
            pohvalaRect.centerx = rezultatRect.centerx
            screen.blit(rezultatRender, rezultatRect)
            screen.blit(pohvalaRender, pohvalaRect)

        screen.blit(recenica, recenicaRect)
        resetRender = font.render("Reset", True, (255, 255, 255))
        resetRect = resetRender.get_rect()
        resetRect.center = (sirina / 2, visina / 1.1)
        pygame.draw.rect(screen, (255, 0, 0), resetRect)
        screen.blit(resetRender, resetRect)
        textRender = font.render(text, True, (255, 255, 255))
        textRect = textRender.get_rect()
        textRect.left = recenicaRect.left - 2
        textRect.top = visina / 2
        textRect.w = recenicaRect.w + 5
        screen.blit(textRender, textRect)
        pygame.draw.rect(screen, (0, 100, 0), textRect, 2)
        pygame.display.flip()

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
