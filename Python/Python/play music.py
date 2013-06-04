import os
import sys
import pygame.mixer
import pygame.cdrom

pygame.mixer.init(44100, -16, 2, 4096)
reload(sys)
sys.setdefaultencoding('utf8')
pygame.mixer.music.load('D:\MUSICA\Mix canciones Cristianas.mp3')
#escribe la ruta completa donde se almacena la cancion y listo "DJ dale PLAY"
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)


