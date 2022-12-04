with open("2022/2022_3.txt") as f:
    lines = f.read().splitlines()


def char_position(letter):
    if letter.isupper():
        value = ord(letter) +27 +32 -97
    else:
        value = ord(letter) +1 -97
    return value


score = 0
letters = []

for line in range(len(lines)):
    next = False
    getlen = int(len(lines[line])/2)
    comparts = [lines[line][:getlen], lines[line][getlen:]]
    while next == False:
        for letter in comparts[0]:
            print(letter)
            if letter in comparts[1]:
                letters.append(letter)
                next = True
                break

result = [char_position(char) for char in letters]
sum(result)

#PART II
score = 0
letters = []

for line in range(0, len(lines), 3):
    #next = False
    #comparts = [lines[line], lines[line+1], lines[line+2]]
    #while next == False:
    #    for letter in comparts[0]:
    #        if letter in comparts[1] and letter in comparts[2]:
    #            print(letter)
    #            letters.append(letter)
    #            next = True
    #           break
1
    #einfacher über sets:
    unique_letter = set(lines[line]) & set(lines[line+1]) & set(lines[line+2])
    letters.append(list(unique_letter)[0])


result = [char_position(char) for char in letters]
sum(result)






 #                   score =+ char_position(letter) +26 +25
  #              else:
   #                 score =+ char_position(letter) + 1