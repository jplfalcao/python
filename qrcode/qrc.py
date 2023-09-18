# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 11/09/2023
# Data de modificação:
# Versão: 1.0


# Importando a biblioteca
import qrcode

# Endereço que será codificado
url = "https://github.com/jplfalcao"

# Cria um objeto 'QRCode' com a versão 1, o tamanho da caixa de 10 pixels
# e a borda de 5 pixels.
qrc = qrcode.QRCode(version = 1, box_size = 10, border = 5)

# Adicionando o valor de 'url'
qrc.add_data(url)

# Configura o QR Code para caber no tamanho mínimo possível
qrc.make(fit = True)

# Cria uma imagem do QR Code com a cor preta para os pixels preenchidos 
# e a cor branca para os pixels não preenchidos.
image = qrc.make_image(fill_color = 'black', back_color = 'white')

# Salva a imagem como um arquivo PNG
image.save('QRCodeGithub.png')

