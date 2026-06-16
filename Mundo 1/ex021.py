# Faça um programa em Python que reproduza o áudio de um arquivo MP3:

import pygame 
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Música tocando! Aperte Enter para pausar...')
