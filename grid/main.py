import pygame


class Grid:
    def __init__(self, width, height, pixel_size=1, grid_color="white"):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.grid_color = grid_color
        if pixel_size > 1:
            self.surface_width = width * ((pixel_size if pixel_size > 1 else 0)  + 1) + 1
            self.surface_height = height * ((pixel_size if pixel_size > 1 else 0) + 1) + 1
        else:
            self.surface_width = width
            self.surface_height = height
        self._surface = pygame.Surface((self.surface_width, self.surface_height))

    @property
    def surface(self):
        return self._surface
    
    def set_grid(self):
        if self.pixel_size == 1:
            return
        for x in range(0, self.surface_width + 1, self.pixel_size + 1):
            pygame.draw.line(self.surface, self.grid_color, (x, 0), (x, self.surface_height - 1))
        for y in range(0, self.surface_height + 1, self.pixel_size + 1):
            pygame.draw.line(self.surface, self.grid_color, (0, y), (self.surface_width, y))
    def set_pixel(self, x, y, color="white"):
        if self.pixel_size == 1:
            self.surface.set_at((x, y), color)
        else:
            pygame.draw.rect(
                self._surface,
                color,
                pygame.Rect(
                    x *(self.pixel_size + 1) + 1, 
                    y *(self.pixel_size + 1) + 1, 
                    self.pixel_size,
                    self.pixel_size
                )
            )

if __name__ == "__main__":
    pygame.init()
    display = Grid(100, 100, 1, "red")
    screen = pygame.display.set_mode((display.surface_width, display.surface_height))
    display.set_grid()
    display.set_pixel(50, 50)

    running = True
    while running:
        screen.blit(display.surface, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                pygame.quit()
                running = False