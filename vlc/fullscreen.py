import logging
import signal
import time
import subprocess
import pygetwindow as gw
import psutil
from tuya_connector import (
    TuyaOpenAPI,
    TUYA_LOGGER
)

# Configurar o logger do Tuya para exibir mensagens de depuração
TUYA_LOGGER.setLevel(logging.DEBUG)

# Definir as credenciais e detalhes do dispositivo Tuya
ACCESS_ID = 'markpnvva535s7wh4yuh'
ACCESS_KEY = 'c40f38372cb24cd58594d8273d82c67d'
USER_ID = 'az1683658824222RajEK'
API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285"
USERNAME = 'marcelo@fttech.com.br'
PASSWORD = 'dcba4321'
DEVICE_ID = 'eb49e9ca19346f0a3abbzd'

openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)

# Função para lidar com interrupções de sinal
def handle_interrupt(signal, frame):
    openapi.disconnect()
    if vlc_process is not None and psutil.pid_exists(vlc_process.pid):
        # Encerrar o processo do VLC
        vlc_process.terminate()
        vlc_process.wait()
    exit(0)

# Definir o manipulador de sinal
signal.signal(signal.SIGINT, handle_interrupt)

# Caminho para o executável do VLC
vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
vlc_process = None

while True:
    # Conectar-se à API Tuya
    openapi.connect()

    # Enviar uma solicitação para obter o link do vídeo M3U8 HSL
    commands = {"type": "hls"}
    request = openapi.post(f'/v1.0/devices/{DEVICE_ID}/stream/actions/allocate', commands)
    link = request["result"]["url"]

    # Iniciar o VLC em segundo plano em modo de tela cheia
    command = [vlc_path, link, '--fullscreen', '--no-video-title-show', '--no-embedded-video', '--qt-start-minimized']
    new_vlc_process = subprocess.Popen(command, stdin=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

    # Aguardar 3,5 segundos para a nova janela do VLC ser aberta e minimizada
    time.sleep(4)

    # Minimizar a janela do VLC anterior, se existir
    if vlc_process is not None and psutil.pid_exists(vlc_process.pid):
        vlc_window = gw.getWindowsWithTitle('VLC (Direct3D11 output)')[0]
        vlc_window.minimize()

    # Aguardar 20 segundos
    time.sleep(10)

    # Encerrar o player anterior, maximizar a janela minimizada e exibir a nova tela do VLC
    if vlc_process is not None and psutil.pid_exists(vlc_process.pid):
        vlc_window = gw.getWindowsWithTitle('VLC (Direct3D11 output)')[1]
        vlc_window.maximize()
        vlc_process.terminate()
        vlc_process.wait()
        new_vlc_process.stdin.write(b'command:fullscreen\n')
        new_vlc_process.stdin.flush()

    vlc_process = new_vlc_process

    # Aguardar 20 segundos antes de repetir o ciclo
    time.sleep(170)
