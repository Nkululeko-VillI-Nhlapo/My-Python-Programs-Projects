#The program accepts the name of a file then prints out its Extension Name
#E.g web.html
#Output:html

name = input("Please give your file name and it's extension:\t")

list= name.split('.')


extension = list[1]

print(f"Your file extension name is: {extension}")
