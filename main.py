import Board
import Player
import random

if __name__ == "__main__":
	horizontal = int(input("Enter the horizontal size of the board: "))
	vertical = int(input("Enter the vertical size of the board: "))
	size = horizontal * vertical
	board = Board(size)

	num_snakes = random.randint(6,8)
	num_ladders = random.randint(6,8)

	snake_positions = set()
	ladder_positions = set()

	print(f"Adding {num_snakes} snakes to the Board...")

	for _ in range(num_snakes):
		while True:
			start = random.randint(2, size-2)
			end = random.randint(1, start-1)
			if start not in snake_positions and start not in ladder_positions and  end not in ladder_positions:
				board.add_snake(start, end)
				snake_positions.add(start)
				snake_positions.add(end)
				break
	print(f"Adding {num_ladders} ladders to the Board...")
	for _ in range(num_ladders):
		while True:
			start = random.randint(2, size-2)
			end = random.randint(1, start-1)
			if start not in ladder_positions and start not in snake_positions and end not in snake_positions:
				board.add_ladder(start, end)
				ladder_positions.add(start)
				ladder_positions.add(end)
				break
	print("\nBoard configuration completed!\n")
	num_players = int(input("Enter the number of players: "))
	for i in range(1, num_players + 1):
		name = input(f"\nEnter the name of player {i}: ")
		board.add_player(Player(i,name))
	print("\nGame started!\n")

	board.play()
