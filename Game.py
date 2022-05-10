import pygame
import Dino
import Road
import time


class Game:
    """Class to running and handling game"""
    def __init__(self, path):
        """
        path - path to folder with game files
        is_run - if game is running
        score - current score
        best - best score so far
        """
        self.__path = path
        self.is_run = True
        self.score = 0
        self.n = 0  # liczy, kiedy dino ma spasc po skoku
        self.m = 0  # licznik do generowania
        try:
            with open(self.__path+r'\best_score.txt', "r") as f:
                self.best_score = int(f.read())
        except (FileNotFoundError, ValueError):
            self.best_score = 0

        """initialization of GUI"""
        pygame.init()
        self.window = pygame.display.set_mode((1000, 300))
        self.dino = Dino.Dino(400, 100, 100, 100, 5)
        self.road = Road.Road(11)
        self.dino.image = pygame.image.load(self.__path + r"\dino_image.png")
        self.road0_image = pygame.image.load(self.__path + r"\road_0.png")
        self.road1_image = pygame.image.load(self.__path + r"\road_1.png")
        """running game"""
        self.run()

    def inc_score(self):
        self.score += 1

    def need_to_kill_game(self):
        if not self.dino.is_alive:
            self.is_run = False
            if self.score > self.best_score:
                self.best_score = self.score
            with open(self.__path + r'\best_score.txt', "w") as f:
                f.write(str(self.best_score))

    def reset(self):
        self.is_run = True
        self.dino.is_alive = True
        self.m = 0
        self.n = 0
        self.dino.is_jump = False
        self.window.blit(self.dino.image, (400, 100))
        self.road.states = len(self.road.states) * [0]

    def run(self):
        self.window.fill((158, 168, 50))
        while self.is_run:
            self.inc_score()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.dino.is_jump:
                self.dino.dec_y(self, 100)
                self.dino.set_jump(True)
            if self.dino.is_jump:
                self.n += 1
            if self.n == 3:
                self.n = 0
                self.dino.set_jump(False)
                self.dino.inc_y(self, 100)
            self.window.fill((158, 168, 50))
            for i in range(11):
                if self.road.states[i] == 1:
                    self.window.blit(self.road1_image, (i * 100 - 100, 100))
                else:
                    self.window.blit(self.road0_image, (i * 100 - 100, 100))
            self.m += 1
            if self.m == 5:
                self.road.generate_next()
                self.m = 0
            self.road.refresh_states()
            self.dino.check_alive(self.road)
            self.need_to_kill_game()
            self.window.blit(self.dino.image, (self.dino.x, self.dino.y))
            if self.is_run:
                pygame.display.update()
            time.sleep(0.1)
            if not self.is_run:
                if keys[pygame.K_r] and not self.is_run:
                    self.reset()
