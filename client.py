import socket, threading, time

KEY = 8194

shutdown = False
join = False

def recerving(name, sock):
    while not shutdown:
        try:
            while True:
                data, address_client = sock.recvfrom(1024)
                print(data.decode('utf-8'))

                #Шифрование
                # decrypt = ''
                # k = False

                # for i in data.decode('utf-8'):
                #     if i == ':':
                #         k = True
                #         decrypt +=  i
                #     elif k == False or i == ' ':
                #         decrypt += i
                #     else:
                #         decrypt += chr(ord(i)^KEY) 
                # print(decrypt)              
                time.sleep(0.2)
        except:
            pass

HOST = socket.gethostbyname(socket.gethostname())
PORT = 0
ip, port = input('Enter (ip port) of server: ').split()
server = (f'{ip}', int(port))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
s.setblocking(0)

name = input('NickName: ')
                                        #аргумент=это функция должна обрабатыватся при помоши tcp ip соединения
rt = threading.Thread(target=recerving, args=('RecvThread', s))
rt.start()

while not shutdown:
    if not join:
        s.sendto((f'[{name}] => join chat ').encode('utf-8'), server)
        join = True
    else:
        try:
            msg = input()

            #Шифрование
            # crypt = ''

            # for i in msg:
            #     crypt += chr(ord(i)^KEY)
            # msg = crypt

            if msg != '':
                s.sendto((f'[{name}]: {msg}').encode('utf-8'), server)
            
            time.sleep(0.2)
        except:
            s.sendto((f'[{name}]: <= left chat').encode('utf-8'), server)
            shutdown = True
rt.join()
s.close()