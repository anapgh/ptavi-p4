#!/usr/bin/python3
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dict_users = {}

    def add_user(self, sip_address, expires_value):
        """Add users to the dictionary."""
        IP_client, Port_client = self.client_address
        self.dict_users[sip_address] = IP_client + ' Expires: '\
                                                 + str(expires_value)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

    def delete_user(self, sip_address):
        """Delete users to the dictionary."""
        try:
            del self.dict_users[sip_address]
            self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
        except KeyError:
            self.wfile.write(b'SIP/2.0 404 User Not Found\r\n\r\n')


    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        for line in self.rfile:
            message_client = line.decode('utf-8')
            if message_client != '\r\n':
                print('El cliente nos manda: ', line.decode('utf-8'))
                parametros_client = ''.join(message_client).split()
                if parametros_client[0] == 'REGISTER':
                    sip_address = parametros_client[1].split(':')[1]
                elif parametros_client[0] == 'Expires:':
                    expires_value = float(parametros_client[1])
                    if expires_value == 0:
                        self.delete_user(sip_address)
                    elif expires_value > 0:
                        self.add_user(sip_address, expires_value)
                else:
                    self.wfile.write(b"SIP/2.0 400 error\r\n")
             # self.request is the TCP socket connected to the client
        print(self.dict_users)

if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    try:
        PORT = int(sys.argv[1])
        serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    except IndexError or ValueError:
        sys.exit('Usage: python3 server.py port')

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
