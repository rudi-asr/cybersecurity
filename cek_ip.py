# - Buka aplikasi vscodium
# - install ekstensi python dan remote ssh
# - konfig ssh, tekan ctl + shift + p dan cari remote (open ssh configuration file)
# - input 

# Host 192.168.253.195
#    HostName 192.168.253.195
#    User parrot
#    PasswordAuthentication yes
# NOTE : 192.168.253.195 => SESUAIKAN dengan ip address private kalian.
# - tekan  ctl + shift + p dan pilih connect to host. input = parrot@192.168.253.195 
# - default password parrot = parrot

####################################################################################
#cek_ip.py
####################################################################################
# fungsi socket untuk komunikasi jaringan, client-server
import socket

hostname = input('Masukkan alamat Domain: ')
ip_address = socket.gethostbyname(hostname)

print(f'Nama Domain: {hostname}')
print(f'Alamat IP Add: {ip_address}')

# running, $ python3 cek.py



    
