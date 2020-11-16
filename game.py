import pygame
import pygame.font
import rotacionar
import inicializar

pygame.init()

textos = ['Alexandre: Aerodinâmica', 'Brenda: Financeiro', 'Fernanda: Gestão', 'Filipe: Elétrica', 'Guilherme: Marketing', 'Heitor: Desempenho', 'Luisa: Gestão', 'Léo: Desempenho', 'Matheus: Cargas', 'Mylena: Capitã', 'Norton: Estabilidade', 'Robert: Elétrica', 'Thais: Aerodinâmica']
posText = []
plus = 0
for i in range(len(textos)):
    posText.append((250,plus))
    plus+=35

present = []
for i,j in zip(textos,posText):
    present.append(inicializar.Texto(i,j))

pngs = ['fly.png','fly.png','fly.png']
pos = [(200, 270),(550, 270),(200, 520)]
obj = []
for i in pngs:
    obj.append(rotacionar2.Rotation(i))

SIZE = (800,700)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

angle = 0
k = 8
done = False
simulate = False

while not done:
    clock.tick(120)
    if simulate:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(0)
        for x in range(len(obj)):
            obj[x].Rotate(screen,pos[x],angle)
        angle += k
        if angle == 48 or angle == -48:
            k = (-1*k)
        pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                simulate = True
        screen.fill(0)
        for y in range(len(present)):
            present[y].Show(screen,posText[y])
        pygame.display.flip()
pygame.quit()
