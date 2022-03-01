import pickle
import socket
import cv2
import argparse
import cv2.cv2
import keyboard

HOST = '127.0.0.1'
PORT = 65432
BYTES_ORDER = "big"


def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument('--time', default='3000', help='int =time between display of each image in ms')
    args = parser.parse_args()
    return args


def open_image(img_path, delay_time_action):
    """
    This function displays an image in a ceratain amount of time in ms.
    :param img_path: the displayed image path
    :param delay_time_action: action for cv2 display time
    :return:
    """
    image = cv2.imread(img_path)
    image_resized = cv2.resize(image, (500, 500))
    cv2.imshow('image', image_resized)
    cv2.waitKey(delay_time_action)


def main():
    args = menu()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        delay_time = args.time
        print('To stop/close images display, press "q" key')

        while True:
            s.sendall(bytes(delay_time, "utf-8"))
            list_image_display_data = s.recv(1048576)
            img_path, index, delay_time_action = pickle.loads(list_image_display_data)
            open_image(img_path, delay_time_action)
            if keyboard.is_pressed('q'):
                print('Pressed "q", image display terminated!')
                break


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)

