from SnakeAndLadders import SnakesAndLadders


def main():
    s = SnakesAndLadders()
    print("STARTING GAME...")
    while True:
        num = input("Press 1 to roll normal die \nPress 2 to roll crooked die::")
        if num == "1":
            if not s.playGame(1):
                break
        else:
            if not s.playGame(2):
                break

main()
