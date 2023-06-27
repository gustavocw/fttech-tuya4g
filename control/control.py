import tkinter as tk
import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

TUYA_LOGGER.setLevel(logging.DEBUG)

ACCESS_ID = 'markpnvva535s7wh4yuh'
ACCESS_KEY = 'c40f38372cb24cd58594d8273d82c67d'
USER_ID = 'az1683658824222RajEK'
API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "v1.0/iot-03/devices/eb49e9ca19346f0a3abbzd/commands"
USERNAME = 'marcelo@fttech.com.br'
PASSWORD = 'dcba4321'
DEVICE_ID = 'eb49e9ca19346f0a3abbzd'

openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

def olhar_cima():
    commands = {
        "commands": [
            {
                "code": "ptz_control",
                "value": "0"
            }
        ]
    }
    request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)

def olhar_baixo():
    commands = {
        "commands": [
            {
                "code": "ptz_control",
                "value": "4"
            }
        ]
    }
    request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)


def girar_esquerda():
    commands = {
        "commands": [
            {
                "code": "ptz_control",
                "value": "6"
            }
        ]
    }
    request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)

def girar_direita():
    commands = {
        "commands": [
            {
                "code": "ptz_control",
                "value": "2"
            }
        ]
    }
    request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)

def parar():
    commands = {
        "commands": [
            {
                "code": "ptz_stop",
                "value": True
            }
        ]
    }
    request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)

root = tk.Tk()
root.geometry("300x200")

girar_button = tk.Button(root, text="Girar pra direita", command=girar_direita, width=20, height=2)
girar_button.pack()

girar_button = tk.Button(root, text="Girar pra esquerda", command=girar_esquerda, width=20, height=2)
girar_button.pack()

girar_button = tk.Button(root, text="Olhar pra cima", command=olhar_cima, width=20, height=2)
girar_button.pack()

girar_button = tk.Button(root, text="Olhar pra baixo", command=olhar_baixo, width=20, height=2)
girar_button.pack()

parar_button = tk.Button(root, text="Parar", command=parar, width=20, height=2)
parar_button.pack()


root.mainloop()
