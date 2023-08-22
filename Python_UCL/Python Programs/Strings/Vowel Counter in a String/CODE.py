string = input("Enter a word: ")
def vowels(s):
    counte = counta = countu= counti = county= counto = 0
    for i in s.lower():
        if i == "e":
            counte += 1
        elif i == "a":
            counta += 1
        elif i == "u":
            countu +=1
        elif i == "i":
            counti += 1
        elif i == "y":
            county += 1
        elif i == "o":
            counto +=1
    if counte == 0 and county == 0 and counta == 0 and counto == 0 and countu == 0 and counti == 0:
        print("There are no vowels in your string")
    else:
        print("The vowels are:")
        if counte > 0:
            print("e", counte)
        if counta > 0:
            print("a", counta)
        if countu > 0:
            print("u", countu)
        if counti > 0:
            print("i", counti)
        if county > 0:
            print("y", county)
        if counto > 0:
            print("o", counto)
    return ""
print(vowels(string))