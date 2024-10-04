# Deret Aritmatika

Proyek ini bertujuan untuk menghasilkan deret bilangan aritmatika dengan jumlah elemen tertentu (N). Setiap elemen dalam deret ini memiliki beda (selisih) tetap antara elemen-elemen berurutan.

## Fitur

- Menghasilkan deret aritmatika berdasarkan input jumlah elemen.
- Suku pertama (a) dan beda (d) bisa disesuaikan (default: a=2, d=3).

## Persyaratan

Pastikan Python telah terinstal di sistem Anda. Proyek ini menggunakan Python 3.x.

Anda dapat memeriksa versi Python dengan menjalankan perintah berikut di terminal atau command prompt:

```bash
python --version
```

## Cara Instalasi

1. **Clone repository atau salin kode:**

   Anda dapat mengunduh kode ini atau menyalinnya ke editor teks favorit Anda.

2. **Buat file Python:**

   Buat file baru dengan nama `deret_aritmatika.py` dan salin kode di bawah ini ke dalam file tersebut:

   ```python
   def deret_aritmatika(n, a=2, d=3):
       deret = [a + i * d for i in range(n)]
       return deret

   if __name__ == "__main__":
       n1 = int(input("Masukkan jumlah elemen untuk deret pertama: "))
       print("Output untuk input", n1, ":", deret_aritmatika(n1))

       n2 = int(input("Masukkan jumlah elemen untuk deret kedua: "))
       print("Output untuk input", n2, ":", deret_aritmatika(n2))
   ```

3. **Jalankan program:**

   Anda dapat menjalankan program dengan membuka terminal atau command prompt, navigasi ke folder di mana file Python disimpan, dan menjalankan perintah berikut:

   ```bash
   python deret_aritmatika.py
   ```

4. **Masukkan jumlah elemen:**

   Setelah program dijalankan, Anda akan diminta untuk memasukkan jumlah elemen yang diinginkan untuk deret bilangan aritmatika. Sebagai contoh:

   ```bash
   Masukkan jumlah elemen untuk deret pertama: 4
   Output untuk input 4 : [2, 5, 8, 11]

   Masukkan jumlah elemen untuk deret kedua: 7
   Output untuk input 7 : [2, 5, 8, 11, 14, 17, 20]
   ```

## Contoh Penggunaan

Misalkan Anda ingin menghasilkan deret aritmatika dengan suku pertama = 2, beda = 3, dan jumlah elemen sebanyak 4. Maka, outputnya akan seperti berikut:

- Input: 4
- Output: [2, 5, 8, 11]

Jika Anda memasukkan jumlah elemen sebanyak 7, outputnya akan:

- Input: 7
- Output: [2, 5, 8, 11, 14, 17, 20]

## Penyesuaian

Anda dapat menyesuaikan suku pertama (a) dan beda (d) sesuai kebutuhan. Jika Anda ingin mengubah suku pertama atau beda, ubahlah parameter `a` dan `d` pada fungsi `deret_aritmatika`.

Contoh:

```python
print(deret_aritmatika(5, a=1, d=4))
```

Akan menghasilkan deret dengan suku pertama 1 dan beda 4.

- Output: [1, 5, 9, 13, 17]

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](https://opensource.org/licenses/MIT).
