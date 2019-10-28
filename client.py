#!/usr/bin/python3
"""
Programa cliente UDP que abre un socket a un servidor
"""
import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    USER = sys.argv[4]
    EXPIRES_VALUE = int(sys.argv[5])
except (IndexError, ValueError):
    sys.exit('Usage: client.py ip port REGISTER sip_address expires_value ')


if sys.argv[3] == 'REGISTER':
    Lines = ('REGISTER' + ' sip:' + USER + ' SIP/2.0\r\n')
    Lines = (Lines + 'Expires: ' + str(EXPIRES_VALUE))
else:
    Lines = sys.argv[3]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", Lines)
    my_socket.send(bytes(Lines, 'utf-8') + b'\r\n\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
