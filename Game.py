from SnakeAndLadders import SnakesAndLadders


def main():
    s = SnakesAndLadders()
    print("STARTING GAME...")
    while True:
        num = input("Press any key to roll die::")
        if num == "":
            if not s.playGame():
                break

main()