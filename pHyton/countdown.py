
jams = int(input("masukkan jam: "))

menits = int(input("masukkan menit: "))


for jam in reversed(range(jams)):
    for menit in reversed(range(menits)):
        for detik in reversed(range(60)):
            print(f"{jam}:{menit}:{detik}")
            


