import random

def main():
    print("Starting price is 10$. If you win you will earn 10x of what you played with.")
    wallet()
    slots()


def wallet():
    while True:
        wallet = input("How much are you gonna put in :D ?")
        if wallet.isdigit():
            wallet = int(wallet)
            if wallet > 9.99:
                break
            elif 0 < wallet < 10:
                print("You need more dollars.")
            else:
                print("You cant play with an empty wallet.")


def slots():
    column_1 = ["A","7","🍓","🍎","🐱"]
    column_2 = ["A","7","🍓","🍎","🐱"]
    column_3 = ["A","7","🍓","🍎","🐱"]
    first_pick = random.choice(column_1)
    second_pick = random.choice(column_2)
    third_pick = random.choice(column_3)
    print(f"{first_pick} | {second_pick} | {third_pick}")


main()
