jams = int(input("masukkan jam: "))
menits = int(input("masukkan menit: "))
detiks = int(input("masukkan detik: "))

for jam in reversed(range(0, jams)):
    for menit in reversed(range(0, menits)):
        for detik in reversed(range(0, detiks)):
            print(f"{jam} : {menit} : {detik}")

                

