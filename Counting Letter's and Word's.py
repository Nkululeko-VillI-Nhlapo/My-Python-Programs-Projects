def game():
    miniword = ''
    count = 0
    string = input("Please Enter Your String: \t")
    check = input("Please enter the letter or alphabet you want to count: \t")
    for k in range(len(string)):
        miniword += string[k]
        if (check in miniword):
            count += 1
            miniword = ''

    print("There are {0} {2}'s in the word {1}".format(count,string,check))


print("::::::::::::::::::::Word-Number Game:::::::::::::::::::")

print("The game tells you how many letter, words are there in a Sentence or a Word ")


while True:
    choice = input('Do you wish to play?, [y,n]: \t')
    if (choice.upper() == 'Y'):
        print("Let's Begin!!!!!\n")
        game()
    else :
      print("Thank You")
      break