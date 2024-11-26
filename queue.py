from collections import deque
def simulasi_antrian():
    queue = deque()
    print("selamat datang di jack bakery ada yang bisa kami bantu?  ")
    while True:
        print("1. Tambah pelanggan ke antrian")
        print("2. Layani pelanggan")
        print("3. Tampilkan antrian")
        print("4. Keluar")
        pilihan = input("Masukkan opsi: ")

        if pilihan=="1":
            print("atas nama siapa?")
            nama = input("Masukkan nama pelanggan: ")
            queue.append(nama)
            print(f"Pelanggan {nama} telah ditambahkan ke antrian.")
        elif pilihan =="2":
            if queue:
                dilayani = queue.popleft() 
                print("a. makanan")
                print("b. minuman")
                print("c. keduanya")
                pilihan_pesanan = input(f"mau pesen apa? {nama}:")
                if pilihan_pesanan == "a":
                    print(f"pelanggan {dilayani} pesen makanan")
                elif pilihan_pesanan == "b":
                    print(f"pelanggan {dilayani} pesen minuman")
                elif pilihan_pesanan == "c":
                    print(f"pelanggan {dilayani} pesen keduanya")
                else:
                    print("Opsi tidak valid")
            else:
                print("Antrian kosong")
        elif pilihan=="3":
            print("Antrian saat ini: ", list(queue))
        elif pilihan=="4":
            print("Keluar dari program")
            break
        else:
            print("Opsi tidak valid")
#menjalankan simulasi
simulasi_antrian()
