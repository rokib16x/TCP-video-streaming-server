from server import server 

server = server('127.0.1.1', 8321)
server.bind_socket()
server.listen()
server.serve()