import socket


code_with_trick = socket.gethostname()


ip = socket.gethostbyname(code_with_trick)


print(ip)