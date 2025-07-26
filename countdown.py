

menits = int(input("masukkan menit: "))

for detik in reversed(range(0,60)):
    for menit in reversed(range(0,menits)):
        print(f"00:{menits-1}:{detik}")


