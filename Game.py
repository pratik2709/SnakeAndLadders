from SnakeAndLadders import SnakesAndLadders


def main():
    snakeAndLadders = SnakesAndLadders()
    print("STARTING GAME...")
    while True:
        playerInput = input("Press 1 to roll normal die \nPress 2 to roll crooked die::")
        if playerInput == "1":
            if not snakeAndLadders.playGame(1):
                break
        else:
            if not snakeAndLadders.playGame(2):
                break

main()
