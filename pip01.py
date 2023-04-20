import qrcode

# criar um código QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# adicionar dados ao código QR
data = 'https://www.youtube.com/watch?v=Gq9bNjJkqdo'
qr.add_data(data)
qr.make(fit=True)

# Criar imagem do código QR
img = qr.make_image(fill_color='black', back_color='white')

# salvar imagem em um arquivo
img.save('qr_code_mark.png')