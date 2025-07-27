detik = int(input("Enter Time in Second: "))

for x in reversed(range(0,detik)):
    detik= x % 60
    menit=int(x/60) % 60
    jam=int(x/3600) % 24
    print(f"{jam} : {menit} : {detik}")