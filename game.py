def gameInfo():
    print('''
################################################
# #####  #   # #   #  ##### #####  ####  #   # #
# #    # #   # ##  # #      #     #    # ##  # #
# #    # #   # # # # #  ### ##### #    # # # # #
# #    # #   # #  ## #    # #     #    # #  ## #
# #####  ##### #   #  ##### #####  ####  #   # #
################################################
''')

    print('''Welcome to Dungeon, a choose your own adventure game that I\'ve made for my intro to CS class.
I hope you have as much fun playing as I did making it! :)''')

    correctInput = True
    while(correctInput):
        
        choice = input('Start/Exit: ')
        print('\n')

        if choice.lower() == 'start' or choice.lower() == 'exit':
            correctInput = False
        else:
            print('Please enter a valid option')

    return choice


def gameIntro():
    print('''You are an adventurer looking to make a name for yourself.
You enter an infamous dungeon in search of rare loot and strong monsters.
    ''')


def startGame():
    gameIntro()



playerChoice = gameInfo()

if playerChoice.lower() == 'start':
    startGame()
elif playerChoice.lower() == 'exit':
    print('Exiting game')

