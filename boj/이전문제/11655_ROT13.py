def ROT13(c):
    num = ord(c)
    if "a" <= c <= "z":
        num = ord(c)
        num += 13
        if num > ord("z"):
            num -= 26
    elif "A" <= c <= "Z":
        num = ord(c)
        num += 13
        if num > ord("Z"):
            num -= 26
    return chr(num)

string = input()
for c in string:
    print(ROT13(c), end="")