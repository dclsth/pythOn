

def data(**kwargs):
    for key, value in  kwargs.items():
        print(f"{key} = {value}", end="\n")

data(Nama= "Dara",
     AsalKota= "Surabaya",
     Tanggallahir = "9 September 2006")