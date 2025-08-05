import sys
def totalan(*args):
    total = 0
    for add in args:
        total += add
    return total
numbers = []

while True:
    add = int(input("Enter Number to Add (00 to quit): "))

    if add == 00 :
        print("Result From: ")
        print(" + ".join(str(number) for number in numbers), end="")   #str itu biar ngubah int jadi string
        print(f" = {totalan(*numbers)}")
        sys.exit()
    else:
        try:
            numbers.append(int(add))
        except ValueError:
            print("Enter a Valid Number or 00")
        
    