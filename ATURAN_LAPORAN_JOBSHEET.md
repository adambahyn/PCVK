# ATURAN PEMBUATAN LAPORAN JOBSHEET
### Instruksi untuk AI agent (berdasarkan template resmi + revisi mahasiswa)

Dokumen ini adalah **spesifikasi mengikat**. Ikuti persis. Semua aturan di bawah
diturunkan dari pembandingan dua berkas nyata:

- `Laporan Jobsheet Minggu 5 - Adam Bahy Maulana.docx` — hasil generate script (ACUAN SALAH)
- `Laporan Jobsheet Minggu 5 - Adam Bahy Maulana - Modified.docx` — versi revisi mahasiswa
  (ACUAN BENAR, inilah yang harus ditiru)
- `Template Laporan Jobsheet.docx` — kerangka resmi dari dosen

Aturan ditulis dari `docs/revisi-vs-generate.md` (laporan diff lengkap).

---

## 1. SUMBER KEBENARAN, URUTAN PRIORITAS

1. **Template resmi** (`Template Laporan Jobsheet.docx`) menentukan STRUKTUR.
2. **Modul jobsheet minggu berjalan** menentukan ISI dan SOAL.
3. **Revisi mahasiswa minggu sebelumnya** menentukan GAYA PENULISAN.
4. **Kode yang benar-benar dieksekusi** menentukan ANGKA. Tidak ada angka karangan.

Kalau ragu: struktur dari template, kata-kata dari revisi mahasiswa. Jangan pernah
mengarang struktur sendiri.

---

## 2. STRUKTUR DOKUMEN (MENGIKAT — JANGAN DIUBAH)

Urutan blok harus persis seperti ini:

```
[tabel identitas 7 baris]
[heading judul]
[penjelasan singkat sumber angka]        <- opsional, 1 paragraf, maks 1 baris-kalimat
## <Nama Praktikum Ke-N>                 <- satu per praktikum, N = 1,2,3,...
[tabel Langkah | Jawaban/Deskripsi]
## Soal Praktikum
[tabel Langkah | Jawaban/Deskripsi]
```

### 2.1 Tabel identitas — WAJIB 7 baris, urutan tetap

| Kolom 1 | Kolom 2 | Kolom 3 |
|---|---|---|
| Mata Kuliah | : | PCVK(contoh) |
| Program Studi | : | D4 – Teknik Informatika |
| Semester | : | 5 |
| Kelas | : | TI - 3E |
| NIM | : | <NIM mahasiswa> |
| Nama | : | <nama mahasiswa> |
| Jobsheet Ke- | : | <nomor minggu> |

Aturan keras:

- Nilai kolom 2 harus `:` (titik dua) sebagai kolom terpisah. JANGAN digabung
  jadi `"Nama: Adam"`.
- Nilai kolom 3 diisi; JANGAN dikosongkan seperti template mentah.
- `Program Studi` nilainya persis `D4 – Teknik Informatika` (pakai tanda hubung
  en-dash `–`, bukan `-`).
- `Jobsheet Ke-` — judul baris menyertakan tanda hubung. JANGAN ditulis `Jobsheet Ke`.
- JANGAN menambahkan baris `No. Absen`. Baris ini DIHAPUS (lihat §6).
- Tabel identitas JANGAN diberi header row.

### 2.2 Judul

```
LAPORAN JOBSHEET
```

Hanya dua kata. JANGAN menuliskan `PENGOLAHAN CITRA DAN VISI KOMPUTER` atau
`MINGGU 5 — ...` di judul — mata kuliah sudah tercantum di tabel identitas.
Center-aligned, bold, 13 pt.

### 2.3 Nama praktikum

```
PRAKTIKUM KE-1 : E-1 PERCOBAAN HISTOGRAM
PRAKTIKUM KE-2 : E-2 PERCOBAAN HISTOGRAM EQUALIZATION
PRAKTIKUM KE-3 : E-3 PERCOBAAN DITHERING
```

- Format: `PRAKTIKUM KE-<N> : <KODE> <NAMA PERCOBAAN>` (huruf besar, bold, 14 pt).
- Pemisah kode dan nama adalah **titik dua ` : `**, BUKAN em-dash `—`.
- Pakai kode `E-1`, `E-2`, `E-3` dari modul.

### 2.4 Sub-soal

```
Soal Praktikum 1 : Verifikasi terhadap numpy.histogram dan cv.calcHist
```

- Format: `Soal Praktikum <n> : <deskripsi>` — titik dua, BUKAN `—`.
- bold, 11 pt.

### 2.5 Penomoran daftar bernomor — DILARANG

Soal refleksi dan kesimpulan ditulis sebagai paragraf biasa **tanpa prefix angka**.
Salah: `1. Mengapa equalization ...`. Benar: `Mengapa equalization ...`.
Tanda hubung, bullet, dan penomoran manual lain juga dilarang. Ini sudah
diterapkan pada revisi — ikuti.

---

## 3. WADAH JAWABAN: TABEL `Langkah | Jawaban/Deskripsi`

Ini bagian **paling sering salah**. Template menyediakan tabel terpisah per
praktikum, dan revisi mahasiswa MEMPERTAHANKAN format dua kolom itu.

- Setiap praktikum dipisah dari praktikum lain, masing-masing punya wadah sendiri.
- Header tabel: `Langkah` | `Jawaban/Deskripsi`.
- Kolom `Langkah` berisi nomor urut (1, 2, 3, ...) atau nama tahap.
- Kolom `Jawaban/Deskripsi` berisi uraian + angka hasil.
- JANGAN menggantikan tabel ini dengan tabel data multi-kolom buatan sendiri.
  Tabel data pendukung boleh ditambahkan **di dalam** sel deskripsi, bukan
  menggantikan wadah.
- Baris `Langkah` jangan dikosongkan; setiap langkah modul harus terisi.

Gunakan gaya revisi: judul kecil bold sebagai pemisah di dalam sel, bukan
sub-heading baru di luar tabel.

---

## 4. GAYA PENULISAN (DARI REVISI MAHASISWA)

### 4.1 Panjang dan kepadatan

- Ringkas. Satu paragraf = satu gagasan.
- JANGAN menulis narasi proses kerja ("pertama saya menjalankan...", "setelah itu
  saya menambahkan..."). Langsung ke temuan.
- JANGAN mengulang angka yang sudah ada di tabel di dalam kalimat paragraf.
  Kalau angka ada di tabel, kalimat cukup menjelaskannya secara kualitatif.
- Pangkas kalimat yang hanya menyatakan ulang isi modul.

### 4.2 Metakomentar — DILARANG

JANGAN menulis kalimat tentang proses penyusunan laporan, misalnya:
"saya melaporkan apa adanya", "bukan diklaim sama persis", "angka tidak diketik
ulang", "seluruh kode telah dijalankan tanpa sel error", "catatan privasi:
repositori diatur privat".

Laporan berisi **hasil**, bukan disklaimer penulis. Kalimat seperti itu dihapus
semua di revisi — jangan dimunculkan kembali.

### 4.3 Nada

- Netral, teknis, orang ketiga.
- JANGAN memakai kata "saya" atau "kami".
- JANGAN memakai "aku", "kita".
- JANGAN menambahkan kalimat penutup bersifat opini atau apresiasi diri.

### 4.4 Bahasa

Bahasa Indonesia baku. Istilah teknis tetap dalam bentuk aslinya
(`histogram equalization`, `clipLimit`, `CDF`, `Floyd-Steinberg`).
Angka desimal memakai titik (`.`), bukan koma, agar seragam dengan keluaran
program.

---

## 5. FORMAT VISUAL

| Elemen | Nilai |
|---|---|
| Ukuran halaman | A4 (21,00 × 29,70 cm) |
| Margin | 2,00 cm semua sisi |
| Judul | bold, 13 pt, center |
| Heading praktikum | bold, 14 pt |
| Sub-soal | bold, 11 pt |
| Teks isi | 10,5 pt |
| Caption gambar | *italic*, 9 pt, center |
| Blok kode | Consolas, 8,5 pt, indent 0,5 cm |
| Font dasar template | 12 pt (`w:sz = 24`), spasi baris 1,3, indent baris pertama 1 cm, rata kanan-kiri |

Catatan spasi baris, indent baris pertama, dan perataan **diwarisi dari template**.
Jangan mengeset ulang sendiri; biarkan default template bekerja.

### 5.1 Gambar

- Center-aligned.
- Lebar bervariasi mengikuti kebutuhan isi gambar, JANGAN dipaksa seragam.
  Revisi memakai rentang 14,00–18,09 cm.
- Gambar lebar (histogram berdampingan, figure 2×2) boleh dilebarkan sampai
  ~18 cm; gambar tunggal cukup ~14–15,5 cm.
- Caption WAJIB: `Gambar <n>. <deskripsi>`, italic 9 pt, center, di bawah gambar.

### 5.2 Tabel

- Border semua sisi, tipis, warna abu `808080`, lebar 4 (`w:sz=4`).
- Header baris: bold, 9 pt.
- Style tabel eksplisit diizinkan (revisi memakai `Table1`..`Table10`). Yang penting
  bukan nama style, melainkan border tipis abu dan header bold.
- Lebar tabel menyesuaikan lebar isi. Tabel yang kolomnya dibuang harus ikut
  menyusut (contoh: tabel bahan turun dari 17,00 cm ke 12,75 cm setelah kolom
  ukuran dihapus). JANGAN memaksa semua tabel 17 cm penuh.

---

## 6. YANG HARUS DIHAPUS DARI HASIL GENERATE

Daftar berikut dikonfirmasi ada di versi generate lalu dihapus di revisi.
Jangan pernah menambahkannya lagi:

1. Baris `No. Absen` di tabel identitas.
2. Judul panjang `LAPORAN JOBSHEET PENGOLAHAN CITRA DAN VISI KOMPUTER MINGGU N — ...`.
3. Semua heading bab buatan sendiri di luar template: `PARAMETER PRIBADI BERBASIS
   NIM`, `ALAT DAN BAHAN`, `Analisis Terpadu dan Keterkaitan dengan Pertemuan 2`,
   `Kesimpulan`, `Lampiran — Berkas Kerja`.
4. Seluruh bagian `Lampiran` beserta tabel daftar berkasnya.
5. Semua kalimat metakomentar (§4.2).
6. Semua prefix angka pada daftar (§2.5).
7. Em-dash `—` sebagai pemisah judul — ganti dengan titik dua ` : `.
8. Kalimat disclaimer privasi/GitHub.
9. Baris tabel berisi kolom kosong atau berisi `-` sebagai penanda data tidak ada.
   Kalau data tidak ada, JANGAN buat barisnya.

---

## 7. GAMBAR YANG DISERTAKAN

Hanya gambar yang menjawab soal. JANGAN menyertakan visualisasi tambahan yang
tidak diminta modul. Setiap gambar harus dirujuk oleh minimal satu kalimat di
sel deskripsi.

Urutan gambar mengikuti urutan soal, bukan urutan sel notebook.

---

## 8. PROSEDUR KERJA AGENT

1. Baca template, modul minggu berjalan, dan revisi minggu sebelumnya.
2. Jalankan seluruh kode lebih dulu sampai tuntas tanpa error.
3. Kumpulkan semua angka hasil eksekusi ke satu berkas data (mis. `results.json`).
   Laporan membaca dari berkas itu — JANGAN mengetik ulang angka.
4. Bangun dokumen dengan membuka template lalu mengganti isi selak-belakang,
   supaya warisan format (spasi, indent, margin, footer) tetap utuh.
5. Isi per praktikum ke dalam tabel `Langkah | Jawaban/Deskripsi`, bukan blok bebas.
6. Jalankan pemeriksaan otomatis sebelum menyerahkan (§9).
7. JANGAN membuat klaim yang tidak bisa dibuktikan keluaran program.

---

## 9. PERIKSAAN WAJIB SEBELUM SERAH

Jalankan sebagai skrip. Semua harus lolos:

- [ ] Tabel identitas tepat 7 baris, `Jobsheet Ke-` terisi, tidak ada `No. Absen`.
- [ ] Setiap praktikum yang dikerjakan punya tabel `Langkah | Jawaban/Deskripsi`.
- [ ] Ada blok `Soal Praktikum` dengan wadah yang sama.
- [ ] Judul = `LAPORAN JOBSHEET` saja.
- [ ] Tidak ada string `—` pada judul praktikum dan sub-soal.
- [ ] Tidak ada paragraf dimulai `1.`, `2.`, `3.` (daftar berprefix angka).
- [ ] Tidak ada kata `saya`, `aku`, `kami`.
- [ ] Tidak ada string `tidak diketik ulang`, `apa adanya`, `tanpa sel error`,
      `privasi`, `repositori`.
- [ ] Semua angka di laporan cocok dengan `results.json`.
- [ ] Setiap gambar punya caption `Gambar <n>.` italic 9 pt dan dirujuk di teks.
- [ ] Footer tetap `Laporan Jobsheet` + `Hal. PAGE / NUMPAGES`.
- [ ] Ukuran halaman A4, margin 2 cm.

---

## 10. CATATAN KHUSUS MINGGU 5 (jangan digeneralisasi tanpa cek modul)

Modul minggu 5 mewajibkan hal-hal berikut pada **notebook**, bukan laporan:

- Sel identitas wajib **sel pertama** dan ikut tersimpan keluarannya, berisi
  `NAMA`, `NIM`, `N`, `PARAM`, waktu Asia/Jakarta, versi sistem, dan
  `TOKEN` = 16 karakter pertama `sha256(NIM + '|' + tanggal)`. Notebook tanpa
  sel ini tidak dinilai.
- Setiap gambar keluaran wajib diberi judul memuat NIM:
  `plt.title(NIM + ' - ...')`.
- Nama berkas notebook: `Week5_<No Absen>.ipynb`.

Parameter diturunkan dari tiga digit terakhir NIM (`N`):
`bins = 2^((N mod 4)+3)`, `clip = 1 + (N mod 5)*0,5`, `tile = (N mod 4)+2`,
`L = 2^((N mod 3)+1)`.

---

## 11. KESALAHAN YANG PERNAH TERJADI — JANGAN ULANG

| Kesalahan | Akibat | Perbaikan |
|---|---|---|
| Menambah heading bab sendiri | dokumen tidak sesuai template | hapus, pakai wadah tabel template |
| Menambah baris `No. Absen` | identitas jadi 8 baris | tepat 7 baris |
| Em-dash `—` di judul | gaya berbeda dari revisi | ganti ` : ` |
| Menulis `1.` sebelum soal refleksi | gaya berbeda dari revisi | tulis sebagai paragraf biasa |
| Menyertakan kalimat disklaimer | laporan jadi tidak profesional | hapus semua metakomentar |
| Memaksa semua gambar 15 cm | gambar detail jadi kekecilan | lebarkan sesuai isi (14–18 cm) |
| Kolom tabel diisi `-` | baris sia-sia | hapus barisnya |
| Menambah bagian Lampiran | tidak ada di template | hapus |
