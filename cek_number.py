# Import library yang diperlukan
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
import requests  # Import library untuk melakukan permintaan HTTP

# Meminta input nomor telepon dengan kode negara
number = input("Masukkan nomor telepon dengan kode negara: ")

# Parsing nomor telepon menjadi format yang sesuai
phoneNumber = phonenumbers.parse(number)

# Masukkan API Key BigDataCloud di sini
bigdatacloud_api_key = "bdc_5d0fa8fc5c734191a2bde68974b9df8c"  # Ganti dengan API Key BigDataCloud Anda

# Menggunakan modul geocoder dari phonenumbers untuk mendapatkan lokasi dalam console
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("Lokasi: " + yourLocation)

# Menggunakan modul carrier dari phonenumbers untuk mendapatkan nama penyedia layanan dalam console
yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("Penyedia Layanan: " + yourServiceProvider)

# Menggunakan BigDataCloud API untuk mendapatkan informasi terkait nomor telepon
bigdatacloud_api_url = f"https://api.bigdatacloud.net/data/phone-number-validate?number={number}&countryCode=ID&localityLanguage=en&key={bigdatacloud_api_key}"
response = requests.get(bigdatacloud_api_url)

if response.status_code == 200:
    data = response.json()
    isValid = data.get("isValid")
    e164Format = data.get("e164Format")
    internationalFormat = data.get("internationalFormat")
    nationalFormat = data.get("nationalFormat")
    lineType = data.get("lineType")
    country = data.get("country")

    print("Valid Number:", isValid)
    print("E164 Format:", e164Format)
    print("International Format:", internationalFormat)
    print("National Format:", nationalFormat)
    print("Line Type:", lineType)
    print("Country:", country)

    # Menyimpan nilai kode negara dan bagian nasional dari nomor telepon
    country_code = phoneNumber.country_code
    national_number = phoneNumber.national_number

    # Membuat peta dengan kode negara dan bagian nasional dari nomor telepon
    myMap = folium.Map(location=[country_code, national_number], zoom_start=9)

    # Menambahkan marker pada peta untuk menampilkan nama lokasi
    folium.Marker([country_code, national_number], popup=yourLocation).add_to(myMap)

    # Menyimpan peta dalam format file HTML untuk melihat lokasi pada peta
    myMap.save("Lokasi.html")
else:
    print("Gagal melakukan permintaan ke API BigDataCloud.")
