import pygame
from random import randint

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		self.image = pygame.image.load("meteor.png")
		self.rect = self.image.get_rect()
		self.rect.x = randint(0, WIDTH-70)
		self.rect.y = 0

class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		self.image = pygame.image.load("bullet.png")
		self.rect = self.image.get_rect()

class Spaceship(pygame.sprite.Sprite):
	def __init__(self):
		self.image = pygame.image.load("spaceship.png")
		self.rect = self.image.get_rect()
		self.rect.y = HEIGHT - 100

WIDTH = 1280
HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра")
clock = pygame.time.Clock()
pygame.font.init()

game_over_font = pygame.font.Font(None, 72)
lifes_font = pygame.font.Font(None, 36)
lifes = 3

METEOR_SPEED = 5
BULLET_SPEED = 10

meteors = []
bullets = []

spaceship = Spaceship()
game_over = False
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and game_over == False:
			new_bullet = Bullet()
			new_bullet.rect.x = spaceship.rect.x + 35
			new_bullet.rect.y = spaceship.rect.y
			bullets.append(new_bullet)
		if event.type == pygame.KEYDOWN:
			game_over = False
			lifes = 3

	if game_over:
		screen.fill("red")
		text = game_over_font.render("GAME OVER", True, "black")
		text_rect = text.get_rect(center = (WIDTH / 2, HEIGHT / 2))
		screen.blit(text, text_rect)
		pygame.display.update()
		clock.tick(FPS)
		continue

	screen.fill("black")

	spaceship.rect.x = pygame.mouse.get_pos()[0] - 35
	screen.blit(spaceship.image, spaceship.rect)

	for meteor in meteors:
		meteor.rect.y += METEOR_SPEED
		screen.blit(meteor.image, meteor.rect)
		if meteor.rect.y >= HEIGHT:
			lifes -= 1
			meteors.remove(meteor)
		if meteor.rect.colliderect(spaceship.rect) or lifes == 0:
			game_over = True
			meteors = []
			bullets = []

	if randint(0, 100) <= 2:
		new_meteor = Meteor()
		meteors.append(new_meteor)

	for bullet in bullets:
		bullet.rect.y -= BULLET_SPEED
		screen.blit(bullet.image, bullet.rect)

	for bullet in bullets:
		for meteor in meteors:
			if bullet.rect.colliderect(meteor.rect):
				bullets.remove(bullet)
				meteors.remove(meteor)

	text = lifes_font.render("Жизни: " + str(lifes), True, "white")
	screen.blit(text, (0, 0))

	pygame.display.update()
	clock.tick(FPS)
