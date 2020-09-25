import sys, pygame, random
from pygame.locals import *
import pygame_gui
from Classes import Img, Deck, Player, Card

#screen set up

pygame.init()

pygame.display.set_caption('Blackjack (Rough Draft)')

#screen and color variables

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

clock = pygame.time.Clock()
is_running = True

manager = pygame_gui.UIManager((800, 600))

#text setting
font_obj = pygame.font.Font('fixedsys.ttf', 64)
text_surface_obj = font_obj.render('pixel pig blackjack', True, BLACK, WHITE)
img_intro_text = Img(text_surface_obj, 60, 70)

font_obj_2 = pygame.font.Font('fixedsys.ttf', 24)
text_surface_obj_2 = font_obj_2.render('Press "h" to hold or "s" to stand for your turn', True, BLACK, WHITE)
text_surface_obj_3 = font_obj_2.render("The house will hit until their score is 17 or higher",
	True, BLACK, WHITE)
text_surface_obj_4 = font_obj_2.render("First to get a total score of 21 wins", True, BLACK, WHITE)
text_surface_obj_5 = font_obj_2.render("Past 21 is a bust, a tied score is a draw", True, BLACK, WHITE)
text_surface_obj_6 = font_obj_2.render("Good Luck", True, BLACK, WHITE)
cont_surface_obj = font_obj_2.render("(press Enter to continue or B to go back)", True, BLACK, WHITE)

instruct_text0 = Img(text_surface_obj_2, 75, 100) #coordinate fix
instruct_text1 = Img(text_surface_obj_3, 75, 100)
instruct_text2 = Img(text_surface_obj_4, 75, 100)
instruct_text3 = Img(text_surface_obj_5, 75, 100)
instruct_text4 = Img(text_surface_obj_6, 75, 100)
cont_text = Img(cont_surface_obj, 160, 400)

# text_rect_obj = text_surface_obj.get_rect()
# text_rect_obj.center = (400, 100)

#assign images

img_temp = pygame.image.load("graphics/pixel_pig.jpg").convert()
img0 = Img(img_temp, 400.0, 500.0)

# button set up
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (150, 50)),
 	text='Start', manager=manager)


#intro stage bool
intro = True
instruct = False
instruct_index = 0
main = False

#global game variables
cards_in_play = []
deck0 = Deck()
house = Player()
player0 = Player()

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
					instruct = True
					intro = False
		manager.process_events(event)
		manager.update(time_delta)
		pygame.display.update()

	while instruct:
		screen.fill(WHITE)
		instruct_img_array = [instruct_text0, instruct_text1, instruct_text2, instruct_text3,
		instruct_text4] #orders the text images
		

		screen.blit(instruct_img_array[instruct_index].obj, (instruct_img_array[instruct_index].x,
		 instruct_img_array[instruct_index].y))
		screen.blit(cont_text.obj, (cont_text.x, cont_text.y))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				instruct, is_running = False, False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER:
					if instruct_index < len(instruct_img_array) - 1:
						instruct_index += 1
						pygame.display.update()
					else:
						main = True
						instruct = False
				if event.key == pygame.K_b:
					if instruct_index > 0:
						instruct_index -= 1
						pygame.display.update()
					else:
						instruct_index = 0
						pygame.display.update()
			
		manager.process_events(event)
		manager.update(time_delta)


		pygame.display.update()


	while main:
		screen.fill(WHITE)
		#add conditional func so array is self-updating w/ more positions
		#what's the max possible number of hands?
		card_position = [(500, 500), (500, 100), (400, 500), (400, 100)]
		
		# deck1 = Deck()
		# initial_hand = deck1.deal_hand()
		# temp = initial_hand[0]
		# temp_img = temp.establish_image()
		# screen.blit(temp_img.obj, (0,0))
		# #VICTORY! ...holy fuck I'm tired. ok, problem now is it keeps reshuffling the card blitted to (0,0)
		move0 = Img.move(screen.fill, screen.blit, pygame.display.update, WHITE, 0)
		deal_visual0 = Deck.deal_visual(move0, card_position) 

		# initial_animation = deck1.deal_visual(move0, card_position) 
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main, is_running = False, False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER:
					#have global cards array append the cards from deal_hand func
					while len(cards_in_play) < 4:
						card_temp = deck0.deal_card()
						#think I'm going to have the cards_in_play array store the cards img objects
						#wait, maybe I should have the card class include its own Img obj --
						#ok. need to research inheritance/class relationships so Card can have an Img obj as a class attribute.
						#also need to reformat the card images
						cards_in_play.append(card_temp)



					initial_hand = deck0.deal_hand() #update all to include modified deal function

					cards_in_play.extend(initial_hand)
					player0.cards.extend([cards_in_play[0], cards_in_play[2]])
					house.cards.extend([cards_in_play[1], cards_in_play[3]])
					player0.update_score()
					house.update_score()
					deal_visual0(deck0, player0.cards[0])


					print(player0.cards[0].img)
			
		manager.process_events(event)
		manager.update(time_delta)


		pygame.display.update()

	
	pygame.display.update()
