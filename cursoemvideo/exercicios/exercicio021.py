import pygame
pygame.init()
pygame.mixer.music.load("exercicio021.mp3")
pygame.mixer.music.play()
#pygame.event.wait()  - Na aula ensinou assim (até aqui), mas não deu certo. Já com as linhas abaixo funcionou!!
pygame.mixer.music.set_volume(1)
x = input('digite enter para encerrar ...')

