import socket
import struct
import cv2
import pickle

class client:
    def __init__(self, server_ip, server_port) -> None:
        # Initilization code
        self.server_ip = server_ip
        self.server_port = server_port

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect_to_server(self) -> None:
        # Code to connect to server
         # Connect to server using server IP and port
        self.client_socket.connect((self.server_ip, self.server_port))
        
        

    def connect_to_server(self) -> None:
    # Connect to server using server IP and port
        self.client_socket.connect((self.server_ip, self.server_port))

    def receive_video_data(self) -> None:
        data = b""
        try:
            # Calculate the size of the payload
            payload_size = struct.calcsize("Q")
            while True:
                # Receive messages chunk by chunk and constitute them into full message
                while len(data) < payload_size:
                    packet = self.client_socket.recv(4*1024)
                    if not packet:
                        break
                    data += packet
                # Unpack the message size from the packed message size
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("Q", packed_msg_size)[0]
                # Receive the remaining data until the full message has been received
                while len(data) < msg_size:
                    data += self.client_socket.recv(4*1024)
                # Extract the frame data from the full message and deserialize it
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)
                # Display the frame and wait for a key press
                cv2.imshow("RECEIVING VIDEO", frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
            # Close the client socket when the video is finished or interrupted
            self.client_socket.close()
        except KeyboardInterrupt:
            self.client_socket.close()

