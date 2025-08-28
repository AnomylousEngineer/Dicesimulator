while True:
    Ones = 0
    Twos = 0
    Threes = 0
    Fours = 0
    Fives = 0
    Sixes = 0
    Sevens = 0
    Eights = 0
    BD = "nan"
    Rolls = 100
    """
          Version 0.98
            Date: 2025-08-28
    Latest Uploaded: 
    """
    import random
    while True:
        BD = input("Use 8 sided Die? Y/n ")
        if BD == "Y" or BD == "n":
            break
        else: print("That is not a correct value, please type again.")
    while True:
        Rolls_input = input("How many times do you want to roll the dice? ")
        if Rolls_input.isnumeric():
            Rolls = int(Rolls_input)
            break
        else: print("Thats not a number lol?")

    for i in range(Rolls):
        if  BD == "n":
            Number = random.randint(1, 6)
        else: Number = random.randint(1, 8)

        if  Number == 1:
            Ones = Ones + 1

        elif Number == 2:
            Twos = Twos +1

        elif Number == 3:
            Threes = Threes +1

        elif Number == 4:
            Fours = Fours + 1

        elif Number == 5:
            Fives = Fives + 1

        elif Number == 6:
            Sixes = Sixes + 1

        elif Number == 7:
            Sevens = Sevens + 1

        elif Number == 8:
            Eights = Eights +1


    print("1:or", Ones)
    print("2:or", Twos)
    print("3:or", Threes)
    print("4:or", Fours)
    print("5:or", Fives)
    print("6:or", Sixes)
    if BD == "Y":
        print("7:or", Sevens)
        print("8:or", Eights)
    svar = input("Roll again?")
    if  svar == "n":
        break
    else: print("Rolling again!")
