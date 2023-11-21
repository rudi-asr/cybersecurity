####################################################################################
#cek_ip.py
####################################################################################
# lib socket untuk komunikasi jaringan, client-server
# lib requests untuk permintaan http dan respons
# lib pprint (pretty-print) untuk modul bawaan python agar mudah (terbaca) mencetak struktur data 
# lib untuk membaca format JSON (JavaScript Object Notation)
#pip3 install --upgrade urllib3 chardet
#  k dan v adalah variabel yang digunakan untuk mengakses kunci (key) dan nilai (value) dari objek geolocation

import socket
import requests
import pprint
import json

hostname = input('Masukkan alamat Domain: ')
ip_address = socket.gethostbyname(hostname)

request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)

# Mengambil string JSON dari response
geolocation_json = response.text

# Mengekstrak data JSON dari dalam tanda kurung kurawal
geolocation_json = geolocation_json.split("(")[1].strip(")")
geolocation = json.loads(geolocation_json)

# Menampilkan hasil menggunakan pprint
for k, v in geolocation.items():
    pprint.pprint(str(k) + ' : ' + str(v))


