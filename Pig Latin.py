import ex115
line = str(input("Please Enter a Sentence >"))

x = line.split(" ")
length = len(x)
output = []

for num in range(0, length):
    print(ex115.function(x[num]), end=" ")