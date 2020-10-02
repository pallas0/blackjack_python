import sys, pygame, random
from pygame.locals import *
import pygame_gui
from Classes import *

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

cont_surface_obj = font_obj_2.render("(press Enter to continue or B to go back)", True, BLACK, WHITE)

instruct_text0 = Img(text_surface_obj_2, 75, 100) #coordinate fix
instruct_text1 = Img(text_surface_obj_3, 75, 100)
instruct_text2 = Img(text_surface_obj_4, 75, 100)
instruct_text3 = Img(text_surface_obj_5, 75, 100)
instruct_text5 = Text("Press Enter to move the game along", 75, 100)

victory_message = Text("You win!", 75, 200)
loss_message = Text("You lost =(", 75, 200)
restart_message = Text("Press Start to play again", 200, 250)


cont_text = Img(cont_surface_obj, 160, 400)

# text_rect_obj = text_surface_obj.get_rect()
# text_rect_obj.center = (400, 100)

#assign images

img_temp = pygame.image.load("graphics/pixel_pig.jpg").convert()
img0 = Img(img_temp, 400.0, 500.0)

# button set up
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (150, 50)),
 	text='Start', manager=manager)


#stage bools
intro = True
instruct = False
instruct_index = 0
main = False
cards_display, text_display = False, False
player_turn, restart_option = False, False

#editing temp variables
flag = False
i = 0

#global game variables
cards_in_play, stage_text = [], []
deck0 = Deck()
house, player0 = Player(), Player()
h_score, p_score = 0, 0

#event [while] loop
while is_running:
	time_delta = clock.tick(60)/1000.0



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
		instruct_img_array = [instruct_text0, instruct_text1, instruct_text2,
		 instruct_text3, instruct_text5] #orders the text images
		

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
						cards_display = True
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
		card_position = [(500, 400), (500, 150), (400, 400), (400, 150)]
		player_card_position = [(300, 400), (200, 400), (100, 400), (0, 400), (300, 300), (200, 300),
		(100, 300), (0, 300)]
		house_card_position = [(300, 150), (200, 150), (100, 150), (0, 150), (300, 200), (200, 200),
		(100, 200), (0, 200)]
		
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main, is_running = False, False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER:
					if len(cards_in_play) < 4:
						i = len(cards_in_play)
						rndm_card = deck0.deal_card()
						rndm_card.img.update_location(*card_position[i])
						cards_in_play.append(rndm_card)


						if len(cards_in_play) == 4:
							player0.cards.extend([cards_in_play[0], cards_in_play[2]])
							house.cards.extend([cards_in_play[1], cards_in_play[3]])
							h_score, p_score = house.update_score(), player0.update_score()

							h_or_s_text = Text("Hit or Stand?", 75, 100)
							stage_text.append(h_or_s_text)

							text_display, player_turn = True, True
							#build player turn promp text using flag bool
							#might be time for that text class

							print(h_score)
							print(p_score)

					if restart_option == True:
						#remember to reset global variables
						cards_in_play, stage_text = [], [restart_message]
						deck0 = Deck()
						house, player0 = Player(), Player()
						h_score, p_score = 0, 0
						manager.draw_ui(screen)


				if event.key == pygame.K_h:
					if player_turn == True:
						i = len(player0.cards) - 2
						rndm_card = deck0.deal_card()
						rndm_card.img.update_location(*player_card_position[i])
						cards_in_play.append(rndm_card)
						player0.cards.append(rndm_card)
						p_score = player0.update_score()
						print(p_score)

				if event.key == pygame.K_s:
					if player_turn == True:
						i = len(house.cards) - 2
						rndm_card = deck0.deal_card()
						rndm_card.img.update_location(*house_card_position[i])
						cards_in_play.append(rndm_card)
						house.cards.append(rndm_card)
						h_score = house.update_score()
						print(h_score)

			if event.type == pygame.USEREVENT:
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
					screen.fill(WHITE)
					pygame.display.update()
					main, text_display = False, False
					cards_in_play, stage_text = [], []
					deck0 = Deck()
					house, player0 = Player(), Player()
					h_score, p_score = 0, 0
					main, intro = False, True



		if h_score >= 21 or p_score >= 21:
			text_display, cards_display = False, False
			player_turn = False
			stage_text.pop()
			p_score_text = Text("Player total: " + str(p_score), 150, 400)
			h_score_text = Text("House total: " + str(h_score), 150, 300)
			restart_option = True
			if p_score == 21 or h_score > 21:
				stage_text.extend([victory_message, p_score_text,
					h_score_text])
				text_display = True
				#add stage change
			else:
				stage_text.extend([loss_message, p_score_text, h_score_text])
				#add stage change
				text_display = True
				#these need to be extended into stage changers, eventually w/ the option to restart


			
		if cards_display:
			for card in cards_in_play:
				screen.blit(card.img.obj, (card.img.x, card.img.y))

		if text_display:
			for text in stage_text:
				screen.blit(text.obj, (text.x, text.y))
			
			
		manager.process_events(event)
		manager.update(time_delta)


		pygame.display.update()

	
	pygame.display.update()
