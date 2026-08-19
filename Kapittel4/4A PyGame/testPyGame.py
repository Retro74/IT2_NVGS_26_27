import pygame
 
pygame.init()
 
skjerm = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Firkant")
 
kjorer = True
while kjorer:
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjorer = False
 
    skjerm.fill((30, 30, 30))  # bakgrunnsfarge
    pygame.draw.rect(skjerm, (50, 150, 255), (150, 150, 100, 100))  # firkant
 
    pygame.display.flip()
 
pygame.quit()