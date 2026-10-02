# Diff: Laporan Generate vs Revisi Mahasiswa

Perbandingan `Laporan Jobsheet Minggu 5 - Adam Bahy Maulana.docx` (generate, **salah**)
dengan `... - Modified.docx` (revisi mahasiswa, **benar**).

Ringkasan blok: generate 92 blok (71 paragraf, 10 tabel, 11 gambar) → revisi 90 blok
(69 paragraf, 10 tabel, 11 gambar). Total 15 blok berubah. Jumlah tabel dan gambar
sama, jadi revisi murni **penyuntingan**, bukan penambahan isi.

---

## A. Perubahan struktur

### A1. Judul dipendekkan

| | |
|---|---|
| Generate | `LAPORAN JOBSHEET PENGOLAHAN CITRA DAN VISI KOMPUTER` + `MINGGU 5 — HISTOGRAM, ...` |
| Revisi | `LAPORAN JOBSHEET` |
| Sebab | Mata kuliah dan minggu sudah ada di tabel identitas. Judul panjang mubazir. |

### A2. Tabel identitas kembali ke bentuk template

| Baris | Generate | Revisi |
|---|---|---|
| Mata Kuliah | `Pengolahan Citra dan Visi Komputer` | `PCVK` |
| Program Studi | `D4 Teknik Informatika` | `D4 – Teknik Informatika` |
| NIM, Nama | ada | ada |
| **No. Absen** | **ADA** | **DIHAPUS** |
| Jobsheet Ke- | ada (urutan terakhir) | ada |

Generate 8 baris → revisi 7 baris. Nama jurusan disamakan persis dengan template
memakai en-dash.

### A3. Metakomentar dihapus

| Generate | Revisi |
|---|---|
| `Notebook sumber: Week5_2.ipynb. Seluruh angka pada laporan ini diambil langsung dari keluaran eksekusi notebook (results.json), bukan diketik ulang.` | `Seluruh angka pada laporan ini diambil langsung dari keluaran eksekusi notebook (results.json).` |
| `Catatan privasi: repositori GitHub diatur privat karena citra KTM memuat data pribadi...` | *(dihapus total)* |
| `Seluruh kode, notebook, dan gambar keluaran disusun pada satu folder kerja dan telah dijalankan sampai tuntas tanpa sel error.` | *(dihapus total)* |
| `Angka pada laporan ini tidak diketik ulang: ... laporan selalu cocok dengan keluaran eksekusi.` | *(dihapus total)* |

Pola: semua kalimat tentang **proses penyusunan** dibuang. Yang tinggal hanya
keterangan minimum dari mana angka berasal.

### A4. Pemisah judul: em-dash → titik dua

| Generate | Revisi |
|---|---|
| `PRAKTIKUM KE-1 — E-1 PERCOBAAN HISTOGRAM` | `PRAKTIKUM KE-1 : E-1 PERCOBAAN HISTOGRAM` |
| `PRAKTIKUM KE-2 — E-2 PERCOBAAN HISTOGRAM EQUALIZATION` | `PRAKTIKUM KE-2 : E-2 PERCOBAAN HISTOGRAM EQUALIZATION` |
| `PRAKTIKUM KE-3 — E-3 PERCOBAAN DITHERING` | `PRAKTIKUM KE-3 : E-3 PERCOBAAN DITHERING` |
| `Soal Praktikum 1 — Verifikasi terhadap numpy...` | `Soal Praktikum 1 : Verifikasi terhadap numpy...` |
| `Soal Praktikum 2 — Histogram ternormalisasi...` | `Soal Praktikum 2 : Histogram ternormalisasi...` |
| `Soal Praktikum 3 — Jumlah bin: 64 bin...` | `Soal Praktikum 3 : Jumlah bin: 64 bin...` |
| `Tahap 1 — Penelusuran manual algoritma...` | `Tahap 1 : Penelusuran manual algoritma...` |
| `Soal Praktikum 4 — Efek pada citra berwarna...` | `Soal Praktikum 4 : Efek pada citra berwarna...` |
| `Soal Praktikum 5 — CLAHE: memperkecil clipLimit` | `Soal Praktikum 5 : CLAHE: memperkecil clipLimit` |

### A5. Prefix angka pada daftar dihapus

Generate menulis `1. Mengapa equalization...`, `2. Apakah equalization...`,
`3. Antara equalization...` (soal refleksi) dan `1.` – `5.` (kesimpulan).
Revisi menghapus semua prefix itu; jadi paragraf biasa tanpa nomor.

### A6. Tabel ALAT DAN BAHAN dipangkas kolom

Generate punya 4 kolom: `Berkas | Ukuran (baris x kolom) | Kondisi akuisisi | Rerata intensitas`.
Revisi jadi 3 kolom: `Berkas | Kondisi akuisisi | Rerata intensitas` — kolom ukuran
dibuang. Lebar tabel turun dari 17,00 cm ke 12,75 cm.

### A7. Paragraf ditambahkan (bukan dikurangi)

Satu paragraf ditambahkan di akhir jawaban Soal Praktikum 2:

> `KTM1b (lampu ruangan) berada di antara keduanya dengan p95-p05 = 124 level, sementara KTM1d (matahari) punya sebaran terlebar, p05 = 38 dan p95 = 172, sehingga pencahayaannya paling merata dari keempat kondisi.`

Generate menyisipkan kalimat ini di dalam paragraf besar sebelumnya; revisi
memecahnya jadi paragraf tersendiri. Pola: **satu gagasan per paragraf**.

### A8. Bagian Lampiran dihapus

Generate menutup dokumen dengan `Lampiran — Berkas Kerja` + tabel 5 baris berisi
daftar berkas dan keterangannya. Revisi **tidak punya bagian ini sama sekali** —
dokumen berakhir di kesimpulan. Template juga tidak menyediakan tempat untuknya.

---

## B. Yang TIDAK berubah

- Ukuran halaman A4, margin 2,00 cm semua sisi.
- Footer: `Laporan Jobsheet` + `Hal. PAGE / NUMPAGES`, font Book Antiqua 10 pt.
- Jumlah tabel (10) dan gambar (11) — tidak ada yang ditambah atau dibuang.
- Caption gambar `Gambar <n>.` italic 9 pt center.
- Blok kode Consolas 8,5 pt.
- Judul praktikum bold 14 pt, sub-soal bold 11 pt.
- Isi angka pada tabel data — semua cocok, hanya wadah dan kalimat yang disunting.

---

## C. Perubahan format gambar

Revisi melebarkan empat gambar besar. Generate memaksa hampir semuanya 15 cm.

| Gambar | Generate | Revisi |
|---|---|---|
| Gambar 1 | 15,50 cm | 15,50 cm |
| Gambar 2 | 14,00 cm | 15,05 cm |
| Gambar 3 | 15,00 cm | 16,53 cm |
| Gambar 4 | 15,00 cm | 16,32 cm |
| Gambar 5 | 15,00 cm | 16,29 cm |
| Gambar 6 | 15,00 cm | 17,69 cm |
| Gambar 7 | 14,00 cm | 14,00 cm |
| Gambar 8 | 15,00 cm | 18,09 cm |
| Gambar 9 | 15,00 cm | 15,00 cm |
| Gambar 10 | 14,00 cm | 14,00 cm |
| Gambar 11 | 14,00 cm | 14,00 cm |

Pola: gambar berisi banyak panel diperlebar (sampai 18,09 cm), gambar tunggal
dibiarkan 14–15 cm.

---

## D. Perubahan tabel format

| Tabel | Generate | Revisi |
|---|---|---|
| T0 identitas | tanpa style, 8 baris | style `Table1`, `tblW` 17,00 cm, **7 baris** |
| T1 parameter NIM | tanpa style, `tblW` 0 | style `Table2`, 17,04 cm |
| T2 alat & bahan | tanpa style, **4 kolom** | style `Table3`, 12,75 cm, **3 kolom** |
| T3–T9 | tanpa style, `tblW` 0 (lebar jatuh ke `tblGrid` bawaan) | style `Table4`–`Table10`, `tblW` 17,00 cm |

Koreksi temuan: revisi **menambahkan** style tabel eksplisit (`Table1`..`Table10`)
dan `tblW` nyata, sedangkan generate membiarkan `tblW=0` sehingga lebar jatuh ke
`tblGrid` bawaan. Efeknya sama (lebar mengikuti `tblGrid`), tapi revisi mengikatnya
eksplisit. Catatan penting: `T2 alat & bahan` di revisi menyusut jadi 12,75 cm
karena kolom ukuran dibuang — lebar mengikuti isi, bukan dipaksa penuh.

Header tabel data di revisi eksplisit 9 pt bold; di generate sebagian tidak
terbaca sebagai bold karena style tidak dipetakan.

---

## E. Kesimpulan yang dipakai di `ATURAN_LAPORAN_JOBSHEET.md`

1. Template menentukan struktur (praktikum per bab, wadah `Langkah | Jawaban/Deskripsi`).
2. Nama bab memakai titik dua, bukan em-dash.
3. Tepat 7 baris identitas, tanpa `No. Absen`.
4. Tanpa prefix angka, tanpa metakomentar, tanpa lampiran.
5. Lebar gambar dan tabel menyesuaikan isi, bukan dipaksa seragam.
6. Angka tidak disentuh saat revisi — yang disunting hanya wadah dan kalimat.
