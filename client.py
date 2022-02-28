import pickle
import socket
import cv2
import argparse
from random import randint

HOST = '127.0.0.1'
PORT = 65432

parser = argparse.ArgumentParser()
parser.add_argument('--display', default='random', help='display modes: loop, random')
parser.add_argument('--time', default=5, help='int =time between display of each image')
args = parser.parse_args()

def open_image(img_path, delay_time):
    image = cv2.imread(img_path)
    image = cv2.resize(image, (500, 500))
    cv2.imshow('image', image)
    get_delay_time(delay_time)

def get_delay_time(delay_time):
    if int(delay_time) < 0:
        return cv2.waitKey(0)
    elif int(delay_time) >= 0:
        return cv2.waitKey(delay_time)

def get_random_image_path(list_images):
    random_img_name = list_images[randint(0, len(list_images)-1)]
    return random_img_name


def get_loop_image_path(list_images,index):
    if index < len(list_images)-1:
        index += 1
    else:
        index = 0
    return list_images[index], index


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    display_mode = args.display
    delay_time = args.time
    index = 0

    while True:
        s.sendall(bytes(display_mode, "utf-8"))
        data = s.recv(2048)
        list_images = pickle.loads(data)

        if display_mode == "random":
            path = get_random_image_path(list_images)

        elif display_mode == "loop":
            path, new_index = get_loop_image_path(list_images, index)
            index = new_index

        open_image(path, delay_time)


