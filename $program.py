#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
#Sample String : 'restart'
#Expected Result : 'resta$t'

def my_string():
    string = input("Please enter any string:\t")
    print()
    char_toChange = input("PLease type in the Charecter you'd like to replace, e.g F OR G:\t")
    print()
    char = input("Please give any charecter you'd like to serve as replacement, e.g % or F:\t")

    conversion = string.replace(char_toChange, char)

    string_2 = conversion[1:]

    print(f"r{string_2}")
    print()

    option()


def option():
    continue_Or_not = input("wanna play again?, 0=yes , 1=n:\t")

    if continue_Or_not == 0:
        my_string()

    else:
        quit()


def quit():
    while True:
        print("Thank You, HOPE YOU ENJOYED!!")
        break



print("Welcome, this is a Python program to get a string from a given string where all\noccurrences of its first char have been changed to any charecter, except the first char itself.")
print()

check =int(input('Press O to play and 1 ro Quit:\t'))

while True:
    if check == 1:
        print("Thank You, Don't hesitate to try it out next time")
        break
    else:
        print("The fun Begins\n")
        my_string()


