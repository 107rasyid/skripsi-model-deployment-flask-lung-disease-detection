# skripsi-model-deployment-flask-lung-disease-detection

Repositori untuk deployment model skripsi berbasis dashboard website menggunakan Flask.

## Deteksi Penyakit Paru-Paru dari Citra X-Ray Menggunakan Segmentasi U-Net dan Klasifikasi CNN

Berdasarkan hasil penelitian, model yang dibuat telah berhasil melakukan deteksi penyakit paru-paru dari citra X-ray dengan baik.  
- **Model U-Net** berhasil mencapai **nilai Intersection over Union (IoU) sebesar 91,69%**, menunjukkan kinerja yang baik dalam melakukan segmentasi region paru-paru.  
- **Model CNN** menunjukkan **akurasi sebesar 95,70%**, mencerminkan performa yang baik dalam melakukan klasifikasi **COVID-19, pneumonia, tuberculosis, dan paru-paru normal**.  

### Perbandingan Performa Model CNN dengan Transfer Learning

| Model            | Waktu Pelatihan | Loss  | Akurasi  |
|-----------------|---------------|------|--------|
| CNN yang diajukan | 756.85 s       | 0.2214 | **95.70%** |
| MobileNetV2      | 904.26 s       | 0.1539 | **95.70%** |
| Xception        | 687.54 s       | 0.2086 | 92.62% |
| VGG19           | 1660.99 s      | 0.1721 | 94.06% |

### Akurasi Perkelas (Recall) Tiap Model

| Model            | Normal | Tuberculosis | Pneumonia | COVID-19 |
|-----------------|--------|--------------|-----------|----------|
| CNN yang diajukan | **96.25%** | 96.88% | **97.09%** | 87.93% |
| MobileNetV2      | 94.37% | **100.00%** | 95.63% | **94.83%** |
| Xception        | 91.25% | 96.88% | 93.69% | 87.93% |
| VGG19           | 94.37% | 93.75% | 97.09% | 82.76% |

---

## Aplikasi Web

Prototipe sistem diimplementasikan dalam bentuk aplikasi berbasis website menggunakan **Flask** sebagai backend dan **Jinja** sebagai template engine.  

Fitur utama aplikasi:
- Upload gambar X-ray untuk analisis penyakit paru-paru.
- Melakukan segmentasi paru-paru dengan model **U-Net**.
- Melakukan klasifikasi penyakit paru-paru (Normal, Tuberculosis, Pneumonia, COVID-19) dengan **CNN**.
- Menampilkan hasil segmentasi dan prediksi secara visual di dashboard.

Berikut adalah tampilan antarmuka aplikasi:

1. **Halaman Awal**  
   ![Halaman Awal](templates/halaman_awal.PNG)

2. **Halaman Hasil**  
   ![Halaman Hasil](templates/halaman_hasil.PNG)

---

## Cara Menjalankan Proyek

### 1. Clone Repository
Clone repositori dan masuk ke dalam folder proyek:
```bash
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection

2. Buat Virtual Environment
Buat dan aktifkan virtual environment untuk mengisolasi dependensi proyek:
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows


Share


You said:
hai bisa bantu aku buatin file readme.md?

ini yang udah kubikin

# skripsi-model-deployment-flask-lung-disease-detection
 Repositori untuk deployment model skripsi berbasis dashboard website menggunakan flask


lanjutin deskripsi tentang penjelasan skripsi ini:
DETEKSI PENYAKIT PARU-PARU DARI CITRA X-RAY MENGGUNAKAN SEGMENTASI U-NET DAN KLASIFIKASI CNN

ini hasilnya
Berdasarkan hasil penelitian, model yang dibuat telah berhasil melakukan deteksi penyakit paru-paru dari citra X-ray dengan baik. Model U-Net berhasil mencapai nilai intersection over union (IoU) sebesar 91,69%, yang menunjukkan kinerja yang baik dalam melakukan segmentasi region paru-paru. Sementara itu, model CNN menunjukkan akurasi sebesar 95,70%, yang mencerminkan performa yang baik dalam melakukan klasifikasi COVID-19, pneumonia, tuberculosis, dan paru-paru normal. 

lanjutin tampilan tabel perbandingan hasil:
Tabel 4.26 Perbandingan Performa Model CNN dengan Transfer Learning
Model	Waktu Pelatihan	Loss	Akurasi
CNN yang diajukan	756.85 s	0.2214	95.70%
MobileNetV2	904.26 s 	0.1539	95.70%
Xception	687.54 s	0.2086	92.62%
VGG19	1660.99 s	0.1721	94.06%

Tabel 4.27 Perhitungan Akurasi Perkelas (Recall) Tiap Model
Model	Akurasi Perkelas (Recall)
	Normal	Tuberculosis	Pneumonia	COVID-19
CNN yang diajukan	96.25%	96.88%	97.09%	87.93%
MobileNetV2	94.37%	100.00%	95.63%	94.83%
Xception	91.25%	96.88%	93.69%	87.93%
VGG19	94.37%	93.75%	97.09%	82.76%

lanjutin tentang aplikasi web yang dibikin itu pake:
Prototipe sistem diimplementasikan dalam aplikasi website menggunakan framework backend Flask dan template engine Jinja

bikinin visualisasi tampilan web-nya, filenya aku simpen di main/templates/halaman_awal.png dan halaman_hasil.png

jelasin gimana kalo mau ngejalanin proyek ini step stepnya

2/2

ChatGPT said:
Berikut adalah file README.md yang sudah diperbarui dengan penjelasan lengkap tentang skripsi, perbandingan model, aplikasi web, serta langkah-langkah menjalankan proyek:

markdown
Copy
Edit
# skripsi-model-deployment-flask-lung-disease-detection

Repositori untuk deployment model skripsi berbasis dashboard website menggunakan Flask.

## Deteksi Penyakit Paru-Paru dari Citra X-Ray Menggunakan Segmentasi U-Net dan Klasifikasi CNN

Berdasarkan hasil penelitian, model yang dibuat telah berhasil melakukan deteksi penyakit paru-paru dari citra X-ray dengan baik.  
- **Model U-Net** berhasil mencapai **nilai Intersection over Union (IoU) sebesar 91,69%**, menunjukkan kinerja yang baik dalam melakukan segmentasi region paru-paru.  
- **Model CNN** menunjukkan **akurasi sebesar 95,70%**, mencerminkan performa yang baik dalam melakukan klasifikasi **COVID-19, pneumonia, tuberculosis, dan paru-paru normal**.  

### Perbandingan Performa Model CNN dengan Transfer Learning

| Model            | Waktu Pelatihan | Loss  | Akurasi  |
|-----------------|---------------|------|--------|
| CNN yang diajukan | 756.85 s       | 0.2214 | **95.70%** |
| MobileNetV2      | 904.26 s       | 0.1539 | **95.70%** |
| Xception        | 687.54 s       | 0.2086 | 92.62% |
| VGG19           | 1660.99 s      | 0.1721 | 94.06% |

### Akurasi Perkelas (Recall) Tiap Model

| Model            | Normal | Tuberculosis | Pneumonia | COVID-19 |
|-----------------|--------|--------------|-----------|----------|
| CNN yang diajukan | **96.25%** | 96.88% | **97.09%** | 87.93% |
| MobileNetV2      | 94.37% | **100.00%** | 95.63% | **94.83%** |
| Xception        | 91.25% | 96.88% | 93.69% | 87.93% |
| VGG19           | 94.37% | 93.75% | 97.09% | 82.76% |

---

## Aplikasi Web

Prototipe sistem diimplementasikan dalam bentuk aplikasi berbasis website menggunakan **Flask** sebagai backend dan **Jinja** sebagai template engine.  

Fitur utama aplikasi:
- Upload gambar X-ray untuk analisis penyakit paru-paru.
- Melakukan segmentasi paru-paru dengan model **U-Net**.
- Melakukan klasifikasi penyakit paru-paru (Normal, Tuberculosis, Pneumonia, COVID-19) dengan **CNN**.
- Menampilkan hasil segmentasi dan prediksi secara visual di dashboard.

Berikut adalah tampilan antarmuka aplikasi:

1. **Halaman Awal**  
   ![Halaman Awal](main/templates/halaman_awal.png)

2. **Halaman Hasil**  
   ![Halaman Hasil](main/templates/halaman_hasil.png)

---

## Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection
2. Buat Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Jalankan Aplikasi Flask
bash
Copy
Edit
python app.py
Aplikasi akan berjalan di http://127.0.0.1:5000/.

5. Gunakan Aplikasi
Buka browser dan akses http://127.0.0.1:5000/.
Upload gambar X-ray untuk mendapatkan hasil segmentasi dan klasifikasi.
Lihat hasilnya di halaman hasil.
Struktur Direktori
php
Copy
Edit
skripsi-model-deployment-flask-lung-disease-detection/
│── main/
│   ├── static/                # Folder untuk file CSS, JS, dan gambar
│   ├── templates/             # Folder untuk file HTML (Jinja)
│   │   ├── halaman_awal.html
│   │   ├── halaman_hasil.html
│   ├── model/                 # Folder untuk model U-Net & CNN
│   │   ├── unet_model.h5
│   │   ├── cnn_model.h5
│── app.py                     # File utama Flask
│── requirements.txt            # Daftar dependensi
│── README.md                   # Dokumentasi proyek
Teknologi yang Digunakan
Python 3.8+
Flask (Backend Framework)
TensorFlow/Keras (Deep Learning Model)
OpenCV (Image Processing)
Matplotlib & Seaborn (Visualisasi Data)
HTML, CSS, Jinja (Frontend)
Kontributor
[Nama Kamu] - Penulis dan pengembang utama
Jika ada pertanyaan atau saran, silakan buat issue atau hubungi saya. 😊

README ini sudah mencakup: ✅ Deskripsi proyek
✅ Perbandingan hasil model
✅ Penjelasan aplikasi web
✅ Langkah-langkah menjalankan proyek
✅ Struktur folder dan teknologi yang digunakan

Kalau ada yang mau ditambah atau diperbaiki, kasih tahu aja! 🚀


2/2

You said:
ehh itu ada yang kepoting code-nyaa 
ChatGPT said:
Berikut adalah revisi README.md dengan format kode yang lengkap:

markdown
Copy
Edit
# skripsi-model-deployment-flask-lung-disease-detection

Repositori untuk deployment model skripsi berbasis dashboard website menggunakan Flask.

## Deteksi Penyakit Paru-Paru dari Citra X-Ray Menggunakan Segmentasi U-Net dan Klasifikasi CNN

Berdasarkan hasil penelitian, model yang dibuat telah berhasil melakukan deteksi penyakit paru-paru dari citra X-ray dengan baik.  
- **Model U-Net** berhasil mencapai **nilai Intersection over Union (IoU) sebesar 91,69%**, menunjukkan kinerja yang baik dalam melakukan segmentasi region paru-paru.  
- **Model CNN** menunjukkan **akurasi sebesar 95,70%**, mencerminkan performa yang baik dalam melakukan klasifikasi **COVID-19, pneumonia, tuberculosis, dan paru-paru normal**.  

### Perbandingan Performa Model CNN dengan Transfer Learning

| Model            | Waktu Pelatihan | Loss  | Akurasi  |
|-----------------|---------------|------|--------|
| CNN yang diajukan | 756.85 s       | 0.2214 | **95.70%** |
| MobileNetV2      | 904.26 s       | 0.1539 | **95.70%** |
| Xception        | 687.54 s       | 0.2086 | 92.62% |
| VGG19           | 1660.99 s      | 0.1721 | 94.06% |

### Akurasi Perkelas (Recall) Tiap Model

| Model            | Normal | Tuberculosis | Pneumonia | COVID-19 |
|-----------------|--------|--------------|-----------|----------|
| CNN yang diajukan | **96.25%** | 96.88% | **97.09%** | 87.93% |
| MobileNetV2      | 94.37% | **100.00%** | 95.63% | **94.83%** |
| Xception        | 91.25% | 96.88% | 93.69% | 87.93% |
| VGG19           | 94.37% | 93.75% | 97.09% | 82.76% |

---

## Aplikasi Web

Prototipe sistem diimplementasikan dalam bentuk aplikasi berbasis website menggunakan **Flask** sebagai backend dan **Jinja** sebagai template engine.  

Fitur utama aplikasi:
- Upload gambar X-ray untuk analisis penyakit paru-paru.
- Melakukan segmentasi paru-paru dengan model **U-Net**.
- Melakukan klasifikasi penyakit paru-paru (Normal, Tuberculosis, Pneumonia, COVID-19) dengan **CNN**.
- Menampilkan hasil segmentasi dan prediksi secara visual di dashboard.

Berikut adalah tampilan antarmuka aplikasi:

1. **Halaman Awal**  
   ![Halaman Awal](main/templates/halaman_awal.png)

2. **Halaman Hasil**  
   ![Halaman Hasil](main/templates/halaman_hasil.png)

---

## Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection
2. Buat Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Jalankan Aplikasi Flask
bash
Copy
Edit
python app.py
Aplikasi akan berjalan di http://127.0.0.1:5000/.

5. Gunakan Aplikasi
Buka browser dan akses http://127.0.0.1:5000/.
Upload gambar X-ray untuk mendapatkan hasil segmentasi dan klasifikasi.
Lihat hasilnya di halaman hasil.
Struktur Direktori
plaintext
Copy
Edit
skripsi-model-deployment-flask-lung-disease-detection/
│── main/
│   ├── static/                # Folder untuk file CSS, JS, dan gambar
│   ├── templates/             # Folder untuk file HTML (Jinja)
│   │   ├── halaman_awal.html
│   │   ├── halaman_hasil.html
│   ├── model/                 # Folder untuk model U-Net & CNN
│   │   ├── unet_model.h5
│   │   ├── cnn_model.h5
│── app.py                     # File utama Flask
│── requirements.txt            # Daftar dependensi
│── README.md                   # Dokumentasi proyek
Teknologi yang Digunakan
Python 3.8+
Flask (Backend Framework)
TensorFlow/Keras (Deep Learning Model)
OpenCV (Image Processing)
Matplotlib & Seaborn (Visualisasi Data)
HTML, CSS, Jinja (Frontend)
Kontributor
[Nama Kamu] - Penulis dan pengembang utama
Jika ada pertanyaan atau saran, silakan buat issue atau hubungi saya. 😊

yaml
Copy
Edit

---

README ini sudah lengkap dan tidak ada bagian yang terpotong.  
Kalau ada yang perlu diperbaiki atau ditambahkan, kasih tahu aja! 🚀





You said:
yang ini kepotong weh

## Cara Menjalankan Proyek

### 1. Clone Repository
bash
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection


lanjutin bagian ini aja
ChatGPT said:
Oke, ini lanjutan bagian cara menjalankan proyeknya:

markdown
Copy
Edit
### 2. Buat Virtual Environment
Buat dan aktifkan virtual environment untuk mengisolasi dependensi proyek.

```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows
3. Install Dependencies
Instal semua paket yang diperlukan menggunakan requirements.txt.

bash
Copy
Edit
pip install -r requirements.txt
4. Jalankan Aplikasi Flask
Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah berikut:

bash
Copy
Edit
python app.py
Jika berhasil,






You said:
jangan dipisah pisah gituu langsung dalam code saja
ChatGPT said:
Siap, ini versi lanjutannya dalam satu blok kode:

bash
Copy
Edit
# 1. Clone Repository
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection

# 2. Buat Virtual Environment
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Jalankan Aplikasi Flask
python app.py

# 5. Akses aplikasi di browser
# Buka http://127.0.0.1:5000/
Udah rapi, langsung bisa di-copy paste ke terminal. 🚀






You said:
eh ini jelek plis

## Cara Menjalankan Proyek

# 1. Clone Repository
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection

# 2. Buat Virtual Environment
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Jalankan Aplikasi Flask
python app.py

# 5. Akses aplikasi di browser
# Buka http://127.0.0.1:5000/


bikin yang bener 
ChatGPT said:
Oke, ini versi yang lebih rapi dan sesuai format Markdown yang benar:

markdown
Copy
Edit
## Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection
2. Buat Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Jalankan Aplikasi Flask
bash
Copy
Edit
python app.py
5. Akses Aplikasi di Browser
Buka browser dan akses:

cpp
Copy
Edit
http://127.0.0.1:5000/
nginx
Copy
Edit

Sekarang lebih rapi dan gampang dibaca. 🚀





You said:
ini yang bener gimanaaa

## Cara Menjalankan Proyek

# 1. Clone Repository
bash
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection

# 2. Buat Virtual Environment
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Jalankan Aplikasi Flask
python app.py

# 5. Akses aplikasi di browser
Buka http://127.0.0.1:5000/


kepotong
ChatGPT said:
Ini versi yang benar dan rapi sesuai format Markdown:

markdown
Copy
Edit
## Cara Menjalankan Proyek

### 1. Clone Repository
Clone repositori dan masuk ke dalam folder proyek:
```bash
git clone https://github.com/username/skripsi-model-deployment-flask-lung-disease-detection.git
cd skripsi-model-deployment-flask-lung-disease-detection

2. Buat Virtual Environment
Buat dan aktifkan virtual environment untuk mengisolasi dependensi proyek:
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate     # Untuk Windows

3. Install Dependencies
Instal semua paket yang diperlukan menggunakan file requirements.txt:
pip install -r requirements.txt

4. Jalankan Aplikasi Flask
Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah berikut:
python app.py

5. Akses Aplikasi di Browser
Setelah aplikasi berjalan, buka browser dan akses:
http://127.0.0.1:5000/
