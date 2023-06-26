@echo off
@echo.
@echo  " /$$$$$$$$/$$$$$$$$/$$$$$$$$/$$$$$$$$  /$$$$$$  /$$   /$$"
@echo  "| $$_____/__  $$__/__  $$__/ $$_____/ /$$__  $$| $$  | $$"
@echo  "| $$        | $$     | $$  | $$      | $$  \__/| $$  | $$"
@echo  "| $$$$$     | $$     | $$  | $$$$$   | $$      | $$$$$$$$"
@echo  "| $$__/     | $$     | $$  | $$__/   | $$      | $$__  $$"
@echo  "| $$        | $$     | $$  | $$      | $$    $$| $$  | $$"
@echo  "| $$        | $$     | $$  | $$$$$$$$|  $$$$$$/| $$  | $$"
@echo  "|__/        |__/     |__/  |________/ \______/ |__/  |__/"
@echo.

title Instalação de Dependencias
color 0A

echo Instalando dependencias...
ping 127.0.0.1 -n 2 > nul

echo.
echo =======================================
echo          Instalando pillow
echo =======================================
echo.

pip install pillow > nul
echo pillow instalada com sucesso!

echo.
echo =======================================
echo        Instalando pygetwindow
echo =======================================
echo.

pip install pygetwindow > nul
echo pygetwindow instalada com sucesso!

echo.
echo =======================================
echo  Instalando tuya-connector-python
echo =======================================
echo.

pip install tuya-connector-python > nul
echo tuya-connector-python instalada com sucesso!

echo.
echo =======================================
echo         Instalando psutil
echo =======================================
echo.

pip install psutil > nul
echo psutil instalada com sucesso!

echo.
echo =======================================
echo      Instalando flask-bootstrap
echo =======================================
echo.

pip install flask-bootstrap > nul
echo flask-bootstrap instalada com sucesso!

echo.
echo =======================================
echo       Instalando pyscreenshot
echo =======================================
echo.

pip install pyscreenshot > nul
echo pyscreenshot instalada com sucesso!

echo.
echo =======================================
echo        Instalando pyopenssl
echo =======================================
echo.

pip install pyopenssl > nul
echo pyopenssl instalada com sucesso!

echo.
ping 127.0.0.1 -n 2 > nul
echo.
echo Fechando em 3...
ping 127.0.0.1 -n 2 > nul
echo Fechando em 2...
ping 127.0.0.1 -n 2 > nul
echo Fechando em 1...
ping 127.0.0.1 -n 2 > nul

exit
