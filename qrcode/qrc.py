# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 11/09/2023
# Data de modificação: 09/10/2023
# Versão: 1.1


# Importando a biblioteca
import qrcode

# Endereço que será codificado
url = "https://github.com/jplfalcao"

# Cria um objeto QR Code
qrc = qrcode.QRCode(version=1, box_size=10, border=5)

# Adicionando o valor de 'url'
qrc.add_data(url)

# Configura o QR Code para caber no tamanho mínimo possível
qrc.make(fit=True)

# Cria uma imagem do QR Code
image = qrc.make_image(fill_color='black', back_color='white')

# Salva a imagem com o formato '.png'
image.save('QRCodeGithub.png')
