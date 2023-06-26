import tkinter as tk
import subprocess
import threading
import psutil

def iniciar_programas():
    subprocess.Popen(['pythonw', './vlc/fullscreen.py'], shell=True)
    subprocess.Popen(['pythonw', './vlc/record.py'], shell=True)

def parar_programas():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'pythonw' or proc.info['name'] == 'vlc':
            p = psutil.Process(proc.info['pid'])
            p.kill()

def instalar_dependencias():
    def instalar():
        dependencias = [
            'pillow',
            'pygetwindow',
            'tuya-connector-python',
            'psutil',
            'flask-bootstrap',
            'pyscreenshot',
            'pyopenssl'
        ]
        total_dependencias = len(dependencias)
        progresso['maximum'] = total_dependencias

        for i, dependencia in enumerate(dependencias, start=1):
            subprocess.Popen(['pip', 'install', dependencia])
            progresso['value'] = i
            janela.update()

        progresso['value'] = 0

    thread = threading.Thread(target=instalar)
    thread.start()

janela = tk.Tk()
janela.geometry("380x250")

# Estilos para os botões
estilos_botao = {
    'background': '#4169E1',
    'foreground': 'white',
    'font': ('Arial', 12),
    'width': 18,
    'height': 2,
    'relief': 'groove'
}

botao_iniciar = tk.Button(janela, text='Iniciar Programa', command=iniciar_programas, **estilos_botao)
botao_iniciar.pack(pady=10)

botao_parar = tk.Button(janela, text='Parar Programa', command=parar_programas, **estilos_botao)
botao_parar.pack(pady=10)

botao_instalar = tk.Button(janela, text='Instalar Dependências', command=instalar_dependencias, **estilos_botao)
botao_instalar.pack(pady=10)

janela.mainloop()
