import socket
import os
import pickle

#instructions
# create a server and a client:
    #client args - time to switch photos, random/loop/negativenumber=button swap images , presents the images
    # servers - reads images from images dir
# create a dir of jpg images
#create venv and requierments.txt

HOST = '127.0.0.1'
PORT = 65432
IMAGE_DIR_PATH = r'C:\Users\chen\PycharmProjects\client_server\images'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    client_socket, client_address = server.accept()
    with client_socket:
        print(f"Connected by {client_address}")
        while True:
            data = client_socket.recv(4096)
            images_list_path_names = [os.path.join(IMAGE_DIR_PATH, image_name) for image_name in os.listdir(IMAGE_DIR_PATH)]
            msg = pickle.dumps(images_list_path_names)
            client_socket.send(msg)
            if not data:
                break


