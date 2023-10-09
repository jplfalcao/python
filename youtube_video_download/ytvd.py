# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 09/10/2023
# Data de modificação:
# Versão: 1.0


# Importando a biblioteca
import yt_dlp

# Endereço do vídeo a ser baixado
url = input("Digite a url do vídeo: ")

# Especificando o formato '.mp4' para o vídeo
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
}

# Usando a classe YoutubeDL para baixar o vídeo
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Vídeo baixado com sucesso!")
