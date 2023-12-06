import socket

def scanning(ip_address, port):

    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(f'Port {str(port)} terbuka')
    except ConnectionRefusedError:
        print(f'Port {str(port)} tertutup')

target = input('Target: ')
ports = input('Port: ')

scanning(target, int(ports))
