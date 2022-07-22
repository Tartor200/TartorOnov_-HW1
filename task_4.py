num = int(input("Enter a number: "))
counter = 1
val = ""
while len(val) <= num:
    val += str(counter)*counter
    counter += 1
val = val[:num]
print(val)

