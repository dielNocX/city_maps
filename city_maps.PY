# Program mencari jarak terpendek

# KAMUS
# Posisi_Awal, Posisi_Akhir, Metode, Awal, Awal2 : string
# DJIKSTRA : matriks of float
# Kumpulan : array of string
# X, Y, Z, P, Q, R, j, k, MIN, MIN2, Hasil_Jarak, KOLOM2  : integer


def ISIKOLOM(Awal,MIN2,j,DJIKSTRA,Metode,X,Y,Z,P,Q,R) :
    # Mengisi matriks DJIKSTRA dengan baris tertentu untuk semua kolom

    # KAMUS LOKAL
    # Awal, Tujuan, J1, Metode : string
    # DJIKSTRA : matriks of float
    # X, Y, Z, P, Q, R, i, j, MIN2, Hasil_Jarak  : integer

    Tujuan = "JAKARTA"
    i = 1
    while i < 8 :              # Pengulangan untuk mengisi setiap kolom
        J1 = Awal+Tujuan
        if J1 == "JAKARTACIREBON" or J1 == "CIREBONJAKARTA" :
            DJIKSTRA[j-1][i-1] = 218 + MIN2
        elif J1 == "JAKARTABANDUNG" or J1 == "BANDUNGJAKARTA" :
            DJIKSTRA[j-1][i-1] = 154 + MIN2
        elif J1 == "CIREBONSEMARANG" or J1 == "SEMARANGCIREBON" :
            DJIKSTRA[j-1][i-1] = 233 + MIN2
        elif J1 == "CIREBONMAGELANG" or J1 == "MAGELANGCIREBON" :
            DJIKSTRA[j-1][i-1] = 274 + MIN2
        elif J1 == "SEMARANGSURABAYA" or J1 == "SURABAYASEMARANG" :
            DJIKSTRA[j-1][i-1] = 350 + MIN2
        elif J1 == "MAGELANGSURABAYA" or J1 == "SURABAYAMAGELANG" :
            DJIKSTRA[j-1][i-1] = 348 + MIN2
        elif J1 == "BANDUNGMAGELANG" or J1 == "MAGELANGBANDUNG" :
            DJIKSTRA[j-1][i-1] = 390 + MIN2
        elif J1 == "BANDUNGJOGJA" or J1 == "JOGJABANDUNG" :
            DJIKSTRA[j-1][i-1] = 402 + MIN2
        elif J1 == "JOGJAMAGELANG" or J1 == "MAGELANGJOGJA" :
            DJIKSTRA[j-1][i-1] = 54 + MIN2
        elif J1 == "JAKARTAJAKARTA" or J1 == "CIREBONCIREBON" or J1 == "BANDUNGBANDUNG" or J1 == "JOGJAJOGJA" or J1 == "MAGELANGMAGELANG" or J1 == "SEMARANGSEMARANG" or J1 == "SURABAYASURABAYA" :
            DJIKSTRA[j-1][i-1] = 0 + MIN2
        else :
            if Metode == "MENGEMUDI MOTOR" :                                  # Penambahan kemungkinan jarak dengan metode MENGEMUDI MOTOR
                if J1 == "BANDUNGCIREBON" or J1 == "CIREBONBANDUNG" :
                    DJIKSTRA[j-1][i-1] = 139 + MIN2
                else :
                    DJIKSTRA[j-1][i-1] = float('inf') 
            elif Metode == "BERJALAN" :                                   # Penambahan kemungkinan jarak dengan metode BERJALAN
                if J1 == "BANDUNGSEMARANG" or J1 == "SEMARANGBANDUNG" :
                    DJIKSTRA[j-1][i-1] = 355 + MIN2
                elif J1 == "BANDUNGCIREBON" or J1 == "CIREBONBANDUNG" :
                    DJIKSTRA[j-1][i-1] = 139 + MIN2
                else :
                    DJIKSTRA[j-1][i-1] = float('inf')     
            else :
                DJIKSTRA[j-1][i-1] = float('inf')
        if j > 1 :                                          
            if DJIKSTRA[j-2][i-1] < DJIKSTRA[j-1][i-1] :        # Membandingkan nilai jarak yang didapat dengan baris sebelumnya pada kolom yang sama untuk menentuan pengisian kolom dengan mencari yang terkecil
                DJIKSTRA[j-1][i-1] = DJIKSTRA[j-2][i-1]
            if X == i or Y == i or Z == i or P == i or Q == i or R == i :     
                DJIKSTRA[j-1][i-1] = float('inf')           # Pengisisan kolom tertentu dengan nilai infinite pada kolom yang sudah memiliki nilai minimum pada baris sebelumnya
        if i == 1 :                # Penentuan tujuan untuk mengisi kolom berikutnya
            Tujuan = "CIREBON"
        elif i == 2 :
            Tujuan = "BANDUNG"
        elif i == 3 :
            Tujuan = "JOGJA"
        elif i == 4 :
            Tujuan = "MAGELANG"
        elif i == 5 :
            Tujuan = "SEMARANG"
        elif i == 6 :
            Tujuan = "SURABAYA"
        i = i + 1
    return DJIKSTRA

def JALAN_DILALUI(A,DJIKSTRA,Kumpulan,Posisi_Akhir) :
    # Mencari titik yang dilalui untuk tiba di tujuan

    # KAMUS LOKAL
    # Posisi, Posisi_Akhir, DILEWATI : string
    # DJIKSTRA : matriks of float
    # urutan : array of string
    # Kumpulan : array of string
    # A, n, count, L   : integer 
    # stop : boolean
    Posisi = Posisi_Akhir
    count = 0
    urutan = [ "*" for i in range (7)]
    DILEWATI = ""
    while A > 0 :
        if Posisi == "JAKARTA" :
            n = 0
        elif Posisi == "CIREBON" :
            n = 1
        elif Posisi == "BANDUNG" :
            n = 2
        elif Posisi == "JOGJA" :
            n = 3
        elif Posisi == "MAGELANG" :
            n = 4
        elif Posisi == "SEMARANG" :
            n = 5
        elif Posisi == "SURABAYA" :
            n = 6
        stop = False 
        while DJIKSTRA[A][n] == DJIKSTRA[A-1][n] and stop == False :
            A = A - 1
            if A-1 == -1 :
                stop = True
        urutan[count] = Kumpulan[A]  # Penentuan urutan dari array kumpulan
        count += 1
        Posisi = Kumpulan[A]
    for L in range (count-1,-1,-1) :    # Pengulangan untuk menyatakan titik yang dilalui
        DILEWATI += urutan[L]+"-"
    DILEWATI += Posisi_Akhir
    return DILEWATI

def AWAL2(KOLOM2) :
    # Mencari titik awal baru

    # KAMUS LOKAL
    # KOLOM2 : integer
    # Awal2 : string

    if KOLOM2 == 0 :         # Penentuan titik awal untuk baris selanjutnya
        Awal2 = "JAKARTA"
    elif KOLOM2 == 1 :
        Awal2 = "CIREBON"
    elif KOLOM2 == 2 :
        Awal2 = "BANDUNG"
    elif KOLOM2 == 3 :
        Awal2 = "JOGJA"
    elif KOLOM2 == 4 :
        Awal2 = "MAGELANG"
    elif KOLOM2 == 5 :
        Awal2 = "SEMARANG"
    elif KOLOM2 == 6 :
        Awal2 = "SURABAYA"
    return Awal2

def INFINITE(MIN,DJIKSTRA,j) :
    # Menghasilkan suatu nilai tertentu untuk kolom tertentu yang memenuhi syarat

    # KAMUS LOKAL
    # L, MIN, j : integer
    # DJIKSTRA : matriks of float

    for L in range (7) :
        if MIN == DJIKSTRA[j-1][L] :
            return L + 1

def MINIMUM(DJIKSTRA,j) :
    # Menghasilkan nilai minimum, minimum ke dua, dan indeks dari minimum ke dua

    # KAMUS LOKAL
    # Posisi, Posisi_Akhir, DILEWATI : string
    # DJIKSTRA : matriks of float
    # urutan : array of string
    # Kumpulan : array of string
    # MIN, MIN2, KOLOM2, L   : integer 

    for L in range (7) :
        if L == 0 :
            MIN = DJIKSTRA[j-1][L]
            KOLOM = L
        else :
            if DJIKSTRA[j-1][L] <= MIN :
                MIN = DJIKSTRA[j-1][L]
                KOLOM = L
    MIN2 = float('inf')
    for L in range (7) :
        if L != KOLOM :
            if DJIKSTRA[j-1][L] <= MIN2 :
                MIN2 = DJIKSTRA[j-1][L]
                KOLOM2 = L
    return MIN,MIN2,KOLOM2

# MAIN PROGRAM 
# INPUT
print("Selamat datang di aplikasi maps versi 1.0.0")
Posisi_Awal = input("Masukkan titik awal(JAKARTA/CIREBON/BANDUNG/JOGJA/MAGELANG/SEMARANG/SURABAYA) : ")
Posisi_Akhir = input("Masukkan tujuan akhir(JAKARTA/CIREBON/BANDUNG/JOGJA/MAGELANG/SEMARANG/SURABAYA) : ")
Metode = input("Masukkan metode yang digunakan untuk sampai tujuan (MENGEMUDI MOBIL/MENGEMUDI MOTOR/BERJALAN) : ")
# INISIALISASI
DJIKSTRA = [[0.0 for L in range (7)] for M in range(7)]
MIN2 = 0
Kumpulan = [ "*" for i in range (7)]    
X = 0
Y = 0
Z = 0
P = 0
Q = 0
R = 0
j = 1
k = 8
Awal = Posisi_Awal
if (Posisi_Awal == "JAKARTA" or Posisi_Awal == "CIREBON" or Posisi_Awal == "BANDUNG" or Posisi_Awal == "JOGJA" or Posisi_Awal == "MAGELANG" or Posisi_Awal == "SEMARANG" or Posisi_Awal == "SURABAYA") :
    if (Posisi_Akhir == "JAKARTA" or Posisi_Akhir == "CIREBON" or Posisi_Akhir == "BANDUNG" or Posisi_Akhir == "JOGJA" or Posisi_Akhir == "MAGELANG" or Posisi_Akhir == "SEMARANG" or Posisi_Akhir == "SURABAYA") :
        if Metode == "MENGEMUDI MOBIL" or Metode == "MENGEMUDI MOTOR" or Metode == "BERJALAN" :
            if Posisi_Awal == Posisi_Akhir :
                print("Anda sudah di tujuan anda dengan menempuh 0 KM") # Output
            else :
                while j < k :                                                          # Pengulangan untuk mengisi baris
                    DJIKSTRA = ISIKOLOM(Awal,MIN2,j,DJIKSTRA,Metode,X,Y,Z,P,Q,R)
                    MIN,MIN2,KOLOM2 = MINIMUM(DJIKSTRA,j)
                    Awal2 = AWAL2(KOLOM2)
                    Kumpulan[j-1] = Awal
                    if j == 1 :                         # Pengisian variabel dengan nilai tertentu yang dimana variabel tersebut berperan untuk mengidentifikasi kolom yang harus diberikan nilai infinite
                        X = INFINITE(MIN,DJIKSTRA,j)
                    elif j == 2 :
                        Y = INFINITE(MIN,DJIKSTRA,j)
                    elif j == 3 :
                        Z = INFINITE(MIN,DJIKSTRA,j)
                    elif j == 4 :
                        P = INFINITE(MIN,DJIKSTRA,j)
                    elif j == 5 :
                        Q = INFINITE(MIN,DJIKSTRA,j)
                    elif j == 6 :
                        R = INFINITE(MIN,DJIKSTRA,j)
                    j += 1
                    Awal = Awal2
                    Hasil_Jarak = MIN
                    if Posisi_Akhir == Awal2 :    # Kondisi untuk membuat program melakukan perulangan hanya satu kali lagi
                        k = j + 1
                JALAN = JALAN_DILALUI(j-2,DJIKSTRA,Kumpulan,Posisi_Akhir)
                if Metode == "MENGEMUDI MOBIL" or Metode == "MENGEMUDI MOTOR" :     # Penentuan output berdasarkan metode
                    print("Jarak terdekat dari", Posisi_Awal,"ke", Posisi_Akhir, "dengan",Metode, "adalah", Hasil_Jarak, "KM dengan urutan titik yang dilalui adalah", JALAN )   # Output
                else :
                    print("Jarak terdekat dari", Posisi_Awal,"ke", Posisi_Akhir, "dengan berjalan kaki adalah", Hasil_Jarak, "KM dengan urutan titik yang dilalui adalah", JALAN )  # Output
        else :
            print("Mohon masukkan jenis metode yang valid")  # Output
    else :
        print("Mohon masukkan tujuan yang valid")  # Output
else :
    print("Mohon masukkan titik awal yang valid") # Output

 