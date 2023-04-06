import pygame
import pygame.mixer 
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD, COLORS, MY_CLOUD, MY_SUN, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, COLORS, RUNNING, OST_MENU, OST_GAME
from dino_runner.components.dinosaur import Dinosaur 
from dino_runner.components.text_utils import TextUtils


class Game:
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 375
        self.x_pos_cloud = SCREEN_WIDTH
        self.y_pos_cloud = 100
        self.x_pos_mycloud = SCREEN_WIDTH
        self.y_pos_mycloud = 0
        self.x_pos_mysun = SCREEN_WIDTH
        self.y_pos_mysun =  40
        self.points = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.powerup_manager = PowerUpManager()
        self.text_utils = TextUtils()
        self.game_running = True
        self.death_count = 0
        self.menu = True

    def execute(self):
        while self.game_running:
            if self.menu:
                OST_MENU.play(-1)
            else:
                OST_MENU.stop() 

            if not self.playing:
                self.show_menu()
            else:
                OST_GAME.play(-1)
            ##self.run() 

    def run(self):

        self.obstacle_manager.reset_obstacles()
        self.powerup_manager.reset_power_ups(self.points)

        self.obstacle_manager.reset_obstacles()
        self.powerup_manager.reset_power_ups(self.points)
        ##esto es para la musica del juego corra 
        self.menu = True
        OST_MENU.stop()
        OST_GAME.play(-1)
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw() 
        OST_GAME.stop()
        OST_MENU.play(-1)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.draw_mycloud()
        self.draw_mysun()
        self.score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        cloud_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (cloud_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud + cloud_width <= 0:
            self.screen.blit(CLOUD,(cloud_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = SCREEN_WIDTH
        self.x_pos_cloud -= self.game_speed / 3
 
    def draw_mycloud(self):
        mycloud_width = MY_CLOUD.get_width()
        self.screen.blit(MY_CLOUD, (self.x_pos_mycloud, self.y_pos_mycloud))
        self.screen.blit(MY_CLOUD, (mycloud_width + self.x_pos_mycloud, self.y_pos_mycloud))
        if self.x_pos_mycloud + mycloud_width <= 0:
            self.screen.blit(MY_CLOUD,(mycloud_width + self.x_pos_mycloud, self.y_pos_mycloud))
            self.x_pos_mycloud = SCREEN_WIDTH
        self.x_pos_mycloud -= self.game_speed / 2


    def draw_mysun(self):
        self.screen.blit(MY_SUN, (self.x_pos_mysun, self.y_pos_mysun))
        self.x_pos_mysun -= self.game_speed / 10
 
    ##Si el sol sale de la pantalla por la izquierda, reinicia en el lado derecho
        if self.x_pos_mysun <= -MY_SUN.get_width():
         self.x_pos_mysun = SCREEN_WIDTH

    
    def score(self):
        self.points +=1
        text, text_rect = self.text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        self.game_running = True
        self.screen.fill(COLORS['blue'])
        self.print_menu_elements()
    
        pygame.display.update()
        self.handle_key_event_on_menu()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2


        if self.death_count == 0:
            text, text_rect = self.text_utils.get_centered_message('Press Any key to start')
            self.screen.blit(text, text_rect)

        elif self.death_count > 0:
            score, score_rect = self.text_utils.get_centered_message('Your Score: ' + str(self.points), height= half_screen_height +50)
            death, death_rect = self.text_utils.get_centered_message('Death count: ' + str(self.death_count), height= half_screen_height +100)

            self.screen.blit(score, score_rect)
            self.screen.blit(death, death_rect)
        self.screen.blit(RUNNING[0], (half_screen_width - 20, half_screen_height -140))

    def handle_key_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()