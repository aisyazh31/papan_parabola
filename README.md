# papan_parabola
Aplikasi web interaktif Phygital (Physical-to-Digital) berbasis Streamlit untuk menganalisis fungsi kuadrat dan grafik parabola dari hasil kerja papan parabola fisik murid.
# 📐 Web Scanner Papan Parabola Transparan

Media pembelajaran matematika interaktif berbasis web (*Phygital: Physical-to-Digital Integration*) yang dirancang khusus untuk murid SMA. Aplikasi ini menjembatani eksperimen fisik menggunakan Papan Parabola dan Lembar Kerja Murid (LKM) dengan analisis digital presisi secara instan melalui HP.

## ✨ Fitur Utama
1. **Unggah Dokumentasi Fisik:** Murid dapat mengunggah foto hasil kerja papan parabola fisik mereka.
2. **Input Koordinat Paku:** Masukkan 3 koordinat titik paku utama pada papan secara ringkas.
3. **Komputasi Otomatis (NumPy):** Mengekstraksi koefisien persamaan kuadrat $f(x) = ax^2 + bx + c$ menggunakan metode *polynomial fitting*.
4. **Analisis Matematika:** Menghitung koordinat titik puncak $(x_p, y_p)$, arah keterbukaan kurva (maksimum/minimum), dan nilai diskriminan ($D$).
5. **Grafik Digital Presisi:** Render kurva parabola mulus dengan gaya GeoGebra menggunakan Matplotlib.

## 🛠️ Teknologi yang Digunakan
* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) (Web Framework)
* [NumPy](https://numpy.org/) (Komputasi Matematika)
* [Matplotlib](https://matplotlib.org/) (Visualisasi Grafik)
* [Pillow (PIL)](https://python-pillow.org/) (Pengolahan Gambar)

## 🚀 Cara Menjalankan Secara Lokal
Jika ingin menjalankan aplikasi ini di komputer lokal:
1. Clone repository ini:
   ```bash
   git clone [https://github.com/username/papan-parabola.git](https://github.com/username/papan-parabola.git)
