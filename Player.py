class Player:
	"""
	Represents a player in the game of Snakes and Ladders.
    
    	Attributes:
	        id (int): The unique identifier for the player.
	        name (str): The name of the player.
	        position (int): The current position of the player on the game board.
	"""
	def __init__(self,  id, name):
		self.name = name
		self.id = id
		self.position = 0
