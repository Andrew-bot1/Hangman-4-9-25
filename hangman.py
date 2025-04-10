import random

# list for words
wordList = [
    "House",
    "Hangman",
    "Jazz",
    "A game of cat and mouse",
    "First come first serve",
    "Python",
    "Doing coding",
    "Road",
    "Taco Bell",
]

# enter loop until user wants to exit'
while True:
    exit = input("Do you wish to exit? y/n: ")
    if exit.lower() == "y":
        # exit program
        break

    # declare variable to keep track of misses
    miss = 0
    # declare variable to hold hidden word
    hid = []

    # declare variable to count correct letters
    correct = 0

    # get random word
    word = random.choice(wordList)

    # get hidden word
    for x in word:
        # check for space
        if x != " ":
            # get letter and hide it
            hid.append("_")
        # get space
        else:
            hid.append(" ")

    # enter loop until gamem is complete
    while miss < 5:
        # declare variable for index
        index = 0

        # declare check variable to flag miss
        check = False
        # output current misses
        print(f"{miss} miss out of 5")

        # print hidden word
        print("".join(hid))

        # get user guess
        guess = input("Enter guess: ")

        # check to see if guess is correct
        for x in word:
            if x.lower() == guess:
                # unhide letter
                hid[index] = x
                check = True
                correct += 1

            index += 1
        # check if there was a miss
        if check != True:
            miss += 1

        # check to see if all letters are revealed
        if correct == len(word.replace(" ", "")):
            # print congrats message
            print("You win!")
            break

    # reveal word
    print(f"The word was {word}")
