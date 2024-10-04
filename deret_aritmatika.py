def deret_aritmatika(n, a=2, d=3):
    deret = [a + i * d for i in range(n)]
    return deret

if __name__ == "__main__":
    n1 = int(input("Masukkan jumlah elemen untuk deret pertama: "))
    print("Output untuk input", n1, ":", deret_aritmatika(n1))

    n2 = int(input("Masukkan jumlah elemen untuk deret kedua: "))
    print("Output untuk input", n2, ":", deret_aritmatika(n2))
