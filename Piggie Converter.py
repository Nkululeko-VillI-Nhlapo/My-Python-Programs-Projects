
def vowel(vow):
    vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if vow in vowel:
        return True
    else:
        return False

def pigLatin(x):
    check = False
    vow_index = 0
    for i in range(len(x)):
        if (vowel(x[i])):
            vow_index = i
            check = True
            break
    if (not check):
        return x
    pigLatin = x[vow_index:] + x[0:vow_index] + "ay"
    return pigLatin

print("Welcome to Word - PiggiE Convertor\n The program words to Piglatin, basically ending them ay" )
string = input("Please Enter a Word or a Sentence")

list = string.split()

print(f"The original sentence is:\t {string}")
pigstring = ""

for word in list:
    pigstring = " " +  pigLatin(word) + pigstring

print(f"The Output is \t\n {pigstring}")
