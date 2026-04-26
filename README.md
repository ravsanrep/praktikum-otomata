# 🧠 Simple Tokenizer Program


## 👤 Team

Muhammad Sayyidil Anam 5025241267
Abdurrahman Arrafi Ravsan Zarnadi 5025241241
Antonius Andy Martono 5025241191

---

Program ini merupakan implementasi sederhana dari **lexical analyzer (tokenizer)** yang dapat membaca input berupa kode program, kemudian memecahnya menjadi token-token dan mengelompokkannya berdasarkan kategori tertentu.

---

## 📌 Fitur Utama

* 🔍 Membaca input kode (multi-line)
* 🧩 Tokenisasi menggunakan Regular Expression (Regex)
* 🗂️ Klasifikasi token ke dalam kategori:

  * Reserved Words
  * Symbol / Tanda Baca
  * Variable
  * Kalimat Matematika
* 🖥️ Tersedia 2 mode:

  * CLI (Command Line Interface)
  * GUI sederhana (Tkinter)

---

## 🏗️ Struktur Project

```
project/
│
├── tokenizer.py   # Logic utama tokenisasi
├── main.py        # Versi CLI
└── ui.py          # Versi GUI (Tkinter)
```

---

## ⚙️ Cara Menjalankan Program

### 1. Pastikan Python sudah terinstall

Cek dengan:

```
python --version
```

---

### 2. Menjalankan versi CLI

```
python main.py
```

Masukkan kode program, lalu akhiri dengan:

```
END
```

---

### 3. Menjalankan versi GUI

```
python ui.py
```

Akan muncul window untuk input kode dan melihat hasil tokenisasi.

---

## 🧪 Contoh Input

```
int x = 10;
y = x + 5;
if (y > 10) {
    return y;
}
```

---

## 📊 Contoh Output

```
[Reserved Words]
['int', 'if', 'return']

[Symbols]
['=', ';', '=', '+', ';', '(', ')', '{', '}']

[Variables]
['x', 'y', 'x', 'y']

[Math Expressions]
x = 10;
y = x + 5;
if (y > 10) {
```

---

## 🧠 Penjelasan Singkat Algoritma

1. Program membaca input berupa teks kode
2. Menggunakan **Regular Expression** untuk memecah string menjadi token
3. Setiap token diklasifikasikan berdasarkan:

   * Kecocokan dengan reserved words
   * Pola simbol
   * Pola variabel
4. Setiap baris yang mengandung operator matematika akan dimasukkan ke kategori **math expression**

---


## 📌 Catatan

Program ini dibuat untuk memenuhi tugas praktikum mengenai **tokenisasi dan klasifikasi string dalam kode program**, dengan fokus pada kesederhanaan dan kejelasan algoritma.

---
