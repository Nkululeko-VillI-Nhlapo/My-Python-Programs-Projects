#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String

print("Welcome this program takes up the first two letters\nof your string and and the last two and adds them")

string = input("Please Enter any string you'd like to jinx:\t")

theFirst_Last_Letter = string[len(string)-1]
theScnd_Last_Letter =  string[len(string)-2]

if (len(string) == 1):
    print("")

else:
    outcome = string[0] + string[1] + theScnd_Last_Letter + theFirst_Last_Letter

    print(f"This your output {outcome}")