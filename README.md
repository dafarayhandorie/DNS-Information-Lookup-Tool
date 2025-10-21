DNS Information Lookup Tool
DNS Information Lookup Tool adalah proyek sederhana berbasis Python yang digunakan untuk melakukan pencarian informasi DNS (Domain Name System) dari sebuah domain.
Alat ini memanfaatkan perintah nslookup untuk mendapatkan detail seperti alamat IP, mail server (MX record), dan name server (NS record) dari domain yang ditentukan.

Fitur Utama:
- Menampilkan alamat IP (A record) dari domain.
- Mendapatkan informasi Mail Exchange (MX record).
- Menampilkan daftar Name Server (NS record).
- Menyimpan hasil pencarian ke file .txt secara otomatis.
- Dapat dijalankan langsung di terminal (Linux/macOS).

Cara menjalankan:
Jalankan program
python3 dns_lookup.py

Masukkan nama domain
Contoh:
Masukkan domain: pcr.ac.id

Hasil:
Program akan menampilkan hasil di terminal dan menyimpannya ke file dns_google.com_<timestamp>.txt.

📘 Contoh Output
Masukkan nama domain (contoh: pcr.ac.id): pcr.ac.id

🔍 Melakukan lookup DNS untuk pcr.ac.id...

--- A Record ---
Non-authoritative answer:
Name:	pcr.ac.id

--- MX Record ---
Non-authoritative answer:
pcr.ac.id	mail exchanger = 5 alt2.aspmx.l.google.com.
pcr.ac.id	mail exchanger = 10 alt3.aspmx.l.google.com.
pcr.ac.id	mail exchanger = 10 alt4.aspmx.l.google.com.
pcr.ac.id	mail exchanger = 1 aspmx.l.google.com.
pcr.ac.id	mail exchanger = 5 alt1.aspmx.l.google.com.
Authoritative answers can be found from:

--- NS Record ---
Non-authoritative answer:
pcr.ac.id	nameserver = ns3.pcr.ac.id.
pcr.ac.id	nameserver = ns1.pcr.ac.id.
pcr.ac.id	nameserver = ns2.pcr.ac.id.
pcr.ac.id	nameserver = ns4.pcr.ac.id.
Authoritative answers can be found from:

--- CNAME Record ---
Non-authoritative answer:
*** Can't find pcr.ac.id: No answer
Authoritative answers can be found from:

--- AAAA Record ---
Non-authoritative answer:
*** Can't find pcr.ac.id: No answer


✅ Hasil DNS lookup disimpan ke file: dns_lookup_pcr-ac-id_2025-10-21_02-19-25.csv

Selesai ✅


Teknologi yang Digunakan:
Python 3.x (3.8.2)
Subprocess module
Command-line tool nslookup
