from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.zombies import Zombie
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, ZOMBIE
import pygame
from random import randint 

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = randint(0, 2)  ##0=Cactus, 1=Bird, 2=zombie
            if obstacle_type == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif obstacle_type == 1:
                self.obstacles.append(Bird(BIRD))
            else:
                self.obstacles.append(Zombie(ZOMBIE))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
             if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count +=1
                    break
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []