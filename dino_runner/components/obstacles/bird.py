
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self, image_list):
        self.type = 0
        self.images = image_list
        self.index = 0
        super().__init__(self.images[self.index])
        self.rect.y = 250
        self.image_change_delay = 10
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed / 3
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
        
        self.image_change_delay -= 1
        if self.image_change_delay == 0:
            self.index = (self.index + 1) % 2  # Cambiar la imagen entre dos posibles
            self.image = self.images[self.index]
            self.image_change_delay = 20

        super().update(game_speed, obstacles)
