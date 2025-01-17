import random
class Board:
	def __init__(self, size):
		self.size = size
		print(f"\nBoard created with size:{size}\n")
		self.snakes = {}
		self.ladders = {}
		self.players = {}
		self.winner = None
	def add_snake(self, start, end):
		self.snakes[start] = end
		print(f"Snake added from {start} to {end}")
	def add_ladder(self, start, end):
		self.ladders[start] = end
		print(f"Ladder added from {start} to {end}")
	def add_player(self, player):
		self.players[player.id] = player
		print(f"Player {player.name} added with ID {player.id}.")
	def move_player(self, player, steps):
		if player.id not in self.players:
			return False
		print(f"{player.name} rolled a {steps}")
		if player.position + steps <= self.size:
			player.position += steps
			print(f"{player.name} moved to {player.position}\n")
		else:
			print(f"{player.name} needs {self.size - player.position} to win. But rolled {steps}.")
			print(f"{player.name} cannot move this turn.\n")
		
		if player.position == self.size - 1:
			print(f"Since game is with 2 dice, rolling 1 is not possible. Reducing 1 from {player.name}'s position.")
			player.position -= 1
			print(f"{player.name} moved to {player.position}\n")
		if player.position in self.snakes:
			player.position = self.snakes[player.position]
			print(f"Oh no! {player.name} bitten by snake. Moved to {player.position}\n")
		elif player.position in self.ladders:
			player.position = self.ladders[player.position]
			print(f"Yay! {player.name} climbed the ladder. Moved to {player.position}\n")
		
		if player.position == self.size:
			self.winner = player
			print(f"{player.name} won the game!\n")
		return True
	
	def roll_dice(self):
		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)
		print(f"Dice 1: {dice1}, Dice 2: {dice2}")
		return dice1 + dice2
	
	def play(self):
		while not self.winner:
			for player in self.players.values():
				input(f"{player.name}'s turn. Press Enter to roll the dice.")
				steps = self.roll_dice()
				self.move_player(player, steps)
				if self.winner:
					break
				print(f"Current Positions : {', '.join([f'{p.name}:{p.position}' for p in self.players.values()])}\n")
		print(f"Congratulations {self.winner.name}!!! You're the winner!")
		return self.winner
