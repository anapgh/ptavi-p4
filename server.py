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

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        IP_client, Puerto_client = self.client_address
        for line in self.rfile:
            print('El cliente con IP nos manda: ', line.decode('utf-8'))
        self.wfile.write(b"SIP/2.0 200 OK\\r\\n\\r\\n")
         # self.request is the TCP socket connected to the client


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
