import random
import collections


class Tile(object):
	def __init__(self, resource, number, adjacency_list):
 		self.resource = resource
 		self.number = number
 		self.hasRobber = False
 		self.adjacency_list = adjacency_list 


''' board will be dictionary of keys such as a1,a2,a3,a4 etc'''
''' each key will have a value as a Tile which will have an adjacency_list to other keys '''
''' the board will be a graph'''
class Board(object):
	def __init__(self):
		self.boardmap = {"a1":Tile("wood",5,["a2", "a3"]), 
		"a1":Tile("wood",5,["a2", "a3"]), "a1":Tile("wood",5,["a2", "a3"])}
 		#self.full_hexicon = "  ____\n" +  " /    \ \n"  + "/      \ \n" + "\      / \n" +  " \____/"
 		#self.down_hexicon = "\n /    \ \n"  + "/      \ \n" + "\      / \n" +  " \____/ \n"
 		#["---,---,---,---,---,---,---,---,---,---,---,---,---"]
 		#["---,---,---,---,S3 ,---,W10,---,S3 ,---,---,---,---"]
 		#["---,---,---,S8 ,---,W10,---,S3 ,---,---,---,---"]
 		#["---,---,---,---,B3 ,---,W10,---,S3 ,---,---,---,---"]
 		#["---,---,---,---,B3 ,---,W10,---,S3 ,---,---,---,---"]
 		#self.boardgraph = 



 	#self.boardgraph = generate_board():
 	
 	#def generate_board():
 	#	a1 = Tile("a1", "stone", 3, "a2", )
    


 	#def print_board():
 	#	filler = "-------"



    

 #   F4
 # / c \
 #F3-- f4
'''example: r = Road("a1", "b2") '''
#class Road(object, color, edge1, edge2):
#	self.color = color?
#	self.edges = [edge1, edge2]

'''example: c = City(["a1", "b2", "b3"]) '''
class City(object):
	def __init__(self, adjacency_list):
		self.color = None
		self.owner = None
		self.adjacency_list = adjacency_list
	

	def give_resources(dice_roll):
		resources_dict = {"wood":0, "stone":0, "brick":0, "wheat":0, "sheep":0}
		# TODO
		# popluate_resources_dict
		# get resources from tiles in adjacency list
		for resource in resources_dict:
			resources_dict[resource] *= 2 
		return resources_dict


class Settlement(object):
	def __init__(self, adjacency_list):
		self.color = None
		self.owner = None
		self.adjacency_list = adjacency_list
	

	def give_resources(dice_roll):
		resources_dict = {"wood":0, "stone":0, "brick":0, "wheat":0, "sheep":0}
		# TODO
		#popluate_resources_dict
		# get resources from tiles in adjacency list
		return resources_dict


class Dice(object):
	def __init__(self):
		self.die1 = random.randint(1,6)
		self.die2 = random.randint(1,6)
	

	def roll(self):
 		self.die1 = random.randint(1,6)
 		self.die2 = random.randint(1,6)
 		return (self.die1+self.die2)


class Player(object):
	def __init__(self, player_number, name, color):
 		self.player_number = player_number
 		self.name = name
 		self.color = color
 		self.hand = {"wood":0, "stone":0, "brick":0, "wheat":0, "sheep":0}
 		self.board_pieces = []
 		self.cards = []
 		self.victory_points = 0
 		self.first_die_roll = 0
 		self.game_order = 0
 		self.cities = []
 		self.settlements = []
 		self.card_victory_points = []
 		self.largest_army = False
 		self.longest_road = False
    
	def add_to_hand(self, resources):
 		for resource in resources:
 			self.hand[resource] += resourcesp[resource]

	'''
# 	def add_settlement(self):
		new_settlement = Settlement(adjacency_list)
		self.settlements.append(new_settlement)

# 	def add_city(self):

# 	def add_road(self):
'''

	def calculate_victory_points(self):
 		city_points = 2*len(self.cities)
 		settlement_points = len(self.settlement_points)
 		card_victory_points = len(self.card_victory_points)

 		if largest_army:
 			largest_army_points = 2
 		else:
 			largest_army_points = 0

 		if longest_road:
 			longest_road_points = 2
 		else:
 			longest_road_points = 0

 		points = city_points + settlement_points + card_victory_points + largest_army_points + longest_road_points

 		return points




class Game(object):
	def __init__(self):
		self.num_players = 2
		self.player_list = []
		self.dice = Dice()
		self.game_is_over = False
		self.game_order = []
		self.current_player = 0


	def print_players(self):
		for player in self.player_list:
			print("player " + player.player_number + ": " + player.name + "," + player.color)


	def decide_player_priority(self):
   	    print("Roll die to decide who goes first")
   	    print("Press Enter to roll dice")
   	    for player in self.player_list:
   	    	print("Ok "+player.name + ", roll the die")
   	    	input()
   	    	dice_roll = self.dice.roll()
   	    	print("you rolled: " + str(dice_roll))
   	    	player.first_die_roll = dice_roll

   	    self.player_list.sort(key=lambda x: x.first_die_roll, reverse=True)
   	    print("the order is: ")
   	    rank = 1
   	    for player in self.player_list:
   	    	print(str(rank) +". " + player.name + " rolled: " + str(player.first_die_roll))
   	    	rank += 1


	def get_player_prefered_order(self):
			available_orders = set()
			for num in range(1, int(self.num_players)+1):
				available_orders.add(num)
			print("Decide what order you want to place your pieces")
			print("Type the number of the order you want")
			for player in self.player_list:
				print("Ok "+player.name + ", choose your order")
				print("Your options are: ")
				for num in available_orders:
					print(num)
				print("desired order:") 
				chosen_order = input()
				available_orders.remove(int(chosen_order))
				player.game_order = chosen_order
				print("your order is: " + player.game_order)

			self.player_list.sort(key=lambda x: x.game_order)
			print("the game order is: ")
			for player in self.player_list:
				print(player.game_order + " " + player.name )

	'''
	# TODO
	def set_pieces(self):
		placement_order_list = self.player_list.delete_last_player() + self.player_list.reverseSort()
		for player in placement_order_list:
			print("this is the game board")
			board.print_board()
			print("select three tiles to place your settlement")
			print("enter three tiles like this:")
			print("b2,b3,b4")
			print("please enter tiles:")
			#ask for user input
			adjacency_list = ["b2","b3","b4"] #example
			player.add_settlement(adjacency_list)
	'''
	def whose_turn_is_it(self):
		if self.current_player >= len(self.player_list):
			self.current_player = 0
		player = self.player_list[self.current_player]
		return player


	def dispense_resources(self, dice_roll):
		for player in self.player_list:
			for city in player.cities:
				resources = city.get_resources(dice_roll)
				player.add_to_hand(resources)

			for settlement in player.settlements:
				resources = settlement.get_resources(dice_roll)
				player.add_to_hand(resources)


	def turn(self):
		player = self.whose_turn_is_it()
		print("It's " + player.name + "'s turn.")
		print("Press Enter to roll dice")
		input()
		dice_roll = self.dice.roll()
		print(player.name + " rolled " + str(dice_roll)+"\n\n")
		#self.dispense_resources(dice_roll)

		#give everyone their resources
		
		# TODO implement all these functions
		#allow player to either
		# 1. Do nothing and end turn
		# 2. Build settlement
		# 3. Build city
		# 4. Build road
		# 5. Buy card
		# 6. Activate card
		# 7. Move robber
		# 8. Trade
		# 6. Finish and end turn

		'''
		for player in self.player_list:
			player.victory_points = player.calculate_victory_points()
			if player.victory_points == 10:
				self.game_is_over = True
				print(player.name + " won!")
		'''
		self.current_player += 1



	def playCatan(self):
		print("how many players?")
		self.num_players = input() # TODO number of players must be valid in both input type and number
		print("there will be " + self.num_players + " players")
		for player in range(1, int(self.num_players)+1):
			print("player " + str(player) + " name: ")
			name = input()
			print("player " + str(player) + " color: ")
			color = input()
			self.player_list.append(Player(str(player), name, color))
		# TODO players can't have same color		
		self.print_players()
		self.decide_player_priority()
		self.get_player_prefered_order()
		#self.set_pieces()


		while not self.game_is_over:
			self.turn()





'''Main method'''

game = Game()
game.playCatan()


