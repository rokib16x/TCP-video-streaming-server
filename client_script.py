from client import client

client = client('127.0.1.1', 8321)
client.connect_to_server()
client.receive_video_data()