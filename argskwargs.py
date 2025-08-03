import sys
def totalan(*args):
    total = 0
    for add in args:
        total += add
    return total

add = input("Enter Number to Add (00 to quit): ")

while True:
    if add == "q" :
        print(totalan(add))
        sys.exit()
    else:
        add = (input("Enter Number to Add (q to quit): "))
    