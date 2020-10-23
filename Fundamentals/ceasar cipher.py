text = input()
string = ""
for i in range(0,len(text)):
    letter = text[i]
    new = 3 + ord(letter)
    string += chr(new)
print(string)