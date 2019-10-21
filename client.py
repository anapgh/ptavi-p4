#!/usr/bin/python3
"""
Programa cliente UDP que abre un socket a un servidor
"""
import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = 'localhost'
PORT = 6001


#Leemos los argumentos desde la shell

if len(sys.argv) < 4:
    sys.exit("Usage: client.py ip puerto linea")

Line = ' '.join(sys.argv[3:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", Line)
    my_socket.send(bytes(Line, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
