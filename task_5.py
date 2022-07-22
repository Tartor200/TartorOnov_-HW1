text = input("Enter text: ")
counter = 1
val = text[0]

#for letters in the remaining text
for letter in text[1:]:
    #if previous letter is the same with present letter at hand
    if (val[-1] != letter):
        val += str(counter) + letter
        counter = 1
    else:
        counter += 1
        
#add count of last number
val += str(counter)
print(val)
