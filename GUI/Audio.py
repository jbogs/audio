
from vidstream import AudioServer, AudioSender, AudioReceiver
import threading
import socket

server_ip = "10.2.106.42"
server_port = 5555 # send to on server
client_port = 2222

class Audio:
    def __init__(self) -> None:
        ip = self.get_ip()

        self.isServer = False
        sender = AudioSender(server_ip, server_port)
        sender_thread = threading.Thread(target=sender.start_stream)
        sender_thread.start()
        self.sender = sender
         
        receiver = AudioReceiver(ip, client_port)
        receiver_thread = threading.Thread(target=receiver.start_stream)
        receiver_thread.start()
        self.receiver = receiver

        if ip == server_ip:
            server = AudioServer(server_ip, server_port)
            server_thread = threading.Thread(target=server.start_server)
            server_thread.start()
            self.isServer = True
            self.server = server
            server.start_server()
        
        sender.start_stream()
        receiver.start_stream()

    def shutdown(self):
        if self.isServer:
            self.server.stop_server()
        self.sender.stop_stream()
        self.receiver.stop_stream()

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
