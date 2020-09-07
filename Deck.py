import sys, pygame, random
from pygame.locals import *
import pygame_gui
from Classes import Img

#screen set up

pygame.init()

pygame.display.set_caption('Blackjack (Rough Draft)')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
background_obj = Rect(0, 0, 800, 600)

clock = pygame.time.Clock()
is_running = True

manager = pygame_gui.UIManager((800, 600))

#text setting
font_obj = pygame.font.Font('fixedsys.ttf', 64)
text_surface_obj = font_obj.render('pixel pig blackjack', True, BLACK, WHITE)
img_intro_text = Img(text_surface_obj, 60, 70)

# text_rect_obj = text_surface_obj.get_rect()
# text_rect_obj.center = (400, 100)

#assign images

img_temp = pygame.image.load("graphics/pixel_pig.jpg").convert()
img0 = Img(img_temp, 400.0, 500.0)

# button set up
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (150, 50)),
 	text='Start', manager=manager)

# goodbye_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 375), (100, 50)),
# 	text='Say Goodbye', manager=manager)

#intro stage bool
intro = True
main = False

#event [while] loop
while is_running:
	time_delta = clock.tick(60)/1000.0


	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	# 		is_running = False

	# 	if event.type == pygame.USEREVENT:
	# 		if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
	# 			if event.ui_element == hello_button:
	# 				print('Hello World!')
	# 				print(hello_button.check_pressed())
	# 				intro = False
	# 				main = True
	# 				img0.x, img0.y = 800, 600
	# 				screen.fill(WHITE)
	# 				screen.blit(background, (0, 0))
	# 				pygame.display.update()
		
	# 	manager.process_events(event)

	manager.update(time_delta)
	
	while intro:
		
		manager.draw_ui(screen)
		move0 = Img.move(screen.fill, screen.blit, pygame.display.update, WHITE, img_intro_text)
		move0(img0, 40.0, 100.0)
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro, is_running = False, False
			if event.type == pygame.USEREVENT:
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
					screen.fill(WHITE)
					pygame.display.update()
					main = True
					intro = False
		manager.process_events(event)
		manager.update(time_delta)
		pygame.display.update()

	while main:
		screen.fill(WHITE)
		manager.process_events(event)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main, is_running = False, False
		manager.update(time_delta)

	# if img0.x != 40:
	# 	img0.x -= 4
	# 	if img0.y != 100:
	# 		img0.y -= 4
	# 		screen.fill(WHITE)

	
	# screen.blit(img0.obj, (img0.x, img0.y))
	# screen.blit(img_intro_text.obj, (img_intro_text.x, img_intro_text.y))
		# manager.draw_ui(screen)
		pygame.display.update()

	
	pygame.display.update()
