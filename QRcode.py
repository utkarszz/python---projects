import qrcode
data = "https://youtu.be/i35AUg11hvo?feature=shared"
qr = qrcode.make(data)
qr.save("my_qr_code.png")
print("QR code generated and saved as my_qr_code.png")
# This code generates a QR code for the specified URL and saves it as an image file.