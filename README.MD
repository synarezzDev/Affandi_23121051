# EduSmart AI Pro — Personal Intelligence Learning System
**Oleh: Affandi (NIM: 23121051)**

---

## Deskripsi Proyek
**EduSmart AI Pro** adalah platform asisten akademik berbasis Web yang mengintegrasikan kecerdasan buatan (AI) untuk membantu mahasiswa mengoptimalkan proses belajar. Aplikasi ini dirancang untuk menyelesaikan masalah beban kognitif saat membaca materi kuliah yang panjang melalui fitur otomatisasi ringkasan, visualisasi konsep, dan pembuatan kuis adaptif.

Aplikasi ini memenuhi seluruh kriteria penilaian UAS:
- **Integrasi AI Multimodal:** Menggunakan Google Gemini 1.5 Flash.
- **Orisinalitas:** Dikembangkan secara mandiri dengan identitas pengembang terintegrasi.
- **Keamanan:** Menerapkan manajemen *environment variables* untuk melindungi kredensial API.
- **Statis & Efisien:** Berjalan di server lokal tanpa ketergantungan database eksternal sesuai instruksi tugas.

---

## Fitur Unggulan
1. **Smart Summary:** Algoritma ekstraksi teks untuk merangkum jurnal atau materi kuliah menjadi poin-poin akademik yang terstruktur.
2. **Mind Matrix (Visual):** Menghasilkan bagan alur konsep secara otomatis menggunakan *Mermaid.js* berdasarkan input teks.
3. **AI Quiz Generator:** Membuat soal pilihan ganda tingkat perguruan tinggi lengkap dengan kunci jawaban untuk evaluasi mandiri.
4. **Professional UI/UX:** Antarmuka modern dengan *Tailwind CSS*, mendukung *Splash Screen* personal, serta mode *Dark/Light* yang kontras.
5. **Smart Export:** Fitur konversi hasil analisis AI langsung ke format PDF yang rapi.

---

## Arsitektur Teknologi
- **Core Engine:** Python 3.x dengan Framework Flask.
- **AI Model:** Google Gemini 1.5 Flash API (SDK Resmi).
- **Frontend:** HTML5, CSS3 (Tailwind), JavaScript (ES6+).
- **Libraries:** `flask-cors`, `python-dotenv`, `mermaid.js`, `html2pdf.js`, `google-generativeai`.

---

## Panduan Instalasi & Penggunaan
Ikuti langkah-langkah berikut untuk menjalankan proyek di lingkungan lokal:

### 1. Persiapan Lingkungan
Clone repository dan pastikan Anda telah menginstal Python. Kemudian instal library yang diperlukan:
```bash
pip install -r requirements.txt