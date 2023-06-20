print('Playing: Tadow by Masego \n')
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): pass
'''Originalmente, esse exercício não era para ser resolvido desse jeito, mas como os controles do pygame mudaram, eu
tive que ver os comentários do vídeo no YouTube. Ainda nem sei usar esse while... Enfim, funcionou!'''
