import socket
import pickle
import cv2
import struct
import threading

class server:
    def __init__(self, ip, port) -> None:
        # Write Initialization Code Here
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.video_dim = (800, 600)

    def bind_socket(self) -> None:
        # Complete this
        # Bind the socket to the given IP and port
        self.server_socket.bind((self.ip, self.port))
        # Set the socket to listen mode
        self.server_socket.listen(5)

    def listen(self) -> None:
        # Complete this
        # Accept incoming connections
        while True:
            client_socket, client_address = self.server_socket.accept()
            # Start a new thread to handle the incoming connection
            thread = threading.Thread(target=self.client_handler, args=(client_socket,))
            thread.start()
        
    def client_handler(self, client_socket) -> None:
            # If the socket is not valid, return

        if client_socket is None:
            return
            # Set the path to the video file to be streamed
    # Create a VideoCapture object to read the video file

        path_to_video_file = "video.mkv"
        vid = cv2.VideoCapture(path_to_video_file)
        try:
                    # While the video file is open

            while vid.isOpened():
                            # Read a frame from the video

                _, frame = vid.read()
                            # Resize the frame to the specified dimensions

                frame = cv2.resize(frame, self.video_dim, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                            # Serialize the frame using pickle

                a = pickle.dumps(frame)
            # Pack the serialized frame with a message length prefix
                message = struct.pack("Q", len(a)) + a
                            # Send the message to the client

                # Write Code to send Message
                client_socket.sendall(message)
        except:
                    # If an exception occurs, do nothing

            None

    
    def serve(self) -> None:
        try:
            self.listen()

            # Code for multithreaded service
        except KeyboardInterrupt:
            self.socket.close()