import random
import sys

import pygame

pygame.init()

# --- Constants ---
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# --- Terrain ---
class Terrain:
    def __init__(self):
        self.rects = [pygame.Rect(100, 500, 600, 20)]

    def drawTerrain(self, screen):
        for r in self.rects:
            pygame.draw.rect(screen, (0, 200, 0), r)

    def getTerain(self):
        return self.rects


# --- Menu ---
class Menu:
    def __init__(self):
        self.visible = True

    def showMenu(self):
        self.visible = True

    def hideMenu(self):
        self.visible = False

    def getMenu(self):
        return self.visible


# --- Character ---
class Character:
    def __init__(self):
        self.alive = True
        self.x, self.y = 100, 400
        self.speed = 5
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.5
        self.on_ground = False
        self.facing_direction = "right"

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 40, 60))

    def update(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
            self.facing_direction = "left"
        elif direction == "right":
            self.x += self.speed
            self.facing_direction = "right"

    def jump(self):
        if self.on_ground:
            self.velocity_y = -10
            self.on_ground = False

    def check_collision(self, terrain):
        self.on_ground = False
        for rect in terrain:
            if pygame.Rect(self.x, self.y + 60, 40, 1).colliderect(rect):
                self.on_ground = True
                self.velocity_y = 0
                self.y = rect.top - 60


# --- Player ---
class Player(Character):
    def __init__(self):
        super().__init__()

    def checkColisions(self, items, terrain):
        self.check_collision(terrain)
        for item in items:
            if pygame.Rect(self.x, self.y, 40, 60).colliderect(item.itemBounds):
                item.collectItem()


# --- Enemy ---
class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.x = 400
        self.y = 400


# --- Items ---
class Items:
    def __init__(self):
        self.itemBounds = pygame.Rect(random.randint(100, 700), 450, 20, 20)
        self.status = True

    def draw(self, screen):
        if self.status:
            pygame.draw.rect(screen, (255, 215, 0), self.itemBounds)

    def collectItem(self):
        self.status = False


# --- MainGame ---
class MainGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("JumpMan")
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0

        self.menu = Menu()
        self.terrain = Terrain()
        self.player = Player()
        self.items = [Items() for _ in range(3)]

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("left")
        if keys[pygame.K_RIGHT]:
            self.player.move("right")
        if keys[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        self.player.update()
        self.player.checkColisions(self.items, self.terrain.getTerain())

    def draw(self):
        self.screen.fill(WHITE)
        self.terrain.drawTerrain(self.screen)
        self.player.draw(self.screen)
        for item in self.items:
            item.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = MainGame()
    game.run()
