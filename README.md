# Passos para utilizar o script

1. Dentro da pasta Instaladores VLC + Python3, terá os 2 instaladores, do python e do vlc vídeo player, instale os 2. 

2. O arquivo dependencias.bat cuidará de instalar as dependências necessárias para iniciar o projeto.

3. Abra o código python `fullscreen.py` na pasta vlc e vá para a linha 40, onde está o seguinte trecho:
```
vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
```
Adicione o diretório onde o .exe do VLC instalado no seu sistema.

4. Na requisição de busca do link M3U8, configure com seus dados da conta na Tuya e os dados da câmera:
```
API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285"
ACCESS_ID = 'SEU ID DE ACESSO'
ACCESS_KEY = 'CHAVE DE ACESSO'
USER_ID = 'ID DO USUÁRIO'
USERNAME = 'SEU LOGIN'
PASSWORD = 'SUA SENHA'
DEVICE_ID = 'ID DO DISPOSITIVO TUYA'
```
5. No arquivo `open.bat`, você encontrará o código de abertura do projeto:

start python record.py
start python fullscreen.py

Irá iniciar a gravação da tela junto com a exibição do vídeo da câmera 4G.

6. Após verificar que tudo está configurado corretamente, execute o arquivo `open.bat` e o VLC será aberto e o código funcionará perfeitamente.

7. No arquivo python record.py na linha 13 direcione a pasta desejada para salvar o arquivo de vídeo gravado.

```
    file_name = f"C:\\Users\\gordhacker\\Videos\\VÍDEOS CAMERA TUYA\\camera_{current_time}.mp4"
```

8. Para visualizar a câmera externamente, tem o atalho de nome "Compartilhar tela" ele inicia o código do arquivo screenshare.py dentro da pasta streaming, que compartilha a tela via navegador.

9. No trecho abaixo poderá configurar o ip, a porta e a senha do compartilhamento de tela, pode conigurar com o ip da máquina, a porta desejada e a senha que deseja como default.

```
    parser.add_argument("-p", "--port", help="port, default 18331", type=int, default=8000)
    parser.add_argument("-w", "--password", help="password, default no password", default="123")
```


# Funcionamento

Este projeto tem como objetivo automatizar a exibição da câmera Tuya 4G, que não possui conectividade 4G. Utilizando uma requisição, a API da Tuya nos retorna o link HSL M3U8 para exibição.

O projeto utiliza o VLC para baixar o arquivo e reproduzi-lo no player. No início do código, há uma requisição para buscar o link de exibição. Automaticamente, quando o link é gerado, o código busca o VLC na pasta raiz e o abre com o link de reprodução M3U8. Junto ele inicia a gravação da tela salvando o vídeo reproduzido pela câmera no VLC e salva com a data e hora da gravação. Também tem a opção de compartilhar as imagens podendo acessar de qualquer lugado se o código de streaming estiver executando.


ENGLISH!!!!!


# Steps to use the script

1. Inside the VLC + Python3 installers folder, you will have the 2 installers, python and vlc video player, install the 2.

2. The dependencias.bat file will take care of installing the necessary dependencies to start the project.

3. Open the `fullscreen.py` python code in the vlc folder and go to line 40, where the following snippet is:
```
vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
```
Add the directory where VLC .exe installed on your system.

4. In the M3U8 link search request, configure with your Tuya account data and camera data:
```
API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285"
ACCESS_ID = 'YOUR ACCESS ID'
ACCESS_KEY = 'ACCESS KEY'
USER_ID = 'USER ID'
USERNAME = 'YOUR LOGIN'
PASSWORD = 'YOUR PASSWORD'
DEVICE_ID = 'TUYA DEVICE ID'
```
5. In the `open.bat` file, you will find the project opening code:

start python record.py
start python fullscreen.py

It will start recording the screen along with showing the video from the 4G camera.

6. After verifying that everything is configured correctly, run the `open.bat` file and VLC will open and the code will work perfectly.

7. In the python file record.py on line 13 direct the desired folder to save the recorded video file.

```
     file_name = f"C:\\Users\\gordhacker\\Videos\\VÍDEOS CAMERA TUYA\\camera_{current_time}.mp4"
```

8. To view the camera externally, there is a shortcut called "Share screen". It starts the code from the screenshare.py file inside the streaming folder, which shares the screen via the browser.

9. In the section below you can configure the ip, port and password for screen sharing, you can configure with the machine ip, the desired port and the password you want as default.

```
     parser.add_argument("-p", "--port", help="port, default 18331", type=int, default=8000)
     parser.add_argument("-w", "--password", help="password, default no password", default="123")
```


# Operation

This project aims to automate the display of the Tuya 4G camera, which does not have 4G connectivity. Using a request, the Tuya API returns the HSL M3U8 link for display.

The project uses VLC to download the file and play it in the player. At the beginning of the code, there is a request to fetch the display link. Automatically, when the link is generated, the code fetches VLC from the root folder and opens it with the M3U8 playback link. Together he starts recording the screen by saving the video played by the camera in VLC and saves it with the date and time of the recording. It also has the option to share the images being able to access them from anywhere if the streaming code is running.