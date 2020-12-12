def main():
    from random import randint
    dice_rolls = 2
    dice_sum = 0
    for _ in range(dice_rolls):
        roll = randint(1,6)
        dice_sum += roll
        print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
    main()