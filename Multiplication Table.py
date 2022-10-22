#Name: Nhlapo Nkululeko
#StuNum: 4129962
#Program that generates a multiplication table of numbers between 1 and 10

print("        Multiplication Table            \n")

for b in range(1,11):
    print(b, end='\t')
print()
print('________________________________________')
for n in range(2,11):
    for v in range(1,11):
        print(n * v, end='\t')
    print('\n')