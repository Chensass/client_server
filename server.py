import socket
import os
import pickle
from random import randint
import argparse

HOST = '127.0.0.1'
PORT = 65432
IMAGE_DIR_PATH = r'C:\Users\chen\PycharmProjects\client_server\images'
RANDOM_DISPLAY = "random"
LOOP_DISPLAY = "loop"
BYTES_ORDER = "big"


def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument('--display', default='random', help='Display modes: loop, random')
    parser.add_argument('--path', default=IMAGE_DIR_PATH, help='Insert full images dir path')
    args = parser.parse_args()
    return args


def get_random_image_path(list_images):
    """
    This function gets a list of images path and return a random path from the list.
    :param list_images: list path images
    :return: random path
    """
    random_img_name = list_images[randint(0, len(list_images)-1)]
    return random_img_name


def get_loop_image_path(list_images, index):
    """
    This function gets a list of images path and index of the path that will be returned.
    :param list_images: list of images path
    :param index: index of returned path
    :return: image_path and index of next path
    """
    if index < len(list_images)-1:
        index += 1
    else:
        index = 0
    return list_images[index], index


def get_delay_time_action(delay_time):
    """
    This function gets the delat time and convert it to an action number for cv2.
    :param delay_time: time in ms
    :return: action number for cv2 delay time
    """
    if int(delay_time) < 0:
        return 0
    elif int(delay_time) >= 0:
        return delay_time


def main():
    args = menu()
    display_mode = args.display
    images_list_path_names = [os.path.join(args.path, image_name) for image_name in os.listdir(args.path)]
    index = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        client_socket, client_address = server.accept()

        with client_socket:
            print(f"Connected by {client_address}")
            while True:
                data_delay_time = client_socket.recv(1048576)
                delay_time_int = int(data_delay_time.decode("utf-8"))
                # delay_time_int = int.from_bytes(data_delay_time, BYTES_ORDER)
                delay_time_action = get_delay_time_action(delay_time_int)

                if display_mode == RANDOM_DISPLAY:
                    path = get_random_image_path(images_list_path_names)
                    index = -1

                elif display_mode == LOOP_DISPLAY:
                    path, new_index = get_loop_image_path(images_list_path_names, index)
                    index = new_index

                msg = pickle.dumps([path, index, delay_time_action])
                client_socket.send(msg)

                if not data_delay_time:
                    break


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)

