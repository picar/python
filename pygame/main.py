import pygame


pygame.init()

screen = pygame.display.set_mode((1200, 800))
display = pygame.Surface((1200,800))

px = None
py = None

running = True

while running:

    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if px is None:
            px, py = mx, my
        display.set_at((mx, my), "white")
        pygame.draw.line(display, "white", (px, py), (mx, my))
        px, py = mx, my
    else:
        px, py = None, None

    screen.blit(display, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.constants.QUIT:
            pygame.quit()
            running = False

