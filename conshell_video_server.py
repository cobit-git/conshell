import socket, cv2, pickle, struct
import threading 

class ConshellVideoServer(object):
    def __init__(self, host_ip, port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host_ip = host_ip
        self.port = port 
        self.sock.bind((self.host_ip, self.port))

    def listen(self):
        print("Conshell video server listen...")
        self.sock.listen(5)
        while True:
            self.client, self.address = self.sock.accept()
            print('GOT CONNECTION FROM:',self.address)
            #client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (self.client,self.address)).start()

    def listenToClient(self, client, address):
        print("Conshell video server thread running...")
        if self.client:
            vid = cv2.VideoCapture(0)
            while(vid.isOpened()):
                img,frame = vid.read()
                a = pickle.dumps(frame)
                message = struct.pack("Q",len(a))+a
                self.client.sendall(message)
                
                cv2.imshow('TRANSMITTING VIDEO',frame)
                key = cv2.waitKey(1) & 0xFF
                if key ==ord('q'):
                    self.sock.close()

if __name__ =="__main__":
    video_server = ConshellVideoServer('172.31.99.111', 9999)
    video_server.listen()
