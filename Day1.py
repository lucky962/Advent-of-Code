inpt = open("input.txt", "r").read().strip().split("\n")

inpt = [int(i) for i in inpt]

def find():
    i = 0
    j = i + 1
    while i < len(inpt) - 1:
        while j < len(inpt):
            if inpt[i] + inpt[j] == 2020:
                print(f"{inpt[i]} {inpt[j]}")
                return inpt[i] * inpt[j]
            else:
                j += 1
        i += 1
        j = i + 1

def findp2():
    i = 0
    j = i + 1
    k = i + 2
    while i < len(inpt) - 2:
        while j < len(inpt) - 1:
            while k < len(inpt):
                if inpt[i] + inpt[j] + inpt[k] == 2020:
                    print(f"{inpt[i]} {inpt[j]} {inpt[k]}")
                    return inpt[i] * inpt[j] * inpt[k]
                else:
                    k += 1
            j += 1
            k = j + 1
        i += 1
        j = i + 1
        k = i + 2

print(str(find()))

