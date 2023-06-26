from multiprocessing import Process
import cv2
import numpy as np
import pyautogui
import time
from datetime import datetime

# Função principal para gravar a tela
def record_screen():
    while True:
        # Obtém a data e hora atual para usar no nome do arquivo
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"C:\\Users\\gordhacker\\Videos\\VÍDEOS CAMERA TUYA\\camera_{current_time}.mp4"

        SCREEN_SIZE = (853, 480)  # Define o tamanho da tela desejado
        # Define o codec para H.264
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        # Frames por segundo
        fps = 15.0
        # Duração da gravação em segundos
        record_seconds = 180

        # Calcula o número de frames a serem gravados
        total_frames = int(record_seconds * fps)

        # Cria o objeto de gravação de vídeo
        out = cv2.VideoWriter(file_name, fourcc, fps, SCREEN_SIZE)

        for i in range(total_frames):
            # Captura uma screenshot
            img = pyautogui.screenshot()
            # Redimensiona a imagem para o tamanho desejado
            img = img.resize(SCREEN_SIZE)
            # Converte os pixels para um array numpy para trabalhar com o OpenCV
            frame = np.array(img)
            # Converte as cores de BGR para RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Escreve o frame
            out.write(frame)

        out.release()
        time.sleep(0.1)

if __name__ == '__main__':
    while True:
        t = Process(target=record_screen)
        t.start()
        time.sleep(180)
        t.join()
