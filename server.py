import socket, time



class Server:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT

        self.clients = []
              
    def run_server(self):
        #создаем сервер и поднимаем его на 8080 порту и на ip
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((self.IP, self.PORT))
        
        not_quit = True
        print(f'[+] SERVER STARTED\nIP: {socket.gethostbyname(socket.gethostname())}\nPORT: 8080')

        while not_quit:
            try:
                data, address_client = server.recvfrom(1024)

                if address_client not in self.clients:
                    self.clients.append(address_client)
#time of connection
                when = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())

                print(f'\nip: {address_client[0]}\nadress: {address_client[1]}\ntime{when}\nwho: ', end='')
                print(data.decode('utf-8'))

                for client in self.clients:
                    if address_client != client:
                        server.sendto(data, client)
            except:
                print('\n[+] SERVER STOPPED')
                not_quit = False
        server.close()


#-----------------------------------------------> Run server

server_1 = Server(socket.gethostbyname(socket.gethostname()), 8080)
server_1.run_server()



