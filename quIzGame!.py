soal = ["Siapa nama presiden pertama di Indonesia?",
        "Tanggal berapa Indonesia merdeka?",
        "Apa nama sumpah Gadjah Mada?",
        "Kemana Presiden Soekarno diculik?",
        "Kenapa Inggris menjajah Indonesia?"]

pilihan = [["A. Mohammad Hatta\nB. Joko Widodo\nC. BJ.Habibie\nD. Soekarno"],
           ["A. 10 Nov 1945\nB. 17 Agustus 1945\nC. 9 September 2006\nD. 17 Oktober 1945"],
           ["A. Sumpah Palapa\nB. Sumpah Pocong\nC. Sumpah Gatau\nD. Sumpah Apa Ja Deh"],
           ["A. Mataram\nB. Jl.A Yani\nC. Rengasdengklok\nD. WIjayaKusuma"],
           ["A. Mau Rempah-rempah\nB. Mau Budak\nC. Mau masuk islam\nD. Mau sound horeg"]]

jawabanbenar = ("D", "B", "A", "C", "A")
skor = 0
jawabanorang = []
nomer = 0


for soals in soal:
    print(soals)
    for pilihans in pilihan[nomer]:
        print(pilihans)
        jawaban = input("Masukkan Jawaban (A, B, C, atau D): ").upper()
        jawabanorang.append(jawaban)

        if jawaban == jawabanbenar[nomer]:
            print("Benar!")
            skor+=20
            print(f"Skor Sekarang: {skor}")
            print("-".center(30, "-"))

        else: 
           print(f"Salah!\nJawaban Benar: {jawabanbenar[nomer]}")
           print("-".center(30, "-"))

        nomer+=1



if skor < 60: 
    print (f"Kamu TIDAK LULUS\nSKOR: {skor}\nCOBA LAGI!")
else:
    print(f"Selamat Kamu LULUS!\nSKOR: {skor}")