

"""
Send to every client who didn't send us the data

so connect each audio recieve to each audio send for each client we add


"""

import socket
import pyaudio
import select
import threading

class Client:
    def __init__(self, ip, port=2222) -> None:
        self.__host = ip
        self.__port = port
        self.__sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sending_socket.connect((self.__host, self.__port))
        
    # send the ip of who's talking
    # even if it's the current client so the UI will show them talking
    # just don't have it call the pyaudio
    def send_audio(self, audio, ip):
        self.__sending_socket.send(audio)

class AudioServer:
    def __init__(self, host, port, slots=8, audio_format=pyaudio.paInt16, channels=1, rate=44100, frame_chunk=4096):
        self.__host = host
        self.__port = port

        self.__slots = slots
        self.__used_slots = 0
        self.__frame_chunk = frame_chunk
        self.__clients = {}

        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.bind((self.__host, self.__port))

        self.__block = threading.Lock()
        self.__running = False

    def start_server(self):
        if self.__running:
            print("Audio server is running already")
        else:
            self.__running = True
            thread = threading.Thread(target=self.__server_listening)
            thread.start()

    def register_client(self, address):
        self.__clients[address] = Client(address)

    def __server_listening(self):
        self.__server_socket.listen()
        while self.__running:
            self.__block.acquire()
            connection, address = self.__server_socket.accept()
            if self.__used_slots >= self.__slots:
                print("Connection refused! No free slots!")
                connection.close()
                self.__block.release()
                continue
            else:
                self.__used_slots += 1

            self.register_client(address[0])

            self.__block.release()
            thread = threading.Thread(target=self.__client_connection, args=(connection, address[0],))
            thread.start()

    def __client_connection(self, connection, address):
        while self.__running:
            data = connection.recv(self.__frame_chunk)
            for client in self.__clients.values():
                client.send_audio(data, address)

    def stop_server(self):
        if self.__running:
            self.__running = False
            closing_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            closing_connection.connect((self.__host, self.__port))
            closing_connection.close()
            self.__block.acquire()
            self.__server_socket.close()
            self.__block.release()
        else:
            print("Server not running!")




